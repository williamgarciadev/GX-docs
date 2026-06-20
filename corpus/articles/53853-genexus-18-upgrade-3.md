---
title: "GeneXus 18 Upgrade 3"
source_id: 53853
source_url: https://wiki.genexus.com/commwiki/wiki?53853
genexus_version: "18"
---

# GeneXus 18 Upgrade 3

This article is an overview of GeneXus 18 Upgrade 3 features (compared to [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396)) and what needs to be taken into account to adopt it.

It was released on April 26th, 2023.

## [Download](#Download)

<https://www.genexus.com/en/developers/downloadcenter?data=5984>  
After its release, a hotfix was provided: GeneXus Build 172101. More info in [SAC #52869](https://www.genexus.com/en/developers/websac?data=52869;;)

## [Overview](#Overview)

This upgrade provides overall stability improvements, especially for Security and Deployment.

IDE

* GXflow can now be enabled by selecting Tools > Workflow > Enable Workflow.

Security

* Security can be defined at the Query Object level. See more information in [SAC #52785](https://www.genexus.com/en/developers/websac?data=52785;;).

Cloud Native

* New Datastore: Support for [Cosmos DB](https://wiki.genexus.com/commwiki/wiki?53329) added.
* Java adds support for:
  + Servlet API 6
  + Tomcat 10.1
  + References to packages in External Objects via [Java Artifact Id property](https://wiki.genexus.com/commwiki/wiki?53865) and [Java Artifact Version property](https://wiki.genexus.com/commwiki/wiki?53866).

DevOps

* Java: External Objects can be based on libraries in Maven repositories. For more information, see: [External Objects published in repositories](https://wiki.genexus.com/commwiki/wiki?52362).
* New MSBuild task to [create offline Database](https://wiki.genexus.com/commwiki/wiki?3908) for native mobile offline apps.
* Improvements to dependency management when deploying to cloud services.
* New [Package Type property](https://wiki.genexus.com/commwiki/wiki?53373) of Deployment Units: The sources corresponding to a deployment unit can be packaged (.NET).

UX

* Enhanced RTL support in Web (.NET, Java) and Angular. See [SAC #52793](https://www.genexus.com/developers/websac?en,,,52793).
* Dark mode support in GXflow.
* Angular: New set of properties for Progressive Web App (PWA) development. See [SAC #52737](https://www.genexus.com/en/developers/websac?data=52737;;).

Test

* [Test objects can be included in deployment units](https://wiki.genexus.com/commwiki/wiki?54122) and executed in deployment environments.
* [Tests can be executed in parallel via MSBuild](https://wiki.genexus.com/commwiki/wiki?40738,,).
* New menu option to Run All Unit Tests (Ctrl + Shift + U) and checkbox to Select/Unselect All tests in Tests Explorer. See [SAC #52718](https://www.genexus.com/en/developers/websac?data=52718;;).

Technology update & Future Proofing

* Java: Support for Tomcat 10.1 and Servlet spec 6.0. See [SAC #52460](https://www.genexus.com/es/developers/websac?data=52460;;).

### [Compatibility & Installation](#Compatibility+%26+Installation)

* 2 Breaking changes for GeneXusServerlessAPI module. See:
  + [SAC #52621](https://www.genexus.com/en/developers/websac?data=52621;;)
  + [SAC #52624](https://www.genexus.com/en/developers/websac?data=52624;;)
* [Tomcat version property](https://wiki.genexus.com/commwiki/wiki?48352): The value 10.x is replaced by 10.0 in the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092). Therefore, if you configure the Deployment using MSBuild Tasks, you must keep in mind that the value 10.x is no longer valid and the value to use instead is 10.0. See [SAC #52460](https://www.genexus.com/es/developers/websac?data=52460;;).
* ​Browsers running applications using Design System require 'dir' attribute support. See [SAC #52783](https://www.genexus.com/en/developers/websac?data=52783;;).
* [Cryptography data types](https://wiki.genexus.com/commwiki/wiki?22980) deprecated. Use [GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) instead.

## [All Details (Features, more Compatibility aspects, Issues)](#All+Details+%28Features%2C+more+Compatibility+aspects%2C+Issues%29)

Please check these links for additional features, compatibility aspects, issues, and details:

* GeneXus: <https://www.genexus.com/developers/rn?data=0;4;V18;3;V18;2;>
* GeneXus Server: <https://www.genexus.com/developers/rn?data=0;6;V18;3;V18;2;>
* GXflow: <https://www.genexus.com/developers/rn?data=0;3;V18;3;V18;2;>
* GXtest: <https://www.genexus.com/developers/rn?data=0;7;V18;3;V18;2;>


|  |
| --- |
| **Backlinks** |
| [Analytics external object](https://wiki.genexus.com/commwiki/wiki?31415) | [Analytics external object (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54509) | [Analytics external object (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57371) |
| [Analytics Provider property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54454) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Azure Cosmos DB external data store](https://wiki.genexus.com/commwiki/wiki?53330) | [Column Class property in Theme Class (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54472) |
| [Compilation process with the Java Generator (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?53881) | [Compiler Options property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54275) | [Toc:Cosmos DB](https://wiki.genexus.com/commwiki/wiki?53329) | [Cosmos DB Functions to be evaluated at the database](https://wiki.genexus.com/commwiki/wiki?53652) |
| [Cosmos DB Inspector](https://wiki.genexus.com/commwiki/wiki?53475) | [Cosmos DB nulls handling](https://wiki.genexus.com/commwiki/wiki?53633) | [Data Selector property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57171) | [Data Selectors in Grids (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57179) |
| [Deploying Tests](https://wiki.genexus.com/commwiki/wiki?54122) | [Deploying Tests (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54520) | [Deselect method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54487) | [Enable Cloud Storage property](https://wiki.genexus.com/commwiki/wiki?54315) |
| [Enable Multiple Selection property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54466) | [Enable Workflow property](https://wiki.genexus.com/commwiki/wiki?54101) | [Even Row Class property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54474) | [Features that are exclusive to Angular development](https://wiki.genexus.com/commwiki/wiki?46455) |
| [Features that are exclusive to Angular development (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57003) | [KB:FestivalTickets - High Scalability Sample](https://wiki.genexus.com/commwiki/wiki?51266) | [KB:FestivalTickets - High Scalability Sample (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54299) | [Flipping The Interface for Right-to-Left (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54489) |
| [For Each Line command (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57248) | [GAM - Automatic Permissions generated by GeneXus (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?53950) | [Toc:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) |
| [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396) | [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) |
| [GeneXus Super App News and Roadmap](https://wiki.genexus.com/commwiki/wiki?53536) | [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644) | [Google Analytics in Native Mobile Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54515) | [Gradle Options property for Java Generator](https://wiki.genexus.com/commwiki/wiki?54273) |
| [Category:Grid control](https://wiki.genexus.com/commwiki/wiki?24817) | [gx-grid-even-row-class property](https://wiki.genexus.com/commwiki/wiki?54460) | [gx-grid-header-row-class property](https://wiki.genexus.com/commwiki/wiki?35382) | [gx-grid-header-row-class property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54491) |
| [gx-grid-hover-row-class property](https://wiki.genexus.com/commwiki/wiki?54463) | [gx-grid-odd-row-class property](https://wiki.genexus.com/commwiki/wiki?54461) | [gx-grid-row-class property](https://wiki.genexus.com/commwiki/wiki?32772) | [gx-grid-row-class property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54492) |
| [gx-grid-selected-row-class property](https://wiki.genexus.com/commwiki/wiki?54462) | [GXtest Menu Commands (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54365) | [Hover Row Class property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54477) | [How to create a PWA using GeneXus (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?55046) |
| [HowTo: Add RTL styles (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54443) | [HowTo: Authenticate to Azure Active Directory using GAM (GeneXus 18 Upgrade 2 or pior)](https://wiki.genexus.com/commwiki/wiki?54393) | [HowTo: Configure OAuth 2.0 authentication with Azure AD (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55882) | [HowTo: Configure OAuth 2.0 authentication with Microsoft Entra ID](https://wiki.genexus.com/commwiki/wiki?54371) |
| [HowTo: Configure Push Notifications in Android Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54521) | [HowTo: Configure Push Notifications in Apple Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54517) | [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?53875) | [HowTo: Deploy an Application to Docker (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54337) |
| [HowTo: Deploy as an Azure Web App (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54348) | [HowTo: Use LocalNotifications external object in Native Mobile apps (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54591) | [Initial value property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54229) | [Install Google Tag Manager Support property](https://wiki.genexus.com/commwiki/wiki?54266) |
| [Integrated Security Level property (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54226) | [iOS Device Registration Mode property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54518) | [Java Artifact Id property](https://wiki.genexus.com/commwiki/wiki?53865) | [Java Artifact Version property](https://wiki.genexus.com/commwiki/wiki?53866) |
| [LocalNotifications external object (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54527) | [Logout options for Single Sign On using GAM](https://wiki.genexus.com/commwiki/wiki?32336) | [MSBuild Tasks (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54112) | [MSBuild Tasks for Running Tests (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54200) |
| [NotificationParameters external object](https://wiki.genexus.com/commwiki/wiki?39559) | [Odd Row Class property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54475) | [OpenAPI import tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54370) | [Package Type property (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54658) |
| [Permission Prefix property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?53928) | [Pin Image property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54382) | [Query Object Compatibility](https://wiki.genexus.com/commwiki/wiki?11032) | [Read Replica property](https://wiki.genexus.com/commwiki/wiki?54190) |
| [Real-time translation of RTL languages (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54495) | [Refresh method for Grid controls (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57357) | [RemoteNotifications external object](https://wiki.genexus.com/commwiki/wiki?39399) | [Running MSbuild using GXtest Target (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54203) |
| [Select method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54486) | [Selected Row Class property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54476) | [Selection Type property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54490) | [SelectionChanged Event (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54483) |
| [Services URL Mode property](https://wiki.genexus.com/commwiki/wiki?54361) | [SetLanguage function (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54431) | [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449) | [Translation types](https://wiki.genexus.com/commwiki/wiki?54437) |
| [Translation types (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54444) | [Trigger type property (GeneXus 18 upgrade 4)](https://wiki.genexus.com/commwiki/wiki?54594) | [Use Read Replica property](https://wiki.genexus.com/commwiki/wiki?54189) | [Using Read Replicas in GeneXus](https://wiki.genexus.com/commwiki/wiki?54289) |
| [Web Frontend Application Description property](https://wiki.genexus.com/commwiki/wiki?54260) | [Web Frontend Application Icon property](https://wiki.genexus.com/commwiki/wiki?54264) | [Web Frontend Application Name property](https://wiki.genexus.com/commwiki/wiki?54258) | [Web Frontend Application property](https://wiki.genexus.com/commwiki/wiki?54265) |
| [Web Frontend Application Short Name property](https://wiki.genexus.com/commwiki/wiki?54259) | [Web Frontend Background Color property](https://wiki.genexus.com/commwiki/wiki?54262) | [Web Frontend Display Mode property](https://wiki.genexus.com/commwiki/wiki?54261) | [Web Frontend Theme Color property](https://wiki.genexus.com/commwiki/wiki?54263) |
| [WebFrontend Google Tag Manager Container Id property](https://wiki.genexus.com/commwiki/wiki?54267) |

---
