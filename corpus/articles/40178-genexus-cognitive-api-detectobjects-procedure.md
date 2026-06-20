---
title: "GeneXus Cognitive API - DetectObjects procedure"
source_id: 40178
source_url: https://wiki.genexus.com/commwiki/wiki?40178
genexus_version: "18"
---

# GeneXus Cognitive API - DetectObjects procedure

Detects objects that appear in an image.

## [Parameters](#Parameters)

* **in**:&image :: [Image data type](https://wiki.genexus.com/commwiki/wiki?15204)  
  An image to detect objects on it.
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&OutputRegions:: [OutputRegion, GeneXusAI (collection)](https://wiki.genexus.com/commwiki/wiki?40194)  
  A set of regions with the recognized objects.

## [Configuration](#Configuration)

The following table resumes the configuration properties (access credentials) you must set in order to use this AI task.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** | | | |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | **Id** | **Key** | **SecretKey** |
| **Alibaba** | - | - | - |
| **Amazon** | - | Rekognition | Rekognition |
| **Baidu** | - | - | - |
| **Google** | - | Cloud Vision API | - |
| **IBM** | - | - | - |
| **Microsoft** | - | Computer Vision | - |
| **MLKit** | ML Kit API | ML Kit API |  |
| **SAP** | - | - | - |
| **Tencent** | 物体识别 | 物体识别 | - |

## [Sample](#Sample)

Taking the following image input, the table below shows how objects are identified for each provider (as a JSON structure) and the time it takes for processing it.

|  |
| --- |
|  |

|  |  |  |  |
| --- | --- | --- | --- |
| **Provider** | **Output** |  | **Benchmark** |
| **Alibaba** | N/A |  | N/A |
| **Amazon** | ``` [{ 	"label": "Sunglasses 1", 	"confidence": 0.996, 	"top": 463, 	"left": 435, 	"width": 110, 	"height": 35 }, { 	"label": "Person 1", 	"confidence": 0.995, 	"top": 408, 	"left": 89, 	"width": 760, 	"height": 434 }, { 	"label": "Person 2", 	"confidence": 0.886, 	"top": 586, 	"left": 19, 	"width": 53, 	"height": 126 }] ``` |  | 11121ms |
| **Baidu** | N/A |  | N/A |
| **Google** | ``` [{     "label": "Person",     "confidence": 0.7952577,     "top": 477,     "left": 115,     "width": 722,     "height": 369 }, {     "label": "Man",     "confidence": 0.64812267,     "top": 409,     "left": 146,     "width": 600,     "height": 372 }] ``` |  | 8218ms |
| **IBM** | N/A |  | N/A |
| **Microsoft** | ``` [{     "label": "outdoor",     "confidence": 0.996472358703613,     "top": 0,     "left": 0,     "width": 0,     "height": 0 }, {     "label": "sky",     "confidence": 0.980476856231689,     "top": 0,     "left": 0,     "width": 0,     "height": 0 }, {     "label": "person",     "confidence": 0.974854707717896,     "top": 0,     "left": 0,     "width": 0,     "height": 0 }, {     "label": "man",     "confidence": 0.922227799892426,     "top": 0,     "left": 0,     "width": 0,     "height": 0 }, {     "label": "building",     "confidence": 0.8099485039711,     "top": 0,     "left": 0,     "width": 0,     "height": 0 }] ``` |  | 4896ms |
| **MLKit** | ``` [{     "label": "FASHION_GOOD",     "confidence": 0.937,     "top": 674,     "left": 446,     "width": 355,     "height": 369 }, {     "label": "FASHION_GOOD",     "confidence": 0.71,     "top": 724,     "left": 369,     "width": 55,     "height": 90 }, {     "label": "FASHION_GOOD",     "confidence": 0.582,     "top": 515,     "left": 199,     "width": 822,     "height": 534 }, {     "label": "UNKNOWN",     "confidence": 0,     "top": 716,     "left": 186,     "width": 48,     "height": 122 }, {     "label": "UNKNOWN",     "confidence": 0,     "top": 729,     "left": 13,     "width": 64,     "height": 145 }] ``` |  | 999ms |
| **SAP** | N/A |  | N/A |
| **Tencent** | ``` [{ 	"label": "GXAI_TCN_OBJECT_668", 	"confidence": 0.623, 	"top": 0, 	"left": 0, 	"width": 0, 	"height": 0 }, { 	"label": "GXAI_TCN_OBJECT_873", 	"confidence": 0.204, 	"top": 0, 	"left": 0, 	"width": 0, 	"height": 0 }, { 	"label": "GXAI_TCN_OBJECT_682", 	"confidence": 0.101, 	"top": 0, 	"left": 0, 	"width": 0, 	"height": 0 }, { 	"label": "GXAI_TCN_OBJECT_442", 	"confidence": 0.017, 	"top": 0, 	"left": 0, 	"width": 0, 	"height": 0 }, { 	"label": "GXAI_TCN_OBJECT_698", 	"confidence": 0.01, 	"top": 0, 	"left": 0, 	"width": 0, 	"height": 0 }] ``` |  | 5587ms |

## [Notes](#Notes)

* The label assigned for an object depends on the provider used. Additional information can be found on the OutputRegion.Info field if it is given by the provider.
* Maximum image file size is 10MB.
* Tencent AI returns labels as 'GXAI\_TCN\_OBJECT\_{id}' tags, where the {id} is a [numeric class](https://ai.qq.com/doc/vision_object.shtml#7-%E7%89%A9%E4%BD%93%E6%A0%87%E8%AF%86%E5%AE%9A%E4%B9%89) provided by Tencent. You can use a [Language object](https://wiki.genexus.com/commwiki/wiki?7258) for mapping each tag with string label as other provider does. You can [download this xpz](https://wiki.genexus.com/commwiki/wiki?41968,,) which contains the SimplifiedChinese language object with the official mapping, and also contains the English language mapping using machine translation (it can be inaccurate). Once you import this xpz, for example, the 'GXAI\_TCN\_OBJECT\_668' label on the sample section will be translated to '清真寺' (or 'mosque' in English) if you have set [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) in your environment with 'Run-time' value.
* Rectangle area has zero values when the provider is not allowed to identify the region.
* GeneXusAI does not provide support for drawing a rectangle over an image. This action is the responsibility of the developer.  
  **TIP**: For Web applications, a good alternative can be combining [HTML5 Canvas control with JavaScript](https://www.w3schools.com/tags/ref_canvas.asp) with [User Control object](https://wiki.genexus.com/commwiki/wiki?39356). On the other hand, for Smart Devices you could use [Image Map control](https://wiki.genexus.com/commwiki/wiki?17823) on which you can set the processed image as background and 'draw' square regions (i.e. set a border color on the table item of the grid).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | .NET, Java, Android, Apple, Angular |
| **Connectivity:** | Online |

## [Availability](#Availability)

This procedure is available as of [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,).

* As of [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/wiki?40782,,):  
  - Google Cloud AI is available.
* As of [GeneXus 16 upgrade 2](https://wiki.genexus.com/commwiki/wiki?41525,,):  
  - Amazon WS and Tencent AI are available.  
  - Google returns rectangles with values different from 0. Applies for .NET and Java environments, .NET Core is still limited.
* As of [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,):  
  - Google returns rectangles with values different from 0 for .NET Core.
* As of [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,):  
  - Firebase ML Kit is available for Android


|  |
| --- |
| **Backlinks** |
| [Confidence domain](https://wiki.genexus.com/commwiki/wiki?40189) | [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) |
| [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) | [Label domain](https://wiki.genexus.com/commwiki/wiki?40191) | [OutputRegion data type](https://wiki.genexus.com/commwiki/wiki?40194) |

---
