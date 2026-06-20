---
title: "Provider data type"
source_id: 40197
source_url: https://wiki.genexus.com/commwiki/wiki?40197
genexus_version: "18"
---

# Provider data type

Used for setting a specific provider, along with its properties, in the context of [GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167).

## [Members](#Members)

* **Name**: VarChar(40)
* **Type**: [ProviderType, GeneXusAI.Configuration](https://wiki.genexus.com/commwiki/wiki?40195)
* **Property**: Collection -- Aditional data on key-value pairs
  + ***Key***: VarChar(64)
  + ***Value***: VarChar(128)

## [Notes](#Notes)

* [PropertyKey domain](https://wiki.genexus.com/commwiki/wiki?40196) can be helpful for defining the Key field in the Provider.Property collection.
* Must be fully set, including Name, Type, and its appropriate Properties. Otherwise, the task will fail.
* When your provider requires a file as a property (e.g., Google's json service-account), you can indicate either the content string or the filepath.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **AI Tasks:** | All |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

## [Availability](#Availability)

This data type is available as of [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Analyze procedure](https://wiki.genexus.com/commwiki/wiki?41041) | [GeneXus Cognitive API - Check procedure](https://wiki.genexus.com/commwiki/wiki?44242) |
| [GeneXus Cognitive API - Classify procedure](https://wiki.genexus.com/commwiki/wiki?40171) | [GeneXus Cognitive API - Delete procedure](https://wiki.genexus.com/commwiki/wiki?44243) | [GeneXus Cognitive API - Deploy procedure](https://wiki.genexus.com/commwiki/wiki?44247) | [GeneXus Cognitive API - DetectFaces procedure](https://wiki.genexus.com/commwiki/wiki?40177) |
| [GeneXus Cognitive API - DetectLanguage procedure](https://wiki.genexus.com/commwiki/wiki?40181) | [GeneXus Cognitive API - DetectObjects procedure](https://wiki.genexus.com/commwiki/wiki?40178) | [GeneXus Cognitive API - DetectScene procedure](https://wiki.genexus.com/commwiki/wiki?40179) | [GeneXus Cognitive API - Error handling and codes](https://wiki.genexus.com/commwiki/wiki?40188) |
| [GeneXus Cognitive API - Evaluate procedure](https://wiki.genexus.com/commwiki/wiki?44244) | [GeneXus Cognitive API - ExtractEntities procedure](https://wiki.genexus.com/commwiki/wiki?40182) | [GeneXus Cognitive API - KeyPhrases procedure](https://wiki.genexus.com/commwiki/wiki?40183) |
| [GeneXus Cognitive API - OCR procedure](https://wiki.genexus.com/commwiki/wiki?40180) | [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245) | [GeneXus Cognitive API - Process procedure](https://wiki.genexus.com/commwiki/wiki?41042) | [GeneXus Cognitive API - SentimentAnalysis procedure](https://wiki.genexus.com/commwiki/wiki?40184) |
| [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) | [GeneXus Cognitive API - Translate procedure](https://wiki.genexus.com/commwiki/wiki?40185) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [HowTo: Get credentials from a cloud provider for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40204) |
| [Model data type](https://wiki.genexus.com/commwiki/wiki?44240) | [PropertyKey domain](https://wiki.genexus.com/commwiki/wiki?40196) | [ProviderType domain](https://wiki.genexus.com/commwiki/wiki?40195) | [SpeechToText procedure](https://wiki.genexus.com/commwiki/wiki?40169) |
| [TextToSpeech procedure](https://wiki.genexus.com/commwiki/wiki?40170) |

---
