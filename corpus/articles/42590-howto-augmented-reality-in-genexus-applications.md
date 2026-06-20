---
title: "HowTo: Augmented Reality in GeneXus applications"
source_id: 42590
source_url: https://wiki.genexus.com/commwiki/wiki?42590
genexus_version: "18"
---

# HowTo: Augmented Reality in GeneXus applications

**Augmented Reality** (AR) is an enhanced version of reality where live views of physical real-world environments are augmented with superimposed computer-generated images over a user's view of the real-world, thus enhancing the current perception of reality.

### [Scenario](#Scenario)

Show a 3D model of some object and how it would fit to a place (augment the given reality).

To cover this scenario, the following API is available in GeneXus:

### [ARPreview external object](#ARPreview+external+object)

#### **IsAvailable property**

|  |  |
| --- | --- |
| **Type** | Boolean |
| **Description** | Indicates if the device supports the 3D models |

#### **PreviewObject method**

|  |  |
| --- | --- |
| **Description** | Displays the 3D Model |
| **Parameters** | 3D object: [URL domain](https://wiki.genexus.com/commwiki/wiki?15668) |
| **Returns** | None |

The file URL can be a local URL (i.e. [offline applications](https://wiki.genexus.com/commwiki/wiki?22237)), or a remote (http/https) URL. When using remote URLs, the content is downloaded before displaying it.

#### **Supported formats of 3D object**

|  |  |
| --- | --- |
| [**Apple**](https://wiki.genexus.com/commwiki/wiki?14917) | [USDZ](https://graphics.pixar.com/usd/docs/Usdz-File-Format-Specification.html) |
| [**Android**](https://wiki.genexus.com/commwiki/wiki?14453) | 3D assets files (glTF), Sceneform binary assets (SFB) |

These file formats group all the information needed to represent a 3D model. There are several sites with models available to download, for example, [AR Quick Look Gallery](https://developer.apple.com/arkit/gallery/) or <https://poly.google.com/>

### [Sample Code](#Sample+Code)

```
Event '3D'
   &URL3D = !"https://developer.apple.com/augmented-reality/quick-look/models/wateringcan/wateringcan.usdz"
   if ARPreview.IsAvailable // Check if device supports 3D models
      ARPreview.PreviewObject(&URL3D) // Display the 3D model of the URL
   else
      msg("Your device doesn't support Augmented Reality")
   endif
Endevent
```

### [Showtime!](#Showtime%21)

`[imagen omitida: wiki id 42597]`

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,).

### [Considerations](#Considerations)

For
[Apple](https://wiki.genexus.com/commwiki/wiki?14917), not all 3D models are suitable for this. If a message like "Preview Universal Scene Description (Mobile)" appears in runtime, refer to [Adding visual effects in AR Quick look](https://developer.apple.com/documentation/arkit/arkit_in_ios/adding_visual_effects_in_ar_quick_look_and_realitykit).


|  |
| --- |
| **Backlinks** |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) |
| [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
