---
title: "GeneXus Cognitive API - ExtractEntities procedure"
source_id: 40182
source_url: https://wiki.genexus.com/commwiki/wiki?40182
genexus_version: "18"
---

# GeneXus Cognitive API - ExtractEntities procedure

Extracts entities from a written text.

## [Parameters](#Parameters)

* **in**:&text:: [Text, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40192)  
  A plain text to extract its named entities.
* **in**:&language :: [Language, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40453)  
  The language of the input text for improving the output accuracy.
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&Labels:: [Label, GeneXusAI (collection)](https://wiki.genexus.com/commwiki/wiki?40191)  
  A set of labels indicating the named entities identified.

x

## [Configuration](#Configuration)

The following table resumes the configuration properties (access credentials) you must set in order to use this AI task.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** | | |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | **Id** | **Key** | **SecretKey** |
| **Alibaba** | - | 用户 AccessKey | 用户 AccessKey |
| **Amazon** | - | Comprehend | Comprehend |
| **Baidu** | 自然语言 | 自然语言 | 自然语言 |
| **Google** | - | Cloud Natural Language API | - |
| **IBM** | - | Natural Language Understanding | - |
| **Microsoft** | - | Text Analytics | - |
| **SAP** | - | - | - |
| **Tencent** | 专有名词 | 专有名词 | - |

## [Sample](#Sample)

Taking the following text as input, the table below shows the identified entities for each provider (as a JSON structure) and the time it takes for processing it.

"*The first question that comes up is: What is GeneXus? GeneXus is a tool that automatically generates software programs such as applications for the Web, and Smart Devices, always at the forefront of technological evolution.*"

  

|  |  |  |
| --- | --- | --- |
| **Provider** | **Output** | **Benchmark** |
| **Alibaba** | ``` ["first","web"] ``` | 789ms |
| **Amazon** | ``` ["first question","genexus"] ``` | 887ms |
| **Baidu** | ``` ["genexus","web应用程序"] ``` | 786ms |
| **Google** | ``` ["GeneXus","Smart Devices"] ``` | 1345ms |
| **IBM** | ``` ["Smart Devices"] ``` | 1919ms |
| **Microsoft** | ``` ["GeneXus"] ``` | 2912ms |
| **SAP** | N/A | N/A |
| **Tencent** | ``` ["applications","technological evolution"] ``` | 2445ms |

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |
| **Connectivity:** | Online |

## [Availability](#Availability)

This procedure is available as of [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,).

* As of [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/wiki?40782,,):  
  - Google Cloud AI is available.
* As of [GeneXus 16 upgrade 2](https://wiki.genexus.com/commwiki/wiki?41525,,):  
  - Amazon WS and Tencent AI are available.
* As of [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,):  
  - Baidu AI is available.
* As of [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,):  
  - Alibaba AI is available.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) |
| [Label domain](https://wiki.genexus.com/commwiki/wiki?40191) | [Language domain](https://wiki.genexus.com/commwiki/wiki?40453) | [Text domain](https://wiki.genexus.com/commwiki/wiki?40192) |

---
