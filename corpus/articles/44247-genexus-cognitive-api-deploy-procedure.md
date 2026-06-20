---
title: "GeneXus Cognitive API - Deploy procedure"
source_id: 44247
source_url: https://wiki.genexus.com/commwiki/wiki?44247
genexus_version: "18"
---

# GeneXus Cognitive API - Deploy procedure

Deploys a custom model, making it available to be used for prediction.

## [Parameters](#Parameters)

* **in**:&model :: [Model, GeneXusAI.Custom](https://wiki.genexus.com/commwiki/wiki?44240)  
  The model information to be deployed.
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&Success :: Boolean  
  Indicates the success of the operation.

## [Configuration](#Configuration)

The following table resumes the configuration properties (access credentials) you must set in order to use this AI task.

|  |  |  |
| --- | --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** | |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | **Key** | **Deploy** |
| **Alibaba** | - | - |
| **Amazon** | - | - |
| **Baidu** | - | - |
| **Google** | Service Account JSON | - |
| **IBM** | - | - |
| **Microsoft** | Custom Vision Training Key | Custom Vision Training Resource Id |
| **SAP** | - | - |
| **Tencent** | - | - |

## [Notes](#Notes)

* Calling this task makes sense after you call the [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) and the [GeneXus Cognitive API - Check procedure](https://wiki.genexus.com/commwiki/wiki?44242) returns a [State.Ready](https://wiki.genexus.com/commwiki/wiki?44235) state.
* Once you call this task successfully, you will be able to call [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245) or the appropriate task by adding  ModelId and  ModelVersion properties to &provider configuration.
* Some providers implicitly deploy your model after training (e.g. IBM). In other words, you do not need to call this task for deploying your model. If you call this task in this scenario, the operation returns True and a [GXAI1001](https://wiki.genexus.com/commwiki/wiki?40188) informative message.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |
| **Connectivity:** | Online |

## [Availability](#Availability)

This procedure is available as of [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).

* As of [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,)  
  -  Google Auto ML is available.

## [See also](#See+also)

* [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246)
* [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245)
* [HowTo: Build a custom model for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?43665)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Delete procedure](https://wiki.genexus.com/commwiki/wiki?44243) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) |
| [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) | [Measure data type](https://wiki.genexus.com/commwiki/wiki?44239) | [Model data type](https://wiki.genexus.com/commwiki/wiki?44240) |

---
