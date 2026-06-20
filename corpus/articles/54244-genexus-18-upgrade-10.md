---
title: "GeneXus 18 Upgrade 10"
source_id: 54244
source_url: https://wiki.genexus.com/commwiki/wiki?54244
genexus_version: "18"
---

# GeneXus 18 Upgrade 10

This article is an overview of GeneXus 18 Upgrade 10 features (compared to [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243)) and what needs to be considered to adopt it.

It was released on June 26, 2024.

### [Download](#Download)

<https://www.genexus.com/en/developers/downloadcenter?data=6276>

### [Overview](#Overview)

This upgrade introduces several new features and improvements, enhancing development capabilities and streamlining deployment processes.

### [Modeling](#Modeling)

* [Dictionary External Object](https://wiki.genexus.com/commwiki/wiki?58246): This EO provides a convenient way to store and retrieve key-value pairs. This object allows you to manage collections of data where each item is uniquely identified by a key.
* Improvements to define object visibility: The [Root module visibility property](https://wiki.genexus.com/commwiki/wiki?58078) is new at the KB [Version](https://wiki.genexus.com/commwiki/wiki?7860) level. The available values are: 'Public', 'Knowledge Base', 'Internal', and 'Private'. In addition, the 'Knowledge Base' value has been added to the [Object Visibility property](https://wiki.genexus.com/commwiki/wiki?22473) so that the same values are available for both properties. Read more at [SAC #54430](https://www.genexus.com/en/developers/websac?data=54430;;).

### [Backend](#Backend)

* (Java) GeneXus now supports [Spring Boot in Java Application Development](https://wiki.genexus.com/commwiki/wiki?55782), enabling you to leverage this popular framework for building robust and scalable backend systems. You can also use Spring Boot to deploy applications using the GeneXus Deploy Engine. Read more at [Deploying Java applications with Spring Boot](https://wiki.genexus.com/commwiki/wiki?58269).
* (.NET) Update of .NET Generator packages. Read more at [SAC #54498](https://www.genexus.com/developers/websac?en,,,54498).

### [Angular](#Angular)

* The generator now generates code updated to [Angular 17.3](https://wiki.genexus.com/commwiki/wiki?42541).
* The OneSignal SDK has been updated to version 5, which uses API 11.2. Read more at [SAC #54445](https://www.genexus.com/developers/websac?en,,,54445).
* Three new methods are now supported for handling Collections: [AddRange](https://wiki.genexus.com/commwiki/wiki?57654), [RemoveRange](https://wiki.genexus.com/commwiki/wiki?57655), and [Set](https://wiki.genexus.com/commwiki/wiki?57662).
* Two new functions are now supported: [UrlEncode](https://wiki.genexus.com/commwiki/wiki?57781), and [UrlDecode](https://wiki.genexus.com/commwiki/wiki?57664).

### [Improvements for Cloud Prototyping](#Improvements+for+Cloud+Prototyping)

This version introduces security improvements for cloud prototyping by changing deployment server URLs to 'sandbox' (instead of 'apps6', 'apps5', 'apps-angular'). In addition, the auto-generated user passwords are different from user IDs. Read more at [SAC #54380](https://www.genexus.com/en/developers/websac?data=54380;;).

### [GAM](#GAM)

* There is a new property for the Timeout handling of the refresh\_token in the GAMSecurityPolicy external object. Read more at [OAuthRefreshTokenExpire property](https://wiki.genexus.com/commwiki/wiki?58097).
* Three new properties are available to improve Timeout configurations in the GAMRepository external object:
  + [TimeoutForUserChangePasswordAfterLogin property](https://wiki.genexus.com/commwiki/wiki?58085)
  + [TimeoutToCompleteRequiredUserDataAfterLogin property](https://wiki.genexus.com/commwiki/wiki?58082)
  + [TimeoutToFinishOAuthAuthenticationUsingIDP property](https://wiki.genexus.com/commwiki/wiki?58086)

### [Super Apps and Mini Apps](#Super+Apps+and+Mini+Apps)

#### [Mini App Object](#Mini+App+Object)

The [Mini App object](https://wiki.genexus.com/commwiki/wiki?58037) has been created to facilitate development and integration with Super Apps.

#### [Super App mock](#Super+App+mock)

This feature allows testing a Mini App on iOS and Android with a [mock Super App API](https://wiki.genexus.com/commwiki/wiki?58219), facilitating independent development and testing without relying on the real Super App.

For that purpose, the Mini App Object offers the following properties that allow emulation and efficient connection with the [Super App API](https://wiki.genexus.com/commwiki/wiki?58207):

* [Super App API Mock property](https://wiki.genexus.com/commwiki/wiki?57943)
* [Super App API External Object property](https://wiki.genexus.com/commwiki/wiki?57944)
* [Main Object property (for Mini Apps)](https://wiki.genexus.com/commwiki/wiki?53629)

#### [Provisioning.GetByFilters Method](#Provisioning.GetByFilters+Method)

The [Provisioning.GetByFilters method](https://wiki.genexus.com/commwiki/wiki?57960) has been introduced to enhance the search capabilities for Mini Apps in the Mini App Center. It allows searching for Mini Apps based on specific filter criteria.

### [Design](#Design)

New classes allow you to edit the texts of the different levels of the Unanimo sidebar. Read more at [SAC #52690](https://www.genexus.com/developers/websac?en,,,52690).

### [All Details (Features, More Compatibility Aspects, Issues)](#All+Details+%28Features%2C+More+Compatibility+Aspects%2C+Issues%29)

Please check these links for additional features, compatibility aspects, issues, and details:

IDE, Modeling & Generators: <https://www.genexus.com/developers/rn?data=0;4;V18;10;V18;9;>  
Super Apps: <https://www.genexus.com/developers/rn?data=0;9;V18;10;V18;9;>  
SAP: <https://www.genexus.com/developers/rn?data=0;8;V18;10;V18;9;>  
GeneXus Server: <https://www.genexus.com/developers/rn?data=0;6;V18;10;V18;9;>  
GXflow: <https://www.genexus.com/developers/rn?data=0;3;V18;10;V18;9;>  
GXtest: <https://www.genexus.com/developers/rn?data=0;7;V18;10;V18;9;>


|  |
| --- |
| **Backlinks** |
| [Abs function (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58057) | [AddRange method (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58261) | [Allow Collection property](https://wiki.genexus.com/commwiki/wiki?57845) |
| [Application Deployment MSBuild tasks (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58040) | [Application Deployment MSBuild tasks (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58052) |
| [KB:Coffee and Muffins - Mini App Sample for Verdant Bank (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58327) | [Comparing the .NET generator with the .NET Framework generator (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58039) | [Control Type property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57964) | [Default Type property](https://wiki.genexus.com/commwiki/wiki?57846) |
| [Deploy to cloud: Step by Step (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58032) | [Deploying Java applications with Spring Boot](https://wiki.genexus.com/commwiki/wiki?58269) | [Dictionary External Object](https://wiki.genexus.com/commwiki/wiki?58246) | [Category:External Object](https://wiki.genexus.com/commwiki/wiki?5669) |
| [Category:External Object (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57996) | [External Object Types Node](https://wiki.genexus.com/commwiki/wiki?57997) | [External Objects with Type property 'Native Object'](https://wiki.genexus.com/commwiki/wiki?6148) | [External Objects with Type property 'Native Object' (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58043) |
| [External Storage for Multimedia](https://wiki.genexus.com/commwiki/wiki?31120) | [font-weight property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57941) | [KB:Frosty Delights - Mini App Sample for Verdant Bank (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58326) | [GAM - Security Policies (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58087) |
| [Generate OpenAPI Interface property at Deploy Target Options](https://wiki.genexus.com/commwiki/wiki?57978) | [Table of contents:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 upgrade 11](https://wiki.genexus.com/commwiki/wiki?54245) | [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243) |
| [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917) | [GeneXus JWT Module](https://wiki.genexus.com/commwiki/wiki?43980) | [GeneXus Super App News and Roadmap](https://wiki.genexus.com/commwiki/wiki?53536) |
| [GeneXus XmlSignature Module](https://wiki.genexus.com/commwiki/wiki?43921) | [GXSpreadsheet control](https://wiki.genexus.com/commwiki/wiki?12736) | [GXtest config file (GeneXus 18 Upgrade 9 and prior)](https://wiki.genexus.com/commwiki/wiki?57993) | [GXtest Menu Commands (GeneXus 18 Upgrade 9 and prior)](https://wiki.genexus.com/commwiki/wiki?57990) |
| [HowTo: Create a Super App on the Mini App Center (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?57953) | [HowTo: Monitor Azure Functions (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58050) | [HowTo: Upload a Mini App version to the Mini App Center (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?57958) | [Keep Parameters property](https://wiki.genexus.com/commwiki/wiki?57986) |
| [Login retries to lock user property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58371) | [Main Object property (for Mini Apps)](https://wiki.genexus.com/commwiki/wiki?53629) | [Maximum pool size per route property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58081) | [Category:Mini App object](https://wiki.genexus.com/commwiki/wiki?58037) |
| [KB:Mini App Payments - Mini App Sample for non-GeneXus Super App API integration (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58312) | [Modules - Defining an interface (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58150) | [Modules Distribution in GeneXus (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58151) | [OAuth Token expire (minutes) GAM Security Policy property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58155) |
| [OAuthRefreshTokenExpire property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?58097) | [Object Visibility property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58120) | [Packaging Java sources (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?57920) | [PDF Reports Library property (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?57946) |
| [Picture property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58071) | [Property Name property](https://wiki.genexus.com/commwiki/wiki?57843) | [Provisioning.GetByFilters method](https://wiki.genexus.com/commwiki/wiki?57960) | [RemoveRange method (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58260) |
| [Root module visibility property](https://wiki.genexus.com/commwiki/wiki?58078) | [SecurityAPICommons Module](https://wiki.genexus.com/commwiki/wiki?47252) | [Set method in Collections (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58262) |
| [Spring Boot in Java Application Development](https://wiki.genexus.com/commwiki/wiki?55782) | [Super App API External Object property](https://wiki.genexus.com/commwiki/wiki?57944) | [Super App API Mock property](https://wiki.genexus.com/commwiki/wiki?57943) | [Super App API Mocking](https://wiki.genexus.com/commwiki/wiki?58219) |
| [Symmetric Stream Encryption](https://wiki.genexus.com/commwiki/wiki?42682) | [KB:The Movies - Mini App Sample for Verdant Bank (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58316) | [TimeoutForUserChangePasswordAfterLogin property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?58085) | [TimeoutToCompleteRequiredUserDataAfterLogin property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?58082) |
| [TimeoutToFinishOAuthAuthenticationUsingIDP property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?58086) | [Unique Clause (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57977) | [urlDecode function (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58079) | [urlEncode function (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58080) |
| [Valid Types property](https://wiki.genexus.com/commwiki/wiki?57844) |

---
