---
title: "GeneXus SDK for SAP Leonardo: Product Text Classification"
source_id: 41792
source_url: https://wiki.genexus.com/commwiki/wiki?41792
genexus_version: "18"
---

# GeneXus SDK for SAP Leonardo: Product Text Classification

The Product Text Classification service(API) allows you to classify each product to relevant categories based on its description.

## [How to use the Product Text Classification API](#How+to+use+the+Product+Text+Classification+API)

To use the Product Text Classification API you need to use the PostInferenceSync procedure

```
GeneXusSAPLeonardo.ProductTextClassification.PostInferenceSync(&files,&Text,&Response,&Message,&IsSuccess)
```

Where:

* &files: This parameter is required only if the parameter **&Text**is null or empty. The file to be uploaded.
  + Archive file - *one file with the format ‘\*/zip’ without folder hierarchy containing the text files to be classified.*
* &Text: This parameter is required only if the parameter **&files**is null or empty. The text to be classified.
* &Response: is a [Structured Data Type(SDT)](https://wiki.genexus.com/commwiki/wiki?1878,,) that contains the result.
* &Message: is a [Message](https://wiki.genexus.com/commwiki/wiki?40335) that contains information about the request.
* &IsSuccess: is a [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) that is true if no errors were encountered.

**&Response SDT Structure**

**`[imagen omitida: wiki id 41793]`**

[Read more about the Product Text Classification API.](https://api.sap.com/api/product_text_classification_api/overview)


|  |
| --- |
| **Backlinks** |
| [GeneXus SDK for SAP Leonardo: Functional Description](https://wiki.genexus.com/commwiki/wiki?41181) |

---
