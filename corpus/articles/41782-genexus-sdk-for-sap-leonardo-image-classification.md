---
title: "GeneXus SDK for SAP Leonardo: Image Classification"
source_id: 41782
source_url: https://wiki.genexus.com/commwiki/wiki?41782
genexus_version: "18"
---

# GeneXus SDK for SAP Leonardo: Image Classification

The Image Classification service allows you to classify images into a pre-defined set of categories or, in case of a customized model, your own set of categories.

## [How to use the Image Classification API](#How+to+use+the+Image+Classification+API)

To use the image classification API you have to use the POSTInferenceSync procedure

```
GXSAPLeonardo.ImageClassification.POSTInferenceSync(&ImageClassificationFile, &options, &Oauth2_ClientCredentials,&ResponseOk,&ResponseError,&ErrorOut, &Message, &IsSuccess)
```

Where:

* &ImageClassificationFile: is the file to be analyzed.
  + Image files: jpg, jpe, jpeg, png, gif, bmp, tif, tiff.
  + Archive files: zip, tar, gz, tgz.
* &options
* &Oauth2\_ClientCredentials
* &ResponseOk: is a [Structured Data Type(SDT)](https://wiki.genexus.com/commwiki/wiki?1878,,) that contains the result if no errors are found.
* &ResponseError:  is a [SDT](https://wiki.genexus.com/commwiki/wiki?1878,,) that contains the error code, the error message, and some details if an error was found.
* &ErrorOut
* &Message: is a [Message](https://wiki.genexus.com/commwiki/wiki?40335) that contains information about the request.
* &IsSuccess: is a [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) that is true if no errors were encountered.

**&ResponseOk SDT Composition**

`[imagen omitida: wiki id 41818]`

**&ResponseError SDT composition**

`[imagen omitida: wiki id 41819]`

[Read more about the Image Classification API.](https://api.sap.com/api/image_classification_api/resource)


|  |
| --- |
| **Backlinks** |
| [GeneXus SDK for SAP Leonardo: Functional Description](https://wiki.genexus.com/commwiki/wiki?41181) |

---
