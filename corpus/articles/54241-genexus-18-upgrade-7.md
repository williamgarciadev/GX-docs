---
title: "GeneXus 18 Upgrade 7"
source_id: 54241
source_url: https://wiki.genexus.com/commwiki/wiki?54241
genexus_version: "18"
---

# GeneXus 18 Upgrade 7

This article is an overview of GeneXus 18 Upgrade 7 features (compared to GeneXus 18 Upgrade 6) and what needs to be considered to adopt it.

It has been released at December 15th, 2023.

## [Download Preview](#Download+Preview)

<https://www.genexus.com/en/developers/downloadcenter?data=6239>

## [Overview](#Overview)

This is an important technology and security update. It features generation for Angular 17 and Android 14 in the front end; .NET 8 and Java 21 in the back end.

### [Design](#Design)

* The new [gx-grid-column-hidden property](https://wiki.genexus.com/commwiki/wiki?56456) allows you to hide/show columns in the [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449)s of [Panels](https://wiki.genexus.com/commwiki/wiki?24829) depending, for example, on screen size or other conditions.
* It is also possible to customize the size of the columns of Tabular Grids in Panels depending, for example, on screen size or other details by setting the [gx-grid-column-size property](https://wiki.genexus.com/commwiki/wiki?56550).
* New properties are available to configure fonts in [DSO](https://wiki.genexus.com/commwiki/wiki?47375) classes: [text-transform property](https://wiki.genexus.com/commwiki/wiki?40682), [font-style property](https://wiki.genexus.com/commwiki/wiki?56524), [font-weight property](https://wiki.genexus.com/commwiki/wiki?43671).

### [User Experience](#User+Experience)

* To improve UI fluency when processes (e.g. Generative AI) send text, some properties and methods have been added to the GeneXus language: [Reading and writing chunked responses](https://wiki.genexus.com/commwiki/wiki?55630).
* New directives of Angular 17 are used to improve performance in grids among others.

### [Integration](#Integration)

* Angular: [External Object](https://wiki.genexus.com/commwiki/wiki?5669) has new properties to reference NPM packages. [SAC #53754](www.genexus.com/es/developers/websac?data=53754;;)

### [Backend](#Backend)

* .NET
  + [Generate Observability span property](https://wiki.genexus.com/commwiki/wiki?55801) to automatically associate telemetry information to related GeneXus objects.
  + New Log Output property value to deploy logs to Azure Application Insights. [SAC #53613](www.genexus.com/es/developers/websac?data=53613;;)
* API
  + New [Description annotation](https://wiki.genexus.com/commwiki/wiki?56430) to add a documentation text to each API Object method.

### [Technology update, installation requirements update, and main compatibility aspects](#Technology+update%2C+installation+requirements+update%2C+and+main+compatibility+aspects)

* [Angular 17](https://wiki.genexus.com/commwiki/wiki?42541)
* [Android 14](https://wiki.genexus.com/commwiki/wiki?14449)
* [.NET 8](https://wiki.genexus.com/commwiki/wiki?38605)
* [Java 21, Gradle 8.4](https://wiki.genexus.com/commwiki/wiki?54302)

## [All Details (Features, More Compatibility Aspects, Issues)](#All+Details+%28Features%2C+More+Compatibility+Aspects%2C+Issues%29)

Please check these links for additional features, compatibility aspects, issues, and details:

GeneXus: <https://www.genexus.com/developers/rn?data=0;4;V18;7;V18;6;>  
GeneXus Server: <https://www.genexus.com/developers/rn?data=0;6;V18;7;V18;6;>  
GXflow: <https://www.genexus.com/developers/rn?data=0;3;V18;7;V18;6;>  
GXtest: <https://www.genexus.com/developers/rn?data=0;7;V18;7;V18;6;>


|  |
| --- |
| **Backlinks** |
| [.NET Generator Requirements (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55956) | [Android Requirements (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56500) | [ApplicationBars Theme Class (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56454) |
| [Buffer Response property](https://wiki.genexus.com/commwiki/wiki?55195) | [Description annotation](https://wiki.genexus.com/commwiki/wiki?56430) | [EOF Property](https://wiki.genexus.com/commwiki/wiki?6975) | [EOF Property (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55641) |
| [Font All Caps property (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56518) | [font-style property](https://wiki.genexus.com/commwiki/wiki?56524) | [GAM - Applications (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?57690) | [GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56244) |
| [Category:GeneXus .NET Generator (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?57219) | [Toc:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) | [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240) |
| [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) | [GeneXus Super App News and Roadmap](https://wiki.genexus.com/commwiki/wiki?53536) | [GeneXus XmlSignature Module](https://wiki.genexus.com/commwiki/wiki?43921) |
| [gx-grid-column-hidden property](https://wiki.genexus.com/commwiki/wiki?56456) | [gx-grid-column-size property](https://wiki.genexus.com/commwiki/wiki?56550) | [gx-hide-date-time-picker property](https://wiki.genexus.com/commwiki/wiki?56050) | [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) |
| [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) | [Javascript External Name property](https://wiki.genexus.com/commwiki/wiki?56499) | [Javascript Module Name property](https://wiki.genexus.com/commwiki/wiki?56496) | [Javascript Module Path property](https://wiki.genexus.com/commwiki/wiki?56406) |
| [Javascript Module Path property in Methods](https://wiki.genexus.com/commwiki/wiki?56478) | [Javascript Module Reference property](https://wiki.genexus.com/commwiki/wiki?56493) | [Log level property (GeneXus 18 upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56151) | [Log output property (GeneXus 18 upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56148) |
| [Log settings with environment variables (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56152) | [MSBuild Tasks for Running Tests (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56137) | [My first Angular application (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?57319) |
| [Observability with Azure Monitor Application Insights (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56153) | [ReadChunk method](https://wiki.genexus.com/commwiki/wiki?55645) | [Reading and writing chunked responses](https://wiki.genexus.com/commwiki/wiki?55630) | [Should Await For Completion property (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?57562) |
| [SOAP Action property in Data Providers](https://wiki.genexus.com/commwiki/wiki?56002) | [Style property in Font Theme Class (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56525) | [Test Preferences (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56007) | [text-transform property](https://wiki.genexus.com/commwiki/wiki?40682) |
| [Use Background Location property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57354) | [KB:Verdant Bank - GeneXus Super App Sample](https://wiki.genexus.com/commwiki/wiki?56766) |

---
