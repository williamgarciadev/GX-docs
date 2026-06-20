---
title: "GeneXus 18 Upgrade 9"
source_id: 54243
source_url: https://wiki.genexus.com/commwiki/wiki?54243
genexus_version: "18"
---

# GeneXus 18 Upgrade 9

This article is an overview of GeneXus 18 Upgrade 9 features (compared to [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242)) and what needs to be considered to adopt it.

It is scheduled to be released by the end of April 2024.

## [Download Preview](#Download+Preview)

<https://www.genexus.com/en/developers/downloadcenter?data=4978>

## [Overview](#Overview)

This upgrade features important stability and security improvements, along with some new features

Cloud-native

* Observability (Traces and Metrics) using AWS X-Ray and AWS CloudWatch for a .NET application. [HowTo](https://wiki.genexus.com/commwiki/wiki?57258).
* Amazon S3 SDK updated, new values for [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121).

### [Design](#Design)

* The new [gx-grid-focused-row-class property](https://wiki.genexus.com/commwiki/wiki?57657) allows you to apply a style to a focused row while navigating a [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449) using the keyboard.

### [New methods and functions](#New+methods+and+functions)

#### [New methods for Collections](#New+methods+for+Collections)

These new methods introduce enhanced capabilities for managing collections:

* [AddRange method](https://wiki.genexus.com/commwiki/wiki?57654)**:** Adds the elements of the specified collection at a given position in the collection to which the method is applied.
* [RemoveRange method](https://wiki.genexus.com/commwiki/wiki?57655): Removes a range of items from a collection starting at Index.
* [Set](https://wiki.genexus.com/commwiki/wiki?57662): Replaces the element that is in the specified position with the provided element. Returns true if the operation succeeds.

#### [New functions](#New+functions)

* [Abs function](https://wiki.genexus.com/commwiki/wiki?57730): Returns the absolute value of a number given as a parameter.
* [urlDecode function](https://wiki.genexus.com/commwiki/wiki?57664): Converts special characters encoded in a URL to their original form.

### [Apple](#Apple)

New Calendar properties were added to explain why an application is requesting access to the iOS device's calendar:

* [Calendars Full Access Usage Description property](https://wiki.genexus.com/commwiki/wiki?57644): is used when the app needs to access, modify and create events in the user's calendar.
* [Calendars Write Only Usage Description property](https://wiki.genexus.com/commwiki/wiki?57643): is used when the app only needs permissions to add events to the calendar, without the need to access or modify existing events.

### [Accessibility](#Accessibility)

[Accessible Name property](https://wiki.genexus.com/commwiki/wiki?55454) is now available for Android generator.

This property allows associating accessible names to UI elements, facilitating the user experience for those relying on assistive technologies.

## [All Details (Features, More Compatibility Aspects, Issues)](#All+Details+%28Features%2C+More+Compatibility+Aspects%2C+Issues%29)

Please check these links for additional features, compatibility aspects, issues, and details:

IDE, Modeling & Generators: <https://www.genexus.com/developers/rn?data=0;4;V18;9;V18;8;>  
Super Apps: <https://www.genexus.com/developers/rn?data=0;9;V18;9;V18;8;>  
SAP: <https://www.genexus.com/developers/rn?data=0;8;V18;9;V18;8;>  
GeneXus Server: <https://www.genexus.com/developers/rn?data=0;6;V18;9;V18;8;>  
GXflow: <https://www.genexus.com/developers/rn?data=0;3;V18;9;V18;8;>  
GXtest: <https://www.genexus.com/developers/rn?data=0;7;V18;9;V18;8;>


|  |
| --- |
| **Backlinks** |
| [Abs function](https://wiki.genexus.com/commwiki/wiki?57730) | [Accessible Name property (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57813) | [AddRange method](https://wiki.genexus.com/commwiki/wiki?57654) |
| [Calendars Full Access Usage Description property](https://wiki.genexus.com/commwiki/wiki?57644) | [Calendars Write Only Usage Description property](https://wiki.genexus.com/commwiki/wiki?57643) | [Deploy Java application to Docker and Kubernetes using Redis](https://wiki.genexus.com/commwiki/wiki?57627) | [Floating Point Operation Precision property](https://wiki.genexus.com/commwiki/wiki?57658) |
| [GAM - Events subscription (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57625) | [GAM - OpenID Connect Authentication Type (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57652) | [GAM configuration to send emails (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57732) | [Toc:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) |
| [GeneXus 18 upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) | [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) | [GeneXus Super App News and Roadmap](https://wiki.genexus.com/commwiki/wiki?53536) |
| [gx-grid-focused-row-class property](https://wiki.genexus.com/commwiki/wiki?57657) | [GXtest UI Commands - WebDriver (GeneXus 18 Upgrade 8)](https://wiki.genexus.com/commwiki/wiki?57767) | [HowTo: Deploy an application to Google App Engine (GeneXus 18 Upgrade 8)](https://wiki.genexus.com/commwiki/wiki?57567) |
| [HowTo: Watch .NET logs using OpenTelemetry (with SigNoz)](https://wiki.genexus.com/commwiki/wiki?57281) | [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57694) | [Json Collection Serialization property (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57774) |
| [Manual Instrumentation: Tracing](https://wiki.genexus.com/commwiki/wiki?57566) | [Merge Dynamic Libraries property (GeneXus 18 Upgrade 8)](https://wiki.genexus.com/commwiki/wiki?57469) | [Modules MSBuild Tasks (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57500) | [RemoveRange method](https://wiki.genexus.com/commwiki/wiki?57655) |
| [Set method in Collections](https://wiki.genexus.com/commwiki/wiki?57662) | [Should Await For Completion property (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?57562) | [Standard Signatures](https://wiki.genexus.com/commwiki/wiki?57502) | [urlDecode function](https://wiki.genexus.com/commwiki/wiki?57664) |

---
