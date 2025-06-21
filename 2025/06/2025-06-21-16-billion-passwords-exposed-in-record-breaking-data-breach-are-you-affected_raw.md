Title: 16 billion passwords exposed in record-breaking data breach, opening access to Facebook, Google, Apple, and any other service imaginable

URL Source: https://cybernews.com/security/billions-credentials-exposed-infostealers-data-leak/

Published Time: 2025-06-18T12:00:00+00:00

Markdown Content:
**_Several collections of login credentials reveal one of the largest data breaches in history, totaling a humongous 16 billion exposed login credentials. The data most likely originates from various infostealers._**

_This story, based on unique Cybernews findings and originally published on the website on June 18, is constantly being updated with clarifications and additional information in response to public discourse. The most recent version of the article features comments from Cybernews researcher Aras Nazarovas and Bob Diachenko who unveiled this recent data leak. We've also added a few screenshots as proof of the leak._

*   The largest data breach in history involves 16 billion login credentials

*   The records are scattered across 30 different databases, and some records are or might be overlapping

*   The data most likely comes from various infostealers

*   The data is recent, not merely recycled from old breaches

*   Cybercriminals now have unprecedented access to personal credentials and could exploit them for account takeovers, identity theft, and targeted phishing attacks

Unnecessarily compiling sensitive information can be as damaging as actively trying to steal it. For example, the Cybernews research team discovered a plethora of supermassive datasets, housing billions upon billions of login credentials. From social media and corporate platforms to VPNs and developer portals, no stone was left unturned.

Our team has been closely monitoring the web since the beginning of the year. So far, they’ve discovered 30 exposed datasets containing from tens of millions to over 3.5 billion records each. In total, the researchers uncovered an unimaginable 16 billion records.

None of the exposed datasets were reported previously, bar one: in late May, Wired magazine reported a security researcher discovering a “mysterious database” with 184 million records. It barely scratches the top 20 of what the team discovered. Most worryingly, researchers claim new massive datasets emerge every few weeks, signaling how prevalent infostealer malware truly is.

![Image 1: “Mysterious database” with 184 million records.](https://media.cybernews.com/2025/06/data-example-goat-breaches.png)

A “mysterious database” with 184 million records. Screenshot by Bob Diachenko.

“This is not just a leak – it’s a blueprint for mass exploitation. With over 16 billion login records exposed, cybercriminals now have unprecedented access to personal credentials that can be used for account takeover, identity theft, and highly targeted phishing. What’s especially concerning is the structure and recency of these datasets – these aren’t just old breaches being recycled. This is fresh, weaponizable intelligence at scale,” researchers said.

The only silver lining here is that all of the datasets were exposed only briefly: long enough for researchers to uncover them, but not long enough to find who was controlling vast amounts of data. Most of the datasets were temporarily accessible through unsecured Elasticsearch or object storage instances.

What do the billions of exposed records contain?
------------------------------------------------

Researchers claim that most of the data in the leaked datasets is a mix of details from stealer malware, credential stuffing sets, and repackaged leaks.

There was no way to effectively compare the data between different datasets, but it’s safe to say overlapping records are definitely present. In other words, it’s impossible to tell how many people or accounts were actually exposed.

However, the information that the team managed to gather revealed that most of the information followed a clear structure: URL, followed by login details and a password. Most modern infostealers – malicious software stealing sensitive information – collect data in exactly this way.

![Image 2: Billions of logins and passwords exposed in a massive data leak](https://media.cybernews.com/2025/06/billions-leaked-multiple-datasets.png)
Information in the leaked datasets opens the doors to pretty much any online service imaginable, from Apple, Facebook, and Google, to GitHub, Telegram, and various government services. It’s hard to miss something when 16 billion records are on the table.

According to the researchers, credential leaks at this scale are fuel for phishing campaigns, account takeovers, ransomware intrusions, and business email compromise (BEC) attacks.

“The inclusion of both old and recent infostealer logs – often with tokens, cookies, and metadata – makes this data particularly dangerous for organizations lacking multi-factor authentication or credential hygiene practices,” the team said.

What dataset exposed billions of credentials?
---------------------------------------------

The datasets that the team uncovered differ widely. For example, the smallest, named after malicious software, had over 16 million records. Meanwhile, the largest one, most likely related to the Portuguese-speaking population, had over 3.5 billion records. On average, one dataset with exposed credentials had 550 million records.

Some of the datasets were named generically, such as “logins,” “credentials,” and similar terms, preventing the team from getting a better understanding of what’s inside. Others, however, hinted at the services they’re related to.

For example, one dataset with over 455 million records was named to indicate its origins in the Russian Federation. Another dataset, with over 60 million records, was named after Telegram, a cloud-based instant messaging platform.

> _“The inclusion of both old and recent infostealer logs – often with tokens, cookies, and metadata – makes this data particularly dangerous for organizations lacking multi-factor authentication or credential hygiene practices,”_
> 
> the team said.

While naming is not the best way to deduce where the data comes from, it seems some of the information relates to cloud services, business-oriented data, and even locked files. Some dataset names likely point to a form of malware that was used to collect the data.

It is unclear who owns the leaked data. While it could be security researchers that compile data to check and monitor data leaks, it’s virtually guaranteed that some of the leaked datasets were owned by cybercriminals. Cybercriminals love massive datasets as aggregated collections allow them to scale up various types of attacks, such as identity theft, phishing schemes, and unauthorized access.

A success rate of less than a percent can open doors to millions of individuals, who can be tricked into revealing more sensitive details, such as financial accounts. Worryingly, since it's unclear who owns the exposed datasets, there’s little impact users can do to protect themselves.

However, basic cyber hygiene is essential. Using a [password manager](https://cybernews.com/best-password-managers/) to generate strong, unique passwords, and updating them regularly, can be the difference between a safe account and stolen details. Users should also review their systems for infostealers, to avoid losing their data to attackers.

No, Facebook, Google, and Apple passwords weren’t leaked. Or were they?
-----------------------------------------------------------------------

With a dataset containing 16 billion passwords, that’s equivalent to two leaked accounts for every person on the planet.

We don’t really know how many duplicate records there are, as the leak comes from multiple datasets. However, some reporting by other media outlets can be quite misleading. Some claim that Facebook, Google, and Apple credentials were leaked. While we can’t completely dismiss such claims, we feel this is somewhat inaccurate.

Bob Diachenko, a Cybernews contributor, cybersecurity researcher, and owner of SecurityDiscovery.com, is behind this recent major discovery.

“There was no centralized data breach at any of these companies,” Diachenko said when I asked him to clarify whether any of the datasets actually came from Facebook, Google, or Apple.

However, that doesn’t mean that none of the logins were breached and leaked to the dark web.

“Credentials we’ve seen in infostealer logs contained login URLs to Apple, Facebook, and Google login pages,” Diachenko said.

So, as mentioned above, this means that the leaked information opens the doors to pretty much any online service imaginable.

As per popular request, we are sharing a few screenshots as proof that such datasets exist. Below, you can see that they actually include URLs to Facebook, Google, Github, Zoom, Twitch, and other login pages.

![Image 3: 16 billion data leak proof](https://media.cybernews.com/2025/06/goat-data-breach-16billion-passwords-leaked.jpeg)

Screenshot by Cybernews.

![Image 4: GOAT data breach](https://media.cybernews.com/2025/06/goat-data-leak-cybernews-screenshot.jpeg)

By Cybernews

![Image 5: 16 billion passwords exposed](https://media.cybernews.com/2025/06/data-leak-cybernews-screenshot-redacted.jpeg)

16 billion passwords exposed. By Cybernews

16-billion-record data breach signals a shift in the underground world
----------------------------------------------------------------------

According to Cybernews researcher Aras Nazarovas, this discovery might signal that criminals are abandoning previously popular methods of obtaining stolen data.

"The increased number of exposed infostealer datasets in the form of centralized, traditional databases, like the ones found be the Cybernews research team, may be a sign, that cybercriminals are actively shifting from previously popular alternatives such as Telegram groups, which were previously the go-to place for obtaining data collected by infostealer malware," Nazarovas said.

He regularly works with exposed datasets, ensuring that defenders secure them before threat actors can access them.

Here’s what Nazarovas suggests you should do to protect yourself.

"Some of the exposed datasets included information such as cookies and session tokens, which makes the mitigation of such exposure more difficult. These cookies can often be used to bypass 2FA methods, and not all services reset these cookies after changing the account password. Best bet in this case is to change your passwords, enable 2FA, if it is not yet enabled, closely monitor your accounts, and contact customer support if suspicious activity is detected."

Has your password ? You can [check here](https://cybernews.com/password-leak-check/)

Billions of records exposed online: recent leaks involve WeChat, Alipay
-----------------------------------------------------------------------

Major data leaks, with billions of exposed records, have become nearly ubiquitous. Last week, Cybernews wrote about what is likely [the biggest data leak to ever hit China](https://cybernews.com/security/chinese-data-leak-billiones-records-exposed/), billions of documents with financial data, WeChat and Alipay details, as well as other sensitive personal data.

Last summer, the largest password compilation with nearly ten billion unique passwords, RockYou2024, was leaked on a popular hacking forum. In 2021, a similar compilation with over [8 billion records was leaked online](https://cybernews.com/security/rockyou2021-alltime-largest-password-compilation-leaked/).

In early 2024, the Cybernews research team discovered what is likely still the [largest data leak](https://cybernews.com/security/billions-passwords-credentials-leaked-mother-of-all-breaches/) ever: the Mother of All Breaches (MOAB), with a mind-boggling 26 billion records.

16 billion passwords exposed: how to protect yourself
-----------------------------------------------------

Huge datasets of passwords spill onto the dark web all the time, highlighting the need to change them regularly. This also demonstrates just how weak our passwords still are.

Last year, someone leaked the [largest password compilation ever](https://cybernews.com/security/rockyou2024-largest-password-compilation-leak/), with nearly ten billion unique passwords published online. Such leaks pose severe threats to people who are prone to reusing passwords.

*    Even if you think you are immune to this or other leaks, go and reset your passwords just in case. 
*    Select strong, [unique passwords](https://cybernews.com/password-generator/) that are not reused across multiple platforms 
*    Enable multi-factor authentication (MFA) wherever possible 
*    Closely monitor your accounts 
*    Contact customer support in case of any suspicious activity 

Further discussion
------------------

No, we didn’t expect the hype when we were writing the article. Data breaches and even the biggest-ever data leaks, unfortunately, have become somewhat mundane, and people don’t seem to care that much.

![Image 6: Media coverage of the data leak](https://media.cybernews.com/2025/06/media-coverage-data-leak.png)

Media coverage of the leak. By Cybernews

These findings are interesting, though, for multiple reasons. First of all, the collection of datasets shows the scale of the problem — billions and billions of passwords and trillions of records, including very private medical, location, and financial data, spill online every day.

Is privacy dead?

Maybe not, but we certainly need to pressure companies holding our data to protect it properly. They often don’t, as we stumble upon treasure troves of “accidentally” unprotected data almost every day.

So we’re not exaggerating this — if anything, we aren’t doing enough as journalists and users to hold those companies accountable by putting them in the spotlight.

“Start holding the data holders accountable, and I bet these leaks and hacks start getting a lot less frequent. Now it only hurts whoevers PR if they get hacked, start making them fiscally responsible or criminally responsible, and they'll secure our info much better,” [one Redditor said](https://www.reddit.com/r/technology/comments/1lfzu5y/no_the_16_billion_credentials_leak_is_not_a_new/).

There’s another interesting aspect to this topic. It is a fact that all information comes from [infostealers](https://cybernews.com/security/infostealers-detected-within-us-military-and-defense-companies/), an incredibly prevalent threat.

According to the Israeli cybersecurity firm, Hudson Rock, when using infostealers, hackers don’t need to brute-force their way into networks. Instead, they wait for users to slip up and download malicious code in the form of pirated software, infected PDFs, a game mode, or other malware.

Infostealers then “exfiltrate everything,” including VPN credentials, authentication session cookies, email logins, internal development tools, stored documents, browsing history, and autofill data.

#### Recent updates

**🟢 [06-20 09:37 GMT]  Added expert insight from Bob Diachenko, who confirmed there was no centralized breach, but noted that credentials tied to services like Google and Facebook were found in the leak Added a Bob Diachenko's expert opinion.**

**🟢 [06-20 12:42 GMT]Added a few screenshots as proof that the exposed data includes pathways to popular services, such as Facebook, Apple, Github, and Google, among others.**

**🟢 [06-20 14:00 GMT]Added another screenshot as proof. Updated with context information on how to protect yourself.**

**🟢 [06-20 15:06 GMT]Updated with additional information about infostealers and where to find more information and discussion on this topic.**
