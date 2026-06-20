---
title: "GeneXus SDK for SAP Leonardo: Language Detection"
source_id: 41808
source_url: https://wiki.genexus.com/commwiki/wiki?41808
genexus_version: "18"
---

# GeneXus SDK for SAP Leonardo: Language Detection

The Language Detection service(API) allows you to detect the language of any given string of text data.

## [How to use the Language Detection API](#How+to+use+the+Language+Detection+API)

To use the Language Detection API you have to use PostUsingPOST procedure.

```
GeneXusSAPLeonardo.LanguageDetection.PostUsingPOST(&textToTranslate, &CustomDetectedLanguage, &Message, &IsSuccess)
```

Where:

* &textToTranslate: is a [Structured Data Type(SDT)](https://wiki.genexus.com/commwiki/wiki?1878,,) that contains the text for which the language needs to be detected.
* &CustomDetectedLanguage: is a [SDT](https://wiki.genexus.com/commwiki/wiki?1878,,) that contains the detected language code and string and also the confidence if no errors were found.
* &Message: is a [Message](https://wiki.genexus.com/commwiki/wiki?40335) that contains information about the request.
* &IsSuccess: is a [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) that is true if no errors were encountered.

**&textToTranslate****SDT Composition**

`[imagen omitida: wiki id 41809]`

**&CustomDetectedLanguage SDT Composition**

`[imagen omitida: wiki id 54531]`

[Read more about the Language Detection API.](https://api.sap.com/api/language_detection_api/overview)


|  |
| --- |
| **Backlinks** |
| [GeneXus SDK for SAP Leonardo: Functional Description](https://wiki.genexus.com/commwiki/wiki?41181) |

---
