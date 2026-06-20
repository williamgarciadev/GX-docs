---
title: "GeneXus SDK for SAP Leonardo: Image Feature Extraction"
source_id: 41789
source_url: https://wiki.genexus.com/commwiki/wiki?41789
genexus_version: "18"
---

# GeneXus SDK for SAP Leonardo: Image Feature Extraction

The Image Feature Extraction service(API) allows you to extract feature vectors for any given image for comparison, information retrieval, clustering, or further processing.

## [How to use the Image Feature Extraction API](#How+to+use+the+Image+Feature+Extraction+API)

To use this API you have to use the POSTInferenceSync procedure

```
GeneXusSAPLeonardo.ImageFeatureExtraction.POSTInferenceSync(&File,&Authorization,&Oauth2_ClientCredentials,&ResponseOK,&ResponseError,&Messages,&IsSuccess)
```

Where:

* &File: is the file to be analyzed.
  + Archive file: zip, tar, gz, tgz.
  + Image file: jpg, jpe, jpeg, png, gif, bmp, tif, tiff.
* &Authorization: is the OAuth2 token to be used for Authentication if needed.
* &Oauth2\_ClientCredentials
* &ResponseOK:  is a [Structured Data Type(SDT)](https://wiki.genexus.com/commwiki/wiki?1878,,) that contains the result if no errors are found.
* &ResponseError: is a [SDT](https://wiki.genexus.com/commwiki/wiki?1878,,) that contains the error code, the error message, and some details if an error was found.
* &Messages: is a [Message](https://wiki.genexus.com/commwiki/wiki?40335) that contains information about the request.
* &IsSuccess: is a [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) that is true if no errors were encountered.

If you have your own trained model you can use the POSTInferenceSyncPrivateModel

```
GXSAPLeonardo.ImageFeatureExtraction.POSTInferenceSyncPrivateModel(&ModelName,&Version,&File,&Authorization,&Oauth2_ClientCredentials,&ResponseOK,&ResponseError,&Messages,&IsSuccess)
```

Where

* &ModelName: is the name of the trained model.
* &Version

And the other variables are the same as the ones of POSTInferenceSync.

**&ResponseOK SDT Composition**

`[imagen omitida: wiki id 41820]`

**&ResponseError SDT composition**

`[imagen omitida: wiki id 41821]`

[Read more about the Image Feature Extraction API.](https://api.sap.com/api/img_feature_extraction_api/resource)


|  |
| --- |
| **Backlinks** |
| [GeneXus SDK for SAP Leonardo: Functional Description](https://wiki.genexus.com/commwiki/wiki?41181) |

---
