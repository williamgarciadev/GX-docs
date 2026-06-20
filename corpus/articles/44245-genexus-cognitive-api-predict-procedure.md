---
title: "GeneXus Cognitive API - Predict procedure"
source_id: 44245
source_url: https://wiki.genexus.com/commwiki/wiki?44245
genexus_version: "18"
---

# GeneXus Cognitive API - Predict procedure

Makes a prediction using a custom model based on the input data.

## [Parameters](#Parameters)

* **in**:&dataInput:: [DataInput, GeneXusAI.Custom](https://wiki.genexus.com/commwiki/wiki?44425)  
  The input data item.
* **in**:&model :: [Model, GeneXusAI.Custom](https://wiki.genexus.com/commwiki/wiki?44240)  
  The model information used to predict.
* **in**:&provider :: [Provider, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40197)  
  Provider settings.
* **inout**:&Messages :: [Messages, GeneXus.Common](https://wiki.genexus.com/commwiki/wiki?40335)  
  A collection of warning and error messages returned by the task. You should check in your code if an error was returned. Refer to [error codes and descriptions](https://wiki.genexus.com/commwiki/wiki?40188) for more information.
* **out**:&DataOutput:: [DataOutput, GeneXusAI.Custom](https://wiki.genexus.com/commwiki/wiki?44426)  
  Output data item.

## [Configuration](#Configuration)

The following table resumes the configuration properties (access credentials) you must set in order to use this AI task.

|  |  |
| --- | --- |
|  | **[PropertyKey](https://wiki.genexus.com/commwiki/wiki?40196)** |
| **[ProviderType](https://wiki.genexus.com/commwiki/wiki?40195)** | **Key** |
| **Alibaba** | - |
| **Amazon** | - |
| **Baidu** | - |
| **Google** | Service Account JSON |
| **IBM** | Visual Recognition Key |
| **Microsoft** | Custom Vision Training Key |
| **SAP** | - |
| **Tencent** | - |

## [Sample](#Sample)

After deploying your model (trained with the [Mamaevs' Flowers Recognition dataset](https://www.kaggle.com/alxmamaev/flowers-recognition)) and taking the following (unseen) image input, the table below shows the prediction made for each provider and the time it takes for processing it.

`[imagen omitida: wiki id 44248]`

**Note**: In the context of custom models, the term "unseen image" means the image will not participate in the training process. In other words, the image is not in the training dataset.

|  |  |  |
| --- | --- | --- |
| **Provider** | **Output** | **Benchmark** |
| **Alibaba** | GXAI6001 - Task 'GeneXusAI.Custom.Evaluate' is unavailable (...) | N/A |
| **Amazon** | GXAI6001 - Task 'GeneXusAI.Custom.Evaluate' is unavailable (...) | N/A |
| **Baidu** | GXAI6001 - Task 'GeneXusAI.Custom.Evaluate' is unavailable (...) | N/A |
| **Google** | ``` {      "Label": "dandelion",      "Confidence": 0.915 } ``` | 3377ms |
| **IBM** | ``` {     "Label": "dandelion",     "Confidence": 0.945 } ``` | 1070ms |
| **Microsoft** | ``` {     "Label": "dandelion",     "Confidence": 0.974 } ``` | 590ms |
| **SAP** | GXAI6001 - Task 'GeneXusAI.Custom.Evaluate' is unavailable (...) | N/A |
| **Tencent** | GXAI6001 - Task 'GeneXusAI.Custom.Evaluate' is unavailable (...) |  |

## [Notes](#Notes)

* If you want to get a set of possible candidates, use a predefined GeneXusAI task instead of the Predict procedure (e.g. use Classify procedure if your model was trained for predicting Labels, or DetectObjects for predicting Regions).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |
| **Connectivity:** | Online |

## [Availability](#Availability)

This procedure is available as of [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).

* As of [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,)  
  -  Google Auto ML is available.

## [See also](#See+also)

* [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246)
* [HowTo: Build a custom model for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?43665)


|  |
| --- |
| **Backlinks** |
| [Data data type](https://wiki.genexus.com/commwiki/wiki?44237) | [DataInput data type](https://wiki.genexus.com/commwiki/wiki?44425) | [DataOutput data type](https://wiki.genexus.com/commwiki/wiki?44426) |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Deploy procedure](https://wiki.genexus.com/commwiki/wiki?44247) | [GeneXus Cognitive API - Evaluate procedure](https://wiki.genexus.com/commwiki/wiki?44244) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) |
| [HowTo: Build a custom model for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?43665) | [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) | [Measure data type](https://wiki.genexus.com/commwiki/wiki?44239) | [Model data type](https://wiki.genexus.com/commwiki/wiki?44240) |

---
