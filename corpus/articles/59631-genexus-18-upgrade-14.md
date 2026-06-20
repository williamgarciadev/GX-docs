---
title: "GeneXus 18 Upgrade 14"
source_id: 59631
source_url: https://wiki.genexus.com/commwiki/wiki?59631
genexus_version: "18"
---

# GeneXus 18 Upgrade 14

This is an overview of the features included in GeneXus 18 Upgrade 14 (compared to [GeneXus 18 Upgrade 13](https://wiki.genexus.com/commwiki/wiki?59630)) and considerations for its adoption.

It will be realeased soon.

## [Download Preview](#Download+Preview)

<https://www.genexus.com/en/developers/downloadcenter?data=6294>

## [Overview](#Overview)

This upgrade delivers significant stability and security enhancements, along with key feature updates across .NET, Java, Native Mobile, and Angular generators. The improvements are designed to increase performance, developer productivity, and compatibility with modern development standards.

### [Backend](#Backend)

* The [ValueHyperlink property](https://wiki.genexus.com/commwiki/wiki?60612) has been implemented in the [ExcelCellRange data type](https://wiki.genexus.com/commwiki/wiki?46081) of the GeneXus Office module. You can now set and obtain hyperlinks in cells or ranges of a spreadsheet, either to a URL or to a local file. ([SAC #60958](https://www.genexus.com/en/developers/websac?data=60958;; ))
* You can use STORAGE\_DEFAULT\_NAME and STORAGE\_DEFAULT\_CLASSNAME environment variables to override the [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) defined in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836). Read more at [Environment Variables for Storage Provider Configuration](https://wiki.genexus.com/commwiki/wiki?60682). ([SAC #60995](https://www.genexus.com/en/developers/websac?data=60995;; ))

### [Modeling](#Modeling)

* The [GeneXusCompression Module](https://wiki.genexus.com/commwiki/wiki?60613) has been implemented, enabling data compression and decompression. It includes the External Objects [Compression External Object](https://wiki.genexus.com/commwiki/wiki?60618), [CompressionConfiguration External Object](https://wiki.genexus.com/commwiki/wiki?60619), and [GXCompressor External Object](https://wiki.genexus.com/commwiki/wiki?60620).
* The GeneXusUI module has been renamed to [GeneXusUIControls module](https://wiki.genexus.com/commwiki/wiki?60714) and now includes the [Chat Control](https://wiki.genexus.com/commwiki/wiki?59254) for enhanced conversational user interfaces ([SAC #60981](https://www.genexus.com/en/developers/websac?data=60981;;)). For example, you can insert a Chat Control in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) or [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) Layout and set the Chat Control [SendMessageHandlerObject property](https://wiki.genexus.com/commwiki/wiki?60797) to the name of a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) that connects to a Globant Enterprise AI API to execute an Assistant defined in a  [Globant Enterprise AI](https://docs.globant.ai/en/wiki?15,Globant+Enterprise+AI+Overview) project. Read more at [HowTo: Use the Chat Control associated with a Procedure that calls a Globant Enterprise AI API](https://wiki.genexus.com/commwiki/wiki?61106).
* [Unanimo](https://wiki.genexus.com/commwiki/wiki?48382) improvements:
  + Complete redesign of Tokens.
  + Restructuring of Design System Objects (each control now includes a DSO with its own styles).
  + The Unanimo\_LegacyTokens module has been added, containing previous token definitions for compatibility reasons. Read more at [Unanimo module components](https://wiki.genexus.com/commwiki/wiki?52175).
  + Additional fixes.

### [Native Mobile](#Native+Mobile)

#### [**Key Highlights, Platform & Technology Support**:](#Key+Highlights%2C+Platform+%26+Technology+Support%3A)

* Android 16 (API Level 36) support added.
* Xcode 26 compatibility for iOS development.

#### [**Android Enhancements**:](#Android+Enhancements%3A)

* Compatibility with Android 16 (API Level 36), ensuring readiness for the latest OS versions.
* Support for 16KB Page Size compatibility in Android dependencies. For more information, read  [Support 16 KB page sizes](https://developer.android.com/guide/practices/page-sizes).
* Compile Android generated code with Gradle. ([SAC #61055](https://www.genexus.com/en/developers/websac?data=61055;; ))

#### [**iOS Enhancements**:](#iOS+Enhancements%3A)

* Full support for Xcode 26 (SDKs iOS 26, watchOS 26, tvOS 29, visionOS 26).
* iOS - Support for Images in Flex tables with 'Adjust container size = true' property. ([SAC #60737](https://www.genexus.com/en/developers/websac?data=60737;; ))

#### [**Miscellaneous**](#Miscellaneous)

* Analytics EO - 'TrackEvent' does not work in some scenarios. ([SAC #60705](https://www.genexus.com/en/developers/websac?data=60705;; ))

### [Angular](#Angular)

* The Angular Generator has been migrated to Angular version 20. ([SAC #61106](https://www.genexus.com/en/developers/websac?data=61106;; ))
* New builder based on ESBuild + Vite has been introduced to reduce development and production times. ([SAC #60991](https://www.genexus.com/en/developers/websac?data=60991;; ))
* Support has been added for 'Orders' and 'Break by' properties in Tabular Grids. ([SAC #60878](https://www.genexus.com/en/developers/websac?data=60878;; ))

### [GAM / Security](#GAM+%2F+Security)

* **OAuth with PKCE**: Support for the PKCE flow in OAuth 2.0. ([SAC #61131](https://www.genexus.com/en/developers/websac?data=61131;; ))
* **GAMRemote with PKCE**: Support for PKCE in GAMRemote. ([SAC #61132](https://www.genexus.com/en/developers/websac?data=61132;; ))
* **New SAML 2.0 implementation**: Adds native support for retrieving user Roles and performing Single Logout (SLO) in SAML 2.0 authentication. ([SAC #61051](https://www.genexus.com/en/developers/websac?data=61051;; ))
* **OAuth 2.0 supports Roles and Sign-out natively**: Support for obtaining user Roles and performing Single Logout (SLO) natively in OAuth 2.0.
* **Allows disabling the oauth/access\_token service**
* **Ability to specify an authentication type instead of a login object**
* **Token reuse at repository level**: Enables token reuse at the repository level.

### [Compatibility](#Compatibility)

* **Unanimo requires NPM (Node Package Manager)**  
  The UserControls distributed with Unanimo version 2.X and the GeneXusUIControls module now use NPM to manage their dependencies. This means that NPM must be installed to perform a Build All in KBs that use them. ([SAC #61107](https://www.genexus.com/developers/websac?,,,61107 ))

## [All Details (Features, More Compatibility Aspects, Issues)](#All+Details+%28Features%2C+More+Compatibility+Aspects%2C+Issues%29)

For additional features, compatibility aspects, issues, and details, refer to the following resources:

IDE, Modeling & Generators: <https://www.genexus.com/developers/rn?data=0;4;V18;14;V18;13;>  
Super Apps: <https://www.genexus.com/developers/rn?data=0;9;V18;14;V18;13;>  
SAP: <https://www.genexus.com/developers/rn?data=0;8;V18;14;V18;13;>  
GeneXus Server: <https://www.genexus.com/developers/rn?data=0;6;V18;14;V18;13;>  
GXflow: <https://www.genexus.com/developers/rn?data=0;3;V18;14;V18;13;>  
GXtest: <https://www.genexus.com/developers/rn?data=0;7;V18;14;V18;13;>


|  |
| --- |
| **Backlinks** |
| [Access Validator property](https://wiki.genexus.com/commwiki/wiki?60421) | [Accessible Role property in Text Blocks](https://wiki.genexus.com/commwiki/wiki?60913) | [Apple Maps API property (GeneXus 18 Upgrade 13)](https://wiki.genexus.com/commwiki/wiki?60792) |
| [AutoScroll property](https://wiki.genexus.com/commwiki/wiki?60865) | [Base CSS property in Design System Object (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60675) |
| [Chat Control](https://wiki.genexus.com/commwiki/wiki?59254) | [Class property in Chat control](https://wiki.genexus.com/commwiki/wiki?60880) | [ClientInformation external object (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60693) | [Compression External Object](https://wiki.genexus.com/commwiki/wiki?60618) |
| [CompressionConfiguration External Object](https://wiki.genexus.com/commwiki/wiki?60619) | [Deploy to SAP Cloud Foundry - SAP BTP (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?61099) | [EnableReusingActiveUserTokens property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?61084) | [Environment Variables for Storage Provider Configuration](https://wiki.genexus.com/commwiki/wiki?60682) |
| [ExcelCellRange data type (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60611) | [Flexible client version property](https://wiki.genexus.com/commwiki/wiki?55856) | [Flexible client version property (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60725) | [GAM - OAuth 2.0 Authentication Type (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60769) |
| [GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60761) | [Table of contents:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 Upgrade 13](https://wiki.genexus.com/commwiki/wiki?59630) | [GeneXus 18 Upgrade 13 Hotfix](https://wiki.genexus.com/commwiki/wiki?60413) |
| [GeneXus 18 Upgrade 15](https://wiki.genexus.com/commwiki/wiki?59632) | [GeneXusCompression Module](https://wiki.genexus.com/commwiki/wiki?60613) | [GeneXusUI module (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60716) |
| [GXCompressor External Object](https://wiki.genexus.com/commwiki/wiki?60620) | [HowTo: Use the Chat Control associated with a Procedure that calls a Globant Enterprise AI API (GeneXus 18 latest upgrade or prior)](https://wiki.genexus.com/commwiki/wiki?61106) | [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60954) | [Instance Name property (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?61040) |
| [MarkdownStyle property](https://wiki.genexus.com/commwiki/wiki?60850) | [Messages property in Chat control](https://wiki.genexus.com/commwiki/wiki?60876) | [MSBuild Tasks (GeneXus 18 latest upgrade or prior)](https://wiki.genexus.com/commwiki/wiki?60737) | [NewUserMessageAlignment property](https://wiki.genexus.com/commwiki/wiki?60866) |
| [NewUserMessageScrollBehavior property](https://wiki.genexus.com/commwiki/wiki?60868) | [PublicKey](https://wiki.genexus.com/commwiki/wiki?54578) | [RestServiceName variable](https://wiki.genexus.com/commwiki/wiki?60844) | [SendMessageHandlerObject property](https://wiki.genexus.com/commwiki/wiki?60797) |
| [Servers available for Cloud prototyping (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60513) | [ShowAdditionalContent property](https://wiki.genexus.com/commwiki/wiki?60840) | [ShowEmptyChatContent property](https://wiki.genexus.com/commwiki/wiki?60842) | [Standard Variables for API Objects (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60839) |
| [Standard Variables List (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60835) | [Translations property](https://wiki.genexus.com/commwiki/wiki?60878) | [Unanimo module components](https://wiki.genexus.com/commwiki/wiki?52175) | [Unanimo module components (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60832) |
| [ValueHyperlink property](https://wiki.genexus.com/commwiki/wiki?60612) |

---
