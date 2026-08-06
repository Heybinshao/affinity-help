---
title: "Fix MSIX installation problems with Affinity for Windows - Affinity Help Center"
source: https://www.affinity.studio/help/msix-installation-problems/
slug: msix-installation-problems
fetched: 2026-08-06
---

# Fix MSIX installation problems with Affinity for Windows - Affinity Help Center

> 官方来源：https://www.affinity.studio/help/msix-installation-problems/

[Skip to main content](https://www.affinity.studio/help/msix-installation-problems/#_r_0_)

[![Image 1](https://content-management-files.canva.com/78303f82-4688-4614-99c7-ad7970d208a9/affinity_logotype_white_min.svg)](https://www.affinity.studio/)

*   Product    

*   Discover    

*   [Help](https://www.affinity.studio/help)

[Get Affinity](https://www.affinity.studio/get-affinity)

[![Image 2](https://content-management-files.canva.com/b916d6a5-3b78-490b-a56a-673b7dc606d0/affinity_symbol_white_min.svg)](https://www.affinity.studio/)

Submit Search

1.   [Help Center](https://www.affinity.studio/help/)
2.   [Installation and setup](https://www.affinity.studio/help/installation-setup/)
3.   Fix MSIX installation problems with Affinity for Windows

# Fix MSIX installation problems with Affinity for Windows

If you have trouble installing or uninstalling the MSIX version of Affinity, first confirm your operating system is supported. Affinity requires Windows 11 or Windows 10 May 2020 Update (version 2004, 20H1, build 19041) or later. Instructions to check your Windows version are provided below.

[](https://www.affinity.studio/help/msix-installation-problems/#common-msix-install-errors)

## **Common MSIX install errors**

[](https://www.affinity.studio/help/msix-installation-problems/#error:-0x80073d10)

### **Error: 0x80073d10**

**Windows cannot install package ... because the package requires architecture x64, but this computer has architecture x86. (0x80073d10)**

This indicates that your machine doesn't have a 64 bit CPU. Our apps require a 64 bit CPU to install and run.

[](https://www.affinity.studio/help/msix-installation-problems/#error:-0x80073cfd)

### **Error: 0x80073cfd**

**Windows cannot install package ... because this package is not compatible with the device. The package requires OS version 10.0.19041.0 or higher on the Windows. Desktop device family. The device is currently running OS version 10.0.xxxxx.xxx. (0x80073cfd)**

This indicates that your version of Windows is not supported. Our apps require Windows 11 or Windows 10 May 2020 Update (2004, 20H1, build 19041) or later to install.

[](https://www.affinity.studio/help/msix-installation-problems/#error:-0x80073cf3)

### **Error: 0x80073CF3**

**Windows cannot install package ... because a different package ... with the same name is already installed. Remove package ... before installing. (0x80073cf3)**

This indicates that there's already an existing version of the app installed. An example of this would be downloading and installing Affinity directly from the Affinity Store and then trying to install Affinity again directly from the Microsoft Store. You can go to **Apps**>**Apps & features** to see if you have an existing version installed.

Please Note: Because of this behavior, it's not possible to have both the Affinity Store and Microsoft Store versions of Affinity apps installed alongside each other on the same device.

[](https://www.affinity.studio/help/msix-installation-problems/#error:-app-installer-failed-to-install-package-dependencies-)

### **Error: App Installer failed to install package dependencies…**

If you're getting the error **App Installer failed to install package dependencies. Ask the developer for package** when installing Affinity on Windows, you will need to download and install the _**Microsoft.VCLibs.x64.14.00.Desktop.appx**_**package** from Microsoft [here](https://learn.microsoft.com/troubleshoot/developer/visualstudio/cpp/libraries/c-runtime-packages-desktop-bridge).

Once installed, you will be able to install Affinity without any issues.

[](https://www.affinity.studio/help/msix-installation-problems/#error:-app-didn-t-start)

### **Error: App didn't start**

This message can occur if you don't have Microsoft App Installer installed. It can be downloaded from within the Microsoft Store [here](https://apps.microsoft.com/store/detail/app-installer/9NBLGGH4NNS1).

[](https://www.affinity.studio/help/msix-installation-problems/#error:-cannot-open-app-package.-error-in-parsing-the-app-package)

### Error: Cannot open app package. Error in parsing the app package

This can happen if the AppX Deployment Service (AppXSVC) is disabled. It can be enabled by following the steps below:

Windows app

1.   Press the **Windows Key** + **R**
2.   Type **Regedit** into the **Run** dialog and press **OK**
3.   Navigate to Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\AppXSvc
4.   On the right pane, double-click the Start entry.
5.   Change **Value data** to _2_ and press **OK**

Now restart your computer and try installing your Affinity again.

[](https://www.affinity.studio/help/msix-installation-problems/#determine-your-version-of-windows)

### Determine your version of Windows

Note: Affinity is **not compatible** with **x32 (32-bit) CPUs** and **Windows**.

Windows app

1.   Press the **Windows key** or **Windows Key** + **R** on your keyboard. 
2.   Type **“Settings”**and press the Return key.
3.   Open the **Settings** app.
4.   Go to **System**>**About**
5.   Under **Windows specifications**, you can see **Edition, Version,**and**OS Build**information**.**

[](https://www.affinity.studio/help/msix-installation-problems/#why-does-my-browser-say-the-msix-installer--may-harm-your-computer--when-i-download-it-from-the-official-affinity-website-)

### Why does my browser say the MSIX installer “may harm your computer” when I download it from the official Affinity website?

This can happen for several reasons, including browser security features and Microsoft Defender SmartScreen being cautious with less frequently downloaded installers. It’s a standard warning and doesn’t mean the installer is malicious. If you downloaded the installer from the official Affinity website, it’s safe to use. Alternatively, you can install Affinity directly from the Microsoft Store if you prefer.

**Still need help?**[Contact Support](https://support.affinity.studio/hc/requests/new).

How would you rate the help you received from this article?

Good

Not so good

*   
    *   Product

    *   [Get Affinity](https://www.affinity.studio/get-affinity)
    *   [Graphic design](https://www.affinity.studio/graphic-design-software)
    *   [Photo editing](https://www.affinity.studio/photo-editing-software)
    *   [Page layout](https://www.affinity.studio/page-layout-software)
    *   [Canva integrations](https://www.affinity.studio/canva-integrations)
    *   [Product integrations](https://www.affinity.studio/integrations)

*   
    *   Discover

    *   [Inspired.af](https://www.affinity.studio/blog)
    *   [Spotlight](https://www.affinity.studio/spotlight)
    *   [Learning resources](https://www.affinity.studio/resources)
    *   [Press](https://www.canva.com/newsroom/news/all-new-affinity)

*   
    *   Help

    *   [Help Center](https://www.affinity.studio/help)
    *   [Affinity V2](https://affinity.serif.com/v2/)
    *   [Affinity V2 account](https://store.serif.com/sign-in/)
    *   [April 2026 update](https://www.affinity.studio/blog/affinity-update-april-2026)
    *   [Release notes](https://www.affinity.studio/help/release-notes/)

*   
    *   Connect

    *   [About](https://www.affinity.studio/about)
    *   [Careers](https://www.lifeatcanva.com/)
    *   [Contact Sales](https://www.canva.com/contact-sales/affinity/)

*   Product 

    *   [Get Affinity](https://www.affinity.studio/get-affinity)
    *   [Graphic design](https://www.affinity.studio/graphic-design-software)
    *   [Photo editing](https://www.affinity.studio/photo-editing-software)
    *   [Page layout](https://www.affinity.studio/page-layout-software)
    *   [Canva integrations](https://www.affinity.studio/canva-integrations)
    *   [Product integrations](https://www.affinity.studio/integrations)

*   Discover 

    *   [Inspired.af](https://www.affinity.studio/blog)
    *   [Spotlight](https://www.affinity.studio/spotlight)
    *   [Learning resources](https://www.affinity.studio/resources)
    *   [Press](https://www.canva.com/newsroom/news/all-new-affinity)

*   Help 

    *   [Help Center](https://www.affinity.studio/help)
    *   [Affinity V2](https://affinity.serif.com/v2/)
    *   [Affinity V2 account](https://store.serif.com/sign-in/)
    *   [April 2026 update](https://www.affinity.studio/blog/affinity-update-april-2026)
    *   [Release notes](https://www.affinity.studio/help/release-notes/)

*   Connect 

    *   [About](https://www.affinity.studio/about)
    *   [Careers](https://www.lifeatcanva.com/)
    *   [Contact Sales](https://www.canva.com/contact-sales/affinity/)

English (US)

*   [![Image 3: Instagram](https://content-management-files.canva.com/42a74cd5-ccc1-43f4-847b-cfee15b387d6/social_instagram.svg)](https://www.instagram.com/affinity/)
*   [![Image 4: Facebook](https://content-management-files.canva.com/c0ee217b-1e52-423a-95cb-6674227da28c/social_facebook.svg)](https://www.facebook.com/affinity)
*   [![Image 5: Threads](https://content-management-files.canva.com/5a46d885-129b-44bc-9bb5-91a1cd24519a/social_threads.svg)](https://www.threads.com/@affinity)
*   [![Image 6: Discord](https://content-management-files.canva.com/4c86f6ba-0400-48aa-b33b-d1ac6e06406f/social_discord.svg)](https://affin.link/dc)
*   [![Image 7: TikTok](https://content-management-files.canva.com/c38ff714-7599-4dc5-869a-7bc1553075e5/social_tiktok.svg)](https://www.tiktok.com/@weareaffinity)
*   [![Image 8: X](https://content-management-files.canva.com/1c162bcb-f637-4d23-ac3f-909ebf33f8c0/social_twitter.svg)](https://x.com/Affinity)
*   [![Image 9: Youtube](https://content-management-files.canva.com/719b9b23-2ce5-4dcf-8487-d81d4fc52d81/social_youtube.svg)](https://www.youtube.com/AffinitySuite)

*   [Privacy](https://www.canva.com/policies/privacy-policy/)
*   [Terms & Conditions](https://www.canva.com/policies/)
*   © 2026 All Rights Reserved, Affinity 

Show main menu

Suggestions will appear below the field as you type

Copy link to heading

Copy link to heading

Copy link to heading

Copy link to heading

Copy link to heading

Copy link to heading

Copy link to heading

Copy link to heading

Copy link to heading

## Affinity Cookies

Affinity is a Canva product, and Canva uses essential cookies to make this site work. We'd like to use other cookies to improve and personalise your visit, tailor ads you see from us on Affinity and partner sites, and to analyze our website's performance, but only if you accept. Learn more about your choices in the [Canva cookies policy.](https://www.canva.com/policies/cookies-policy/)

Manage Cookies Accept All

![Image 10: Affinity Logo](https://cdn-au.onetrust.com/logos/3dbea99f-abc0-4dbd-bcd7-8f6dfcaea28d/019a2649-863c-7345-9b60-9a618abba327/5c38b3e1-3c43-4eda-b904-88377c9b9c2e/full-logo.png)

## Manage Cookies

Cookies and similar technologies collect certain information about how you’re using our website. Some of them are essential, and without them this affinity.studio website might not work. But others are optional, and you get to choose whether we use them or not. 

 Hungry for more? 

[Read our full Cookie policy here.](https://www.canva.com/policies/cookies-policy/)

Allow All

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work.

Cookies Details

#### Performance Cookies

- [x] Performance Cookies 

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

Cookies Details

#### Targeting Cookies

- [x] Targeting Cookies 

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

Cookies Details

### Learn More

Clear
*   - [x] checkbox label label 

Apply Cancel

Consent Leg.Interest

- [x] checkbox label label

- [x] checkbox label label

- [x] checkbox label label

Reject All Confirm My Choices

[![Image 11: Powered by Onetrust](https://cdn-au.onetrust.com/logos/static/powered_by_logo.svg)](https://www.onetrust.com/solutions/consent-and-preferences/)
