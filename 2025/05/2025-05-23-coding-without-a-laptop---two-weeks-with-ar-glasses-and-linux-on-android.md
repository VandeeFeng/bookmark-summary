# Coding Without a Laptop - Two Weeks with AR Glasses and Linux on Android
- URL: https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/
- Added At: 2025-05-23 05:59:40
- [Link To Text](2025-05-23-coding-without-a-laptop---two-weeks-with-ar-glasses-and-linux-on-android_raw.md)

## Summary
**摘要**：
这篇文章详细记录了作者如何在安卓手机上通过chroot容器运行完整的桌面Linux环境，并结合AR眼镜和折叠键盘实现移动开发的体验。作者选择了Pixel 8 Pro手机、Xreal Air 2 Pro AR眼镜和折叠键盘组成便携系统，总成本约636美元。该方案的优势在于超便携性（可放入口袋）、户外使用的阳光可视性、狭小空间适应性以及蜂窝网络连接能力。作者使用Void Linux的aarch64 glibc版本作为基础系统，搭配i3窗口管理器，成功运行了包括Neovim、Flutter等开发工具。虽然存在眼镜视野调节、键盘质量等痛点，但整体性能接近中端笔记本，电池续航约4-5小时。经过两周实际使用，作者认为这种方案为开发者提供了传统笔记本无法实现的移动自由度，展现了超移动开发的潜力。

**要点总结**：
1. **智能手机运行完整Linux环境的可行性**：通过Android的chroot容器技术运行原生arm64二进制程序，使用Void Linux的aarch64 glibc版本作为轻量级发行版，配合i3窗口管理器实现完整的桌面Linux开发环境，包括Neovim、Flutter等工具链。

2. **便携硬件组合的优势**：Pixel 8 Pro手机（支持DisplayPort Alt模式）、Xreal Air 2 Pro AR眼镜（1080p OLED显示）和折叠键盘组成的系统完全可放入口袋，在户外阳光、飞机座位等传统笔记本使用受限的场景下表现出色，同时保持蜂窝网络连接能力。

3. **技术实现的挑战与选择**：经过虚拟机、Termux、proot等多种方案比较后，最终选择需要root权限的chroot方案，因其性能最好且兼容性最强，能运行标准arm64编译的软件，而其他方案在速度或兼容性上存在明显局限。

4. **实际使用体验与限制**：系统性能接近中端笔记本（如Nim编译测试耗时11分20秒），但AR眼镜存在视野范围调节困难、键盘质量欠佳等问题；电池续航约4-5小时，适合短时移动办公，提供了传统笔记本无法实现的场景灵活性。
