---
title: "GeneXus 18 Upgrade 8"
source_id: 54242
source_url: https://wiki.genexus.com/commwiki/wiki?54242
genexus_version: "18"
---

# GeneXus 18 Upgrade 8

This article is an overview of GeneXus 18 Upgrade 8 features (compared to [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241)) and what needs to be considered to adopt it.

It was released on February 20, 2024.

## [Download Preview](#Download+Preview)

<https://www.genexus.com/en/developers/downloadcenter?data=6254>

## [Overview](#Overview)

This is an important technology and security update. It improves the sharing of secure APIs through modules and also features UI improvements in Angular apps and observability metrics in the backend.

### [Knowledge Sharing](#Knowledge+Sharing)

* Now you can share [your API Objects](https://wiki.genexus.com/commwiki/wiki?46151) using the [module distribution mechanism](https://wiki.genexus.com/commwiki/wiki?31376) and call its services from the target KB. [More information ...](https://wiki.genexus.com/commwiki/wiki?55076,,)

### [Backend](#Backend)

* (Java) Springboot updated to version 3.2. This improves performance and observability
* (.NET) [Azure Event Grid triggered functions](https://wiki.genexus.com/commwiki/wiki?56742) support added
* (.NET) Observability
  + [ASP.NET Core 8 built-in metrics](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/built-in-metrics-aspnetcore?view=aspnetcore-8.0) support added
  + [Configure metrics, traces and logs via Environment Variables](https://wiki.genexus.com/commwiki/wiki?57151).

### [BPM](#BPM)

* New methods and properties in several APIs: [WorkflowBackend Data Type](https://wiki.genexus.com/commwiki/wiki?56537,,), [WorkflowMenu Data Type](https://wiki.genexus.com/commwiki/wiki?56534,,), [WorkflowComponent Data Type](https://wiki.genexus.com/commwiki/wiki?56535,,), [WorkflowAction Data Type](https://wiki.genexus.com/commwiki/wiki?56536,,), [WorkflowUser Data Type](https://wiki.genexus.com/commwiki/wiki?17273), [Workflow Setting Data Type](https://wiki.genexus.com/commwiki/wiki?15084). [WorkflowSettingValue Data Type](https://wiki.genexus.com/commwiki/wiki?56532,,). More information at SACs [53775](https://www.genexus.com/en/developers/websac?data=53775;;), [53765](https://www.genexus.com/en/developers/websac?data=53765;;), [53762](https://www.genexus.com/en/developers/websac?data=53762;;).

### [Testing](#Testing)

* [Object Mock Testing](https://wiki.genexus.com/commwiki/wiki?55859). New property to enable object mock: [Generate Mockable Objects property](https://wiki.genexus.com/commwiki/wiki?56903)
* Organizing your Test objects in the KB: [Test Preferences](https://wiki.genexus.com/commwiki/wiki?45420)

### [Super Apps and Mini Apps](#Super+Apps+and+Mini+Apps)

* 'Sandbox mode' support added for loading and testing apps that are not ready for production yet. More information at [SAC 53920](https://www.genexus.com/developers/websac?en,,,53920) and [GeneXusSuperApps Module](https://wiki.genexus.com/commwiki/wiki?50959,,).
* [More information ...](https://wiki.genexus.com/commwiki/wiki?53536)
* In addition to the possibility of creating [Native mobile Mini Apps](https://wiki.genexus.com/commwiki/wiki?50900,,), it is possible to create [Web Mini Apps](https://wiki.genexus.com/commwiki/wiki?57422).

### [Compatibility](#Compatibility)

* .NET Framework:
  + Due to security reasons, the Medium trust policy is not supported anymore. [SAC 53894](https://www.genexus.com/developers/websac?es,,,53894)
  + The .NET Framework generator has been declared Legacy. Read more at [.NET 8 and the future of .NET in GeneXus](https://www.genexus.com/en/news/read-news/-net-8-and-the-future-of-net-in-genexus).  
    We suggest moving from [GeneXus .NET Framework Generator](https://wiki.genexus.com/commwiki/wiki?2892) to [GeneXus .NET Generator](https://wiki.genexus.com/commwiki/wiki?38604).

## All Details (Features, More Compatibility Aspects, Issues)

Please check these links for additional features, compatibility aspects, issues, and details:

GeneXus: <https://www.genexus.com/developers/rn?data=0;4;V18;8;V18;7;>  
GeneXus Server: <https://www.genexus.com/developers/rn?data=0;6;V18;8;V18;7;>  
GXflow: <https://www.genexus.com/developers/rn?data=0;3;V18;8;V18;7;>  
GXtest: <https://www.genexus.com/developers/rn?data=0;7;V18;8;V18;7;>


|  |
| --- |
| **Backlinks** |
| [Analytics external object (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57371) | [Azure Event Grid triggered functions](https://wiki.genexus.com/commwiki/wiki?56742) |
| [Building Azure Serverless from sources (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?56809) | [Distribution of Apple's Flexible Client through Swift Packages](https://wiki.genexus.com/commwiki/wiki?55960) | [Enable Copy To Clipboard property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57272) | [Enable Zoom property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57238) |
| [Extension Library concept for Extending GeneXus for Native Mobile](https://wiki.genexus.com/commwiki/wiki?33545) | [Extract Zip property](https://wiki.genexus.com/commwiki/wiki?56753) | [Flexible client update policy property](https://wiki.genexus.com/commwiki/wiki?55890) | [Generate Mockable Objects property](https://wiki.genexus.com/commwiki/wiki?56903) |
| [Toc:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241) | [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243) |
| [GeneXus Cryptography Module](https://wiki.genexus.com/commwiki/wiki?43917) | [GeneXus JWT Module](https://wiki.genexus.com/commwiki/wiki?43980) | [GeneXus Super App News and Roadmap](https://wiki.genexus.com/commwiki/wiki?53536) |
| [GeneXus XmlSignature Module](https://wiki.genexus.com/commwiki/wiki?43921) | [HowTo: Set up the environment to test Observability (using Grafana)](https://wiki.genexus.com/commwiki/wiki?56829) | [HowTo: Setup the environment to test Observability (using AWS CloudWatch)](https://wiki.genexus.com/commwiki/wiki?57258) | [HowTo: Watch .NET logs using OpenTelemetry (with SigNoz)](https://wiki.genexus.com/commwiki/wiki?57281) |
| [HowTo: Watching .NET logs at AWS CloudWatch](https://wiki.genexus.com/commwiki/wiki?57287) | [Log output property (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?57249) | [Log settings with environment variables (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?57632) | [Max Zoom property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57273) |
| [Max Zoom Relative To property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57252) | [Merge Dynamic Libraries property (GeneXus 18 Upgrade 8)](https://wiki.genexus.com/commwiki/wiki?57469) | [Object Mock Testing](https://wiki.genexus.com/commwiki/wiki?55859) | [Observability in GeneXus Apps and Environment variables](https://wiki.genexus.com/commwiki/wiki?57151) |
| [SecurityAPICommons Module](https://wiki.genexus.com/commwiki/wiki?47252) | [Test Execution Results Report (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?56988) | [Trigger type property](https://wiki.genexus.com/commwiki/wiki?51466) |
| [WorkflowUser Data Type](https://wiki.genexus.com/commwiki/wiki?17273) | [Zoom Outside Control property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57270) |

---
