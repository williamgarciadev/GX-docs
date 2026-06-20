---
title: "GeneXus 18 Upgrade 6"
source_id: 54240
source_url: https://wiki.genexus.com/commwiki/wiki?54240
genexus_version: "18"
---

# GeneXus 18 Upgrade 6

This is an overview of GeneXus 18 Upgrade 6 (compared to GeneXus 18 Upgrade 5) and what should be taken into account when adopting it.

Upgrade 6 was released on November 3, 2023.

## [Download](#Download)

<https://www.genexus.com/en/developers/downloadcenter?data=6004>

## [Overview](#Overview)

This upgrade features important advancements in several key aspects. It includes a new Super App Object to create Super Apps with GeneXus, which completes the features required for creating a Super App from scratch, or for converting any app into a super app. It is also a step forward in simplifying the creation of back offices with Angular since it features the tabular grid UI control, as well as automatic refresh mechanisms in Panels.

Additionally, it contains important technology updates, as it supports XCode 15 and MacOS Sonoma (14) to develop native mobile iOS Applications or Super Apps; it also features a GeneXus Projects Navigator for prototyping Android apps and mini apps (as iOS). It is the first stable version that makes it possible to develop Java Spring Boot solutions (Beta).

Below is a list of other interesting features in several areas:

#### [Angular](#Angular)

* The new [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449) is now ready to be used for production purposes. New properties have been added to [control paging](https://wiki.genexus.com/commwiki/wiki?55902), to [hide](https://wiki.genexus.com/commwiki/wiki?55877) or [freeze](https://wiki.genexus.com/commwiki/wiki?55833) columns, etc.
* The [Automatic refresh property](https://wiki.genexus.com/commwiki/wiki?6803) has been added to Panels so that grids are refreshed automatically upon changes in filter values.

#### [Backend](#Backend)

* APIs: [Authorization permissions](https://wiki.genexus.com/commwiki/wiki?55405) can now be set at the service level.
* Java
  + [Spring Boot](https://wiki.genexus.com/commwiki/wiki?55782) support added (Beta).
  + [Generate Observability span property](https://wiki.genexus.com/commwiki/wiki?55801) to automatically associate telemetry information to related GeneXus objects.
* .NET:
  + Support for [iText 8](https://wiki.genexus.com/commwiki/wiki?54844) added.
  + Connection to SQL Server can use Microsoft Entra ID (ex Azure AD) authentication.

#### [GAM & Security](#GAM+%26+Security)

* Simplified support for SSO and privacy matters in Super apps and Mini apps scenarios.
* API Key authentication support added. [More Information...](https://wiki.genexus.com/commwiki/wiki?56104)
* Out-of-the-box GAM backoffice now available in [multiple languages](https://wiki.genexus.com/commwiki/wiki?55986), allowing you to choose between light and dark UI, among other UI improvements.

#### [Native Mobile](#Native+Mobile)

* Knowledge Base Navigator (KBN) has been renamed to GeneXus Projects Navigator (GPN).
* A GPN for Android has been published in the Google Play Store. Now you can prototype online apps, or Mini apps, using the GPN in Android as in iOS, which accelerates prototyping and reduces some related software requirements. See [Android Execution Type property](https://wiki.genexus.com/commwiki/wiki?55300).
* MacOS Sonoma (14) support added.
* XCode 15 support added.

#### [Testing](#Testing)

* Web UI Tests support Chrome 116 or higher.

#### [Super Apps](#Super+Apps)

* The new [Super App object](https://wiki.genexus.com/commwiki/wiki?53457) allows modeling and building Super Apps with GeneXus. Now, in addition to converting an existing app that has not been built with GeneXus into a Super App, you will also be able to create, with GeneXus, a Super App from scratch, or convert an app built with GeneXus into a Super App.
* Support for Web Mini apps has been added. Therefore, Mini apps can be either native mobile (built with the Native Mobile generators), or Web (built with GeneXus Web generators or with other technologies).

### [Technology update, installation requirements update, and main compatibility aspects](#Technology+update%2C+installation+requirements+update%2C+and+main+compatibility+aspects)

* Java: Gradle version was upgraded to 8.3, making it possible to build KBs with JDK 20.

## [All Details (Features, More Compatibility Aspects, Issues)](#All+Details+%28Features%2C+More+Compatibility+Aspects%2C+Issues%29)

Please check these links for additional features, compatibility aspects, issues, and details:

GeneXus: <https://www.genexus.com/developers/rn?data=0;4;V18;6;V18;5;>  
GeneXus Server: <https://www.genexus.com/developers/rn?data=0;6;V18;6;V18;5;>  
GXflow: <https://www.genexus.com/developers/rn?data=0;3;V18;6;V18;5;>  
GXtest: <https://www.genexus.com/developers/rn?data=0;7;V18;6;V18;5;>


|  |
| --- |
| **Backlinks** |
| [Android Execution Type property](https://wiki.genexus.com/commwiki/wiki?55300) | [Apple Requirements](https://wiki.genexus.com/commwiki/wiki?19478) | [Automatic refresh property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55923) |
| [AzureQueue.MessageQueueProvider external object (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55673) | [AzureServiceBus.MessageBrokerProvider external object (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55677) | [Base Trn property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55948) | [Client Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57067) |
| [Client side configuration for GAMRemoteREST Authentication type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57064) | [Column Freeze property in Tabular Grid Control Column](https://wiki.genexus.com/commwiki/wiki?55833) | [Column Hidden property in Tabular Grid Control Column](https://wiki.genexus.com/commwiki/wiki?55816) | [Column Hideable property in Tabular Grid Control Column](https://wiki.genexus.com/commwiki/wiki?55877) |
| [Column Image property in Tabular Grid Control Column](https://wiki.genexus.com/commwiki/wiki?55829) | [Column Resizable property in Tabular Grid Control Column](https://wiki.genexus.com/commwiki/wiki?55876) | [Column Title Visible property in Tabular Grid Control Column](https://wiki.genexus.com/commwiki/wiki?55860) | [Column Tooltip property in Tabular Grid Control Column](https://wiki.genexus.com/commwiki/wiki?55830) |
| [Column Visible property in Tabular Grid control Column](https://wiki.genexus.com/commwiki/wiki?55858) | [Conditions property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55966) | [Date data type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55760) | [Execution for Android Using the Device (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?56063) |
| [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55934) | [FirstPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55984) | [Flexible client version property](https://wiki.genexus.com/commwiki/wiki?55856) | [GAM - OAuth User Scopes (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55820) |
| [Toc:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55768) | [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239) |
| [Category:GeneXus Generators (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55944) | [GeneXus Super App News and Roadmap](https://wiki.genexus.com/commwiki/wiki?53536) | [GotoPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55994) | [GXtest MSBuild Tasks (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?57487) |
| [HowTo: Authenticate to Azure Active Directory using GAM (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55881) | [HowTo: My first GeneXus Java Application (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55769) | [HowTo: Observability of your GeneXus applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55863) |
| [HowTo: Use API Key to request services from an application](https://wiki.genexus.com/commwiki/wiki?56104) | [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57020) | [Image manipulation API](https://wiki.genexus.com/commwiki/wiki?39415) | [Image manipulation API (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55714) |
| [Java Framework property](https://wiki.genexus.com/commwiki/wiki?55711) | [Knowledge Base Navigator (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?56059) | [LastPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55989) | [NextPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55985) |
| [Observability in GeneXus Apps (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55862) | [Orders property (GeneXus 18 upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55997) | [Paging Controls property](https://wiki.genexus.com/commwiki/wiki?55744) | [PDF Reports (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55935) |
| [PDF Reports Library property (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55933) | [Permissions by Method in the API object](https://wiki.genexus.com/commwiki/wiki?55405) | [PreviousPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55992) | [SecurityLevel annotation](https://wiki.genexus.com/commwiki/wiki?55437) |
| [SecurityPermission annotation](https://wiki.genexus.com/commwiki/wiki?55422) | [Server side configuration for GAMRemoteREST Authentication type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57068) | [Spring Boot in Java Application Development](https://wiki.genexus.com/commwiki/wiki?55782) | [Unique property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55955) |

---
