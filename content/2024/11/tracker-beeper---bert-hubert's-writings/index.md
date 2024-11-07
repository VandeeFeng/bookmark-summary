---
title: Tracker Beeper - Bert Hubert's writings
date: 2024-11-07
extra:
  source: https://berthub.eu/articles/posts/tracker-beeper/
  original_title: Tracker Beeper - Bert Hubert's writings
---
## Summary
**摘要**：
Bert Hubert 在过去一周上线了一款名为“Tracker Beeper”的工具，它能让用户听到每次向 Google 发送数据时计算机发出的声响。通过这个工具，人们可以直观地看到，即使是在没有明确授权的情况下，很多网站会自动将用户的点击行为传送给 Google 及其他追踪器如 Facebook。这个工具在 Bert Hubert 的推特中发售后受到广泛的注意，仅一周内便获得了百万级的观看量。Bert Hubert 表示下一步将为这个工具添加对其他平台和设备的支持，如 Windows，iOS 和 Android，并计划创建一台基于 Raspberry Pi 的现场演示设备，让用户在实际体验中直观地感受到追踪器的运行情况。

**要点总结**：
1. **工具原理**：Bert Hubert 开发的“Tracker Beeper”工作原理是针对每次向特定服务，如 Google 或 Facebook 发送数据的行为触发计算机发出声音警报，帮助用户直观感知数据传输过程。
2. **工具可行性及限制**：目前，该工具适用于 Linux、OSX 与 BSD 用户，并且可通过命令行操作。Bert Hubert 计划未来为 Linux 系统完成更多功能，后续开发包括支持 Apple（OSX）与 Windows 系统，以及手机和安卓设备的支持。但是进一步实现 iOS 和 Android 版本成为可能但困难，因这些系统可能出于隐私考虑倾向于让用户的设备上传数据。
3. **现场演示计划**：Bert Hubert 提议使用 Raspberry Pi 结合另一部手机提供互联网连接创建现场演示设备，实现用户扫描 QR 条码后即时收到跟踪器声音通知的体验。这一概念尤为适用于容易泄露数据的 Android 设备，以增强观察公共区域或会议中数据传输的直观效果。
4. **未来目标**：Bert Hubert 的长远目标包括扩大工具兼容的追踪器应用范围，并让用户可根据需求配置需要监听的追踪器，同时探索定制警报声音功能（可能是立体声配置，如 Google 位于中心，Facebook 在右侧等）。
5. **社区协作**：Bert Hubert 邀请愿意共同助力实现现场演示设备的个人或团队参与。实现这一目标所需的基本硬件包括一台 Raspberry Pi 和另一部用于连接互联网的设备。
## Full Content
Title: Tracker Beeper - Bert Hubert's writings

URL Source: https://berthub.eu/articles/posts/tracker-beeper/

Published Time: 2022-08-29T10:45:14+02:00

Markdown Content:
A week ago, I finally got round to implementing an idea I’d been toying with for years: what if your computer made a little bit of noise every time it sent data to Google?

From studying logs, I’d long known just how many sites send all your visits and clicks to (at least) Google, but a log that you have to manually create first and then analyze is not very dramatic. You need to work on it and finally you think “well yeah that is a lot”.

 Sorry, your browser doesn't support embedded videos.

The video above beeps only on Google, and it shows how the [official Dutch government jobs site](https://werkenvoornederland.nl/) (which also advertises for the intelligence and security services) sends your every click to Google - despite never asking for your permission to do so. It also reports to Google if you clicked the button “apply for this job”, or even “call us for information”. Nice.

I announced the tool in a tweet:

![Image 1](https://berthub.eu/articles/beeper-tweet.png)

And within a week, the video received a million views. This spurred me on to add support for Facebook and dozens of the other trackers that infest our sites. Behold the noise when you visit some well known news sites:

 Sorry, your browser doesn't support embedded videos.

*   [RTLNieuws.nl](https://www.rtlnieuws.nl/tech/artikel/5329774/google-tracking-klikker-googerteller-bert-hubert-privacy-online)
*   [9to5Google](https://9to5google.com/2022/08/22/app-beeps-send-data-google/)
*   [it-daily.net](https://www.it-daily.net/shortnews/google-teller-browser-plugin-macht-ein-geraeusch-wenn-google-daten-erhaelt)
*   [Stadt Bremerhaven](https://stadt-bremerhaven.de/googerteller-app-piept-jedes-mal-wenn-der-rechner-daten-an-google-uebertraegt/)
*   [Tarnkappe.info](https://tarnkappe.info/artikel/datenschutz/googerteller-dem-datenkraken-auf-der-spur-254630.html)

Status of the software
----------------------

For now, [it is still pretty rough stuff](https://github.com/berthubert/googerteller), suitable only for Linux, OSX and BSD users comfortable entering command lines. The goals are:

1.  Continue development on Linux until the necessary features are implemented and stable
2.  Perhaps simultaneously make an Apple / OSX version available that runs with a single click
3.  Create a Windows version
4.  Perhaps perhaps try to implement something similar on iOS and Android, which will not be easy: phones prefer to snitch on you in full privacy

Live demo installation
----------------------

I would also **love** to turn this into a live demo for use on phones and tablets. The idea would then be to have a low power WiFi network. There’s a big QR code (on a poster or a big screen). If you scan that, your phone asks you if you want to join the demo WiFi.

And when you do and use your phone, big speakers make the tracker noises. For extra points, make one speaker per tracker, so a huge Google speaker, one for Facebook and dozens of smaller ones.

Especially Android phones leak information 24/7 so this should be a pretty convincing demo.

If anyone wants to help make this happen, let me know. All it requires is a Raspberry Pi and another phone to deliver internet connectivity.

Further Goals
-------------

*   Support all popular trackers
*   Configurable which ones you want to hear about
*   With configurable sounds (also in stereo, so “google” in the middle, “Facebook” on the right speaker)

