---
title: "Executing From QR Codes"
source_id: 18260
source_url: https://wiki.genexus.com/commwiki/wiki?18260
genexus_version: "18"
---

# Executing From QR Codes

When you run your application (F5 or "Run" in the GeneXus menu bar) without [Startup Object](https://wiki.genexus.com/commwiki/wiki?5393), the web application [Developer Menu](https://wiki.genexus.com/commwiki/wiki?18484) will be opened in the browser.

`[imagen omitida: wiki id 37573]`

### [Option 1 - Browse Web Objects](#Option+1+-+Browse+Web+Objects)

List the web objects in the Knowledge Base, such as [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)s, [Work With Web](https://wiki.genexus.com/commwiki/wiki?25475), etc. This information is only accessible from a web browser.

### [Option 2 - Install iOS Apps](#Option+2+-+Install+iOS+Apps)

Display the [QR Code](https://wiki.genexus.com/commwiki/wiki?18095) for scanning the application from an iOS device that has [KBN](https://wiki.genexus.com/commwiki/wiki?18653) installed. If you don't have the KBN installed in your device, you can download it from the Developer Menu in the corresponding option. Once you've scanned the QR Code, KBN will add the application to its catalog, and the tester can execute it.

`[imagen omitida: wiki id 37574]`

The Service URL must be visible from the device. To do this, you have two ways:

1. Deploy to the cloud. See this for more information: [Deploy to cloud: Step by Step](https://wiki.genexus.com/commwiki/wiki?18250).
2. To use a Wifi or a network to connect the device to the computer where the application is running.

### [Option 3 - Install Android Apps](#Option+3+-+Install+Android+Apps)

Display a [QR Code](https://wiki.genexus.com/commwiki/wiki?18095) for each application (main smart device object) in the Knowledge Base in order to scan its code and download its package (**\*.apk** file).

`[imagen omitida: wiki id 37575]`

This scenario is slightly different from the *Install iOS App* section. In this case, the tester must install the application manually in the device, thus in the iOS case, the tester will execute the application through [KBN](https://wiki.genexus.com/commwiki/wiki?18653). There is no [KBN](https://wiki.genexus.com/commwiki/wiki?18653) support for the Android system. The tester must enable [apps from unknown sources](https://developer.android.com/distribute/marketing-tools/alternative-distribution.html#unknown-sources) on the device settings, and then, install the \*.apk.

If the QR Codes appear greyed out means the application was not generated nor compiled. In the example above, two of the three apps weren't generated. To do it, simply build the concerned object (Right-click > Build), Run it (F5 if it's startup object or Right-click > Run), or make a Rebuild All of the KB.

### [Notes](#Notes)

* If you set a [Startup Object](https://wiki.genexus.com/commwiki/wiki?5393), when you run the application (F5/Run) the Developer Menu won't be generated nor displayed.
* You can see the Developer Menu QR Codes directly from the IDE by executing "View > Show QR Codes" from the GeneXus menu bar.
* QR Code is not available for iOS because you can't install an **\*****.ipa** file --- the file which stores an iPhone/iPad/iPod app (analogous to \*.apk from Android). You must download the application from the Apple Store or install it through iTunes or other tools. Please refer to [Prototyping in iOS with a compiled application](https://wiki.genexus.com/commwiki/wiki?17380) for more information.

### [See also](#See+also)

* [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974)
* [Emulation for Android](https://wiki.genexus.com/commwiki/wiki?18270)
* [Execution for Android Using the Device](https://wiki.genexus.com/commwiki/wiki?14910)
* [Prototyping in iOS with a compiled application](https://wiki.genexus.com/commwiki/wiki?17380)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Prototyping features and Deployment of applications for Smart Devices](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/prototyping-features-and-deployment-of-applications-for-smart-devices?p=3694)  
`[imagen omitida: wiki id 20668]` [Application Deployment Tool](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/application-deployment-tool?p=5489)


|  |
| --- |
| **Backlinks** |
| [Deploy to cloud: Step by Step](https://wiki.genexus.com/commwiki/wiki?18250) | [Developer Menu](https://wiki.genexus.com/commwiki/wiki?18484) | [Execution for Android Using the Device](https://wiki.genexus.com/commwiki/wiki?14910) |
| [Execution for Android Using the Device (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?56063) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |
| [QR Code](https://wiki.genexus.com/commwiki/wiki?18095) |

---
