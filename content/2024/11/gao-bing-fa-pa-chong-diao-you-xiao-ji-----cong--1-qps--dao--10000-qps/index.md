---
title: 高并发爬虫调优小记 - 从 1 QPS 到 10000 QPS
date: 2024-11-24
extra:
  source: https://blog.lyc8503.net/post/high-performance-crawler/
  original_title: 高并发爬虫调优小记 - 从 1 QPS 到 10000 QPS
---
## Summary
**摘要**：
本文详细记录了一次从原始爬虫的低并发QPS优化至10,000 QPS的经历。作者通过实践和调整，最终解决了高频API访问的困扰，优化了爬虫性能，并成功使用IPv6避开IP频控限制。

**要点总结**：
1. **初始问题识别与多线程实现**：开始时，爬虫QPS仅为个位数。引入多线程功能后，虽然能够并发请求，但在短时间内因频繁遭受403、429、400、412等状态码的响应和跳转验证而挂掉。原因在于访问频控触发了限流机制。

2. **IPv6资源应用与策略选择**：作者发现部分网站限制较宽松仅按照/128或更细粒度进行限制，而家庭宽带的/64相当宽松。最终选择将爬虫流量代理至本地消息极小的IPv6地址，以绕过IP访问限制。同时，活跃使用Xray代理增大代理池饱和度，有效缓解代理服务器用量。

3. **性能调优：异步优化**：通过将异步操作接入，如使用`aiohttp`与`asyncio`，显著提升了爬取性能，线路程数到40多后性能表现依旧稳定。这意味着，每完成一轮请求后，通过结束进行中的任务，系统能够预留出线程资源以服务于下一批请求，形成有效的线程流转。

4. **性能瓶颈与并发战术优化**：发现了连接数限制成为瓶颈，通过临时提升系统配置参数，重新关注不同请求集成于单个客户端会话以减少全局连接数，进而减少资源消耗，提高系统效率。

5. **并行进程与API带宽探索**：在保证响应时间和系统稳定性的前提下，最大化并发数量，利用多进程实现并行处理，甚至达到同时满足1万离峰请求的性能。作者通过实践探索了丰富的性能与环境配置，最终形成规模和效率的优化模型，实质上研究了爬虫设计在并发、连接复用和调度策略上的挑战与解答。

注意，文章作者采取了多种策略和工具调整来最大化系统性能并尽量减轻资源消耗，包括IPv6的巧妙使用、异步编程技术的应用、适当的代理管理和多进程的调度。整个过程展示了高并发环境下优化爬虫策略的复杂度与实现路径，对理解现代网络环境下的分布式和资源调配有着重要启示。
## Full Content
Title: 高并发爬虫调优小记 - 从 1 QPS 到 10000 QPS

URL Source: https://blog.lyc8503.net/post/high-performance-crawler/

Published Time: 2024-11-23T06:27:16.000Z

Markdown Content:
高并发爬虫调优小记 - 从 1 QPS 到 10000 QPS
LYC8503  2024-11-23 软件研究=) › 各式爬虫

本文记录的是真实的一次爬虫调优经历, 数据已脱敏, 仅供参考学习

某天, 你随手写了个爬虫:

1
2
3
4
5

	
def fetch_data(i):
    return requests.get(f"https://api.example.com/{i}").json()

for i in tqdm.trange(1, 10_0000_0000):
    print(fetch_data(i))


爬虫很愉快的跑了起来, 但一看进度条 QPS 只有个位数 (实测 56/999999999 [00:09<47662:00:38, 5.83it/s]), 这得跑到猴年马月…

要优化也不难, 加个多线程吧:

1
2
3
4
5
6
7
8
9
10
11

	
def fetch_data(i):
    return requests.get(f"https://api.example.com/{i}").json()

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = set()
    for i in tqdm.trange(1, 10_0000_0000):
        while len(futures) >= 20:
            completed, futures = wait(futures, return_when=FIRST_COMPLETED)
            for future in completed:
                print(future.result())
        futures.add(executor.submit(fetch_data, i))


结果刚跑起来没多久, 程序挂了…

1

	
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)


打印下请求情况, 你得到了一堆 403/429/400/412 或者其他什么乱七八糟的状态码, 一看响应体, 跳验证码了.

“喵的, 又是麻烦的 IP 频控…”, 你心想.

“代理池又贵又不稳定又接入繁琐, 之前薅阿里云/腾讯云的 IP 做代理不错, 但这次要爬的量太大了… 用家宽重新拨号或者挂 Tor 之类的应该也可行, 但效率也不够高…”

突然你想起了数量巨大的 IPv6 资源, 部分网站对 IPv6 的频控是按照 /64 甚至 /128 限制的, 就算严格一点的网站不怕误伤按照 /48 进行限制, 在人手一个 ASN 的当下, 谁还没段 /40 的 IPv6 呢.

经过测试, 运气很好, 这个网站属于最宽松的按照 /128 完全匹配的限流, 这样家宽的 /64 就够用了… “这不就等于没限制嘛… 不过又省了一笔购置服务器和 IP 段的费用”, 你边吐槽边开始实践.

先从 OpenWRT 入手, 随手选一段地址 (此处选/80) 路由到爬虫所在的主机:

1
2
3

	
# 按上文链接配置 NDP 会带来额外的开销, 还是建议在路由器上手动配路由, 除非你是光猫或傻瓜路由器拨号
# 此处假设运营商分配的前缀是 2409:1:2:3::/64, 爬虫主机为 2409:1:2:3:abcd::1
ip -6 route add 2409:1:2:3:abcd::/80 via 2409:1:2:3:abcd::1


在爬虫主机上, 同样配置路由, 并开启 ip_nonlocal_bind:

1
2
3
4
5

	
ip route add local 2409:1:2:3:abcd::/80 dev ens18
sysctl net.ipv6.ip_nonlocal_bind=1

# 配好了拿 curl 测试下
curl -v --interface 2409:1:2:3:abcd::2333 ip.p3terx.com


之后还得想个办法让每个请求绑定到一个随机的本地地址, 各类工具不少, 就用熟悉的 Xray 吧:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16

	
{
  "inbounds": [
    {
      "listen": "127.0.0.1",
      "port": 1234,
      "protocol": "http"
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom",
      "tag": "direct",
      "sendThrough": "2409:1:2:3:abcd::/80"
    }
  ]
}


终于搞定了 IP 问题, 用本地的 Xray 代理下爬虫流量:

1

	
https_proxy=http://127.0.0.1:1234 python3 crawl.py


终于! 爬虫稳定的跑在了… 40 QPS… (10773/999999999 [04:48<6206:23:37, 44.76it/s])

“搞什么鬼啊, 虽然比刚刚快了六七倍, 但还是要 6000 多个小时, 这可是… (掏出计算器一阵敲) 250 多天啊!”

你尝试暴力增加爬虫的线程数, 把线程 max_workers 从 20 一路拉到了 100, 可速度稳稳的 40 QPS 一动不动, 反而是 CPU 占用率水涨船高.

这下是从 “一核有难 十五核围观” 变成 “一核有难 十五核上下文切换” 了…

你无奈扶额, 大手一挥重新打开 IDE 改代码:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17

	
async def fetch(i):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.example.com/{i}", proxy='http://127.0.0.1:1234') as response:
            return await response.json()

async def main():
    tasks = set()
    for i in tqdm.trange(1, 10_0000_0000):
        tasks.add(asyncio.create_task(fetch(i)))
        while len(tasks) >= 20:
            finished, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            
            for r in finished:
                print(r.result())

if __name__ == "__main__":
    asyncio.run(main())


果然改用 asyncio 之后性能有了大幅提升, I/O 还得靠异步, CPU 占用率下降的同时 QPS 来到了 180+ (4622/999999999 [00:33<1505:59:35, 184.45it/s])

然而还没高兴三分钟, 进度条突然卡住不动了, QPS 掉到很低. 检查了下不是本机 ulimit 的问题, 也没报错 too many open files.

顺着链路一路向上排查, 在 OpenWRT 里发现了一打这样的日志: nf_conntrack: table full, dropping packet

好家伙, 这已经把路由器连接表给打满了… 所以没法建立新连接了.

临时使用 echo 65535 > /proc/sys/net/netfilter/nf_conntrack_max 提高 conntrack 上限, 终于让 QPS 稳定在了开始的 180, 不过此时路由器已经需要维护 3w 多个连接.

“这样下去也不是办法啊… 虽然一代神 u MT7621 暂时还撑得住, 或者就算我这边 OpenWRT 可以手动配防火墙规则 don’t track, 这么多连接数也容易被运营商制裁”, 你嘀咕着.

“每个 IP 并不是只能用一次就会被封, HTTP 也是支持 pipelining 的, 完全可以在一个 TCP 连接里进行多次请求, 省下握手开销.”

“不过这样需要一个连接池, 去翻翻文档吧… 咦, 等等… 艹原来 ClientSession 本来就包括连接池只是我用错了”

简单改下, 只要让不同的请求共用一个 Session 就行了:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17

	
async def fetch(session, av):
    async with session.get(f"https://api.example.com/{i}", proxy='http://127.0.0.1:1234') as response:
        return await response.json()

async def main():
    tasks = set()
    async with aiohttp.ClientSession() as session:
        for i in tqdm.trange(1, 10_0000_0000):
            tasks.add(asyncio.create_task(fetch(session, i)))
            while len(tasks) >= 20:
                finished, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                
                for r in finished:
                    print(r.result())

if __name__ == "__main__":
    asyncio.run(main())


改完后不仅连接数大幅下降到了数百, 还获得了一个不小的性能提升: QPS 到了 280+ (4678/999999999 [00:18<982:43:14, 282.66it/s)

此时代码已经优化的很不错了, 但仍需要 982 个小时(40 天).

打开监控看看总带宽, 大约才下行 4Mbps 上行 2 Mbps, python 单核占用 30%, 还有很大压榨空间.

直接拉大并发任务数到 80, 经过一堆优化, 这次 QPS 很顺利地跟着起飞了, 达到了惊人的 1280 (35126/999999999 [00:28<217:00:56, 1279.94it/s]), 宽带下行 12Mbps 上行 5Mbps.

再提高并发数效果就不太显著了, 因为此时的 python CPU 占用率已经来到了 90%, 这又成为了一个 CPU-bound 的任务…

“愚蠢的 GIL, 让我没法很方便的多线程, 这下又得搞 multi-processing 了. 不过现在的速度爬 1e9 条数据也只要不到 10 天了, 好像也不是不能接受~”

最后挑战一下极限: 将 range 切分后开 8 个进程, 实测峰值 QPS 可以达到 10000 并维持, 此时不太方便展示进度条, 但仅仅访问 API 的带宽就高达下行 70 Mbps 上行 30 Mbps. 根据下行 300Mbps 上行 120Mbps 的带宽和剩余的 CPU 核心数保守估计, 继续开进程至少可以达到 20000+ 的 QPS.

“不过… 程序员何苦为难程序员, 这到底是爬虫还是 DOS 攻击, 半夜流量要是把接口打告警了, 就有苦逼程序员要起来修了, 万一之后再改改反爬策略就又得折腾了, 感谢某网站宽松的反爬策略, 严格的反爬策略对谁都没好处… 我还是收敛一点就跑个一两千 QPS 吧”,

写完爬虫的你心满意足, 瞥了一眼时间, “草, 怎么一转眼已经半夜三点了, 今天还是’早点’睡吧, 明天还得研究这么多条数据塞什么数据库好, 甚至我的 SSD 都要存不下了…”

作者有话说: 第一次尝试另一种风格写博客, 也是第一次研究如此高并发的爬虫, 过程还算顺利, 最终代码比起单线程串行优化上万倍, 比起多线程同步 requests 优化上千倍, 还成功使用 IPv6 绕过 IP rate-limit, 收获颇丰.

本文采用 CC BY-NC-SA 4.0 许可协议发布.

作者: lyc8503, 文章链接: https://blog.lyc8503.net/post/high-performance-crawler/
如果本文给你带来了帮助或让你觉得有趣, 可以考虑赞助我¬_¬

Copyright © 2018-2024 lyc8503
HomeAboutWritingCategoryFriendsSearch

