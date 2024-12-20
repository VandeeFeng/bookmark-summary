---
title: 基础设施即代码 IaC 初探 - Ansible 与 Terraform
date: 2024-12-20
extra:
  source: https://blog.lyc8503.net/post/iac-explore-ansible-and-terraform/
  original_title: 基础设施即代码 IaC 初探 - Ansible 与 Terraform
---
## Summary
**摘要**：
文章通过实践探究了基于基础设施即代码（IaC）的自动化部署方法，重点讨论了Ansible和Terraform在不同场景下的应用。作者从简单的Linux VPS配置转向更复杂的云服务管理，发现Ansible提供了灵活而优雅的集中式资源管理方式，适合操作常用的Linux服务器环境。对于涉及云服务（如Cloudflare Workers等）的场景，Terraform则凭借其代码定义远程基础设施地特性展现出直接管理云资源的优势，能够简化配置和部署流程。

**要点总结**：
1. **Ansible简介**：Ansible是无需Agent的远程管理工具，通过SSH连接控制远程Linux服务器。作者展示了在Ansible中的任务定义格式，包括安装所需软件、更新配置文件到应用服务启动，实现了简单、幂等的配置流程。

2. **Ansible优点**：相比Docker Compose和Bash脚本，Ansible的YAML语法简洁明了，易于维护且具有全局一致性。此外，Ansible可直接操控服务器配置和元数据，提供模块化的扩展能力，通过使用如geerlingguy docker角色来方便地安装软件。这使得Ansible在高效、方便地配置和运维Linux VPS场景下具有显著优势。

3. **Terraform简介**：Terraform提供了另一种方法，通过代码定义并自动更新云基础结构的状态，简化了与第三方云服务（如Cloudflare）的交互，避免了繁琐的手动配置。通过提供丰富的provider和用例示例，Terraform创造了低门槛的云环境配置体验。

4. **Terraform优点**：引入Terraform使得云服务配置和部署自动化成为可能，通过对基础设施状态的代码化管理，大幅减少了错误发生并提高了工作效率。此工具使复杂的云基础设施部署和管理流程简化，即使针对非标准如Cloudflare Workers等服务，也可轻松实现一键式部署，提高用户体验。

5. **整合IaC优势**：综上所述，Ansible和Terraform各自特色使得其在自动化部署、基础设施配置管理等方面展现出独特优势。借助IaC方案，不仅提高了部署效率与安全性，也简化了基础设施的维护操作，为个人开发者提供了理想的技术方案。这些工具有助于提高生产力，促进高效、自助式的云资源管理。

---

以上总结概括了文章的主要内容与作者体验，强调了Ansible和Terraform在不同场景下的功能特点与解决方案，强调了基础设施即代码IaC的重要性。
## Full Content
Title: 基础设施即代码 IaC 初探 - Ansible 与 Terraform

URL Source: https://blog.lyc8503.net/post/iac-explore-ansible-and-terraform/

Published Time: 2023-11-18T04:47:38.000Z

Markdown Content:
基础设施即代码 IaC 初探 - Ansible 与 Terraform
LYC8503  2023-11-18 软件研究=) › 服务器维护&配置der日常

很久以前就听说过了 基础设施即代码 (Infrastructure-as-Code, 缩写 IaC) 的做法, 最近正好有不错的机会实践了一下, 写此文以记录.

背景

我现有的基础设施主要是我的 HomeLab 和阿里云的一些 Serverless 服务, 两者之前都有相关的博客提到过, 现在都处于稳定运行状态, 相对不需要大的变动.

不过我还有些必要的辅助服务需要在海外 VPS 上运行, 主要出于网络连接性和成本的考量, VPS 提供商可能会时不时更换. 每次给服务器搬家相对就比较麻烦了.

简单粗暴一点的做法是编写一个 Docker Compose 文件或者 bash 脚本, 每次拿到新 VPS 安装一下 docker 就算搞定了. 不过 Ansible 似乎是一种更加优雅的解决方案, 故来尝试一下.

Ansible - 无需 Agent 远程设置 Linux 服务器

在一台新的 Linux VPS 上配环境和安装需要的软件不算什么难事, 但如果要多次配置/迁移或者一次配置多台机器就是件麻烦事了.

Ansible 的官方文档可以说是比较清晰易懂的, 阅读一遍就能基本掌握 Ansible 的常见用法.

如果使用了 Ansible 配置流程大概是这样:

在本地机器安装 Ansible
在本地机器配置 inventory(VPS 连接信息), 编写 playbook(VPS 的目标状态)
本地执行 playbook, Ansible 直接通过 SSH 协议连接并操控 VPS, 使得 VPS 达到 playbook 中定义的状态.

大概感受一下 playbook 的样子:

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
18
19

	
---
- name: Install nginx package
  package:
    name:
      - nginx
    state: present

- name: Update nginx config
  ansible.builtin.template:
    src: templates/nginx.conf.j2
    dest: /etc/nginx/sites-available/default
  notify:
    - Restart nginx

- name: Start nginx
  ansible.builtin.systemd_service:
    name: nginx
    state: started
    daemon_reload: true


上面是一个配置 Nginx 服务的 task 定义: 第一步确保 Nginx 包已安装, 第二步更新 Nginx 站点配置文件(如果配置更新还需要重启 Nginx), 第三步确保 Nginx 已经启动, 就是这么简单~

相比 Docker Compose, Ansible 更加灵活和方便, 可以直接操作主机的各项配置, 并且也可以使用 Ansible 安装并启动 Docker, 两者并不冲突.

相比直接使用 Bash 脚本, Ansible 使用更加优雅的 yaml 并且是”幂等”的, 多次执行不会造成冲突, 修改起来远比 Bash 脚本方便.

同时 Ansbile 提供了名为 galaxy 的一个 registry, 可以直接使用他人写好的模块 (Role), 比如在服务器上安装 Docker 和 Docker Compose 只需要这么写:

1
2
3
4
5
6
7
8
9

	
---
- include_role:
    name: geerlingguy.docker
- include_role:
    name: geerlingguy.pip
  vars:
    pip_install_packages:
      - name: docker
      - name: docker-compose


很多常见的功能都能以模块的形式导入, 不需要再手动编写和维护, 并具有一定的跨发行版运行的能力.

如果我服务器发生迁移, 现在我只需要修改 inventory 文件, 重新执行当前的 playbook, VPS 就会部署好全部的服务, 大幅提高了效率并降低了犯错的可能性, 也给我更强的信心和灵活度去调整我的基础设施.

目前我 VPS 的 playbook 已经开源. IaC 也可以直接利用现有的代码版本控制工具 (如 git) 来进行管理, 方便多人协同和历史追溯.

Terraform - 使用代码定义云上基础架构

Ansible 主要解决了 Linux VPS 部署的问题, 但云上的很多基础架构也不是以 Linux 虚拟机的形式提供的.

比如最近我在 GitHub 上开源的 UptimeFlare 就使用了 Cloudflare Workers / KV / Pages 这几个服务, 写部署文档的时候发现… 部署真的好麻烦, 得登录 Cloudflare 的 Dashboard 点一大堆按钮, 完全不想写这种又臭又长的文档. 本来想写个 bash 脚本进行一键部署, 发现 wrangler (Cloudflare 的部署工具) 也缺一堆参数和文档, 还是得配合手动操作, 还是非常麻烦.

于是懒惰又一次成为了生产力的来源, 正好刚研究完 Ansible, 就发现了 Terraform 这个工具.

Terraform 同样是通过代码定义云上基础设施的状态, Terraform 会自己保证云上的状态与用户的定义一致.

Cloudflare 官方也提供了 Terraform 的文档, 每个云厂商有自己的 provider 和相关文档, Terraform 本身的语言也十分简单, 按照文档依葫芦画瓢就能完成配置.

同样是上一段代码感受一下:

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
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59

	
terraform {
  required_providers {
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = "~> 4"
    }
  }
}

provider "cloudflare" {
  # read token from $CLOUDFLARE_API_TOKEN
}

variable "CLOUDFLARE_ACCOUNT_ID" {
  # read account id from $TF_VAR_CLOUDFLARE_ACCOUNT_ID
  type = string
}

resource "cloudflare_workers_kv_namespace" "uptimeflare_kv" {
  account_id = var.CLOUDFLARE_ACCOUNT_ID
  title      = "uptimeflare_kv"
}

resource "cloudflare_worker_script" "uptimeflare" {
  account_id         = var.CLOUDFLARE_ACCOUNT_ID
  name               = "uptimeflare_worker"
  content            = file("worker/dist/index.js")
  module             = true
  compatibility_date = "2023-11-08"

  kv_namespace_binding {
    name         = "UPTIMEFLARE_STATE"
    namespace_id = cloudflare_workers_kv_namespace.uptimeflare_kv.id
  }
}

resource "cloudflare_worker_cron_trigger" "uptimeflare_worker_cron" {
  account_id  = var.CLOUDFLARE_ACCOUNT_ID
  script_name = cloudflare_worker_script.uptimeflare.name
  schedules = [
    "*/2 * * * *", # every 2 minutes
  ]
}

resource "cloudflare_pages_project" "uptimeflare" {
  account_id        = var.CLOUDFLARE_ACCOUNT_ID
  name              = "uptimeflare"
  production_branch = "main"

  deployment_configs {
    production {
      kv_namespaces = {
        UPTIMEFLARE_STATE = cloudflare_workers_kv_namespace.uptimeflare_kv.id
      }
      compatibility_date  = "2023-11-08"
      compatibility_flags = ["nodejs_compat"]
    }
  }
}


基本上就是不同的块定义不同的资源, 传入文档中指定的参数就行了.

随后直接在本地执行 terraform init 和 terraform plan 就能规划出需要的更改.

执行 terraform apply 就能将列出的更改应用到云, 随后基础设施有修改, 只要修改代码再次 terraform apply 就能应用新的更改.

在我这个使用场景, 我就不用写很长很繁琐的文档教用户怎么部署了, 直接让用户提供 API Token 即可自动部署~

小结

IaC 的一些初体验就是这样了, 果然懒才是第一生产力, Ansible 和 Terraform 入门门槛很低, 配置简单, 个人开发者使用也不会像某些所谓的”企业级”方案一样繁琐(aka. 脱裤子放屁), 优势是能提供更高的一致性和可拓展性, 同时可以省去很多繁杂的手动操作步骤提高效率.

本文采用 CC BY-NC-SA 4.0 许可协议发布.

作者: lyc8503, 文章链接: https://blog.lyc8503.net/post/iac-explore-ansible-and-terraform/
如果本文给你带来了帮助或让你觉得有趣, 可以考虑赞助我¬_¬

Copyright © 2018-2024 lyc8503
HomeAboutWritingCategoryFriendsSearch

