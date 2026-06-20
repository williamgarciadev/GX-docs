---
title: "Distribution of Apple's Flexible Client through Swift Packages"
source_id: 55960
source_url: https://wiki.genexus.com/commwiki/wiki?55960
genexus_version: "18"
---

# Distribution of Apple's Flexible Client through Swift Packages

Flexible Client is a set of components and libraries used to generate native mobile applications on [Android](https://wiki.genexus.com/commwiki/wiki?14453) and [Apple](https://wiki.genexus.com/commwiki/wiki?14917) platforms. These libraries allow applications developed with GeneXus to efficiently interact with mobile operating systems and take advantage of the specific capabilities of each platform.

Flexible Client distribution for Apple: They are downloaded from the Internet and automatically installed when building any object. In this way, a package manager mechanism is used to download the binaries through [Swift Package Manager](https://developer.apple.com/documentation/xcode/swift-packages).

This mechanism offers significant advantages in terms of efficiency and easy updating. Instead of relying on a monolithic installation of GeneXus, where the entire environment is updated, Swift Package Manager allows you to independently and accurately manage Flexible Client dependencies.

When the Flexible Client is migrated to Swift Package Manager, it takes advantage of the Flexible Client's ability to manage libraries and components as individual packages. These packages are managed as independent modules that can be selectively updated without affecting other parts of the system. This means that if you need a quick fix to GeneXus or third parties in the Flexible Client, you only need to update the corresponding package, instead of having to update the entire GeneXus version. This saves time and simplifies the process of developing applications for the Apple platform.

In addition, through the [Flexible Client Version](https://wiki.genexus.com/commwiki/wiki?55856) and [Flexible Client Update Policy](https://wiki.genexus.com/commwiki/wiki?55890) properties in the Apple generator, it is possible to specify the Flexible Client version that should be downloaded. These properties are essential to determine the version and update policy of the Flexible Client referenced by the application generated on the Apple platform.

### [Build process](#Build+process)

In the initial build process, Swift Package Manager queries the public package repositories on [GitHub.com](https://github.com/GeneXus-SwiftPackages/GXUIApplication/tags), where all the packages needed for the Flexible Client are grouped together.

**Note**: When using a proxy, to allow package downloads you must authorize access to GitHub and the specific IP addresses used by Azure. To do so, follow the instructions provided in the [https://learn.microsoft.com/en-us/azure/devops/organizations/security/allow-list-ip-url?view=azure-devops&tabs=IP-V4.

GeneXus downloads the Flexible Client dependencies and stores them in a local cache on your machine, in a location similar to the following:

/Library/GeneXus/GeneXus/<GX\_VERSION>/SwiftPackages

This local cache is located by default in the user folder of the machine and is used for future builds.

It offers the advantage of retrieving binaries quickly and with no problems during the development process, even if you are working on different applications that share the same Flexible Client dependencies.

### [Offline scenario](#Offline+scenario)

The "OfflineMode" property in MacTransfer, configurable through the "MacTransfer.exe.config" file, is essential for controlling the behavior of the compilation process on a Mac, especially when working with Swift Packages.

When enabled, the offline mode is activated, which means that the compile commands on the Mac will not try to connect to the Internet to download packages in real time. Instead, they will rely on packages previously downloaded locally.

However, for the offline mode to operate effectively, advance preparation is required. It is essential that all the necessary Flexible Client components are already downloaded and stored on the local machine. This is achieved with the following steps:

1. Compile your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) or [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) at least once with the "OfflineMode" property disabled.
2. Open the "MacTransfer.exe.config" file and find the "OfflineMode" property. Set this property to "true" to enable the offline mode. Compile your KB.
3. The compilation process will use the components you have previously downloaded and stored on your local machine. It will not try to connect to the Internet to download additional packages.

Note that if you open the generated project in Xcode and want to use it in an offline environment, you may face problems, as Xcode will look for the Swift Packages in a default directory instead of using the specific path provided by GeneXus.

### [Availability](#Availability)

This functionality is available since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242).

### [See Also](#See+Also)

[iOS Flexible Client Deprecations](https://wiki.genexus.com/commwiki/wiki?48112,,)


|  |
| --- |
| **Backlinks** |
| [Flexible client version property](https://wiki.genexus.com/commwiki/wiki?55856) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
