---
title: "PropertyKey domain"
source_id: 40196
source_url: https://wiki.genexus.com/commwiki/wiki?40196
genexus_version: "18"
---

# PropertyKey domain

Indicates the possible set of [Provider.Property.key names](https://wiki.genexus.com/commwiki/wiki?40197) in the context of [GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167).

## [Values](#Values)

The description of a key name indicates which value must have the [Provider.Property.value field](https://wiki.genexus.com/commwiki/wiki?40197).

|  |  |
| --- | --- |
| **Account** | Service account identifier. |
| **Deploy** | Service deploy identifier for custom models. |
| **Id** | Service application identifier. |
| **Key** | Service access API key. |
| **SecretKey** | Service access secret key. |
| **Username** | Service access username. |
| **Password** | Service access password for a username. |
| **ModelId** | Custom model identifier. |
| **ModelVersion** | Custom model version. |
| **ModelCredential** | Custom model access credential. |

Refer to [Required Credentials by Task document](https://wiki.genexus.com/commwiki/wiki?40204) for a summary of what configuration properties are required on each case. These properties are also specified on the "Configuration" section of each GeneXusAI's procedure.

## [Notes](#Notes)

* For Amazon provider, the *Access Key* must be indicated with the PropertyKey.Key value.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

## [Availability](#Availability)

This domain is available as of [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,).

* As of [GeneXus 16 upgrade 2](https://wiki.genexus.com/commwiki/wiki?41525,,):  
  - Id and SecretKey values added.

## [See also](#See+also)

* [Provider data type](https://wiki.genexus.com/commwiki/wiki?40197)
* [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Analyze procedure](https://wiki.genexus.com/commwiki/wiki?41041) | [GeneXus Cognitive API - Check procedure](https://wiki.genexus.com/commwiki/wiki?44242) |
| [GeneXus Cognitive API - Classify procedure](https://wiki.genexus.com/commwiki/wiki?40171) | [GeneXus Cognitive API - Delete procedure](https://wiki.genexus.com/commwiki/wiki?44243) | [GeneXus Cognitive API - Deploy procedure](https://wiki.genexus.com/commwiki/wiki?44247) | [GeneXus Cognitive API - DetectFaces procedure](https://wiki.genexus.com/commwiki/wiki?40177) |
| [GeneXus Cognitive API - DetectLanguage procedure](https://wiki.genexus.com/commwiki/wiki?40181) | [GeneXus Cognitive API - DetectObjects procedure](https://wiki.genexus.com/commwiki/wiki?40178) | [GeneXus Cognitive API - DetectScene procedure](https://wiki.genexus.com/commwiki/wiki?40179) | [GeneXus Cognitive API - Evaluate procedure](https://wiki.genexus.com/commwiki/wiki?44244) |
| [GeneXus Cognitive API - ExtractEntities procedure](https://wiki.genexus.com/commwiki/wiki?40182) | [GeneXus Cognitive API - KeyPhrases procedure](https://wiki.genexus.com/commwiki/wiki?40183) | [GeneXus Cognitive API - OCR procedure](https://wiki.genexus.com/commwiki/wiki?40180) | [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245) |
| [GeneXus Cognitive API - Process procedure](https://wiki.genexus.com/commwiki/wiki?41042) | [GeneXus Cognitive API - SentimentAnalysis procedure](https://wiki.genexus.com/commwiki/wiki?40184) | [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) | [GeneXus Cognitive API - Translate procedure](https://wiki.genexus.com/commwiki/wiki?40185) |
| [Model data type](https://wiki.genexus.com/commwiki/wiki?44240) | [Provider data type](https://wiki.genexus.com/commwiki/wiki?40197) | [SpeechToText procedure](https://wiki.genexus.com/commwiki/wiki?40169) | [TextToSpeech procedure](https://wiki.genexus.com/commwiki/wiki?40170) |

---
