---
title: "OutputAnalysis data type"
source_id: 41043
source_url: https://wiki.genexus.com/commwiki/wiki?41043
genexus_version: "18"
---

# OutputAnalysis data type

Represent a set of features analyzed in a video.

## [Members](#Members)

* **Completed**: Boolean
* **Progress**: [Percentage, GeneXusAI.Video](https://wiki.genexus.com/commwiki/wiki?41274)
* **VideoId**: [VideoId, GeneXusAI.Video](https://wiki.genexus.com/commwiki/wiki?41109)
* **Speeches**: [OutputLabel, GeneXusAI (collection)](https://wiki.genexus.com/commwiki/wiki?40193)
* **Categories**: [OutputLabel, GeneXusAI (collection)](https://wiki.genexus.com/commwiki/wiki?40193)
* **Faces**: [OutputRegion, GeneXusAI (collection)](https://wiki.genexus.com/commwiki/wiki?40194)
* **OCRs**: [OutputRegion, GeneXusAI (collection)](https://wiki.genexus.com/commwiki/wiki?40194)
* **Sentiments**: [OutputScore, GeneXusAI (collection)](https://wiki.genexus.com/commwiki/wiki?41044)

## [Example](#Example)

Taking the following video fragment from [this conference](https://www.youtube.com/watch?v=v2kGhwE__po):

[[GeneXusAI - OutputAnalysis - Example](https://wiki.genexus.com/commwiki/wiki?41133,,)]( ./afiledownload?41133,2 )

**[GeneXusAI - OutputAnalysis - Example](https://wiki.genexus.com/commwiki/wiki?41133,,)**

**0:00/0:00**

The OutputAnalysis, for Microsoft, will be:

|  |  |
| --- | --- |
| **Completed** | true |
| **Progress** | 100 |
| **VideoId** | {your\_video\_id} |
| **Speeches** | **.item(1)** |  |  | | --- | --- | | **label** | Traducción y próximamente mostrenco sino también otro módulo para el tratamiento de video. | | **confidence** | 0.7496 | | **Info** | [ {"property": "START-1","value": "0:00:00"} , {"property": "END-1","value": "0:00:03.71"} ] | |
| **Categories** | **.item(1)** |  |  | | --- | --- | | **label** | tennis | | **confidence** | 0.9916 | | **Info** | [ {"property": "START-1","value": "0:00:00"} , {"property": "END-1","value": "0:00:01.068"} ] |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **.item(2)** |  |  | | --- | --- | | **label** | person | | **confidence** | 0.9818 | | **Info** | [ {"property": "START-1","value": "0:00:00"} , {"property": "END-1","value": "0:00:01.068"} ] | | ... |  | | |
| **Sentiments** | **.item(1)** |  |  | | --- | --- | | **score** | 0.5779 | | **Info** | [ {"property": "START-1","value": "0:00:00"} , {"property": "END-1","value": "0:00:03.741"} ] | |
| **Faces** | **.item(1)** |  |  | | --- | --- | | **label** | Unknown #1 | | **confidence** | 0.0000 | | **top** | 0 | | **left** | 0 | | **width** | 0 | | **height** | 0 | | **Info** | [ {"property": "START-1","value": "0:00:00"} , {"property": "END-1","value": "0:00:00.5"} ,  {"property": "thumbnail","value": "\_\_url\_\_"} ]  where "\_\_url\_\_" is an URL to the following image: | |
| **OCRs** | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | |  | **.item(1)** |  |  | | --- | --- | | **label** | SpeechToText | | **confidence** | 0.9916 | | **top** | 0 | | **left** | 0 | | **width** | 0 | | **height** | 0 | | **Info** | [ {"property": "START-1","value": "0:00:00.934"} , {"property": "END-1","value": "0:00:02.369"} ] | | ... |  | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | |  | **.item(14)** |  |  | | --- | --- | | **label** | Video | | **confidence** | 0.9661 | | **top** | 0 | | **left** | 0 | | **width** | 0 | | **height** | 0 | | **Info** | [ {"property": "START-1","value": "0:00:00.934"} , {"property": "END-1","value": "0:00:02.369"} ] | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | |  | **.item(15)** |  |  | | --- | --- | | **label** | Coming soon... | | **confidence** | 0.5185 | | **top** | 0 | | **left** | 0 | | **width** | 0 | | **height** | 0 | | **Info** | [ {"property": "START-1","value": "0:00:00.934"} , {"property": "END-1","value": "0:00:02.369"} ] | | |  |  | |

## [Notes](#Notes)

* The **'Info' field**, present on each member of the structured data type, has the timestamps where the recognition starts and/or ends.  
  - If the recognition is instantaneous, only 'START' key is present.  
  - If the recognition is lasting, both 'START' and 'END' keys are present.  
  - In both cases, the keys 'START' (and 'END') could be suffixed by an index in case there are multiple recognitions for the same item.  
  For instance, in the most general case, 'START-1'/'END-1' keys indicates the first recognition, 'START-2'/'END-2' key for the second recognition, and so on.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **AI Tasks:** | [GeneXus Cognitive API - Analyze procedure](https://wiki.genexus.com/commwiki/wiki?41041) |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

## [Availability](#Availability)

This data type is available as of [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/wiki?40782,,).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167) | [GeneXus Cognitive API - Analyze procedure](https://wiki.genexus.com/commwiki/wiki?41041) |

---
