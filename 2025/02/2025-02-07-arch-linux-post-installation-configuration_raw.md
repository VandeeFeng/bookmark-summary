Title: Arch Linux Post-Installation Configuration | ejmastnak

URL Source: https://ejmastnak.com/tutorials/arch/about/

Markdown Content:
**What you’re reading:** Bite-sized, actionable tutorials to help you set up a functional work environment after a minimal install of Arch Linux. The material should be applicable, with adjustments to package installation, to most `systemd`\-based Linux distros.

**Purpose:** improve the transition and onboarding experience for new users.

**What about the ArchWiki?** (click to expand)

I’ve tried to address the following issue: the ArchWiki, kind of like the Unix `man` pages, is the best place to go when you know what you’re doing and what you’re looking for, but can be intimidating to new users because of the sheer amount of information, the lack of strong opinions on how to approach a given topic, and the need to read multiple cross-linked articles before fully understanding a concept.

This series is _intentionally_ opinionated, and leans towards a minimalistic setup of the i3 window manager with the X Window System. It aims to make you quickly functional by teaching atomic tasks in self-contained, immediately actionable articles.

Spending hours hopping through the ArchWiki’s cross-referenced articles is great—that’s how I learned myself—but in hindsight I’d argue that it’s not excessive hand-holding to first walk a new user through reliably connecting to the Internet, using their monitor, copying and pasting text, and confidently performing the handful of other basic, generally taken-for-granted tasks needed to find your footing on Arch Linux.

**X11 Warning:** most of these tutorials involve the X Window System in one form or another, so Wayland users may have to look elsewhere.

Useful basics
-------------

[**Make Caps Lock useful**](https://ejmastnak.com/tutorials/arch/caps2esc/)  
Remap your Caps Lock key to Escape when pressed alone and Control when pressed in combination with other keys. Your pinky will thank you.

[**Network**](https://ejmastnak.com/tutorials/arch/network-manager/)  
Connect to the Internet via WiFi or Ethernet using NetworkManager.

[**X Window System**](https://ejmastnak.com/tutorials/arch/startx/)  
Set up a minimal graphical environment using the Xorg display server and the i3 window manager.

[**USB**](https://ejmastnak.com/tutorials/arch/usb/)  
Read from, write to, and safely eject external USB drives.

[**Battery alert**](https://ejmastnak.com/tutorials/arch/battery-alert/)  
Get a desktop notification to _Charge your battery!_ for low battery levels.

[**Copy and paste**](https://ejmastnak.com/tutorials/arch/copy-paste/)  
A unified clipboard experience across your GUI applications, the Alacritty terminal, and Vim.

[**Type faster**](https://ejmastnak.com/tutorials/arch/typematic-rate/)  
Change your typematic rate and typematic delay—basically make pressed-down keys repeat faster—in X and in the console.

Graphics
--------

[**Control laptop backlight brightness**](https://ejmastnak.com/tutorials/arch/backlight/)  
Change your laptop’s backlight brightness with your keyboard function keys.

[**External monitor I: First steps**](https://ejmastnak.com/tutorials/arch/displays/)  
Make your display appear on an external monitor.

[**External monitor II: Hotplugging**](https://ejmastnak.com/tutorials/arch/monitor-hotplug/)  
Automatically switch display to an external monitor after plugging in an HDMI or DisplayPort cable.

[**Media player control**](https://ejmastnak.com/tutorials/arch/playerctl/)  
Play, pause, and skip music/videos system-wide with a single press of your keyboard.

[**Control volume**](https://ejmastnak.com/tutorials/arch/volume/)  
Change audio volume with your keyboard function keys.

Eye candy
---------

[**Background wallpaper**](https://ejmastnak.com/tutorials/arch/wallpaper/)  
Set your background wallpaper to an image of your choice, or to a slideshow of images. Best served with transparent windows and `i3gaps`.

[**Transparent windows**](https://ejmastnak.com/tutorials/arch/picom/)  
Use the `picom` compositor to make unfocused window backgrounds slightly transparent, so you can enjoy your background wallpaper.

Feedback, suggestions, etc.
---------------------------

If you have ideas for improving the series, I will quite likely implement them, appreciate your input, and give you a shoutout for your contributions. Feedback is welcome and appreciated.

Shoutouts to previous readers: many thanks to Tristan Harris for catching mistakes and offering good ideas on how to improve this series.

You can reach me by email at [elijan@ejmastnak.com](mailto:elijan@ejmastnak.com) or by opening an issue or pull request at [github.com/ejmastnak/ejmastnak.com](https://github.com/ejmastnak/ejmastnak.com).

Want to say thank you?
----------------------

You could:

*   [Send me an email!](https://ejmastnak.com/contact/) Seriously, if this material helped you, it will make my day to know. I love hearing from readers, and you’ll almost certainly get a message back from me.
    
*   [Contribute financially.](https://www.buymeacoffee.com/ejmastnak) Based on reader input, there are in fact people out there interested in compensating me financially for this guide. That’s awesome—thank you! You can [Buy Me a Coffee here.](https://www.buymeacoffee.com/ejmastnak)
