---
title: "Data data type"
source_id: 44237
source_url: https://wiki.genexus.com/commwiki/wiki?44237
genexus_version: "18"
---

# Data data type

Describes an item of a data-set in the context of the [GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) for custom models.

## [Members](#Members)

* **Purpose**: [Purpose, GeneXusAI.Custom](https://wiki.genexus.com/commwiki/wiki?44234)
* **Input** -- Your input data
  + **Resource**: VarChar(512)
* **Output** -- The inference for your input data
  + **Label**: [Label, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40191) (mandatory for training)
  + **Region**
    - **Top**: Numeric(4.0-)
    - **Left**: Numeric(4.0-)
    - **Width**: Numeric(4.0-)
    - **Height**: Numeric(4.0-)

## [Notes](#Notes)

* The Region's subfields are negative where they are not available.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **AI Tasks:** | [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246), [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245) |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), , [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

## [Availability](#Availability)

This data type is available as of [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).


|  |
| --- |
| **Backlinks** |
| [DataInput data type](https://wiki.genexus.com/commwiki/wiki?44425) | [DataOutput data type](https://wiki.genexus.com/commwiki/wiki?44426) | [Definition data type](https://wiki.genexus.com/commwiki/wiki?44427) |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) | [Purpose domain](https://wiki.genexus.com/commwiki/wiki?44234) | [TDiff function](https://wiki.genexus.com/commwiki/wiki?8513) |

---
