---
title: "GeneXus Cognitive API - DetectLanguage procedure"
source_id: 40181
source_url: https://wiki.genexus.com/commwiki/wiki?40181
genexus_version: "18"
---

# GeneXus Cognitive API - DetectLanguage procedure

Determines the language of a written text.

## [Parameters](#Parameters)

* **in**:&text :: [Text, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40192)  
  Plain text to detect its language.
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&OutputLabel :: [OutputLabel, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40193)  
  A label indicating the detected language (in two-letters code) with its confidence

x

## [Configuration](#Configuration)

The following table resumes the configuration properties (access credentials) you must set in order to use this AI task.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** | | |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | **Id** | **Key** | **SecretKey** |
| **Alibaba** | - | - | - |
| **Amazon** | - | Comprehend | Comprehend |
| **Baidu** | 通用翻译 | 通用翻译 | 通用翻译 |
| **Google** | - | Cloud Translation API | - |
| **IBM** | - | Language Translator | - |
| **Microsoft** | - | Translator Text | - |
| **MLKit** | ML Kit API | ML Kit API | - |
| **SAP** | - | Sandbox Environment  (Deprecated) | - |
| **Tencent** | 语种识别 | 语种识别 | - |

## [Sample](#Sample)

Taking the following text as input, the table below shows the identified language for each provider (as a JSON structure) and the time it takes for processing it.

"*The first question that comes up is: What is GeneXus? GeneXus is a tool that automatically generates software programs such as applications for the Web, and Smart Devices, always at the forefront of technological evolution.*"

  

tr style="border-bottom: 1.0px solid silver;">

|  |  |  |
| --- | --- | --- |
| **Provider** | **Output** | **Benchmark** |
| **Alibaba** | N/A | N/A |
| **Amazon** | ``` {     "label": "en",     "confidence": 0.994 } ``` | 1016ms |
| **Baidu** | ``` {     "label": "en",     "confidence": 1.000 } ``` | 2460ms |
| **Google** | ``` {     "label": "en",     "confidence": 1.000 } ``` | 817ms |
| **IBM** | ``` {     "label": "en",     "confidence": 0.999 } ``` | 3595ms |
| **Microsoft** | ``` {     "label": "en",     "confidence": 1.000 } ``` | 2912ms |
| **MLKit** | ``` {     "label": "en",     "confidence": 1.000 } ``` | 135ms |
| **SAP** | ``` {     "label": "en",     "confidence": 1.000 } ``` | 2355ms |
| **Tencent** | ``` {     "label": "en",     "confidence": 1.000 } ``` | 3148ms |

And, by taking a language ambiguous source text as follows.

"*The first question that comes up is: ¿Qué es GeneXus? GeneXus is a tool that automatically generates software programs como aplicaciones Web, y Smart Devices, always at the forefront of la evolución tecnlológica.*"

|  |  |  |
| --- | --- | --- |
| **Provider** | **Output** | **Benchmark** |
| **Alibaba** | N/A | N/A |
| **Amazon** | ``` {     "label": "en",     "confidence": 0.807 } ``` | 1049ms |
| **Baidu** | ``` {     "label": "spa",     "confidence": 1 } ``` | 2747ms |
| **Google** | ``` {     "label": "en",     "confidence": 0.855 } ``` | 703ms |
| **IBM** | ``` {     "label": "es",     "confidence": 0.797 } ``` | 3595ms |
| **Microsoft** | ``` {     "label": "en",     "confidence": 1.000 } ``` | 2912ms |
| **MLKit** | ``` {     "label": "en",     "confidence": 1.000 } ``` | 210ms |
| **SAP** | ``` {     "label": "en",     "confidence": 0.999 } ``` | 2989ms |
| **Tencent** | ``` {     "label": "en",     "confidence": 1.000 } ``` | 2293ms |

## [Notes](#Notes)

* The label assigned will be a two-letter code according to the [ISO 639-1](https://www.w3schools.com/tags/ref_language_codes.asp).

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
* As of [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,):  
  - SAP Leonardo has been deprecated
* As of [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,):  
  + Firebase ML Kit is available for Android.


|  |
| --- |
| **Backlinks** |
| [Confidence domain](https://wiki.genexus.com/commwiki/wiki?40189) | [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Translate procedure](https://wiki.genexus.com/commwiki/wiki?40185) |
| [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) | [Label domain](https://wiki.genexus.com/commwiki/wiki?40191) | [OutputLabel data type](https://wiki.genexus.com/commwiki/wiki?40193) |
| [Sample: GeneXus Cognitive API proof of concept](https://wiki.genexus.com/commwiki/wiki?40853) | [Text domain](https://wiki.genexus.com/commwiki/wiki?40192) |

---
