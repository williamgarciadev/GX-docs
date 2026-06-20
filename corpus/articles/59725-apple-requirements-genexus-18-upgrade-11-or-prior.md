---
title: "Apple Requirements (GeneXus 18 Upgrade 11 or prior)"
source_id: 59725
source_url: https://wiki.genexus.com/commwiki/wiki?59725
genexus_version: "18"
---

# Apple Requirements (GeneXus 18 Upgrade 11 or prior)

This article describes the requirements for developing Apple applications with GeneXus, as well as the requirements of the target devices.

**Note:** Requirements vary depending on whether you want to prototype using [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974) or compile your app.

To use F5 (Run) from the GeneXus IDE, you will have to [register](https://wiki.genexus.com/commwiki/wiki?15576) your devices using the GeneXus Account (Associated Smart Devices tab in the account configuration) from the device. Check the Supported OS versions section below.

### [Requirements for compiling your app](#Requirements+for+compiling+your+app)

The necessary components are available on the [Apple Developer website](https://developer.apple.com/download/release/).

**Warning**: Since April 2025, all iOS and iPadOS apps submitted to the App Store must be built with Xcode 16 and the iOS 18 SDK [(read Apple announcement)](https://developer.apple.com/news/upcoming-requirements/?id=02212025a). Therefore, only apps generated with [GeneXus 18 Upgrade 12](https://wiki.genexus.com/commwiki/wiki?59446) onwards can be submitted to the App Store.

|  |  |  |  |
| --- | --- | --- | --- |
| **Component** | **Required** | **Recommended** | **Comments** |
| **OS** | macOS Ventura (13.3 or later) | macOS Sonoma (14.0) |  |
| [**Xcode**](http://developer.apple.com/xcode/) | 15.0 | 15.0 | [How To: Change the Xcode version used by GeneXus](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?29380,,) |
| [**iOS SDK**](https://developer.apple.com/ios/) | 16.4 | 18.0 | Included with Xcode |
| [**watchOS SDK**](https://developer.apple.com/watchos/) | 9.4 | 11.0 | Included with Xcode |
| [**tvOS SDK**](https://developer.apple.com/tvos/) | 18.0 | 18.0 | Included with Xcode |
| [**SSH**](https://en.wikipedia.org/wiki/Secure_Shell) | - | - | Enable SSH access on your Mac computer. |
| [**CocoaPods**](https://cocoapods.org/) | 1.12.0 | Latest released | Execute this command in your Mac's terminal: For Intel-based Macs:  ``` sudo gem install cocoapods ```  For Apple silicon-based Macs:  ``` brew install cocoapods ```   Check:   [SAC#42942](https://www.genexus.com/en/developers/websac?data=42942;;). |
| **[iOS-Deploy](https://github.com/ios-control/ios-deploy)** | 1.11.2 | Latest released | This is only required if you use Execution type = "iOS Device (Mac)". Check [SAC#43850](https://www.genexus.com/en/developers/websac?data=43850;) |

### [Supported OS versions](#Supported+OS+versions)

* To run compiled applications, devices with iOS 12 or higher are required.
* To run the [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974), devices with iOS 13 or higher are required.
* There is no "maximum" OS version supported for a given GeneXus upgrade. Generated applications will continue to work in OS versions released after the GeneXus upgrade is released. However, the new features of these newer OS versions will require a new GeneXus upgrade release to be fully supported.

### [Notes](#Notes)

* In the requirement tables, the "-" symbol means there is no recommendation or requirement in particular for that component.
* After installing Xcode:
  + Open it. Xcode usually installs additional components while opening it for the first time:
    - If you don't do this, you may get compilation errors.
  + Check that Xcode > Preferences > Locations > Derived Data > Advanced > Build locations is not set to "Legacy".
* For KBs compiled with previous GeneXus (and Xcode) versions, before compiling, it is recommended to do the following:
  + Delete the content of /Library/Developer/Xcode/DerivedData (for each user of the Mac that is about to compile code).
  + Delete the folder “build” that is in /Documents/Projects/<KB\_NAME>/<ENVIRONMET\_NAME>/<MAIN\_NAME>.
* GeneXus is not compatible with Ruby Version Manager ([RVM](https://rvm.io)).[SAC #46543](https://www.genexus.com/developers/websac?data=46543).
* [Solutions for 404 or 500.19 errors](https://wiki.genexus.com/commwiki/wiki?18398).
* Note that only SSH authentication using a username and password is supported.

### [See Also](#See+Also)

[Apple platform](https://wiki.genexus.com/commwiki/wiki?14917)  
[Deployment and Prototyping in the Apple Platform](https://wiki.genexus.com/commwiki/wiki?16234)  
[Prototyping My Application on My Mac](https://wiki.genexus.com/commwiki/wiki?14761)  
[Apple - FAQ and Common Issues](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?14925,,)
