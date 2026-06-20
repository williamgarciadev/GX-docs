---
title: "GeneXus Super App Render"
source_id: 58435
source_url: https://wiki.genexus.com/commwiki/wiki?58435
genexus_version: "18"
---

# GeneXus Super App Render

The Super App Render SDK (also known as Flexible Client) transforms a Native Mobile application into a [Super App](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,) by dynamically loading other applications ([Mini Apps](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,)) within the host application.

This allows for easy incorporation of products and services from the Native Mobile application or third parties, making it an essential component for building or transforming a Super App.

### [Features of Super App Render](#Features+of+Super+App+Render)

One of the notable features of the GeneXus Super App Render is the ability to load [Native Mobile Mini Apps](https://wiki.genexus.com/commwiki/wiki?58298) at runtime, not just [Web Mini Apps](https://wiki.genexus.com/commwiki/wiki?57422).

These Mini Apps are rendered on each platform ([Apple](https://wiki.genexus.com/commwiki/wiki?14917) or [Android](https://wiki.genexus.com/commwiki/wiki?14453)) as purely Native Mobile applications, which allows for a better experience and easier access to the different components of the operating system.

### [Architecture and Security](#Architecture+and+Security)

* In addition to loading Mini Apps, the Super App Render acts as a communication channel with the [Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) to obtain the list of available Mini Apps.
* It also acts as the communication channel between the Mini Apps and the Super App for those functionalities or information that the Super App provides to its Mini Apps through its API (e.g., payment, access to user data, etc.).
* It has an architecture that guarantees information security, as it is not possible to share user data between different Mini Apps or between the Super App and Mini Apps unless it is explicitly done through the [Super App API](https://wiki.genexus.com/commwiki/wiki?58207).

### [For Super Apps Not Developed with GeneXus](#For+Super+Apps+Not+Developed+with+GeneXus)

For Native Super Apps not developed with GeneXus, it is necessary to include the SDK in the Super App project references. The SDK is distributed as [Swift Packages for iOS](https://github.com/genexus-books/gx-super-app/blob/main/iOS/GeneXus%20Frameworks/README.md) and through [Maven for Android](https://github.com/genexus-books/gx-super-app/blob/main/Android/GeneXus%20Libraries/README.md).

### [For Super Apps Developed with GeneXus](#For+Super+Apps+Developed+with+GeneXus)

For a Super App developed with GeneXus, the Super App Render is already included as part of the app's build process.

### [Composition of Super App Render](#Composition+of+Super+App+Render)

The SDK consists of a base module and several modules that implement specific functionalities called feature-modules. These additional modules must be included depending on the functionalities to be incorporated from the Mini Apps (for example, Grids, Location, Maps, etc.).

When creating an application with GeneXus, the GeneXus generation process automatically determines which GeneXus Super App Render dependencies should be included in the compiled project.

In the case of a Native Mobile Mini App (where the application is not compiled), the necessary dependencies must be included in the Super App. That is, the corresponding Super App Render modules must be installed in the Super App.

### [GeneXus Super App Render Versions](#GeneXus+Super+App+Render+Versions)

Information about available GeneXus Super App Render versions and their compatibility with Mini Apps developed with GeneXus can be found in the following article: [GeneXus Super App Render Releases](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?58156,,).

### [See Also](#See+Also)

[Distribution of Apple's Flexible Client through Swift Packages](https://wiki.genexus.com/commwiki/wiki?55960)  
[Flexible client version property](https://wiki.genexus.com/commwiki/wiki?55856)  
[Flexible client update policy property](https://wiki.genexus.com/commwiki/wiki?55890)


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) |

---
