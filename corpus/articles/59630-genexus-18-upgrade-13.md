---
title: "GeneXus 18 Upgrade 13"
source_id: 59630
source_url: https://wiki.genexus.com/commwiki/wiki?59630
genexus_version: "18"
---

# GeneXus 18 Upgrade 13

This is an overview of GeneXus 18 Upgrade 13 features (compared to [GeneXus 18 Upgrade 12](https://wiki.genexus.com/commwiki/wiki?59446)) and what needs to be considered to adopt it.

It was released on 13th June 2025.

## [Download](#Download)

<https://www.genexus.com/en/developers/downloadcenter?data=6312;;>

## [Overview](#Overview)

This upgrade delivers significant stability and security enhancements, along with key feature updates across [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Native Mobile](https://wiki.genexus.com/commwiki/wiki?14451), and [Angular](https://wiki.genexus.com/commwiki/wiki?42550) Generators. The improvements are designed to increase performance, developer productivity, and compatibility with modern development standards.

### [Backend](#Backend)

* **Azure Functions**  
  Now supports **Deploy Sources**, enabling more flexible and manageable deployment scenarios. Read more at [SAC #60799](https://www.genexus.com/developers/websac?es,,,60799).

#### [.NET-Specific Improvements](#.NET-Specific+Improvements)

* **Security Enhancements**  
  Support for **Authentication and Authorization** has been added to **gRPC services** in GeneXus, enabling secure and robust service communication.
* **REST Services Modernization**  
  REST services are now implemented using **attribute routing**, aligning with Microsoft’s recommendations and common practices in the C# ecosystem. Read more at [Service and web page handling in .NET Applications](https://wiki.genexus.com/commwiki/wiki?51326).
* **Deployment Performance**  
  Deployment times have been notably reduced, resulting in a more efficient development cycle.

#### [Java-Specific Improvements](#Java-Specific+Improvements)

* **Security and Cleanup**  
  Unused generated application sources are now automatically deleted, minimizing clutter and reducing potential security risks.
* **Reorganization Management**  
  Reorganization sources are now generated in a **separate folder**, allowing the reorganization process to be run independently—even if the application fails to compile.
* **Cache Database Selection**  
  It is now possible to specify the database in the [Cache Location property](https://wiki.genexus.com/commwiki/wiki?31331) when configuring [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147) to 'Redis' in the Java Generator. For example, to connect to database 4, use Cache Location = redis://localhost:6379/4.

### [Native Mobile](#Native+Mobile)

* **Enhanced Scanner Capabilities**  
  The **Scanner external object** now supports scanning barcodes and QR codes from user-selected images.
* **Screen Management**  
  A new **"Keep Device Screen On"** property prevents the device from sleeping, even when the application is inactive.
* **Android Client Versioning**  
  New properties allow setting a specific **Flexible Client version**, enabling projects to reference newer clients without requiring a GeneXus upgrade:
* FlexibleClientUpdatePolicy - [Flexible client update policy property](https://wiki.genexus.com/commwiki/wiki?55890)
* FlexibleClientVersion - [Flexible client version property](https://wiki.genexus.com/commwiki/wiki?55856)

### [GXflow](#GXflow)

* **Multiple browser tabs support**  
  Users can now work and navigate in separate tabs, since context is handled separately.

### [Reporting & Analytics](#Reporting+%26+Analytics)

* **GXquery Integration**  
  The **GXquery extension** is now included in the IDE. It enables easy metadata export for integration with platforms such as **Globant Enterprise AI**, allowing users to perform [chat-based data exploration](https://wiki.genexus.com/enterprise-ai/wiki?170,How+to+create+a+Chat+with+Data+Assistant).

### [Compatibility](#Compatibility)

* **REST Services Compatibility in .NET**  
  Improvements to REST Services generation in .NET include compatibility aspects to consider.  [SAC 60795](https://www.genexus.com/developers/websac?,,,60795)

## [All Details (Features, More Compatibility Aspects, Issues)](#All+Details+%28Features%2C+More+Compatibility+Aspects%2C+Issues%29)

Please check these links for additional features, compatibility aspects, issues, and details:

IDE, Modeling & Generators: <https://www.genexus.com/developers/rn?data=0;4;V18;13;V18;12;>  
Super Apps: <https://www.genexus.com/developers/rn?data=0;9;V18;13;V18;12;>  
SAP: <https://www.genexus.com/developers/rn?data=0;8;V18;13;V18;12;>  
GeneXus Server: <https://www.genexus.com/developers/rn?data=0;6;V18;13;V18;12;>  
GXflow: <https://www.genexus.com/developers/rn?data=0;3;V18;13;V18;12;>  
GXtest: <https://www.genexus.com/developers/rn?data=0;7;V18;13;V18;12;>


|  |
| --- |
| **Backlinks** |
| [Accessible Name property (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60147) | [Android Requirements (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60679) | [API object - Delete service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60083) |
| [API object - GetByKey service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60074) | [API object - Insert service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60081) | [API object - ListCustomers service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60073) | [API object - Update service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60082) |
| [Apple Maps API property (GeneXus 18 Upgrade 12)](https://wiki.genexus.com/commwiki/wiki?60791) | [Building Azure functions from sources](https://wiki.genexus.com/commwiki/wiki?59963) | [Building Azure Serverless from sources (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?59962) |
| [Create tests for Rest objects (GeneXus 18 Upgrade 12 and prior)](https://wiki.genexus.com/commwiki/wiki?59801) | [Flexible client update policy property (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60310) | [Table of contents:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 Upgrade 12](https://wiki.genexus.com/commwiki/wiki?59446) |
| [GeneXus 18 Upgrade 13 Hotfix](https://wiki.genexus.com/commwiki/wiki?60413) |
| [GeneXus Server Azure Variable Definition (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60207) | [GeneXus Super App News and Roadmap](https://wiki.genexus.com/commwiki/wiki?53536) |
| [GXflow Software Requirements (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60055) | [Handling parameters via headers in API Objects methods](https://wiki.genexus.com/commwiki/wiki?60084) | [HowTo: Set Up a Secure gRPC API Object using GAM and Remote Modules](https://wiki.genexus.com/commwiki/wiki?60125) |
| [Kafka Producer and Consumer External Objects](https://wiki.genexus.com/commwiki/wiki?40593) | [Kafka Producer and Consumer External Objects (GeneXus 18 Upgrade 12)](https://wiki.genexus.com/commwiki/wiki?59996) |
| [Keep Device Screen On property](https://wiki.genexus.com/commwiki/wiki?60061) | [Link function (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60052) | [KB:Pesobook](https://wiki.genexus.com/commwiki/wiki?17538) | [Scanner external object (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60124) |
| [Service and web page handling in .NET Applications (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60110) |

---
