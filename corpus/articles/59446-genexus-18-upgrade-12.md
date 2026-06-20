---
title: "GeneXus 18 Upgrade 12"
source_id: 59446
source_url: https://wiki.genexus.com/commwiki/wiki?59446
genexus_version: "18"
---

# GeneXus 18 Upgrade 12

This article is an overview of GeneXus 18 Upgrade 12 features (compared to [GeneXus 18 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?54245)) and what needs to be considered to adopt it.

It was released on 24th March 2025.

## [Download](#Download)

<https://www.genexus.com/en/developers/downloadcenter?data=6302;;>

## [Overview](#Overview)

This upgrade delivers significant stability and security enhancements alongside new features and expanded technology support, further strengthening the platform’s low-code development capabilities. This release ensures better alignment with the latest industry standards and provides developers with improved tools for building modern, scalable applications.

Key Highlights:

#### [Platform & Technology Support:](#Platform+%26+Technology+Support%3A)

* Android 15 (API Level 35) support added.
* Xcode 16 compatibility for iOS development.
* Angular 19 support integrated.

#### [iOS Enhancements:](#iOS+Enhancements%3A)

* Full support for Xcode 16.
* Enhanced radio button visualization options for improved UI customization.

#### [Android Enhancements:](#Android+Enhancements%3A)

* Compatibility with Android 15 (API Level 35), ensuring readiness for the latest OS versions.

#### [Angular:](#Angular%3A)

* Updated support for Angular 19, keeping web applications aligned with the latest framework improvements.
* Language Improvements:
  + Support for the [Expression data type](https://wiki.genexus.com/commwiki/wiki?6631).
  + New Clipboard methods: Clipboard.GetText() and Clipboard.SetText().
  + Enhanced LIKE operator usage.
  + Improved RegEx error handling.
  + New Sleep() function for timed execution handling.

#### [Backend Enhancements:](#Backend+Enhancements%3A)

* Support for [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430) in Java, in addition to .NET.
* Extended support for Azure Batch Functions in .NET and Java environments. More information: [Batch Function property](https://wiki.genexus.com/commwiki/wiki?59714).

#### [Team Development Improvements:](#Team+Development+Improvements%3A)

* Event Dispatcher enhancements now allow the cancellation of commits via AfterCommit events—ideal for automating code review processes or enforcing commit policies.

#### [Super Apps Enhancements:](#Super+Apps+Enhancements%3A)

* Security improvements and improved Single Sign-On (SSO) capabilities for both Mini Apps and Super Apps, enabling more secure and seamless user experiences.

### [Compatibility](#Compatibility)

* Android
  + Code generation for Android has new software requirements. Devices require Android 7 or higher.
  + Some default values for HttpClient have been reverted to values of v18u10 or prior.
* New considerations related to PDF Reports that use CJK fonts.

## [All Details (Features, More Compatibility Aspects, Issues)](#All+Details+%28Features%2C+More+Compatibility+Aspects%2C+Issues%29)

Please visit these links for additional features, compatibility aspects, issues, and details:

IDE, Modeling & Generators: <https://www.genexus.com/developers/rn?data=0;4;V18;12;V18;11;>  
Super Apps: <https://www.genexus.com/developers/rn?data=0;9;V18;12;V18;11;>  
SAP: <https://www.genexus.com/developers/rn?data=0;8;V18;12;V18;11;>  
GeneXus Server: <https://www.genexus.com/developers/rn?data=0;6;V18;12;V18;11;>  
GXflow: <https://www.genexus.com/developers/rn?data=0;3;V18;12;V18;11;>  
GXtest: <https://www.genexus.com/developers/rn?data=0;7;V18;12;V18;11;>


|  |
| --- |
| **Backlinks** |
| [Android Requirements (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59561) | [Apple Requirements (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59725) | [Azure Blob Storage triggered functions (GeneXus 18 upgrade 11)](https://wiki.genexus.com/commwiki/wiki?59490) |
| [Azure CosmosDB-triggered functions](https://wiki.genexus.com/commwiki/wiki?54574) | [Azure Event Grid triggered functions](https://wiki.genexus.com/commwiki/wiki?56742) | [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430) | [Azure timer triggered functions (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59656) |
| [Batch Function property](https://wiki.genexus.com/commwiki/wiki?59714) | [Expression data type (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59675) | [Table of contents:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?54245) |
| [GeneXus Super App News and Roadmap](https://wiki.genexus.com/commwiki/wiki?53536) |
| [HowTo: Deploy as Azure Functions (GeneXus 18 Upgrade 11)](https://wiki.genexus.com/commwiki/wiki?59528) | [Include GAM Backend property (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59722) | [Service Bus and Queue Storage triggered Azure functions (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59657) | [Sleep function (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59671) |
| [ToFile method (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59676) | [Trigger Type property](https://wiki.genexus.com/commwiki/wiki?51466) | [Trigger type property (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59705) |

---
