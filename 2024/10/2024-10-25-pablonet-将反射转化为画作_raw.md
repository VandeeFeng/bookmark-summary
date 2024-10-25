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
