---
title: Development On Apple Silicon with UTM
date: 2025-04-25
extra:
  source: https://rkiselenko.dev/blog/development-on-mac-with-utm/development-on-mac-with-lima/
  original_title: Development On Apple Silicon with UTM
---
## Summary
**摘要**：
本文介绍了如何使用UTM虚拟机在Apple Silicon上创建Linux开发环境。UTM是一款允许在iOS设备上运行其他操作系统的应用。文章基于之前在Lima上的技术，首先通过Homebrew安装UTM和cdrtools（包含mkisofs工具，用于创建初始化VM的init.iso镜像）。接着，需要下载Fedora或Ubuntu的Cloud镜像，包括aarch64和x86_64架构的版本。文章详细展示了如何配置cloud-init脚本，以便在VM启动时自动安装开发所需的工具和设置，如git、jq、go和docker，并配置SSH密钥。cloud-init通过user-data文件定义用户、用户组、安装包和系统设置。通过mkisofs命令生成包含cloud-init配置的init.iso文件。在UTM中创建虚拟机时，选择"Emulate"模式，移除默认硬件，添加Serial接口，并导入Fedora的qcow2镜像和init.iso镜像。启动VM后，使用cloud-init中设置的用户名和密码登录，并等待初始化完成。最后，关闭虚拟机并移除init.iso驱动器。对于Apple Silicon，可以选择"Virtualize"模式，并使用arm64镜像。

**要点总结**：
1.  **UTM虚拟机配置**：UTM是一个在Apple Silicon上创建Linux开发环境的工具。通过安装UTM和依赖工具，可以模拟或虚拟化不同的操作系统。选择"Emulate"模式进行x86_64架构的模拟，或者选择"Virtualize"模式进行ARM架构的虚拟化，这取决于目标系统的架构和需求。
2.  **Cloud-Init自动化配置**：Cloud-init用于自动化配置虚拟机，通过`user-data`文件定义用户、密码、SSH密钥、软件包安装等。例如，可以预装git、jq、go、docker等常用开发工具，简化了手动配置过程，提高了效率。
3.  **init.iso镜像创建**：使用`mkisofs`工具将Cloud-init的`user-data`和`meta-data`文件打包成`init.iso`镜像，该镜像在VM首次启动时加载，用于自动化配置系统。这个过程类似于在物理服务器上使用Kickstart或Preseed文件进行自动化安装。
4.  **虚拟机硬件配置调整**：在UTM中创建虚拟机时，需要移除默认的Display和Sound设备，添加Serial接口，并移除默认硬盘，然后添加VirtiO类型的驱动器，并导入下载的qcow2镜像和init.iso镜像。VirtiO是一种虚拟化驱动框架，可以提供更好的性能和效率。
5.  **Apple Silicon平台的特殊配置**：对于Apple Silicon上的VM，应选择"Virtualize"模式，并使用arm64架构的cloud镜像。Ubuntu镜像需要先解压`*.img.xz`文件。与x86_64架构的配置不同，Ubuntu在ARM架构上通常不需要禁用UEFI启动。

## Full Content
Title: Development On Apple Silicon with UTM

URL Source: https://rkiselenko.dev/blog/development-on-mac-with-utm/development-on-mac-with-lima/

Markdown Content:
*   17 April 2025
*   [vm](https://rkiselenko.dev/tags/vm/),
*   [utm](https://rkiselenko.dev/tags/utm/),
*   [arm](https://rkiselenko.dev/tags/arm/),
*   [macbook](https://rkiselenko.dev/tags/macbook/),
*   [apple silicon](https://rkiselenko.dev/tags/apple-silicon/)

"UTM is an app for running other operating systems on your iPhone or iPad. It is not for running iOS on other systems. This allows you, among other things, to run Windows or Linux on your iOS device at a usable speed." – UTM Website

![Image 1](https://rkiselenko.dev/img/_LgTXEGM9x-900.jpeg)

In this article, I'll show you how to use [UTM VMs](https://getutm.app/) virtual machines to create Linux development environments on Apple Silicon.

This approach builds on the technique I described in [here](https://rkiselenko.dev/blog/development-on-mac-with-lima).

### Dependencies [#](https://rkiselenko.dev/blog/development-on-mac-with-utm/development-on-mac-with-lima/#dependencies)

First, install UTM using Homebrew: `brew install --cask utm`.

Then, install `brew install cdrtools`, which provides `mkisofs`. We'll use that tool to create an `init.iso` - our seed script for initializing the VM.

We need a bunch of tools and images.

*   Fedora Cloud images [mirror.bahnhof.net](https://mirror.bahnhof.net/pub/fedora/linux/releases/).
    
    1.  `aarch64` [Fedora-Cloud-Base-Generic-42-1.1.aarch64.qcow2](https://mirror.bahnhof.net/pub/fedora/linux/releases/42/Cloud/aarch64/images/Fedora-Cloud-Base-Generic-42-1.1.aarch64.qcow2)
    2.  `x86_64` [Fedora-Cloud-Base-Generic-42-1.1.x86\_64.qcow2](https://mirror.bahnhof.net/pub/fedora/linux/releases/42/Cloud/x86_64/images/Fedora-Cloud-Base-Generic-42-1.1.x86_64.qcow2)
*   Ubuntu Cloud images [cdimage.ubuntu.com](https://cdimage.ubuntu.com/ubuntu-server/daily-preinstalled/current).
    
    1.  `aarch64` [plucky-preinstalled-server-arm64.img.xz](https://cdimage.ubuntu.com/ubuntu-server/daily-preinstalled/current/plucky-preinstalled-server-arm64.img.xz)
    2.  `x86_64` [plucky-preinstalled-server-amd64.img.xz](https://cdimage.ubuntu.com/ubuntu-server/daily-preinstalled/current/plucky-preinstalled-server-amd64.img.xz)

### Cloud-Init [#](https://rkiselenko.dev/blog/development-on-mac-with-utm/development-on-mac-with-lima/#cloud-init)

We’ll use [cloud-init](https://cloudinit.readthedocs.io/en/latest/index.html) scripts to bootstrap the VM with the tools and settings needed for development - things like `git`, `jq`, `go`, `docker`, and more. We'll also use it to provision an SSH key for easy access.

**user-data**

```
#cloud-config

system_info:
   default_user:
     name: fedora

users:
  - name: fedora
    sudo: ['ALL=(ALL) NOPASSWD:ALL']
    groups: users, admin, docker
    shell: /bin/bash

ssh_authorized_keys:
   - ssh-rsa AAAAB3Nza...

groups:
  - docker

packages:
  - curl
  - wget
  - git
  - jq
  - gcc
  - clang

chpasswd:
  list: |
    fedora:password
  expire: False

resize_rootfs: True

write_files:
  - path: /etc/sysctl.d/enabled_ipv4_forwarding.conf
    content: |
      net.ipv4.conf.all.forwarding=1
  - path: /opt/go.sh
    owner: fedora:fedora
    permissions: '0700'
    content: |
      #!/usr/bin/env bash
      set -ex
      wget https://go.dev/dl/go1.24.1.linux-amd64.tar.gz -O go.tar.gz
      sudo tar -C /usr/local -xzvf go.tar.gz
      rm -rf go
      echo 'export GOROOT=/usr/local/go' >> /home/fedora/.bashrc
      echo 'export GOPATH=$HOME/.go' >> /home/fedora/.bashrc
      echo 'export PATH=$GOPATH/bin:$GOROOT/bin:$PATH' >> /home/fedora/.bashrc
runcmd:
  - [dnf, config-manager, addrepo, --from-repofile="https://download.docker.com/linux/fedora/docker-ce.repo"]
  - [dnf, install, docker-ce, docker-ce-cli, containerd.io]
  - [systemctl, enable, --now, docker]
  - /opt/go.sh
```

Generate `init.iso` (`mkisofs` is a part of `cdrtools`):

```
touch meta-data # going to be empty
mkisofs -output init.iso -volid cidata -joliet -rock {user-data,meta-data}
```

### Create VM [#](https://rkiselenko.dev/blog/development-on-mac-with-utm/development-on-mac-with-lima/#create-vm)

Create VM, chose Emulate:

![Image 2](https://rkiselenko.dev/img/33dhKW_moC-900.jpeg)

Chose Other:

![Image 3](https://rkiselenko.dev/img/eRe6E24zN4-900.jpeg)

No changes in Hardware:

![Image 4](https://rkiselenko.dev/img/x-GhIz-RzX-900.jpeg)

Use `8GB` disk, we dont need it and will remove it later.

In Summary name the VM and check `Open VM Settings`:

![Image 5](https://rkiselenko.dev/img/XyFnZeSbG_-900.jpeg)

Uncheck `UEFI Boot`:

![Image 6](https://rkiselenko.dev/img/XC6rVytqkq-900.jpeg)

Remove `Display`, `Sound` with rigth mouse click, and add `Serial` -\> `Built-In`:

![Image 7](https://rkiselenko.dev/img/YPTDgqEhFk-900.jpeg)

Remove created `Drive`, and add new one `VirtiO`, `Import` the [Fedora-Cloud-Base-Generic-42-1.1.x86\_64.qcow2](https://rkiselenko.dev/blog/development-on-mac-with-utm/development-on-mac-with-lima/#dependencies)

![Image 8](https://rkiselenko.dev/img/mLLwXLEswf-490.jpeg)

![Image 9](https://rkiselenko.dev/img/7r6y5QrvrR-900.jpeg)

Create another one `Drive` -\> `VirtiO`, import the [init.iso](https://rkiselenko.dev/blog/development-on-mac-with-utm/development-on-mac-with-lima/#dependencies-for-vm)

![Image 10](https://rkiselenko.dev/img/4JspUqD-is-900.jpeg)

Run VM, if everything goes right you'll see boot terminal, like on the image below:

![Image 11](https://rkiselenko.dev/img/NRbwvJX1q_-900.jpeg)

Wait until the login screen appears. The default username is fedora and the password is password, as defined in our cloud-init script.

Give it a moment after logging in [cloud-init script.](https://rkiselenko.dev/blog/development-on-mac-with-utm/development-on-mac-with-lima/#cloud-init) will need some time to finish setting everything up.

![Image 12](https://rkiselenko.dev/img/B_-08aAIMK-900.jpeg)

After the VM has finished initializing, power it off and remove the init.iso drive—it only needs to run during the first boot.

You can check the output of the cloud-init scripts with `sudo cat /var/log/cloud-init-output.log`

Tip:

To create a VM for Apple Silicon (aarch64), follow these steps:

*   Choose `Virtualize`, since Apple Silicon is ARM-based.
*   Use `arm64` cloud images.
*   For Ubuntu, the process is almost the same - except you don’t need to disable UEFI boot.
*   Don’t forget to extract the `*.img.xz` file before using it.

Happy coding!

*   Previous: [Use CRI-O Container Runtime with KIND](https://rkiselenko.dev/blog/crio-in-kind/)

