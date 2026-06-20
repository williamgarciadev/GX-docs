---
title: "SpeechToText procedure"
source_id: 40169
source_url: https://wiki.genexus.com/commwiki/wiki?40169
genexus_version: "18"
---

# SpeechToText procedure

Converts an audio stream to plain text by transcribing the speech detected in the audio stream.

## [Parameters](#Parameters)

* **in**:&audio :: [Audio data type](https://wiki.genexus.com/commwiki/wiki?16529)  
  An audio stream to be transcribed.
* **in**:&locale :: [Locale, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40450)  
  The language locale of the input speech.
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&OutputText :: [OutputText, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?45364)  
  The transcribed text.

## [Configuration](#Configuration)

The following table resumes the configuration properties (access credentials) you must set in order to use this AI task.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** | | |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | **Id** | **Key** | **SecretKey** |
| **Alibaba** | 智能语音交互 app-key | 用户AccessKey | 用户AccessKey |
| **Amazon** | - | Transcribe | Transcribe |
| **Baidu** | 百度语音 | 百度语音 | 百度语音 |
| **Google** | - | Cloud Speech API | - |
| **IBM** | - | SpeechToText API | - |
| **Microsoft** | - | Speech API | - |
| **SAP** | - | - | - |
| **Tencent** | 语音识别 | 语音识别 | - |

## [Sample](#Sample)

Taking the following spoken audio input, the table below shows the transcription made for each provider and the time it takes for processing it.

[SpeechToText - Sample input](https://wiki.genexus.com/commwiki/wiki?40318,,)

[SpeechToText - Sample input](https://wiki.genexus.com/commwiki/wiki?40318,,)

0:00

|  |  |  |
| --- | --- | --- |
| **Provider** | **Output** | **Benchmark** |
| **Alibaba** | GXAI4101 - Parameter '&Locale' is malformed. Expected values: [Chinese (Simplified, Mainland), Mandarin (Simplified, Mainland), Cantonese (Traditional, Hong Kong)] | 9040ms |
| **Amazon** | ``` {     "Text": "The first question that comes to mind is, What is the nexus you Nexus is a tool that automatically generate software programs such as applications for Windows, the Web and, smart devices which are always at the forefront of technological evolution."     "Confidence": 0.982     "Info":[         {             "Property":"The",              "Value": "{\"start\":0.70000,\"duration\":0.17000}"         },         ...         {             "Property":"evolution",              "Value": "{\"start\":14.51000,\"duration\":0.60000}"         },         {             "Property":".",              "Value": "{\"start\":15.11000,\"duration\":00.00000}"         }     ] } ``` | 202627ms |
| **Baidu** | GXAI4101 - Parameter '&Locale' is malformed. Expected values: [Chinese (Simplified, Mainland), Mandarin (Simplified, Mainland), Cantonese (Traditional, Hong Kong)] | N/A |
| **Google** | ``` {     "Text": "The first question that comes to mind is what is Genesis. The Nexus is a tool that automatically generate software program such as applications for Windows."     "Confidence": 0.982     "Info":[         {             "Property":"the",             "Value": "{\"start\":0.00000,\"duration\":0.90000}"         },         ...         {             "Property":"Windows",             "Value": "{\"start\":10.10000,\"duration\":0.50000}"         },         {             "Property":".",             "Value": "{\"start\":10.60000,\"duration\":0.00000}"         }     ] } ``` | 6986ms |
| **IBM** | ``` {     "Text": "The first question that comes to mind is. What is your nexus. Next is a tool that automatically generate software programs such as applications for windows the web and smart devices which are always at the forefront technological evolution."     "Confidence": 0.982     "Info":[         {             "Property":"The",             "Value": "{\"start\":0.71000,\"duration\":0.12000}"         },         ...         {             "Property":"evolution",             "Value": "{\"start\":14.48000,\"duration\":0.63000}"         },         {             "Property":".",             "Value": "{\"start\":15.11000,\"duration\":0.00000}"         }     ] } ``` | 8682ms |
| **Microsoft** | ``` {     "Text": "The first question that comes to mind is what is genexus.",     "Confidence": 1.0 } ``` | 3412ms |
| **SAP** | N/A | N/A |
| **Tencent** | GXAI4101 - Parameter '&Locale' is malformed. Expected values: [Chinese (Simplified, Mainland), Mandarin (Simplified, Mainland), Cantonese (Traditional, Hong Kong)] | N/A |

## [Considerations](#Considerations)

### [Short transcriptions](#Short+transcriptions)

The transcription will be made only for short timing audio (up to 15 seconds) and short utterances. As a consequence of this second condition, text output can be "incomplete" regarding the audio input because the transcription will be made up to the first "silence mark" (e.g. as Microsoft does). The aim is to identify a voice command.

### [Chinese providers](#Chinese+providers)

Only support Chinese-spoken audios. Otherwise, it will raise a GXAI5000 error when the audio is provided in another (unknown) language.

For example, taking the following Chinese-spoken audio, you will get the result detailed on the below table.

[SpeechToText - Sample - Chinese](https://wiki.genexus.com/commwiki/wiki?41960,,)

[SpeechToText - Sample - Chinese](https://wiki.genexus.com/commwiki/wiki?41960,,)

0:00

|  |  |  |
| --- | --- | --- |
| **Provider** | **Output** | **Benchmark** |
| **Alibaba** | ``` {     "Text": "提出的第一个问题是什么是冰山冰山是一个自动生成软件，程序的工具，例如为应用程序和智能设备始终处于技术发展的最前沿。"     "Confidence": 1.0 } ``` | 13160ms |
| **Baidu** | ``` {     "Text": "提出的第一个问题是一个自动生成软件程序的工具，例如应用程序，智能设备始终处于技术发展的最前沿",     "Confidence": 1.0 } ``` | 101354ms |
| **Tencent** | ``` {     "Text": "提出的第一个问题是什么仅三十一个自动生成软件程序的工具例如应用程序可智能设备始终处于技术发展的最前沿",     "Confidence": 1.0 } ``` | 98457ms |

### [Amazon provider](#Amazon+provider)

The audio file must be uploaded to Amazon S3. In case you have set [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) with your Amazon credentials, any audio will be automatically stored on your S3 bucket to be processed. In another case, you must provide an URL with one of the following expressions:  
+ *http**://{bucket}.s3.amazonaws.com/{path/to/filename.ext}*  
+ *http://{bucket}.s3-{region}.amazonaws.com/{path/to/filename.ext}*  
+ *http://s3.amazonaws.com/{bucket}/{path/to/filename.ext}*  
+ *http://s3-{region}.amazonaws.com/{bucket}/{path/to/filename.ext}*  
The {region} must match with the region of your access credentials (or can be empty only when your region is 'us-east-1').

## [Notes](#Notes)

* Input audio format depends on the provider type.  
  - Amazon WS supports *mp3*, *mp4*, *wav* and *flac*.  
  - Baidu AI supports *pcm*, *wav*, and *amr*.  
  - IBM Watson supports *mp3, mp4, wav, ogg, flac* and *webm*(GeneXus 16 Upgrade 0 only supports *mp3*)  
  - Microsoft Azure supports *wav* only.  
  - Google Cloud AI supports *mp3*, *wav* and *ogg*.  
  - Tencent AI supports *wav* only.  
  Use [this site](http://mime.ritey.com/) to verify your audio has an appropriate mime-type.
* Audio format conversion can be done by using an external tool.  
  GeneXusAI integrates this feature automatically as an experimental feature if you follow these steps:  
  1) Download the [ffmpeg tool](https://www.ffmpeg.org) depending on your server's operative system (i.e. Linux or Windows).  
  2) Attach the binary file to your knowledge base as a [File object](https://wiki.genexus.com/commwiki/wiki?5852).  
  3) Set the [Extract for {gen} Generator property](https://wiki.genexus.com/commwiki/wiki?5852) in True, being '{gen}' your working generator (Java, .NET or .NET Core).  
  4) Set the [{gen} Generator Extract Directory property](https://wiki.genexus.com/commwiki/wiki?5852) with "*Resources*" value.  
  5) Ensure that the extracted binary file has execution permission where the webapp is running.  
  6) Give an &audio input to this task without worrying about its format.  
  Take into account that adding this feature the performance can be degraded.

  IMPORTANT: As an experimental feature, no support is provided and it is subject to breaking changes without any advertisement. Use it at your own risk.
* Microsoft's Bing Speech API will be deprecated and its credentials must be updated to Speech API before October 2019.

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

* [TextToSpeech procedure](https://wiki.genexus.com/commwiki/wiki?40170)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) |
| [Locale domain](https://wiki.genexus.com/commwiki/wiki?40450) | [OutputText data type](https://wiki.genexus.com/commwiki/wiki?45364) | [Sample: GeneXus Cognitive API proof of concept](https://wiki.genexus.com/commwiki/wiki?40853) | [Text domain](https://wiki.genexus.com/commwiki/wiki?40192) |
| [TextToSpeech procedure](https://wiki.genexus.com/commwiki/wiki?40170) |

---
