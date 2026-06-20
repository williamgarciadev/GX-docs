---
title: "GeneXus Cognitive API - Translate procedure"
source_id: 40185
source_url: https://wiki.genexus.com/commwiki/wiki?40185
genexus_version: "18"
---

# GeneXus Cognitive API - Translate procedure

Translates a written text from a source language to a target language.

## [Parameters](#Parameters)

* **in**:&text:: [Text, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40192)  
  Plain text to be translated.
* **in**:&sourceLanguage :: [Language, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40453)  
  The source language for the input text with an [ISO 639-1](https://www.w3schools.com/tags/ref_language_codes.asp) two-letters code.
* **in**:&targetLanguage :: [Language, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40453)  
  The target language to translate the input text with an [ISO 639-1](https://www.w3schools.com/tags/ref_language_codes.asp) two-letters code.
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&TranslatedText:: [Text, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40192)  
  The translated text.

x

## [Configuration](#Configuration)

The following table resumes the configuration properties (access credentials) you must set in order to use this AI task.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** | | |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | **Id** | **Key** | **SecretKey** |
| **Alibaba** | - | 用户AccessKey | 用户AccessKey |
| **Amazon** | - | Translate | Translate |
| **Baidu** | 通用翻译 | 通用翻译 | 通用翻译 |
| **Google** | - | Cloud Translation API | - |
| **IBM** | - | Language Translator | - |
| **Microsoft** | - | Translator Text | - |
| **MLKit** | ML Kit API | ML Kit API | - |
| **SAP** | - | Sandbox Environment  (Deprecated) | - |
| **Tencent** | 文本翻译 | 文本翻译 | - |

## [Sample](#Sample)

Taking the following text (in Spanish) as input, the table below shows the translations (to English) made for each provider and the time it takes for processing it.

"*La primera pregunta que surge es: ¿Qué es GeneXus? GeneXus es una herramienta que genera programas de software automáticamente, tales como aplicaciones para la Web y Smart Devices, siempre a la vanguardia de la evolución tecnológica.*"

|  |  |  |
| --- | --- | --- |
| **Provider** | **Output** | **Benchmark** |
| **Alibaba** | "*The first question that arises is: what is genexus? Genexus is a tool that automatically generates software programs such as web applications and smart devices, always at the forefront of technological evolution.*" | 1621ms |
| **Amazon** | "*The first question that arises is: What is GeneXus? GeneXus is a tool that generates software programs automatically, such as Web applications and Smart Devices, always at the forefront of technological evolution*" | 1347ms |
| **Baidu** | "*The first question that arises is: What is GeneXus? GeneXus is a tool that automatically generates software programs such as web applications and Smart Devices, always at the forefront of Technological Development.*" | 1924ms |
| **Google** | "*The first question that arises is: What is GeneXus? GeneXus is a tool that generates software programs automatically, such as applications for the Web and Smart Devices, always at the forefront of technological evolution*" | 1895ms |
| **IBM** | "*The first question that emerges is: What is GeneXus? GeneXus is a tool that generates software programs automatically, such as Web applications and Smart Devices, always at the forefront of technological evolution.*" | 1967ms |
| **Microsoft** | "*The first question that arises is: what is GeneXus? GeneXus is a tool that generates software programs automatically, such as applications for the WEB and Smart devices, always at the forefront of technological evolution*" | 2912ms |
| **MLKit** | "*The first question that arises is: What is Genexus? Genexus is a tool that automatically generates software programs as applications for the Web and smart devices, always at the forefront of technological evolution.*" | 1832ms |
| **SAP** | "*The first question that arises is: What is GeneXus? GeneXus is a tool that generates software programs automatically, such as applications for the Web and Smart Devices, always at the forefront of technological developments.*" | 6313ms |
| **Tencent** | "*The first question that arises is: What is GeneXus? GeneXus is a tool that generates software, such as Web applications and Smart* *Devics**, always at the forefront of technological evolution.*" | 3353ms |

## [Notes](#Notes)

* Official documentation about languages translation pairs support:

  |  |  |
  | --- | --- |
  | **Provider** | **Languages** |
  | **Alibaba** | [121 pairs](https://help.aliyun.com/document_detail/98695.html?spm=a2c4g.11186623.6.543.51c62f32XkNnxe) |
  | **Amazon** | [417 pairs](https://docs.aws.amazon.com/en_en/translate/latest/dg/pairs.html) |
  | **Baidu** | [756 pairs](https://api.fanyi.baidu.com/api/trans/product/apidoc#languageList) (28 for source, 27 for target) |
  | **Google** | [195 pairs](https://cloud.google.com/translate/docs/languages#languages-nmt) |
  | **IBM** | [33 pairs](https://console.bluemix.net/docs/services/language-translator/translation-models.html#translation-models) |
  | **Microsoft** | [40 pairs](https://docs.microsoft.com/es-es/azure/cognitive-services/Translator/language-support) |
  | **ML Kit** | [59 pairs](https://developers.google.com/ml-kit/language/translation/translation-language-support) |
  | **SAP** | [92 pairs](https://help.sap.com/viewer/f09b2311283b4f32a44e106729e11412/1.0/en-US/c730c916e6e947df9a634b33b66e5ee0.html#Supported%20Languages) |
  | **Tencent** | [16 pairs](https://ai.qq.com/doc/nlptrans.shtml#5-翻译类型定义) |

  Please note that language translation is limited by the values of [Language domain](https://wiki.genexus.com/commwiki/wiki?40453) and language variants are not available.
* Automatically source language recognition (i.e. &sourceLanguage input with Language.None value) is supported by:  
  Amazon, Baidu, Google, Microsoft, Tencent.
* Firebase ML Kit downloads the selected translation model the first time it is used. Then, it will used it locally.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |
| **Connectivity:** | Online |

## [Availability](#Availability)

This procedure is available as of [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,).

* As of [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/wiki?40782,,):  
  - Google Cloud AI is available.
* As of [GeneXus 16 upgrade 2](https://wiki.genexus.com/commwiki/wiki?41525,,):  
  - Amazon WS and Tencent AI are available.
* As of [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,):  
  - Baidu AI is available.
* As of [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,):  
  - Alibaba AI is available.
* As of [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,):  
  - SAP Leonardo has been deprecated.
* As of [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,):  
  - Firebase ML Kit is available for Android.

## [See also](#See+also)

* [GeneXus Cognitive API - DetectLanguage procedure](https://wiki.genexus.com/commwiki/wiki?40181)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) |
| [Language domain](https://wiki.genexus.com/commwiki/wiki?40453) | [Sample: GeneXus Cognitive API proof of concept](https://wiki.genexus.com/commwiki/wiki?40853) | [Text domain](https://wiki.genexus.com/commwiki/wiki?40192) |

---
