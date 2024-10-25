---
title: PabloNet-将反射转化为画作
date: 2024-10-25
extra:
  source: https://www.matthieulc.com/posts/pablonet/
  original_title: PabloNet-将反射转化为画作
---
## TL;DR
PabloNet 是一个结合了 AI 和艺术的创作项目，利用 webcam 视频和人工神经网络生成艺术图像。作者 Matthieu Lecauchois 用一个可挂壁的 LCD 框架来展示 AI 生成的作品。项目旨在探索 AI 创作独特艺术的可能性，虽然存在帧率问题，但已开源邀请社区参与和贡献。
## Summary
**摘要**

PabloNet 是一个结合了 AI 技术和艺术的创作项目，它通过使用 webcam 视频和人工神经网络来生成艺术图像。作者 Matthieu Lecauchois 在他的文章中描述了他如何利用 AI 生成艺术并将其展示在一个可以挂在墙上的 LCD 框架中。这个项目的灵感来自于探索 AI 是否可以像人类艺术家一样创作出独特的艺术作品。作者以他对艺术和 AI 的看法为基础，实现了一个具有新颖的艺术形式和互动方式的作品。

**要点总结**

1. **AI 生成艺术的可能性**：作者 Matthieu Lecauchois 认为，AI 技术可以帮助人类探索新的艺术形式和创作方式，他开发的 PabloNet 项目就是一个典型的例子。

    > PabloNet 是一个结合了 AI 技术和艺术的创作项目，它通过使用 webcam 视频和人工神经网络来生成艺术图像。

2. **LCD 框架的设计和实现**：为了展示 AI 生成的艺术作品，作者设计并制作了一个可以挂在墙上的 LCD 框架，可以提供一个更沉浸式的艺术体验。

    > 作者以他对艺术和 AI 的看法为基础，实现了一个具有新颖的艺术形式和互动方式的作品。

3. **提高帧率和性能**：虽然 PabloNet 项目成功实现了 AI 生成艺术，但目前仍然存在低帧率的问题，作者表示他正在研究提高帧率和性能的方法。

    > 作者表示他成功提高了帧率，但仍有很多潜力需要挖掘。

4. **开源和社区贡献**：PabloNet 项目的代码和详细信息已经开源，欢迎技术爱好者和艺术家参与和贡献。

    > 作者提供了详细信息和开源代码，方便其他人可以参考和参与他的项目。

5. **艺术和技术的融合**：PabloNet 项目是艺术和技术融合的例子，作者 Matthieu Lecauchois 期望可以开拓更多与艺术相关的新鲜可能性。

    > 作者 Matthieu Lecauchois 希望可以通过这样的探索，推动艺术和技术的创新与融合。
## Full Content
Title: PabloNet

URL Source: https://www.matthieulc.com/posts/pablonet/

Markdown Content:
![Image 1](https://www.matthieulc.com/posts/pablonet/main.jpeg)

The debate about whether internet-fitted AIs can be creative always seemed besides the point to me. Making art is hard. My view is that art is about surfacing the inner world, and only in part about skill. It’s unfortunate that art selects so strongly for skill. Can we decorrelate the two? It seems so. Cheap interpolative\* creativity used by 8 billion non-artists surely surfaces new views of the world.

For these reasons and since I suck at art I’ve been very excited about the various AI-driven art forms popping up. A couple of months ago I started playing with real-time diffusion of my webcam feed using [StreamDiffusion](https://github.com/cumulo-autumn/StreamDiffusion). Specifically, with the intent of generating pretty visuals and hoping to elicit new/interesting feelings. Although it’s very fun, the laptop form-factor breaks the illusion. It feels all temporary and geeky. So, I recently built an LCD frame that can be hanged to a wall with minimal illusion breakers. What I really like about this setup is that making it a proper object opens up new channels of interaction. It’s no longer just a screen, it has permanence. You can leave it there, come back to it at a different time, in a different mood, with different lighting, objects, friends, etc.

Infrared light in the dark

Plus, it looks pretty:

![Image 2](https://www.matthieulc.com/posts/pablonet/stairs.jpeg)

The main issue with the current setup is the low frame rate. I managed to increase it using TensorRT and compressing the images in and out, but there’s still a lot of room for improvement.

For those of you that are interested in creating your own or contributing, here are the details:

*   Code for the client and server [here](https://github.com/mlecauchois/pablonet).
*   [RunPod](https://www.runpod.io/) for hosting the server.
*   Client runs on a [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/).
*   This [10.1" Pi screen](https://www.amazon.fr/HMTECH-Raspberry-Moniteur-portable-Raspbian/dp/B098762GVK).
*   This [infrared light](https://www.amazon.fr/dp/B0BG5HM2Q8?ref=ppx_yo2ov_dt_b_fed_asin_title).
*   This generic [frame](https://www.leroymerlin.fr/produits/decoration-eclairage/decoration-murale/cadre-photo/cadre-noir/cadre-milo-21-x-29-7-cm-noir-inspire-71670942.html).
*   This infrared [Pi camera](https://www.raspberrypi.com/products/pi-noir-camera-v2/).
*   I used a puncher to cut a hole in the frame’s cardboard for the camera (drills didn’t work).
*   I spent hours playing with different preprocessing filters, not just prompting. In general I found the two to be equally important. Without preprocessing, img2img often looked too realistic. To get the blue Picasso style seen in this post, I ended up using a mix of canny edge detection, blue coloration and blurring.

![Image 3](https://www.matthieulc.com/posts/pablonet/behind.png)

![Image 4](https://www.matthieulc.com/posts/pablonet/closeup.png)

* * *

\*Technically, [learning in high dimension always amounts to extrapolation](https://arxiv.org/abs/2110.09485).

