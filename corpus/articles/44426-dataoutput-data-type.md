---
title: "DataOutput data type"
source_id: 44426
source_url: https://wiki.genexus.com/commwiki/wiki?44426
genexus_version: "18"
---

# DataOutput data type

Represents the output data in the data-set in the context of the [GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) for custom models.

## [Members](#Members)

* **Label**: [Label, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40191)
* **Region** (structure) -- Describes a bounding-box
  + **Top**: Numeric(4.0)
  + **Left**: Numeric(4.0)
  + **Width**: Numeric(4.0)
  + **Height**: Numeric(4.0)
* **Numeric**: Numeric(18.5)
* **Confidence**: [Confidence, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40189) (read-only)

## [Notes](#Notes)

* When it is used in [Data data type](https://wiki.genexus.com/commwiki/wiki?44237), it represents the output row for a single data in your data-set.
* The value of Features[k] represents the k-value (o k-column) of a single input data (row).
* Features' field count must be equal to the [Definition Features' field](https://wiki.genexus.com/commwiki/wiki?44427) count.
* When it is used as the output of [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245), Region's fields will be -1 if no region was returned.

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
| [DataOutputType domain](https://wiki.genexus.com/commwiki/wiki?44424) | [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245) |

---
