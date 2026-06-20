---
title: "GeneXus 18 Upgrade 4"
source_id: 54238
source_url: https://wiki.genexus.com/commwiki/wiki?54238
genexus_version: "18"
---

# GeneXus 18 Upgrade 4

This article is an overview of GeneXus 18 Upgrade 4 features (compared to [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853)) and what needs to be taken into account to adopt it.

It was released on July 4th, 2023.

## [Download](#Download)

<https://www.genexus.com/en/developers/downloadcenter?data=5990>

## [Overview](#Overview)

This upgrade fosters modularization of KBs, allows observability via the OpenTelemetry standard, and reinforces our commitment to future-proofing by updating the Angular generator to generate Angular 16 and the SAP Fiori Pattern to support SAP Horizon. It is a required update for those who use Google Analytics in Web applications. Furthermore, it improves stability and security as usual.

Modules

* Automatic dependencies management: Nuget is supported as a [Modules Server](https://wiki.genexus.com/commwiki/wiki?45933) type. As of now, the Nuget repository manager is recommended for storing modules because it automatically handles dependencies. If you have on Nuget a Module A that depends on B, and that in turn depends on C, when you install A on a KB it automatically brings B and C. This greatly simplifies module management and usage.

Web Generators

* Google Analytics Control has been updated to support Google Analytics 4
* Java: PDFBox and iText 2.x or 8.x can be used to generate PDF Reports. It's important to notice that each has different licensing. More information at [PDF Reports Library property](https://wiki.genexus.com/commwiki/wiki?54844).  
  In upcoming versions, the .NET generator will also support an open source library and iText 8.

Angular Generator

* The generator now generates code updated to Angular 16.
* The way to modularize the JavaScript of Angular applications is updated, promoting a modern code splitting and lazy loading mechanism. This makes the initial loading of applications faster because now the size of the initial package depends on the size of the screen you want to view.
* Performance improvements to the UI Attribute/Variable Edit and TextBlock controls. Now they are simpler, lighter, and faster.
* Improved lazy loading of images. A library is no longer used to implement lazy loading of images; instead, the native implementation of browsers is used. This removes additional weight from the initial load and additionally provides a time saving of a few milliseconds in loading the images.
* Popups can now be closed with the Escape key on the keyboard.
* New Sample: [WanderNest - Online Booking Sample](https://wiki.genexus.com/commwiki/wiki?55028)

Cloud Native & DevOps

* Azure CosmosDB-triggered functions. See [here](https://wiki.genexus.com/commwiki/wiki?54574) for more information.
* Support for [Observability](https://wiki.genexus.com/commwiki/wiki?53765) using OpenTelemetry.
* [Packaging Java sources](https://wiki.genexus.com/commwiki/wiki?54656) as [Packaging .NET sources](https://wiki.genexus.com/commwiki/wiki?54683).
* .NET: [Session State provider properties](https://wiki.genexus.com/commwiki/wiki?54782) can be configured in the IDE.

GXflow

* The grid of GXflow's Inbox now has filters by column.

Test

* Webdrivers are managed automatically and not distributed by GXtest.
* Improved [CompareImage command](https://wiki.genexus.com/commwiki/wiki?48889) allows setting color difference tolerance.
* Set generated folders and modules as such for preventing GXserver conflicts when committing/updating them.

GeneXus for SAP System pack

* New Design System: SAP Fiori Horizon. See [SAC 52853](https://www.genexus.com/developers/websac?en,,,52853)
* New feature: Grid Expanded Line in SAP Fiori pattern. See [SAC 52851](https://www.genexus.com/developers/websac?en,,,52851)
* New feature: Grid Column Title Group, Multiline in SAP Fiori pattern. See [SAC 52852](https://www.genexus.com/developers/websac?en,,,52852)
* New Sample: [GeneXus for SAP Systems - Showcase](https://wiki.genexus.com/commwiki/wiki?54839)

### [Technology update, installation requirements update, and main compatibility aspects](#Technology+update%2C+installation+requirements+update%2C+and+main+compatibility+aspects)

* Google Analytics 4: A GA-4 code has to be used in the [Google Analytics Control](https://wiki.genexus.com/commwiki/wiki?11847)
* .NET 6 SDK is required for the IDE ([Query object](https://wiki.genexus.com/commwiki/wiki?9026), [Dashboard object](https://wiki.genexus.com/commwiki/wiki?36769))
* Java: Support for java.time (JSR-310). This may affect compatibility; you should use the latest Java VMs. See [SAC #52835](https://www.genexus.com/developers/websac?en,,,52835).
* Apple: XCode 14.3 is supported. See [SAC #52826](https://www.genexus.com/en/developers/websac?data=52826;;).
* Angular: Updated to Angular 16.
* Android: Intel announced that HAXM will be discontinued. Therefore, it is recommended to have GVM (for AMD processors) or WHPX (for Intel or AMD processors) installed and enabled so that the x86 Emulator uses one of them.

## [All Details (Features, more Compatibility aspects, Issues)](#All+Details+%28Features%2C+more+Compatibility+aspects%2C+Issues%29)

Please check these links for additional features, compatibility aspects, issues, and details:

GeneXus: <https://www.genexus.com/developers/rn?data=0;4;V18;4;V18;3;>  
GeneXus Server: <https://www.genexus.com/developers/rn?data=0;6;V18;4;V18;3;>  
GXflow: <https://www.genexus.com/developers/rn?data=0;3;V18;4;V18;3;>  
GXtest: <https://www.genexus.com/developers/rn?data=0;7;V18;4;V18;3;>


|  |
| --- |
| **Backlinks** |
| [Android Requirements (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55100) | [Asymmetric Encryption Block Cipher](https://wiki.genexus.com/commwiki/wiki?42686) | [Asymmetric Key Management](https://wiki.genexus.com/commwiki/wiki?43918) |
| [Asymmetric Signing](https://wiki.genexus.com/commwiki/wiki?42687) | [Azure CosmosDB-triggered functions](https://wiki.genexus.com/commwiki/wiki?54574) | [Certificate](https://wiki.genexus.com/commwiki/wiki?43920) | [Column Class property in Grid (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55106) |
| [CrashAnalytics external object](https://wiki.genexus.com/commwiki/wiki?55161) | [Database Table Name property](https://wiki.genexus.com/commwiki/wiki?54777) | [Deploy to SAP Cloud Foundry - SAP BTP (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54602) | [Deploying Tests (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54520) |
| [Design Import option (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55439) | [Display Number Clustered Points property](https://wiki.genexus.com/commwiki/wiki?54842) | [Display Style Clustered Points property](https://wiki.genexus.com/commwiki/wiki?54843) | [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54956) |
| [Toc:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) | [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853) | [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239) |
| [GeneXus for SAP Systems - Initialize Fiori](https://wiki.genexus.com/commwiki/wiki?54721) | [KB:GeneXus for SAP Systems - Showcase](https://wiki.genexus.com/commwiki/wiki?54839) | [GeneXus For SAP Systems - Split Screen Master List with amount Floorplan (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?55230) |
| [GeneXus for SAP Systems Data Model changes (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54688) | [GeneXus for SAP Systems Fiori Pattern for Web (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54739) | [GeneXus For SAP Systems FioriLaunchpad object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54867) | [GeneXus for SAP Systems First Application (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54653) |
| [GeneXus for SAP Systems First Build and Run (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54669) | [GeneXus for SAP Systems First Formulas (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54708) | [GeneXus for SAP Systems First Rules definitions (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54700) | [GeneXus for SAP Systems Initialize Fiori (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54730) |
| [GeneXus For SAP Systems KPI Worklist Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54915) | [GeneXus For SAP Systems List Report Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54853) | [GeneXus For SAP Systems Simple Worklist Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54970) | [GeneXus For SAP Systems Simple Worklist with global action Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55017) |
| [GeneXus For SAP Systems Split Screen Master List Floorplan (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54939) | [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) | [Google Analytics Dimensions property (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?55189) | [GXML (GeneXus Markup Language) (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55385) |
| [GXtest UI Commands - CompareImage (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54847) | [How to configure Session State In ASP.NET Core (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54892) | [HowTo: apply the Fiori pattern for the first time (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54785) | [HowTo: Create Angular User Controls in GeneXus](https://wiki.genexus.com/commwiki/wiki?57330) |
| [HowTo: Observability of your GeneXus applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55863) | [HowTo: Pass additional parameters to external authentication programs using GAM (GeneXus 18 Upgrade)](https://wiki.genexus.com/commwiki/wiki?55358) | [Instance Name property](https://wiki.genexus.com/commwiki/wiki?54780) | [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) |
| [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) | [Intersection Observer control](https://wiki.genexus.com/commwiki/wiki?55147) | [JWT Creator](https://wiki.genexus.com/commwiki/wiki?43989) | [JWT Optional Data](https://wiki.genexus.com/commwiki/wiki?43983) |
| [Manage Module References (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55064) | [Marker Clustering property for Maps in Web Panels](https://wiki.genexus.com/commwiki/wiki?54841) | [Modules MsBuild Tasks (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55011) | [Modules Server (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55061) |
| [Observability in GeneXus Apps (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55862) | [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) | [Observability with AWS Distro for OpenTelemetry](https://wiki.genexus.com/commwiki/wiki?53774) | [Observability with Azure Monitor Application Insights](https://wiki.genexus.com/commwiki/wiki?54383) |
| [Observability with Azure Monitor Application Insights (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56153) | [Observability with Lightstep](https://wiki.genexus.com/commwiki/wiki?53776) | [Observability with OpenTelemetry](https://wiki.genexus.com/commwiki/wiki?53775) | [Package and Publish Modules (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55057) |
| [Packaged Modules Management messages (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55022) | [Packaging .NET sources](https://wiki.genexus.com/commwiki/wiki?54683) | [Packaging Java sources](https://wiki.genexus.com/commwiki/wiki?54656) | [Password property at Back end Generator level](https://wiki.genexus.com/commwiki/wiki?54884) |
| [PDF Reports (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54937) | [PDF Reports Library property (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55459) | [KB:PlantCare - ECommerce Sample](https://wiki.genexus.com/commwiki/wiki?50476) | [KB:PlantCare and SweetWorld - ECommerce Sample (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?56139) |
| [PrivateKey](https://wiki.genexus.com/commwiki/wiki?43919) | [PublicKey](https://wiki.genexus.com/commwiki/wiki?54578) | [Query Object Compatibility](https://wiki.genexus.com/commwiki/wiki?11032) | [Query Object Considerations (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54655) |
| [Session State Provider property](https://wiki.genexus.com/commwiki/wiki?54782) | [Session Timeout property](https://wiki.genexus.com/commwiki/wiki?54781) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) | [SQL Server Data Store property](https://wiki.genexus.com/commwiki/wiki?55060) |
| [Trigger type property](https://wiki.genexus.com/commwiki/wiki?51466) | [Update Android SDK tool (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55101) | [KB:WanderNest - Online Booking Sample](https://wiki.genexus.com/commwiki/wiki?55028) | [XML DSig Signer](https://wiki.genexus.com/commwiki/wiki?43579) |

---
