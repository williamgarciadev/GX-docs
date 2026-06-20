---
title: "GeneXus Cognitive API - DetectScene procedure"
source_id: 40179
source_url: https://wiki.genexus.com/commwiki/wiki?40179
genexus_version: "18"
---

# GeneXus Cognitive API - DetectScene procedure

Determines the scenario that the image is about (a city, a beach, a desert, etc.).

## [Parameters](#Parameters)

* **in**:&image :: [Image data type](https://wiki.genexus.com/commwiki/wiki?15204)  
  An image to identify its scenario.
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&OutputLabels:: [OutputLabel, GeneXusAI (collection)](https://wiki.genexus.com/commwiki/wiki?40193)  
  A set of labels with their confidence describing the image's scenario.

## [Configuration](#Configuration)

The following table resumes the configuration properties (access credentials) you must set in order to use this AI task.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** | | |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | **Id** | **Key** | **SecretKey** |
| **Alibaba** | - | 用户AccessKey | 用户AccessKey |
| **Amazon** | - | Rekognition | Rekognition |
| **Baidu** | 视觉技术 | 视觉技术 | 视觉技术 |
| **Google** | - | Cloud Vision API | - |
| **IBM** | - | - | - |
| **Microsoft** | - | Computer Vision | - |
| **MLKit** | ML Kit API | ML Kit API | - |
| **SAP** | - | - | - |
| **Tencent** | 场景识别 | 场景识别 | - |

## [Sample](#Sample)

Taking the following image input, the table below shows the scenarios are identified for each provider (as a JSON structure) and the time it takes for processing it.

|  |
| --- |
|  |

|  |  |  |
| --- | --- | --- |
| **Provider** | **Output** | **Benchmark** |
| **Alibaba** | ``` [{ 	"label": "建筑", 	"confidence": 0.930 }, { 	"label": "广场", 	"confidence": 0.190 }, { 	"label": "人物", 	"confidence": 0.140 }, { 	"label": "户外", 	"confidence": 0.110 }, { 	"label": "室外", 	"confidence": 0.110 }] ``` | 4106ms |
| **Amazon** | ``` [{     "label": "Vacation",     "confidence": 0.997 }, {     "label": "Tourist",     "confidence": 0.976 }, {     "label": "Architecture",     "confidence": 0.924 }, {     "label": "Building",     "confidence": 0.924 }, {     "label": "Dome",     "confidence": 0.787 }, {     "label": "Clothing",     "confidence": 0.715 }, {     "label": "Monument",     "confidence": 0.675 }, {     "label": "People",     "confidence": 0.610 }] ``` | 2818ms |
| **Baidu** | ``` [{ 	"label": "泰姬陵", 	"confidence": 1.000 }] ``` | 6742ms |
| **Google** | ``` [{     "label": "Taj Mahal",     "confidence": 0.72149533 }] ``` | 10426ms |
| **IBM** | N/A | N/A |
| **Microsoft** | ``` [{     "label": "outdoor, Taj Mahal",     "confidence": 0.985146582126618 }, {     "label": "people",     "confidence": 0.64453125 }] ``` | 4125ms |
| **MLKit** | ``` [] ``` | 1322ms |
| **SAP** | N/A | N/A |
| **Tencent** | ``` [{     "label": "GXAI_TCN_SCENE_193",     "confidence": 0.974 }, {     "label": "GXAI_TCN_SCENE_210",     "confidence": 0.004 }, {     "label": "GXAI_TCN_SCENE_92",     "confidence": 0.004 }, {     "label": "GXAI_TCN_SCENE_223",     "confidence": 0.003 }, {     "label": "GXAI_TCN_SCENE_65",     "confidence": 0.002 }] ``` | 11409ms |

## [Notes](#Notes)

* The label assigned for an object depends on the provider used.
* Maximum image file size is 10MB.
* Tencent AI returns labels as 'GXAI\_TCN\_SCENE\_{id}' tags, where the {id} is a [numeric class](https://ai.qq.com/doc/vision_scene.shtml#7-场景标识定义) provided by Tencent. You can use a [Language object](https://wiki.genexus.com/commwiki/wiki?7258) for mapping each tag with string label as other provider does. You can [download this xpz](https://wiki.genexus.com/commwiki/wiki?41968,,) which contains the SimplifiedChinese language object with the official mapping, and also contains the English language mapping using machine translation (it can be inaccurate). Once you import this xpz, for example, the 'GXAI\_TCN\_SCENE\_193' label on the sample section will be translated to '清真寺外面' (or 'outside the mosque' in English) if you have set [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) in your environment with 'Run-time' value.
* ML Kit requires [Google Vision enabled](https://console.developers.google.com/apis/library/vision.googleapis.com) and works on the cloud (the inference is not made on the device).

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
* As of [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,):  
  - Firebase ML Kit is available for Android.


|  |
| --- |
| **Backlinks** |
| [Confidence domain](https://wiki.genexus.com/commwiki/wiki?40189) | [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) |
| [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) | [Label domain](https://wiki.genexus.com/commwiki/wiki?40191) | [OutputLabel data type](https://wiki.genexus.com/commwiki/wiki?40193) |

---
