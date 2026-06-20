---
title: "GeneXus Cognitive API - Classify procedure"
source_id: 40171
source_url: https://wiki.genexus.com/commwiki/wiki?40171
genexus_version: "18"
---

# GeneXus Cognitive API - Classify procedure

Classifies an image in a set of categories.

## [Parameters](#Parameters)

* **in**:&image :: [Image data type](https://wiki.genexus.com/commwiki/wiki?15204)  
  An image to be classified.
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&OutputLabels:: [OutputLabel, GeneXusAI (collection)](https://wiki.genexus.com/commwiki/wiki?40193)  
  A set of classification categories along with their confidence.

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
| **IBM** | - | Visual Recognition | - |
| **Microsoft** | - | Computer Vision | - |
| **MLKit** | ML Kit API | ML Kit API | - |
| **SAP** | - | Sandbox Environment  (Deprecated) | - |
| **Tencent** | 多标签识别 | 多标签识别 | - |

Additionally, for custom models, you must set the properties described in the following table. For more information, refer to [HowTo: Build a custom model for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?43665).

|  |  |  |  |
| --- | --- | --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** | | |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | **ModelId** | **ModelVersion** | **ModelCredential** |
| **Alibaba** | - | - | - |
| **Amazon** | - | - | - |
| **Baidu** | - | - | - |
| **Google** | AutoML *(Project Id)* | - | AutoML *(Service Account Json)* |
| **IBM** | Visual Recognition *(Model Id)* | - | Visual Recognition *(API Key)* |
| **Microsoft** | Custom Vision *(Project Id)* | Custom Vision *(Published Name)* | Custom Vision *(Prediction Key)* |
| **MLKit** | - | - | - |
| **SAP** | Customizable Image  Classification *(Model Version)*  (Deprecated) | Customizable Image  Classification *(Model Version)*  (Deprecated) |  |
| **Tencent** | - | - | - |

## [Sample](#Sample)

Taking the following image input, the table below shows the classification made for each provider and the time it takes for processing it.

|  |
| --- |
|  |

|  |  |  |
| --- | --- | --- |
| **Provider** | **Output** | **Benchmark** |
| **Alibaba** | ``` [{     "label": "清真寺",     "confidence": 0.99 }] ``` | 12435ms |
| **Amazon** | ``` [{ 	"label": "Vacation", 	"confidence": 0.998 }, { 	"label": "Sunglasses", 	"confidence": 0.996 }, { 	"label": "Person", 	"confidence": 0.995 }, { 	"label": "Tourist", 	"confidence": 0.982 }, { 	"label": "Building", 	"confidence": 0.906 }, { 	"label": "Architecture", 	"confidence": 0.906 }, { 	"label": "Clothing", 	"confidence": 0.709 }, { 	"label": "Dome", 	"confidence": 0.693 }, { 	"label": "Monument", 	"confidence": 0.656 }, { 	"label": "People", 	"confidence": 0.644 }] ``` | 4135ms |
| **Baidu** | ``` [{     "label": "建筑",     "confidence": 0.952,     "Info": [{         "property": "ROOT",         "value": "建筑-现代建筑"     }] }, {     "label": "李维斯",     "confidence": 0.799,     "Info": [{         "property": "ROOT",         "value": "Logo"     }] }, {     "label": "历史遗迹",     "confidence": 0.515,     "Info": [{         "property": "ROOT",         "value": "建筑-文明遗迹"     }] }, {     "label": "情侣",     "confidence": 0.235,     "Info": [{         "property": "ROOT",         "value": "人物-人物特写"     }] }, {     "label": "卡通动漫人物",     "confidence": 0.023,     "Info": [{         "property": "ROOT",         "value": "非自然图像-彩色动漫"     }] }] ``` | 8476ms |
| **Google** | ``` [{     "label": "landmark",     "confidence": 0.914 }, {     "label": "tourism",     "confidence": 0.889 }, {     "label": "tourist attraction",     "confidence": 0.827 }, {     "label": "historic site",     "confidence": 0.824 }, {     "label": "vacation",     "confidence": 0.792 }, {     "label": "travel",     "confidence": 0.765 }, {     "label": "temple",     "confidence": 0.733 }, {     "label": "sky",     "confidence": 0.688 }, {     "label": "fun",     "confidence": 0.632 }, {     "label": "place of worship",     "confidence": 0.560 }] ``` | 8263ms |
| **IBM** | ``` [{     "label": "Taj Mahal",     "confidence": 0.777 }, {     "label": "Seven Wonders of the Ancient World",     "confidence": 0.753 }, {     "label": "religious building",     "confidence": 0.635 }, {     "label": "building",     "confidence": 0.635 }, {     "label": "memorial",     "confidence": 0.601 }, {     "label": "alabaster color",     "confidence": 0.927 }] ``` | 6160ms |
| **Microsoft** | ``` [{     "label": "outdoor",     "confidence": 0.003 }, {     "label": "people",     "confidence": 0.644 }] ``` | 3489ms |
| **MLKit** | ``` [{     "label": "Monument",     "confidence": 0.861 }, {     "label": "Vacation",     "confidence": 0.787 }, {     "label": "Sunglasses",     "confidence": 0.782 }, {     "label": "Building",     "confidence": 0.715 }, {     "label": "Event",     "confidence": 0.627 }, {     "label": "Leisure",     "confidence": 0.612 }, {     "label": "Plant",     "confidence": 0.5 }] ``` | 1294ms |
| **SAP** | ``` [{     "label": "mosque",     "confidence": 0.821 }, {     "label": "palace",     "confidence": 0.008 }, {     "label": "bell cote, bell cot",     "confidence": 0.003 }, {     "label": "dome",     "confidence": 0.003 }, {     "label": "gondola",     "confidence": 0.002 }] ``` | 4682ms |
| **Tencent** | ``` [{ 	"label": "广场", 	"confidence": 0.410 }, { 	"label": "天空", 	"confidence": 0.400 }, { 	"label": "欧式建筑", 	"confidence": 0.240 }, { 	"label": "男孩", 	"confidence": 0.190 }, { 	"label": "树木", 	"confidence": 0.140 }, { 	"label": "合影", 	"confidence": 0.120 }] ``` | 18196ms |

## [Notes](#Notes)

* The classification is made with the default classifier of each provider. For such reason, the categories (or labels) returned are not predefined and they depend on the provider used.
* The maximum image file size is 10MB.
* SAP Leonardo allows images of 1.0 MP at most.
* Tencent AI and Baidu AI return labels as Chinese strings.
* **IBM provider**: Deprecated as of December 22 (2021). Check [IBM Visual Recognition's Release Notes](https://www.ibm.com/docs/en/app-connect/containers_eus?topic=SSTTDS_conteus/com.ibm.ace.icp.eus.doc/localconn_ibmwatsonvr.htm).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |
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
* As of [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,):  
  - Custom models integration for Google, IBM, Microsoft, and SAP are available.
* As of [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,):  
  - SAP Leonardo has been deprecated
* As of [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,):  
  - Firebase ML Kit for Android is available

## [See also](#See+also)

* [HowTo: Build a custom model for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?43665)


|  |
| --- |
| **Backlinks** |
| [Confidence domain](https://wiki.genexus.com/commwiki/wiki?40189) | [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) |
| [HowTo: Build a custom model for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?43665) | [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) | [Model data type](https://wiki.genexus.com/commwiki/wiki?44240) | [OutputLabel data type](https://wiki.genexus.com/commwiki/wiki?40193) |

---
