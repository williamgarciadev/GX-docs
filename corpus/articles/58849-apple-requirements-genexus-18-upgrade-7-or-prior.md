---
title: "Apple Requirements (GeneXus 18 Upgrade 7 or prior)"
source_id: 58849
source_url: https://wiki.genexus.com/commwiki/wiki?58849
genexus_version: "18"
---

# Apple Requirements (GeneXus 18 Upgrade 7 or prior)

This article describes the requirements for developing Apple applications with GeneXus, as well as the requirements of the target devices.

**Note:** Requirements vary if you want to prototype using [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974) or compile your app.

If you want to use F5 (Run) from GeneXus IDE, you will have to [register](https://wiki.genexus.com/commwiki/wiki?15576) your devices using the GeneXus Account (Associated Smart Devices tab in the account configuration) from the device. Check below the Supported OS versions section.

### [Requirements for compiling your app](#Requirements+for+compiling+your+app)

Necessary components are available on the [Apple Developer website](https://developer.apple.com/download/release/).

**Warning**: Since April 2025, all iOS and iPadOS apps submitted to the App Store must be built with Xcode 16 and the iOS 18 SDK [(read Apple announcement)](https://developer.apple.com/news/upcoming-requirements/?id=02212025a). Therefore, only apps generated with [GeneXus 18 Upgrade 12](https://wiki.genexus.com/commwiki/wiki?59446) onwards can be submitted to the App Store.

|  |  |  |  |
| --- | --- | --- | --- |
| **GeneXus 18 Upgrade 6****or higher users** | | | |
| **Component** | **Required** | **Recommended** | **Comments** |
| **OS** | macOS Ventura (13.3 or later) | macOS Sonoma (14.0) |  |  |
| [**Xcode**](http://developer.apple.com/xcode/) | 14.3 | 15 | [How To: Change the Xcode version used by GeneXus](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?29380,,) |
| [**iOS SDK**](https://developer.apple.com/ios/) | 16.4 | 18.0 | Included with Xcode |
| [**watchOS SDK**](https://developer.apple.com/watchos/) | 9.4 | 11.0 | Included with Xcode |
| [**tvOS SDK**](https://developer.apple.com/tvos/) | 18.0 | 18.0 | Included with Xcode |
| [**SSH**](https://en.wikipedia.org/wiki/Secure_Shell) | - | - | Enable SSH access on your Mac computer |
| [**CocoaPods**](https://cocoapods.org/) | 1.12.0 | Latest released | Execute this command in your Mac's terminal: For Intel-based Macs:  ``` sudo gem install cocoapods ```  For Apple silicon-based Macs:  ``` brew install cocoapods ```   Check:   [SAC#42942](https://www.genexus.com/en/developers/websac?data=42942;;). |
| **[iOS-Deploy](https://github.com/ios-control/ios-deploy)** | 1.11.2 | Latest released | This is only required if you use Execution type = "iOS Device (Mac)". Check [SAC#43850](https://www.genexus.com/en/developers/websac?data=43850;) |

|  |  |  |  |
| --- | --- | --- | --- |
| **GeneXus 18 Upgrade 5****or higher users** | | | |
| **Component** | **Required** | **Recommended** | **Comments** |
| **OS** | macOS Ventura (13.3 or later) | macOS Ventura (13.5 or later) |  |  |
| [**Xcode**](http://developer.apple.com/xcode/) | 14.3 | 14.3.1 | Included with Xcode |
| [**iOS SDK**](https://developer.apple.com/ios/) | 16.4 | 16.x | Included with Xcode |
| [**watchOS SDK**](https://developer.apple.com/watchos/) | 9.4 | 9.x | Included with Xcode |
| [**tvOS SDK**](https://developer.apple.com/tvos/) | 16.4 | 16.x | Included with Xcode |
| [**SSH**](https://en.wikipedia.org/wiki/Secure_Shell) | - | - | Enable SSH access on your Mac computer |
| [**CocoaPods**](https://cocoapods.org/) | 1.12.0 | Latest released | Execute this command in your Mac's terminal: For Intel-based Macs:  ``` sudo gem install cocoapods ```  For Apple silicon-based Macs:  ``` brew install cocoapods ```   Check:   [SAC#42942](https://www.genexus.com/en/developers/websac?data=42942;;). |
| **[iOS-Deploy](https://github.com/ios-control/ios-deploy)** | 1.11.2 | Latest released | This is only required if you use Execution type = "iOS Device (Mac)". Check [SAC#43850](https://www.genexus.com/en/developers/websac?data=43850;) |

|  |  |  |  |
| --- | --- | --- | --- |
| **GeneXus 18 Upgrade 4****or higher users** | | | |
| **Component** | **Required** | **Recommended** | **Comments** |
| **OS** | macOS Ventura (13.0 or later) | macOS Ventura (13.0 or later) |  |  |
| [**Xcode**](http://developer.apple.com/xcode/) | 14.0 | 14.3 | Included with Xcode |
| [**iOS SDK**](https://developer.apple.com/ios/) | 16.0 | 16.x | Included with Xcode |
| [**watchOS SDK**](https://developer.apple.com/watchos/) | 9.0 | 9.x | Included with Xcode |
| [**tvOS SDK**](https://developer.apple.com/tvos/) | 16.0 | 16.x | Included with Xcode |
| [**SSH**](https://en.wikipedia.org/wiki/Secure_Shell) | - | - | Enable SSH access on your Mac computer |
| [**CocoaPods**](https://cocoapods.org/) | 1.12.0 | Latest released | Execute this command in your Mac's terminal: For Intel-based Macs:  ``` sudo gem install cocoapods ```  For Apple silicon-based Macs:  ``` brew install cocoapods ```   Check:   [SAC#42942](https://www.genexus.com/en/developers/websac?data=42942;;). |
| **[iOS-Deploy](https://github.com/ios-control/ios-deploy)** | 1.11.2 | Latest released | This is only required if you use Execution type = "iOS Device (Mac)". Check [SAC#43850](https://www.genexus.com/en/developers/websac?data=43850;) |

|  |  |  |  |
| --- | --- | --- | --- |
| **GeneXus 18 Upgrade 2****or higher users** | | | |
| **Component** | **Required** | **Recommended** | **Comments** |
| **OS** | macOS Monterey (12.5 or later) | macOS Ventura (13.0 or later) | Note that macOS Venture is only compatible with Xcode 14.x |
| [**Xcode**](http://developer.apple.com/xcode/) | 14.0 | 14.2 | Includes Swift 5.7 |
| [**iOS SDK**](https://developer.apple.com/ios/) | 16.0 | 16.x | Included with Xcode |
| [**watchOS SDK**](https://developer.apple.com/watchos/) | 9.0 | 9.x | Included with Xcode |
| [**tvOS SDK**](https://developer.apple.com/tvos/) | 16.0 | 16.x | Included with Xcode |
| [**SSH**](https://en.wikipedia.org/wiki/Secure_Shell) | - | - | Enable SSH access on your Mac computer |
| [**CocoaPods**](https://cocoapods.org/) | 1.11.0 | Latest released | Execute this command in your Mac's terminal: For Intel-based Macs:  ``` sudo gem install cocoapods ```  For Apple Silicon-based Macs:  ``` brew install cocoapods ```   Check:   [SAC#42942](https://www.genexus.com/en/developers/websac?data=42942;;). |
| **[iOS-Deploy](https://github.com/ios-control/ios-deploy)** | 1.11.2 | Latest released | This is only required if you use Execution type = "iOS Device (Mac)". Check [SAC#43850](https://www.genexus.com/en/developers/websac?data=43850;) |

|  |  |  |  |
| --- | --- | --- | --- |
| **[GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066)****or higher users** | | | |
| **Component** | **Required** | **Recommended** | **Comments** |
| **OS** | macOS Monterey (12.0 or later) | macOS Monterey (12.5 or later) | Note that macOS Monterey is only compatible with Xcode 13.x |
| [**Xcode**](http://developer.apple.com/xcode/) | 13.2 | 14.2 | Includes Swift 5.5 |
| [**iOS SDK**](https://developer.apple.com/ios/) | 15.2 | 16 | Included with Xcode |
| [**watchOS SDK**](https://developer.apple.com/watchos/) | 8.3 | 9.0 | Included with Xcode |
| [**tvOS SDK**](https://developer.apple.com/tvos/) | 15.2 | 16.0 | Included with Xcode |
| [**SSH**](https://en.wikipedia.org/wiki/Secure_Shell) | - | - | Enable SSH access on your Mac computer |
| [**CocoaPods**](https://cocoapods.org/) | 1.11.0 | Latest released | Execute this command in your Mac's terminal: For Intel-based Macs:  ``` sudo gem install cocoapods ```  For Apple Silicon-based Macs:  ``` brew install cocoapods ```   Check:   [SAC#42942](https://www.genexus.com/en/developers/websac?data=42942;;). |
| **[iOS-Deploy](https://github.com/ios-control/ios-deploy)** | 1.11.2 | Latest released | This is only required if you use Execution type = "iOS Device (Mac)". Check [SAC#43850](https://www.genexus.com/en/developers/websac?data=43850;) |

### [Supported OS versions](#Supported+OS+versions)

* To run compiled applications, devices with iOS 12 or higher are required.
* To run the [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974), devices with iOS 13 or higher are required.
* There is no "maximum" OS version supported for a given GeneXus upgrade. Generated applications will still function in OS versions released after the release of the GeneXus upgrade. However, new features of these newer OS versions will require a new GeneXus upgrade release to be fully supported.

### [Notes](#Notes)

* In the requirement tables, the "-" symbol means there is no recommendation or requirement in particular for that component.
* After installing Xcode:
  + open it. Xcode usually installs additional components while opening it for the first time
    - If you do not this you may get compilation errors
  + check that Xcode -> Preferences -> Locations -> Derived Data -> Advanced -> Build locations is not set to "Legacy"
* For KBs compiled with previous GeneXus (and Xcode) versions, before compiling, it is recommended doing the following:
  + Delete the content of /Library/Developer/Xcode/DerivedData (for each user of the mac that is about to compile code)
  + Delete the folder “build” that is in /Documents/Projects/<KB\_NAME>/<ENVIRONMET\_NAME>/<MAIN\_NAME>
* GeneXus is not compatible with Ruby Version Manager ([RVM](https://rvm.io)).[SAC #46543](https://www.genexus.com/developers/websac?data=46543)
* [Solutions for the case that a 404 or 500.19 error occurs](https://wiki.genexus.com/commwiki/wiki?18398)
* Please note that only SSH authentication using a username and password is supported.

### [See Also](#See+Also)

[Apple platform](https://wiki.genexus.com/commwiki/wiki?14917)  
[Deployment and Prototyping in the Apple Platform](https://wiki.genexus.com/commwiki/wiki?16234)  
[Prototyping My Application on My Mac](https://wiki.genexus.com/commwiki/wiki?14761)  
[Apple - FAQ and Common Issues](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?14925,,)
