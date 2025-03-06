# Tailscale is pretty useful
- URL: https://blog.6nok.org/tailscale-is-pretty-useful/
- Added At: 2025-03-06 14:34:20
- [Link To Text](2025-03-06-tailscale-is-pretty-useful_raw.md)

## Summary
**摘要**：
作者分享了自己使用Tailscale的体验。起初，作者想通过DDNS访问家里的树莓派服务器，但因CGNAT的限制而失败。于是，作者尝试使用Tailscale，它创建了一个虚拟专用网络(VPN)，使得可以随时通过Tailscale生成的域名简写访问设备。虽然旧的树莓派性能不足以运行Tailscale，但这个经历让体会到了Tailscale的便利。使用Tailscale，可以将笔记本电脑的端口暴露给手机，方便web应用开发时的真机调试，摆脱了对ngrok的依赖。Taildrop功能可以像Airdrop一样轻松地在设备间传输文件，解决了在Macbook和Windows HTPC之间传输文件的难题。此外，Tailscale还可以设置出口节点，使之具有VPN的功能，甚至可以通过与Mullvad的合作，实现类似于iCloud Private Relay的双层VPN，提升隐私性。作者目前仅在个人用途上使用了Tailscale的免费套餐，并提到Headscale这个开源的服务器实现方案。

**要点总结**：

1.  **虚拟专用网络(VPN)访问**: Tailscale创建了一个虚拟专用网络，允许用户通过Tailscale生成的域名简写从任何地方安全地访问其设备，解决了传统DDNS方案在CGNAT环境下的问题。虚拟专用网络通过加密和隧道技术，为用户创建一个安全的网络连接，使其能够安全地访问位于其他网络上的资源，就像设备直接连接到目标网络一样。

2.  **便捷的端口暴露和真机调试**: Tailscale允许将本地开发服务器的端口暴露给移动设备，从而简化了web应用在实际设备上的测试过程。这避免了对ngrok等工具的依赖，开发者可以直接通过Tailscale生成的域名在手机或平板电脑上访问本地服务器，实时调试和预览应用效果。

3.  **Taildrop文件传输**: Taildrop功能实现了类似于Airdrop的便捷文件传输体验，用户可以在不同设备之间轻松共享文件，无需依赖局域网或复杂的设置。这项功能特别适用于在不同操作系统的设备之间传输文件，例如在Macbook和Windows电脑之间共享文件。

4.  **出口节点和隐私保护**: Tailscale允许用户指定一个机器作为出口节点，从而实现VPN的功能，用户可以选择位于不同国家/地区的服务器作为出口，突破地域限制。通过与Mullvad的合作，Tailscale提供了一种双层VPN的方案，类似于iCloud Private Relay，Tailscale无法看到用户的流量，而Mullvad不知道用户的身份，从而增强了隐私保护。

