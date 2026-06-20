---
title: "GeneXus SDK for SAP Leonardo: Face Detection"
source_id: 41794
source_url: https://wiki.genexus.com/commwiki/wiki?41794
genexus_version: "18"
---

# GeneXus SDK for SAP Leonardo: Face Detection

The Face Detection service(API) detects faces in images and, if any, returns bounding box per face for every image.

## [How to use the Face Detection API](#How+to+use+the+Face+Detection+API)

To use the Face Detection API you have to use POSTInferenceSync procedure

```
GeneXusSAPLeonardo.FaceDetection.POSTInferenceSync(&File,&Oauth2_ClientCredentials, &ResponseOK, &ResponseError,&Message,&IsSuccess)
```

Where

* &File: is the file containing the image/images to analyze in order to search for faces.
  + Archive file: zip, tar, gz, tgz.
  + Image file: jpg, jpe, jpeg, png, gif, bmp.
* &Oauth2\_ClientCredentials
* &ResponseOK:  is a [Structured Data Type(SDT)](https://wiki.genexus.com/commwiki/wiki?1878,,) that contains the result if no errors are found.
* &ResponseError: is a [SDT](https://wiki.genexus.com/commwiki/wiki?1878,,) that contains the error code, the error message, and some details if an error was found.
* &Messages: is a [Message](https://wiki.genexus.com/commwiki/wiki?40335) that contains information about the request.
* &IsSuccess: is a [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) that is true if no errors were encountered.

**&ResponseOK SDT Composition**

`[imagen omitida: wiki id 41816]`

**&ResponseError SDT composition**

`[imagen omitida: wiki id 41817]`

[Read more about the Face Detection API.](https://api.sap.com/api/face_detection_api/overview)


|  |
| --- |
| **Backlinks** |
| [GeneXus SDK for SAP Leonardo: Functional Description](https://wiki.genexus.com/commwiki/wiki?41181) |

---
