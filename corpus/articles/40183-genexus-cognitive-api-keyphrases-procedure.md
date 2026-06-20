---
title: "GeneXus Cognitive API - KeyPhrases procedure"
source_id: 40183
source_url: https://wiki.genexus.com/commwiki/wiki?40183
genexus_version: "18"
---

# GeneXus Cognitive API - KeyPhrases procedure

Gets the key phrases (including keywords) from a written text.

## [Parameters](#Parameters)

* **in**:&text:: [Text, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40192)  
  A plain text to get its key phrases.
* **in**:&language :: [Language, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40453)  
  The language of the input text for improving the output accuracy.
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&Labels:: [Label, GeneXusAI (collection)](https://wiki.genexus.com/commwiki/wiki?40191)  
  A set of labels indicating the key phrases detected.

x

## [Configuration](#Configuration)

The following table resumes the configuration properties (access credentials) you must set in order to use this AI task.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** | | |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | **Id** | **Key** | **SecretKey** |
| **Alibaba** | - | 用户AccessKey | 用户AccessKey |
| **Amazon** | - | Comprehend | Comprehend |
| **Baidu** | 自然语言 | 自然语言 | 自然语言 |
| **Google** | - | Cloud Natural Language API | - |
| **IBM** | - | Natural Language Understanding | - |
| **Microsoft** | - | Text Analytics | - |
| **SAP** | - | Sandbox Environment  (Deprecated) | - |
| **Tencent** | - | - | - |

## [Sample](#Sample)

Taking the following text as input, the table below shows the identified entities for each provider (as a JSON structure) and the time it takes for processing it.

"*The first question that comes up is: What is GeneXus? GeneXus is a tool that automatically generates software programs such as applications for the Web, and Smart Devices, always at the forefront of technological evolution.*"

  

|  |  |  |
| --- | --- | --- |
| **Provider** | **Output** | **Benchmark** |
| **Alibaba** | ``` [ 	"always",  	"applications",  	"automatically",  	"devices",  	"evolution",  	"forefront",  	"generates",  	"genexus",  	"question",  	"software",  	"such",  	"technological" ] ``` | 808ms |
| **Amazon** | ``` [     "a tool",      "applications",      "genexus",      "smart devices",      "software programs",      "technological evolution",      "the first question",      "the forefront",      "the web" ] ``` | 1004ms |
| **Baidu** | ``` [] ``` | 1712ms |
| **Google** | ``` [     "GeneXus",      "question",      "software programs",      "applications",      "forefront",      "evolution",      "Web",      "Smart Devices" ] ``` | 984ms |
| **IBM** | ``` [     "technological evolution",     "Smart Devices",     "software programs",     "forefront",     "question",     "GeneXus",     "tool",     "applications",     "Web" ] ``` | 1284ms |
| **Microsoft** | ``` [     "GeneXus",      "applications",      "Web",      "software programs",      "Smart Devices",      "tool",      "forefront of technological evolution",      "question" ] ``` | 1354ms |
| **SAP** | ``` [     "genexus",     "web",     "tool",     "technological",     "software",     "smart",     "question",     "program",     "generate",     "forefront",     "evolution",     "device",     "come",     "automatically",     "application" ] ``` | 2466ms |
| **Tencent** | N/A | N/A |

## [Notes](#Notes)

* The term 'key-phrase' also includes 'key-words'.
* The labels are sorted from higher to lower confidence.
* **Baidu AI** provider only returns a result when you input Chinese-text.  
  e.g.

  |  |  |
  | --- | --- |
  | Input | : "*提出的第一个问题是：什么是GeneXus？ GeneXus是一个自动生成软件程序的工具，例如Web应用程序和智能设备，始终处于技术发展的最前沿。*" |
  | Output | : ["软件"] |

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
* As of [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,):  
  - SAP Leonardo has been deprecated


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) |
| [Label domain](https://wiki.genexus.com/commwiki/wiki?40191) | [Language domain](https://wiki.genexus.com/commwiki/wiki?40453) | [Text domain](https://wiki.genexus.com/commwiki/wiki?40192) |

---
