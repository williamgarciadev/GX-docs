---
title: "OutputText data type"
source_id: 45364
source_url: https://wiki.genexus.com/commwiki/wiki?45364
genexus_version: "18"
---

# OutputText data type

Represents a text along with its confidence and additional data in the context of [GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167).

## [Members](#Members)

* **Text**: [Text, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40192)
* **Confidence**: [Confidence, GeneXusAI](https://wiki.genexus.com/commwiki/wiki?40189)
* **Info**: Collection -- Additional data on key-value pairs
  + ***Property***: VarChar(40)
  + ***Value***: VarChar(40)

## [Notes](#Notes)

* The property-value pairs of Info field represent the word sequence of Text field with the associated start/end time (in seconds) inferred from the speech.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **AI Tasks:** | [SpeechToText procedure](https://wiki.genexus.com/commwiki/wiki?40169) |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

## [Availability](#Availability)

This data type is available as of [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [SpeechToText procedure](https://wiki.genexus.com/commwiki/wiki?40169) |

---
