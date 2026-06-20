---
title: "Model data type"
source_id: 44240
source_url: https://wiki.genexus.com/commwiki/wiki?44240
genexus_version: "18"
---

# Model data type

Represents a trained model in the context of the [GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) for custom models.

## [Members](#Members)

* **Id**: VarChar(256)
* **Version**: VarChar(64)
* **Dataset**: VarChar(512) -- Filepath to CSV file with dataset summarize.
* **Type**: [DataOutputType, GeneXusAI.Custom](https://wiki.genexus.com/commwiki/wiki?44424)

## [Notes](#Notes)

* This data type is used as input of every task in the Custom model except for the [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) where this data type is the output.
* The fields' value of this data type can be used as Properties of the [Provider data type](https://wiki.genexus.com/commwiki/wiki?40197) in order to use a custom model in a predefined GeneXusAI's tasks (e.g. in [GeneXus Cognitive API - Classify procedure](https://wiki.genexus.com/commwiki/wiki?40171) instead of using [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245)). In this case, you should use [ProeprtyKey.ModelId](https://wiki.genexus.com/commwiki/wiki?40196) and [ProeprtyKey.ModelVersion](https://wiki.genexus.com/commwiki/wiki?40196) to set the properties' values.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **AI Tasks:** | [GeneXus Cognitive API - Check procedure](https://wiki.genexus.com/commwiki/wiki?44242), [GeneXus Cognitive API - Delete procedure](https://wiki.genexus.com/commwiki/wiki?44243), [GeneXus Cognitive API - Deploy procedure](https://wiki.genexus.com/commwiki/wiki?44247), [GeneXus Cognitive API - Evaluate procedure](https://wiki.genexus.com/commwiki/wiki?44244), [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245), [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

## [Availability](#Availability)

This data type is available as of [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Check procedure](https://wiki.genexus.com/commwiki/wiki?44242) | [GeneXus Cognitive API - Delete procedure](https://wiki.genexus.com/commwiki/wiki?44243) |
| [GeneXus Cognitive API - Deploy procedure](https://wiki.genexus.com/commwiki/wiki?44247) | [GeneXus Cognitive API - Evaluate procedure](https://wiki.genexus.com/commwiki/wiki?44244) | [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245) | [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) |
| [Measure data type](https://wiki.genexus.com/commwiki/wiki?44239) |

---
