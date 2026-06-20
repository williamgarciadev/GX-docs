---
title: "GeneXus 18 Upgrade 5"
source_id: 54239
source_url: https://wiki.genexus.com/commwiki/wiki?54239
genexus_version: "18"
---

# GeneXus 18 Upgrade 5

This article is an overview of GeneXus 18 Upgrade 5 features (compared to [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238)) and what needs to be taken into account to adopt it.

It was released on August 29.

## [Download](#Download)

<https://www.genexus.com/en/developers/downloadcenter?data=5996>

## [Overview](#Overview)

UX of generated applications is improved in this upgrade, since now it adds Accessibility support in Angular apps, and UIs can show responses that APIs send in chunks, which is particularly useful when interacting with Generative AI APIs. In addition, it has the new Event Messaging API, a step forward to broader support for Event-driven scenarios. For GXflow users, the adoption of new upgrades is simplified because the installation of non-standard platforms is now automated.

Below is a list of other interesting features in several areas:

#### [Design](#Design)

* [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) brings your experience closer to the functionality of the [Theme object](https://wiki.genexus.com/commwiki/wiki?16595), by displaying and configuring CSS properties and gx-properties in the [Properties Editor](https://wiki.genexus.com/commwiki/wiki?3160). More information in [HowTo: Configure Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49494).

#### [Modeling](#Modeling)

* [Suggest](https://wiki.genexus.com/commwiki/wiki?8800) supports loading data from Data providers.
* UI Controls in Panels now have specific properties for modeling Accessibility.

#### [Angular](#Angular)

* [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) support was added.
* Accessibility support was added ([Accessible Name property](https://wiki.genexus.com/commwiki/wiki?55454), [Accessible Role property](https://wiki.genexus.com/commwiki/wiki?55453),[Accessible Name Custom property](https://wiki.genexus.com/commwiki/wiki?55469), [Accessible Name Control property](https://wiki.genexus.com/commwiki/wiki?55456)).
* Several improvements in [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449), including Paging support.

#### [Backend generation](#Backend+generation)

* .NET
  + [Event Messaging API](https://wiki.genexus.com/commwiki/wiki?55334) for Azure Event Grid.
  + [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430) can now be triggered by Blob Storage.
  + [GeneXus Office Module](https://wiki.genexus.com/commwiki/wiki?45973) is now available in .NET too.
  + Support for PDF/A in PDF reports.
* Java
  + Support for chunked messages in [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932).

#### [GXflow](#GXflow)

* New database version that requires database reorganization.
* Automatic installation of non-standard platforms (such as .NET/DB2, Java/Oracle, etc.).

#### [DevOps](#DevOps)

* Impact Analysis Report: New message informs when the reorganization cannot be done just with scripting.

GXtest

* Set As Expected button is available in the Assertion comparer tab.
* Improved [HTML Report](https://wiki.genexus.com/commwiki/wiki?43925).
* Improved SDT and SDT collections initialization when using Create Unit Test option.
* Enabled filtering by test results in the Tests Results window.

### [Installation and Compatibility aspects to take into account:](#Installation+and+Compatibility+aspects+to+take+into+account%3A)

* GXflow:
  + New database version that requires database reorganization.
  + New minimum version supported for MySQL (5.7.0).

## [All Details (Features, more Compatibility aspects, Issues)](#All+Details+%28Features%2C+more+Compatibility+aspects%2C+Issues%29)

Please check these links for additional features, compatibility aspects, issues, and details:

GeneXus: <https://www.genexus.com/developers/rn?data=0;4;V18;5;V18;4;>  
GeneXus Server: <https://www.genexus.com/developers/rn?data=0;6;V18;5;V18;4;>  
GXflow: <https://www.genexus.com/developers/rn?data=0;3;V18;5;V18;4;>  
GXtest: <https://www.genexus.com/developers/rn?data=0;7;V18;5;V18;4;>


|  |
| --- |
| **Backlinks** |
| [Accessible Name Control property](https://wiki.genexus.com/commwiki/wiki?55456) | [Accessible Name Custom property](https://wiki.genexus.com/commwiki/wiki?55469) | [Accessible Name property](https://wiki.genexus.com/commwiki/wiki?55454) |
| [Accessible Role property](https://wiki.genexus.com/commwiki/wiki?55453) | [Additional connection string attributes property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55988) | [Azure Blob Storage triggered functions](https://wiki.genexus.com/commwiki/wiki?55088) | [AzureEventGrid.EventGridRouterProvider external object](https://wiki.genexus.com/commwiki/wiki?55341) |
| [Base64UrlEncoder](https://wiki.genexus.com/commwiki/wiki?55420) | [Building Azure Serverless from sources](https://wiki.genexus.com/commwiki/wiki?55350) | [Building Azure Serverless from sources (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?56809) | [Column Size property in Tabular Grid Control Column](https://wiki.genexus.com/commwiki/wiki?55506) |
| [Data Source From property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55489) | [Design System Class Properties (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55682) | [Design System Class Properties List (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55680) | [DesignOps - Conventions (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55465) |
| [DesignOps - FAQ and Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46880) | [Edit with Suggest](https://wiki.genexus.com/commwiki/wiki?55531) | [Event Messaging API](https://wiki.genexus.com/commwiki/wiki?55334) | [Event Messaging API: CloudEvent SDT](https://wiki.genexus.com/commwiki/wiki?55339) |
| [Event Messaging API: EventGridSchema SDT](https://wiki.genexus.com/commwiki/wiki?55344) | [EventRouter external object](https://wiki.genexus.com/commwiki/wiki?55337) | [Filter by UI property](https://wiki.genexus.com/commwiki/wiki?55701) | [Flip.Start event (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55467) |
| [Toc:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238) | [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917) |
| [GeneXus JWT Module](https://wiki.genexus.com/commwiki/wiki?43980) | [GeneXus Office Module](https://wiki.genexus.com/commwiki/wiki?45973) | [GeneXus Office Module (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55218) | [GeneXus XmlSignature Module](https://wiki.genexus.com/commwiki/wiki?43921) |
| [GetDescriptionByKey Procedure Parameters property](https://wiki.genexus.com/commwiki/wiki?55468) | [GetDescriptionByKey Procedure property](https://wiki.genexus.com/commwiki/wiki?55413) | [HowTo: Configure Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49494) |
| [HowTo: Configure OAuth 2.0 authentication with Azure AD (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55882) | [HowTo: Define an API object with a security scheme (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55404) | [HowTo: Using the Data Source From property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55521) | [Item Descriptions property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?56079) |
| [Item Values property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?56077) | [JWT Utils](https://wiki.genexus.com/commwiki/wiki?43986) | [Marker Clustering property for Maps in Panels](https://wiki.genexus.com/commwiki/wiki?55187) | [On assignment change property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55694) |
| [Paging property in Tabular Grid Control](https://wiki.genexus.com/commwiki/wiki?55902) | [PDF Reports Library property (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55459) | [PDF/A format in PDF reports](https://wiki.genexus.com/commwiki/wiki?55602) | [PDFReport.ini file format (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55599) |
| [Permission Prefix property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55357) | [SecurityAPICommons Module](https://wiki.genexus.com/commwiki/wiki?47252) | [StoreInterop external object](https://wiki.genexus.com/commwiki/wiki?53952) | [Test Execution Results Report (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55594) |
| [Trigger type property](https://wiki.genexus.com/commwiki/wiki?51466) |

---
