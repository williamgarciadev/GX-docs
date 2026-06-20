---
title: "DataOutputType domain"
source_id: 44424
source_url: https://wiki.genexus.com/commwiki/wiki?44424
genexus_version: "18"
---

# DataOutputType domain

Enumerated domain indicating a field of [DataOutput data type](https://wiki.genexus.com/commwiki/wiki?44426) in the context of [GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) for custom models.

## [Values](#Values)

|  |  |
| --- | --- |
| **Label** | The inference will be made on the Label field (e.g. a category). |
| **Region** | The inference will be made on the Label and Region fields (e.g. a face or object) |
| **Numeric** | The inference will be made on the Numeric field (e.g. a price in tabular model) |

## [Notes](#Notes)

* Note that the Confidence field is not considered in this domain because its value is read-only (you cannot predict confidence).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Data types:** | [DataOutput data type](https://wiki.genexus.com/commwiki/wiki?44426) |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

## [Availability](#Availability)

This domain is available as of [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).

## [See also](#See+also)

* [HowTo: Build a custom model for GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?43665)


|  |
| --- |
| **Backlinks** |
| [Definition data type](https://wiki.genexus.com/commwiki/wiki?44427) | [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [Model data type](https://wiki.genexus.com/commwiki/wiki?44240) |

---
