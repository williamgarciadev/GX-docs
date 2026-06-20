---
title: "GeneXus SDK for SAP Leonardo: Scene Text Recognition"
source_id: 41774
source_url: https://wiki.genexus.com/commwiki/wiki?41774
genexus_version: "18"
---

# GeneXus SDK for SAP Leonardo: Scene Text Recognition

Scene Text Recognition API allows you to localize and extract text from natural images and scenes.

## [How to use the Scene Text Recognition API](#How+to+use+the+Scene+Text+Recognition+API)

The Scene Text Recognition API allows you to extrapolate text from natural sceneries. To use this you have to use the POSTInferenceSync procedure.

```
GeneXusSAPLeonardo.SceneTextRecognition.POSTInferenceSync(&SceneTextFile,&OAuth2.0_credentials, &ResponseOK, &ResponseError, &Message)
```

Where:

* &SceneTextFile: the image to be analyzed
  + Image types allowed jpg, jpe, jpeg, png.
  + Dimension size: equal or greater to 64 pixels.
* &OAuth2.0\_credentials:
* &ResponseOK: is a [Structured Data Type(SDT)](https://wiki.genexus.com/commwiki/wiki?1878,,) that contains the result if no errors are found.
* &ResponseError: is a [SDT](https://wiki.genexus.com/commwiki/wiki?1878,,) that contains the error code, the error message, and some details if an error was found.
* &Message: is a [Message](https://wiki.genexus.com/commwiki/wiki?40335) that contains information about the request.

**&ResponseOK SDT Composition**

`[imagen omitida: wiki id 41786]`

**&ResponseError SDT composition**

`[imagen omitida: wiki id 41784]`

[Read more about the Scene Text Recognition API.](https://api.sap.com/api/scene_text_recognition_api/overview)


|  |
| --- |
| **Backlinks** |
| [GeneXus SDK for SAP Leonardo: Functional Description](https://wiki.genexus.com/commwiki/wiki?41181) |

---
