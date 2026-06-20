---
title: "TextToSpeech procedure"
source_id: 40170
source_url: https://wiki.genexus.com/commwiki/wiki?40170
genexus_version: "18"
---

# TextToSpeech procedure

Converts a plain text into an audio stream.

## [Parameters](#Parameters)

* **in**:&Text :: [Text, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40192)  
  The plain text to be synthesized.
* **in**:&locale :: [Locale, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40450)  
  The language locale of the output speech.
* **in**:&voiceType :: [VoiceType, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40269)  
  The output voice type (female or male).
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&Audio :: [Audio data type](https://wiki.genexus.com/commwiki/wiki?16529)  
  The input text's synthesized audio stream.

## [Configuration](#Configuration)

The following table resumes the configuration properties (access credentials) you must set in order to use this AI task.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** | | |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | **Id** | **Key** | **SecretKey** |
| **Alibaba** | 智能语音交互 app-key | 用户AccessKey | 用户AccessKey |
| **Amazon** | - | Polly | Polly |
| **Baidu** | 百度语音 | 百度语音 | 百度语音 |
| **Google** | - | Cloud Speech API | - |
| **IBM** | - | TextToSpeech API | - |
| **Microsoft** | - | Speech API | - |
| **SAP** | - | - | - |
| **Tencent** | 音合成 | 音合成 | - |

## [Sample](#Sample)

Taking the following plain text, the table below shows the synthesis made for each provider and the time it takes to process it.

"*The first question that comes up is: What is GeneXus? GeneXus is a tool that automatically generates software programs such as applications for the Web, and Smart Devices, always at the forefront of technological evolution.*"

|  |  |  |
| --- | --- | --- |
| **Provider** | **Output** | **Benchmark** |
| **Alibaba** | [TextToSpeech - Alibaba output](https://wiki.genexus.com/commwiki/wiki?43234,,)   [TextToSpeech - Alibaba output](https://wiki.genexus.com/commwiki/wiki?43234,,)  0:00 | 3325ms |
| **Amazon** | [TextToSpeech - Amazon output](https://wiki.genexus.com/commwiki/wiki?41961,,)   [TextToSpeech - Amazon output](https://wiki.genexus.com/commwiki/wiki?41961,,)  0:00 | 1486ms |
| **Baidu** | [TextToSpeech - Baidu output](https://wiki.genexus.com/commwiki/wiki?42622,,)   [TextToSpeech - Baidu output](https://wiki.genexus.com/commwiki/wiki?42622,,)  0:00 | 4634ms |
| **Google** | [TextToSpeech - Google output](https://wiki.genexus.com/commwiki/wiki?41053,,)   [TextToSpeech - Google output](https://wiki.genexus.com/commwiki/wiki?41053,,)  0:00 | 1887ms |
| **IBM** | [TextToSpeech - IBM output](https://wiki.genexus.com/commwiki/wiki?40319,,)   [TextToSpeech - IBM output](https://wiki.genexus.com/commwiki/wiki?40319,,)  0:00 | 3205ms |
| **Microsoft** | [TextToSpeech - Microsoft output](https://wiki.genexus.com/commwiki/wiki?40320,,)   [TextToSpeech - Microsoft output](https://wiki.genexus.com/commwiki/wiki?40320,,)  0:00 | 3412ms |
| **SAP** | N/A | N/A |
| **Tencent** | [TextToSpeech - Tencent output](https://wiki.genexus.com/commwiki/wiki?41962,,)   [TextToSpeech - Tencent output](https://wiki.genexus.com/commwiki/wiki?41962,,)  0:00 | 4614ms |

The &Text input parameter also admits [SSML](https://en.wikipedia.org/wiki/Speech_Synthesis_Markup_Language) inner nodes (excluding <speak> root) for formatting pronunciation, intonation, etc. For example:

"<emphasis level='strong'>*GeneXus<emphasis> is a tool that <prosody pinth='high'>automatically generates software programs</prosody> such as applications for the Web, and <sub alias='Smart Devices'>SD</sub>, with over <say-as interpret-as='cardinal'>30</say-as> years of experience.*"

Giving the following result:

[TextToSpeech - SSML input](https://wiki.genexus.com/commwiki/wiki?40321,,)

[TextToSpeech - SSML input](https://wiki.genexus.com/commwiki/wiki?40321,,)

0:00

## [Notes](#Notes)

* For SSML input, not all of the elements and options of [W3 SSML specification](https://www.w3.org/TR/speech-synthesis/) are currently supported on every provider. GeneXusAI specifically does not allow the  <voice> tag, it must be set in the &voiceType input parameter.
* For Google Cloud AI, when you enable Speech Cloud API to use this task, you must select '*Standard Voices*' option.
* For Microsoft Speech API, when you want to use another locale or voice type, you can use [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) to load them. For instance, if you want to use the 'es-UY' locale with the female voice "ValentinaNeural", you can do &locale.FromString("es-UY") and &voiceType.FromString("ValentinaNeural") when setting the input parameters.
* Tencent AI and Baidu AI providers only allow Chinese or English (or mixed) text input.

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

## [See also](#See+also)

* [VoiceType domain](https://wiki.genexus.com/commwiki/wiki?40269)
* [SpeechToText procedure](https://wiki.genexus.com/commwiki/wiki?40169)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) |
| [Locale domain](https://wiki.genexus.com/commwiki/wiki?40450) | [Sample: GeneXus Cognitive API proof of concept](https://wiki.genexus.com/commwiki/wiki?40853) | [SpeechToText procedure](https://wiki.genexus.com/commwiki/wiki?40169) | [Text domain](https://wiki.genexus.com/commwiki/wiki?40192) |
| [VoiceType domain](https://wiki.genexus.com/commwiki/wiki?40269) |

---
