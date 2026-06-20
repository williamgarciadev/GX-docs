---
title: "OutputRegion data type"
source_id: 40194
source_url: https://wiki.genexus.com/commwiki/wiki?40194
genexus_version: "18"
---

# OutputRegion data type

Represents a labeled confidence region in the context of [GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167).

A region is a rectangle area defined by its upper left corner (top-left coordinates) and its width/height values. It is said to be 'confidence labeled' because the region can be tagged and can indicate a confidence for it (along with the delimited region predicted itself). The region also admits extra information about the region, e.g. the estimated age of a person face region.

## [Members](#Members)

* **Label**: [Label, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40191)
* **Confidence**: [Confidence, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40189)
* **Top**: Numeric(8.0)
* **Left**: Numeric(8.0)
* **Height**: Numeric(8.0)
* **Width**: Numeric(8.0)
* **Info**: Collection -- Additional data on key-value pairs
  + ***Property***: VarChar(40)
  + ***Value***: VarChar(40)

## [Scope](#Scope)

|  |  |
| --- | --- |
| **AI Tasks:** | [GeneXus Cognitive API - DetectFaces procedure](https://wiki.genexus.com/commwiki/wiki?40177), [GeneXus Cognitive API - DetectObjects procedure](https://wiki.genexus.com/commwiki/wiki?40178), [GeneXus Cognitive API - OCR procedure](https://wiki.genexus.com/commwiki/wiki?40180), [GeneXus Cognitive API - Analyze procedure](https://wiki.genexus.com/commwiki/wiki?41041) |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

## [Availability](#Availability)

This data type is available as of [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - DetectFaces procedure](https://wiki.genexus.com/commwiki/wiki?40177) | [GeneXus Cognitive API - DetectObjects procedure](https://wiki.genexus.com/commwiki/wiki?40178) |
| [GeneXus Cognitive API - OCR procedure](https://wiki.genexus.com/commwiki/wiki?40180) | [OutputAnalysis data type](https://wiki.genexus.com/commwiki/wiki?41043) | [Sample: GeneXus Cognitive API proof of concept](https://wiki.genexus.com/commwiki/wiki?40853) |

---
