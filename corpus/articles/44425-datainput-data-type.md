---
title: "DataInput data type"
source_id: 44425
source_url: https://wiki.genexus.com/commwiki/wiki?44425
genexus_version: "18"
---

# DataInput data type

Represents a single input data in the context of the [GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) for custom models.

## [Members](#Members)

* **Features** (collection) -- Set of features (columns) as strings
  + **Value**: VarChar(512)

## [Notes](#Notes)

* When it is used in [Data data type](https://wiki.genexus.com/commwiki/wiki?44237), it represents an input row for a single data of your data-set.
* The value of Features[k] represents the k-value (o k-column) of a single input data (row).
* Features' field count must be equal to the [Definition Features' field](https://wiki.genexus.com/commwiki/wiki?44427) count.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **AI Tasks:** | [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245) |
| **Data Types:** | [Data data type](https://wiki.genexus.com/commwiki/wiki?44237) |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

## [Availability](#Availability)

This data type is available as of [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).


|  |
| --- |
| **Backlinks** |
| [DataInputType domain](https://wiki.genexus.com/commwiki/wiki?44423) | [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245) |

---
