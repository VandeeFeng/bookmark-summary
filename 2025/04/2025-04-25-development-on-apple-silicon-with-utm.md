# Development On Apple Silicon with UTM
- URL: https://rkiselenko.dev/blog/development-on-mac-with-utm/development-on-mac-with-lima/
- Added At: 2025-04-25 02:46:22
- [Link To Text](2025-04-25-development-on-apple-silicon-with-utm_raw.md)

## Summary
**摘要**：
本文介绍了如何使用UTM虚拟机在Apple Silicon上创建Linux开发环境。UTM是一款允许在iOS设备上运行其他操作系统的应用。文章基于之前在Lima上的技术，首先通过Homebrew安装UTM和cdrtools（包含mkisofs工具，用于创建初始化VM的init.iso镜像）。接着，需要下载Fedora或Ubuntu的Cloud镜像，包括aarch64和x86_64架构的版本。文章详细展示了如何配置cloud-init脚本，以便在VM启动时自动安装开发所需的工具和设置，如git、jq、go和docker，并配置SSH密钥。cloud-init通过user-data文件定义用户、用户组、安装包和系统设置。通过mkisofs命令生成包含cloud-init配置的init.iso文件。在UTM中创建虚拟机时，选择"Emulate"模式，移除默认硬件，添加Serial接口，并导入Fedora的qcow2镜像和init.iso镜像。启动VM后，使用cloud-init中设置的用户名和密码登录，并等待初始化完成。最后，关闭虚拟机并移除init.iso驱动器。对于Apple Silicon，可以选择"Virtualize"模式，并使用arm64镜像。

**要点总结**：
1.  **UTM虚拟机配置**：UTM是一个在Apple Silicon上创建Linux开发环境的工具。通过安装UTM和依赖工具，可以模拟或虚拟化不同的操作系统。选择"Emulate"模式进行x86_64架构的模拟，或者选择"Virtualize"模式进行ARM架构的虚拟化，这取决于目标系统的架构和需求。
2.  **Cloud-Init自动化配置**：Cloud-init用于自动化配置虚拟机，通过`user-data`文件定义用户、密码、SSH密钥、软件包安装等。例如，可以预装git、jq、go、docker等常用开发工具，简化了手动配置过程，提高了效率。
3.  **init.iso镜像创建**：使用`mkisofs`工具将Cloud-init的`user-data`和`meta-data`文件打包成`init.iso`镜像，该镜像在VM首次启动时加载，用于自动化配置系统。这个过程类似于在物理服务器上使用Kickstart或Preseed文件进行自动化安装。
4.  **虚拟机硬件配置调整**：在UTM中创建虚拟机时，需要移除默认的Display和Sound设备，添加Serial接口，并移除默认硬盘，然后添加VirtiO类型的驱动器，并导入下载的qcow2镜像和init.iso镜像。VirtiO是一种虚拟化驱动框架，可以提供更好的性能和效率。
5.  **Apple Silicon平台的特殊配置**：对于Apple Silicon上的VM，应选择"Virtualize"模式，并使用arm64架构的cloud镜像。Ubuntu镜像需要先解压`*.img.xz`文件。与x86_64架构的配置不同，Ubuntu在ARM架构上通常不需要禁用UEFI启动。

