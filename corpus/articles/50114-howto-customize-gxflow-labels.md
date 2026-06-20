---
title: "HowTo: Customize GXflow labels"
source_id: 50114
source_url: https://wiki.genexus.com/commwiki/wiki?50114
genexus_version: "18"
---

# HowTo: Customize GXflow labels

This document explains how to customize GXflow labels and provides a brief overview about it.

The GXflow backoffice web is translated to Arabic, English, Italian, Japanese, Portuguese, Simplified and Traditional Chinese, and Spanish.

If you want to use any of these languages, you must configure the [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) in your generation environment with the value Run-time and also enable in the Localization tree all the languages you need.

`[imagen omitida: wiki id 50115]`

If you want to translate to another language or change some of GeneXus's translation, you can open the object Language for the specific language you want and filter by the text GXWF and uncheck the filter “Show only user messages” to locate the required label.

If you want to translate to a new whole language, for example, French, you can save as the English language to initialize all the labels and then translate to French.

`[imagen omitida: wiki id 50116]`

After you activate a new Language in your [KB](https://wiki.genexus.com/commwiki/wiki?2428) you need to do a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691) and a Business Process Deploy to enable the new language in GXflow metadata.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXFlow Client Default Language Settings](https://wiki.genexus.com/commwiki/wiki?10110) | [HowTo: Create a language selector for the GXflow Client](https://wiki.genexus.com/commwiki/wiki?53727) |

---
