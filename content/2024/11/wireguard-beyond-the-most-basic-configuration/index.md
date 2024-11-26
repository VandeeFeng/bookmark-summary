---
title: Wireguard - Beyond the most basic configuration
date: 2024-11-26
extra:
  source: https://sloonz.github.io/posts/wireguard-beyond-basic-configuration/
  original_title: Wireguard - Beyond the most basic configuration
---
## Summary
**摘要**：
文章作者通过亲身体验将他所学到的在 WireGuard 配置上超越基础设置的知识进行了分享。主要内容涵盖了如何配置 WireGuard 以替代 OpenVPN，强调了 WireGuard 的基本配置步骤，强调了UPnP 在解决 NAT 相关问题中的重要性，并深入讨论了如何配置 WireGuard 支持 IPv6，从而避免了 NAT 的引入，构建了更安全、简单的网络连接方案。文章还说明了如何通过防火墙规则来配置 WireGuard 的端口寻址和转发。

**要点总结**：
1. **基本配置步骤**：为服务器生成密钥对，并为每一客户端生成密钥对。选定为 vpn 使用的网络，并配置服务器和客户端的配置文件，包括 IP 地址、网络接口和密钥信息。通过命令启动服务器和客户端。
2. **解决 NAT 问题**：描述使用 UPnP 作为让应用程序，如 BitTorrent 客户端在受 NAT 限制的环境下仍能正常工作的解决方案。解释了背后的原理，并说明了 WireGuard 作为 NAT 代理机制在其基本配置下不支持 UPnP。
3. **安装和配置 miniupnpd**：添加了 miniupnpd 的安装和配置，以实现代理功能。需要在服务器上配置专门的文件（`miniupnpd.conf`）来协助适配外部 IP 地址和 WireGuard 网络之间的连接。
4. **IPv6 支持的优化配置**：作者利用本地提供的 IPv6 地址（不仅限于前缀 /48）改进 IPv6 配置并重绘数据流路径，通过前端 IP 同步了 IPv6 地址分发到客户端，直接使得客户端无需等待 UPnP 自动配置，从而实现端到端的 IPO堆积。
5. **端口映射和防火墙规则**：解释了如何通过防火墙规则（如 iptables）来配置 WireGuard 的端口寻址和转发，促进数据通过合适的路径传输，特别是在需要外网可达的应用程序中实现了高效的端口分发。
## Full Content
Title: Wireguard: Beyond the most basic configuration

URL Source: https://sloonz.github.io/posts/wireguard-beyond-basic-configuration/

Published Time: 2024-06-28T00:00:00Z

Markdown Content:
Last week I wanted to replace my OpenVPN setup with WireGuard. The basics were well-documented, going beyond the basics was a bit trickier. Let me teach you want I learned.

The basics
----------

But first, let’s summarize the basics. I have a server with a hosting provider that I want to use as a VPN server. I won’t delve into details here, since there are so many great explanations on the web already ([here](https://www.wireguard.com/quickstart/#nat-and-firewall-traversal-persistence), [here](https://www.wireguard.com/netns/), [here](https://volatilesystems.org/wireguard-in-a-separate-linux-network-namespace.html) or [here](https://wiki.archlinux.org/title/WireGuard)), let’s just make a quick summary of a simple setup, as a base for discussing the (slightly) more advanced usages I had to configure myself:

1.  Generate a keypair (private key/public key) for the server.
    
2.  Generate a keypair (private key/public key) for each client.
    
3.  Pick a network for the VPN (for me: `10.100.0.0/16`), an IP for the server (`10.100.0.1`) and the clients (`10.100.0.2`, `10.100.0.3`, etc.)
    
4.  Create the configuration for the server
    

```
[Interface]
Address = 10.100.0.1/24
PrivateKey = (redacted)
ListenPort = 51820
PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -A FORWARD -o %i -j ACCEPT; iptables -t nat -A POSTROUTING -o ens0 -j MASQUERADE
PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -D FORWARD -o %i -j ACCEPT; iptables -t nat -D POSTROUTING -o ens0 -j MASQUERADE

[Peer]
PublicKey = (redacted)
AllowedIPs = 10.100.0.2/32

[Peer]
PublicKey = (redacted)
AllowedIPs = 10.100.0.3/32
```

5.  Start the server, `wg up /etc/wireguard/wg0.conf`
    
6.  Create the configuration for the client
    

```
[Interface]
PrivateKey = (redacted)

[Peer]
PublicKey = (redacted)
Endpoint = my-server.example.com:51820
AllowedIPs = 0.0.0.0/0, ::/0
```

7.  Start the client: `wg up /etc/wireguard/wg0.conf`

(optionally, not pictured here: create a network namespace for your VPN, so your main connection still has a direct access to the internet, but you can put applications that want the VPN in the VPN network namespace).

NAT
---

Some applications (looking at you, BitTorrent client) do not play well behind a NAT. Unfortunately, your VPN (wireguard or not) acts as a NAT. One widely used method to work around those issues is UPnP.

UPnP solves two issues:

*   Your computer does not know its public address on the internet (from the point of view of an external system) ; behind a VPN, you public address is the address of the VPN server, not the address assigned to you by your ISP (your VPN software knows that address — but the rest of the system generally has absolutely no knowledge of it). And if that address is not known by your peer-to-peer software, it cannot communicate it to other peers.
    
*   Even if that address is known and correctly communicated to a peer, if you listen to a port (for example, TCP 8043), the peer will try to reach you on that port, but on your VPN server IP. For that connection to actually reach your computer, your VPN software will have to set up a port forwarding rule (from VPN server 8043 to your ISP-assigned IP address, port 8043 — in a real setup, the two ports may actually differ, but let’s keep it simple for that explanation). UPnP provides a way to do that.
    

Let’s show that (obviously) our simple WireGuard-based VPN setup does not provide UPnP (`external-ip` is a tool provided by `miniupnpc`, an UPnP client):

```
$ external-ip
No IGD UPnP Device found on the network !
```

That was expected. Wireguard, being a very simple kernel module, does not come with batteries included in the form of a UPnP server. We will have to do it manually. Thankfully, it is pretty straightforward:

1.  Install `miniupnpd` (on the server, obviously).
    
2.  Configure `miniupnpd`.
    
3.  Add `PostUp = systemctl start miniupnpd` and `PostDown = systemctl stop miniupnpd` in your wireguard configuration file.
    

The only non-trivial step here is configuring `miniupnpd`. All the action lies in `/etc/miniupnpd/miniupnpd.conf`. Here is what you have to configure:

*   `ext_ifname=ens0`: this is the internet-facing interface of your server (it may be different from `ens0`).
    
*   `listening_ip=wg0`: this is the wireguard network interface on your server.
    
*   `uuid=06df7440-dbac-404c-9c07-0b0dbfca609e`: use `uuidgen` to generate one. Or you can steal mine, it doesn’t matter, since everything happens in a private, non-routable network.
    
*   `allow 1024-65535 10.100.0.0/16 1024-65535`: this is where you specify your wireguard network (in my basic setup `10.100.0.0/16`).
    

Let’s check that it works:

```
$ external-ip
(redacted, but it correctly returned my server IP)
$ upnpc -n 10.100.0.2 8043 8043 tcp 300
external (redacted:server-ip):8043 TCP is redirected to internal 10.100.0.2:8043 (duration=300)
$ socat TCP-LISTEN:8043 STDIO
```

And on another machine:

```
$ socat TCP:(redacted:server-ip):8043 STDIO
```

You can see that the two `socat` instances can communicate with each other, passing through your VPN.

IPv6
----

You know what’s even better than supporting UPnP to work around the issues introduced that NAT ? Not having NAT. And the good news is, with IPv6, you actually can.

The few tutorials who actually explains how to setup IPv6 for a WireGuard-based VPN usually mirror the IPv4 setup: assign a private, non-routable network to it (`10.100.0.0/16` for IPv4 get translated to something like `fd00:dead:beef::/48` for IPv6), assign IP addresses in this network to the server and the clients, and add an `ip6tables` masquerade action.

We’re not going to do that. We can do better, and we will do better.

The first thing to notice is that my hosting provider has assigned to me a whole /48 network for my account (`2001:aaaa:bbbb::/48`), and a /56 (`2001:aaaa:bbbb:1000::1/56`) for my server. We can take advantage of that to assign different publicly routable IPv6 addresses to our clients, instead of assigning private, non-routable addresses.

Let’s start with the server configuration. Let’s add IPv6. We assign the /80 subnetwork `2001:aaaa:bbbb:1000:cafe::/80` to VPN network. I’ll only list added configuration lines, not repeating existing ones:

```
[Interface]
Address = 2001:aaaa:bbbb:1000:cafe::1/80

[Peer]
AllowedIPs = 2001:aaaa:bbbb:1000:cafe::2/128

[Peer]
AllowedIPs = 2001:aaaa:bbbb:1000:cafe::3/128
```

Client-side, this is not much more complicated:

```
[Interface]
Address = 2001:aaaa:bbbb:1000:cafe::2/128
```

Just one sanity check: on your server, `ip -6 route get 2001:aaaa:bbbb:1000:cafe::2` must return the WireGuard interface (`wg0`). If not, you will have to give a lower metric to `wg0` in your routes. But you can now, on your client, directly listen to a port:

```
$ socat TCP6-LISTEN:8043
```

and it will be accessible from the public internet without any UPnP setup:

```
$ socat TCP6:[2001:aaaa:bbbb:1000:cafe::2]:8043
```

Also, the IP address on the device of your default route will be `2001:aaaa:bbbb:1000:cafe::2`, meaning no need for UPnP to dectect your public, routable IPv6: your VPN interface IP (which is private in the IPv4 case, but now public for IPv6) is also your public IP.

