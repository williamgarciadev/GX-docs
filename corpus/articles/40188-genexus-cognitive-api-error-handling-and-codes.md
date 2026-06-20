---
title: "GeneXus Cognitive API - Error handling and codes"
source_id: 40188
source_url: https://wiki.genexus.com/commwiki/wiki?40188
genexus_version: "18"
---

# GeneXus Cognitive API - Error handling and codes

Every GeneXus AI task has a parameter based on [Messages structured data type](https://wiki.genexus.com/commwiki/wiki?40335), which includes information about the status of the operation. This parameter is always the second last on the list, allowing you to write an AI task as follows.

```
&result = GeneXusAI.<Category>.<AI_Task>(&parm1, ..., &parmN, &messages)
```

|  |  |
| --- | --- |
| where |  |
| &parm1,...,&parmN | : Set of parameters whose types depends on the AI task. |
| &messages | : [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335) |
| &result | : Returned value whose type depends on the  AI task. |

## [Codes](#Codes)

The table below lists the possible error codes raised by GeneXusAI, and is stored in the 'Id' field of the Messages.Message data type.

|  |  |
| --- | --- |
| **Code** | **Description** |
| [**GXAI1000**](#GXAI1000+) | *There is no result*  Raised as an informational status when the provider does not give any output result. |
| [**GXAI1001**](#GXAI1001) | *There is no processing*  Raised as an informational status when the provider does not process any output. |
| [**GXAI1002**](#GXAI1002) | *Language is not set*  Raised as an informational status when a language is not set, but by setting it you could achieve higher accuracy. |
| [**GXAI4000**](#GXAI4000) | *Credentials are missing*  Raised when you do not provide your access credentials properly. |
| [**GXAI4001**](#GXAI4001) | *Text is empty*  Raised when the given input required text is empty. |
| [**GXAI4002**](#GXAI4002) | *Language is empty*  Raised when the given input required language is empty. |
| [**GXAI4003**](#GXAI4003) | *Source language is empty*  Raised when the given input required source language, in translation task context, is empty. |
| [**GXAI4004**](#GXAI4004) | *Target language is empty*  Raised when the given input required target language, in translation task context, is empty. |
| [**GXAI4005**](#GXAI4005) | *Language has an incorrect format*  Raised when the given input language is a two-letter code (e.g. 'en') but a language/locale is expected (e.g. 'en-US'). |
| [**GXAI4006**](#GXAI4006) | *File path is empty*  Raised when the given input required file path is empty. |
| [**GXAI4007**](#GXAI4007) | *File path does not exist*  Raised when the given input file path does not exist. |
| [**GXAI4008**](#GXAI4008) | *File format is not supported*  Raised when the given file format is not supported. |
| [**GXAI4009**](#GXAI4009) | *File fetch from URL failed*  Raised when the given file URL cannot be fetched. |
| [**GXAI4010**](#GXAI4010) | *File upload failed*  Raised when the given file could not be uploaded to the application server. |
| [**GXAI4011**](#GXAI4011) | *Model name '%1' is unknown*  Raised when the given model name (%1) is unknown by the provider. |
| [**GXAI4012**](#GXAI4012) | *File source is ambiguous, path and URL are both given*  Raised when you give both URL and path for a file resource. |
| [**GXAI4013**](#GXAI4013) | *File source is unspecified, path or URL must be given*  Raised when you do not give any URL or path for a file resource. |
| [**GXAI4014**](#GXAI4014) | *Collection '%1' is empty*  Raised when the given collection input does not have elements. |
| [**GXAI4015**](#GXAI4015) | *Recognition mode '%1' is unknown*  Raised when the given recognition mode is unknown by the provider. |
| [**GXAI4016**](#GXAI4016) | *SSML has a wrong format*  Raised when the given [SSML](https://en.wikipedia.org/wiki/Speech_Synthesis_Markup_Language), in text-to-speech context, is unknown by the provider. |
| [**GXAI4017**](#GXAI4017) | *Voice is unavailable*  Raised when the given voice, in text-to-speech context, is not available by the provider. |
| [**GXA4018**](#GXA4018) | *File content or location is empty*  Raised when the given file content or location (path/URL) is empty. |
| [**GXA4019**](#GXA4019) | *File is unavailable*  Raised when your input file is not available or reachable. |
| [**GXA4020**](#GXA4020) | *URL has a wrong format*.  Raised when you provide a URL with an unexpected format. |
| [**GXA4021**](#GXA4021) | *Credentials are ambiguous, username/password and key are both given.*  Raised when you provide both Username/Password and Key for authenticating, you must set only one mechanism. |
| [**GXAI4022**](#GXAI4022) | *Text is too large*  Raised when the given text is too large. |
| [**GXAI4023**](#GXAI4023) | *Proxy is enabled but host/port is missing*  Raised when you enable a proxy but connection information is missing. |
| [**GXAI4024**](#GXAI4024) | *Model is unavailable*  Raised when your model is unavailable. |
| [**GXAI4025**](#GXAI4025) | *Model sample is empty*  Raised when your model's dataset generator (procedure or data provider object) raise an empty collection. |
| [**GXAI4100**](#GXAI4100) | *Parameter '%1' is malformed*  Raised when a required parameter is malformed. |
| [**GXAI4101**](#GXAI4101) | *Parameter '%1' is missing*  Raised when a required parameter is missing. |
| [**GXAI5000**](#GXAI5000) | *External provider raises an error '%1'*  Raised when the provider has not finished successfully. |
| [**GXAI5001**](#GXAI5001) | *Authentication failed due to an invalid token*  Raised when the authentication has failed due to an invalid access token. |
| [**GXAI5002**](#GXAI5002) | *Authentication failed during communication. Reason %1*  Raised when the authentication has failed due to an unknown issue. |
| [**GXAI5003**](#GXAI5003) | *Operation failed*  Raised when the current operation has failed. |
| [**GXAI5100**](#GXAI5100) | *Deprecated*  Raised when a provider has deprecated the service used by some task. |
| [**GXAI6000**](#GXAI6000) | *Provider name is empty*  Raised when you set a provider at runtime, but the [Provider.Name field](https://wiki.genexus.com/commwiki/wiki?40197) has not been set. |
| [**GXAI6001**](#GXAI6001) | *Task '%1' is unavailable for '%2' provider*  Raised when you try to execute an AI task which is not available for the given provider. |
| [**GXAI6002**](#GXAI6002) | *Unhandled exception*  Raised when the module catch an unhandled exception. |
| [**GXAI6003**](#GXAI6003) | *An error has occurred*  Raised when the AI task return an error, giving a code/detail of its cause. |

## [Scope](#Scope)

|  |  |
| --- | --- |
| **AI Tasks:** | All |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

## [Availability](#Availability)

This document applies as of [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Analyze procedure](https://wiki.genexus.com/commwiki/wiki?41041) | [GeneXus Cognitive API - Check procedure](https://wiki.genexus.com/commwiki/wiki?44242) |
| [GeneXus Cognitive API - Classify procedure](https://wiki.genexus.com/commwiki/wiki?40171) | [GeneXus Cognitive API - Delete procedure](https://wiki.genexus.com/commwiki/wiki?44243) | [GeneXus Cognitive API - Deploy procedure](https://wiki.genexus.com/commwiki/wiki?44247) | [GeneXus Cognitive API - DetectFaces procedure](https://wiki.genexus.com/commwiki/wiki?40177) |
| [GeneXus Cognitive API - DetectLanguage procedure](https://wiki.genexus.com/commwiki/wiki?40181) | [GeneXus Cognitive API - DetectObjects procedure](https://wiki.genexus.com/commwiki/wiki?40178) | [GeneXus Cognitive API - DetectScene procedure](https://wiki.genexus.com/commwiki/wiki?40179) | [GeneXus Cognitive API - Evaluate procedure](https://wiki.genexus.com/commwiki/wiki?44244) |
| [GeneXus Cognitive API - ExtractEntities procedure](https://wiki.genexus.com/commwiki/wiki?40182) | [GeneXus Cognitive API - KeyPhrases procedure](https://wiki.genexus.com/commwiki/wiki?40183) | [GeneXus Cognitive API - OCR procedure](https://wiki.genexus.com/commwiki/wiki?40180) | [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245) |
| [GeneXus Cognitive API - Process procedure](https://wiki.genexus.com/commwiki/wiki?41042) | [GeneXus Cognitive API - SentimentAnalysis procedure](https://wiki.genexus.com/commwiki/wiki?40184) | [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) | [GeneXus Cognitive API - Translate procedure](https://wiki.genexus.com/commwiki/wiki?40185) |
| [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) | [Language domain](https://wiki.genexus.com/commwiki/wiki?40453) | [Locale domain](https://wiki.genexus.com/commwiki/wiki?40450) | [SpeechToText procedure](https://wiki.genexus.com/commwiki/wiki?40169) |
| [TextToSpeech procedure](https://wiki.genexus.com/commwiki/wiki?40170) |

---
