---
title: "GeneXus 18 Upgrade 11"
source_id: 54245
source_url: https://wiki.genexus.com/commwiki/wiki?54245
genexus_version: "18"
---

# GeneXus 18 Upgrade 11

This article is an overview of GeneXus 18 Upgrade 11 features (compared to [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244)) and what needs to be considered to adopt it.

It was released on 23 December 2024.

## [Download](#Download)

<https://www.genexus.com/en/developers/downloadcenter?data=6291>

## [Overview](#Overview)

This upgrade features important stability and security improvements, as well as some new features.

#### [Security](#Security)

* New values for [Privacy property (Object Ownership)](https://wiki.genexus.com/commwiki/wiki?59170) to support that ownership is enforced by Bucket and not by ACL.
* Security API supports loading [public key](https://wiki.genexus.com/commwiki/wiki?54578) from Jwks.
* GAM API has new methods in several objects.
* Performance improved in GAM; queries to 'gam.Repository' are cached.
* Several libraries updated.

#### [UX](#UX)

* Design: Import from Design (from Figma) supports designs with events, animations, and transitions.
* In Web Panels at runtime, the cursor is kept in position when an event adds rows.

#### [Android specific](#Android+specific)

* Android: Autogrow support in flex control.
* Performance improvements related to device location API.
* Several libraries have been updated to comply with Google Play.
* Important update related to push notifications (OneSignal library update).

#### [Angular specific](#Angular+specific)

* Numeric fields are shown with pictures even when the field is editable.
* The generator has been updated to Angular 18, the [latest LTS version of Angular](https://angular.dev/reference/releases#actively-supported-versions). Along with Angular 18 you benefit from improved performance and the support of [User Controls](https://wiki.genexus.com/commwiki/wiki?39356) based on Material 3, for example.

#### [GXflow specific](#GXflow+specific)

* Only the standard platforms .NET, .NET Framework, and Java generators for SQL Server will be available in this release of GXflow. Non-standard platforms will not be included. However, this is a temporary situation. If you need support for a non-standard platform, you can request it directly from the support team.

### [Some additional remarks](#Some+additional+remarks)

Over the past few months, we’ve been upgrading our internal development platform and implementing Globant's security policies related to source code protection and deployment processes. This is the first GeneXus release built with our new process, which will be instrumental in delivering new versions more quickly and securely. This transition also enhances our capabilities for regression testing and security scanning of libraries and dependencies in generated applications.

We are excited to see these changes positively impact the overall quality of GeneXus and the applications it generates from now on.

### [Compatibility](#Compatibility)

* This upgrade requires updated patterns (eg.: K2BTools, WWPlus). Please ask their providers for the corresponding update.
* Some components are on the way or need special attention: [More Information...](https://www.genexus.com/developers/websac?en,,,60340)

## [All Details (Features, More Compatibility Aspects, Issues)](#All+Details+%28Features%2C+More+Compatibility+Aspects%2C+Issues%29)

Please check these links for additional features, compatibility aspects, issues, and details:

IDE, Modeling & Generators: <https://www.genexus.com/developers/rn?data=0;4;V18;11;V18;10;>  
Super Apps: <https://www.genexus.com/developers/rn?data=0;9;V18;11;V18;10;>  
SAP: <https://www.genexus.com/developers/rn?data=0;8;V18;11;V18;10;>  
GeneXus Server: <https://www.genexus.com/developers/rn?data=0;6;V18;11;V18;10;>  
GXflow: <https://www.genexus.com/developers/rn?data=0;3;V18;11;V18;10;>  
GXtest: <https://www.genexus.com/developers/rn?data=0;7;V18;11;V18;10;>


|  |
| --- |
| **Backlinks** |
| [Azure Blob Storage triggered functions](https://wiki.genexus.com/commwiki/wiki?55088) | [ContextPath Rewrite: X-Forwarded Headers Support (App behind Reverse Proxy) (GeneXus 18 Upgrade 10)](https://wiki.genexus.com/commwiki/wiki?59271) |
| [Deploying Java applications with Spring Boot (GeneXus 18 Upgrade 10)](https://wiki.genexus.com/commwiki/wiki?59292) | [Table of contents:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) | [GeneXus JWT Module](https://wiki.genexus.com/commwiki/wiki?43980) |
| [GeneXus XmlSignature Module](https://wiki.genexus.com/commwiki/wiki?43921) | [HowTo: Generate GAM trace (GeneXus 18 Upgrade 10 or prior)](https://wiki.genexus.com/commwiki/wiki?58291) | [PublicKey](https://wiki.genexus.com/commwiki/wiki?54578) |
| [RemoteAddr function (GeneXus 18 Upgrade 10 or prior)](https://wiki.genexus.com/commwiki/wiki?59268) | [UrlDecode function (GeneXus 18 Upgrade 10)](https://wiki.genexus.com/commwiki/wiki?59696) | [UrlEncode function (GeneXus 18 Upgrade 10)](https://wiki.genexus.com/commwiki/wiki?59695) |

---
