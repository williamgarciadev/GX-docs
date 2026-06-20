---
title: "GeneXus 18 Upgrade 2"
source_id: 53396
source_url: https://wiki.genexus.com/commwiki/wiki?53396
genexus_version: "18"
---

# GeneXus 18 Upgrade 2

This article is an overview of GeneXus 18 Upgrade 2 features (compared to [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081)) and what needs to be taken into account to adopt it.

It has been released on February 16th, 2023.

## [Download](#Download)

<https://www.genexus.com/en/developers/downloadcenter?data=5979>

## [Overview](#Overview)

This upgrade provides overall stability improvements, especially related to the IDE and Design Systems.

#### [IDE](#IDE)

* This version can be executed without Administrator privileges. More information in [SAC #39359](https://www.genexus.com/developers/websac?es,,,39359)

#### Native Mobile

* The [Invite Message property](https://wiki.genexus.com/commwiki/wiki?19697) can be used in [Wheel Controls](https://wiki.genexus.com/commwiki/wiki?20180)
* Performance improvements in several points, especially when loading the application.

#### Security

* With the [Rm](https://wiki.genexus.com/commwiki/wiki?44966) (remove/delete) function, you can delete files on the remote SFTP server.

#### Angular

* Improved multimedia support: Support added for Video data type, camera API (TakePhoto() and RecordVideo() methods), etc. More information in SACs  [#52300](https://www.genexus.com/developers/websac?es,,,52300), [#52301](https://www.genexus.com/developers/websac?es,,,52301), [#52302](https://www.genexus.com/developers/websac?es,,,52302)
* Support for Tabular grid control (Beta)
* [OTP](https://wiki.genexus.com/commwiki/wiki?48197) and [2FA](https://wiki.genexus.com/commwiki/wiki?48254) support added.

#### User Controls

* Now you can define the [scope (Design, Runtime) of a property](https://wiki.genexus.com/commwiki/wiki?39541)

#### Design System Object

* With the [Go to Class Option (F12)](https://wiki.genexus.com/commwiki/wiki?49353) it is possible to go to the definition of a class that is referenced in an include rule.

#### Back end

* [OpenTelemetry support added](https://wiki.genexus.com/commwiki/wiki?53773) (Beta).
* Java
  + Improvements to dependency management and packaging of third-party libraries related to cloud services & Maven.
  + Dependencies to several third-party libraries updated to the latest versions.
  + The [Parameter Style property](https://wiki.genexus.com/commwiki/wiki?53486) is enabled in the External Objects. This property allows setting how the parameters travel in the invocation of a SOAP service.
* Now you can export a selected Transaction's structure with a parameter called [OnlyStructTrn in the MSBuild Task](https://wiki.genexus.com/commwiki/wiki?3908).
* Improvements to modify at Runtime the [Log settings](https://wiki.genexus.com/commwiki/wiki?53361) in Contained environments.

### Compatibility & Installation

* Apple: XCode 14 is now the lowest supported version. More information in [SAC #52345](https://www.genexus.com/es/developers/websac?data=52345;;).
* Announcement: [Cryptography data types](https://wiki.genexus.com/commwiki/wiki?22980) will be discontinued in GeneXus 18 Upgrade 5. [GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) is on the way to replace these data types. It is recommended to migrate your code and use this API before GeneXus 18 Upgrade 5.

## All Details (Features, more Compatibility aspects, Issues)

Please check these links for additional features, compatibility aspects, issues, and details:

GeneXus: <https://www.genexus.com/developers/rn?data=0;4;V18;2;V18;1;>  
GeneXus Server: <https://www.genexus.com/developers/rn?data=0;6;V18;2;V18;1;>  
GXflow: <https://www.genexus.com/developers/rn?data=0;3;V18;2;V18;1;>  
GXtest: <https://www.genexus.com/developers/rn?data=0;7;V18;2;V18;1;>


|  |
| --- |
| **Backlinks** |
| [Accent Color property (GeneXus 18 Upgrade 1)](https://wiki.genexus.com/commwiki/wiki?56819) | [Camera external object](https://wiki.genexus.com/commwiki/wiki?31296) | [Camera external object (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53919) |
| [KB:eBanking Chatbot sample](https://wiki.genexus.com/commwiki/wiki?54220) | [External Object: Native Object (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?56447) | [FTPS Client](https://wiki.genexus.com/commwiki/wiki?45277) |
| [Toc:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081) | [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853) | [GeneXus FTPS Module](https://wiki.genexus.com/commwiki/wiki?45274) |
| [GeneXus JWT Module](https://wiki.genexus.com/commwiki/wiki?43980) | [HowTo: Use Camera external object in GeneXus for Native Mobile apps (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53920) | [Include style rule (GeneXus 18 Upgrade 1)](https://wiki.genexus.com/commwiki/wiki?53833) | [Invite Message property](https://wiki.genexus.com/commwiki/wiki?19697) |
| [InviteMessage property (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53870) | [Log settings with environment variables (GeneXus 18 upgrade 1)](https://wiki.genexus.com/commwiki/wiki?53615) | [MSBuild Tasks (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53867) | [Parameters Style property in External Object](https://wiki.genexus.com/commwiki/wiki?53486) |
| [PivotTable Main color](https://wiki.genexus.com/commwiki/wiki?41081) | [SFTP Client](https://wiki.genexus.com/commwiki/wiki?44966) | [Start Day property](https://wiki.genexus.com/commwiki/wiki?53764) | [Table Main color property](https://wiki.genexus.com/commwiki/wiki?41115) |
| [User Control Object - Definition of properties (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53689) | [Video data type (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53910) |

---
