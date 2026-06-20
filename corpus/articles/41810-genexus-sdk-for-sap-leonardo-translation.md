---
title: "GeneXus SDK for SAP Leonardo: Translation"
source_id: 41810
source_url: https://wiki.genexus.com/commwiki/wiki?41810
genexus_version: "18"
---

# GeneXus SDK for SAP Leonardo: Translation

The Translation service (API) allows you to translate multiple translation units from a source language into multiple target languages.

## [How to use the Translation API](#How+to+use+the+Translation+API)

To use the Translation API you have to use the Translation Procedure

```
GeneXusSAPLeonardo.Translation.Translation(&body, &TranslationResult, &Message, &IsSuccess)
```

Where:

* &body: is a [Structured Data Type(SDT)](https://wiki.genexus.com/commwiki/wiki?1878,,) that contains:
  + The source language of the text to be translated
  + A collection of target languages.
  + A collection of texts to be translated
* &TranslationResult: is a [SDT](https://wiki.genexus.com/commwiki/wiki?1878,,) that contains:
  + A collection of translated texts.
* &Message: is a [Message](https://wiki.genexus.com/commwiki/wiki?40335) that contains information about the request.
* &IsSuccess: is a [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) that is true if no errors were encountered.

**&body SDT composition**

`[imagen omitida: wiki id 41811]`

TextTranslationRequest SDT composition

`[imagen omitida: wiki id 41812]`

**&TranslationResult SDT composition**

**`[imagen omitida: wiki id 41813]`**

TextTranslationResult SDT composition

`[imagen omitida: wiki id 41814]`

TextTranslationTranslation SDT composition

`[imagen omitida: wiki id 41815]`

[Read more about the Translation API.](https://api.sap.com/api/translation_api/overview)


|  |
| --- |
| **Backlinks** |
| [GeneXus SDK for SAP Leonardo: Functional Description](https://wiki.genexus.com/commwiki/wiki?41181) |

---
