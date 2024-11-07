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
