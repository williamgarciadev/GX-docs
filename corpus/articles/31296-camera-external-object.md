---
title: "Camera external object"
source_id: 31296
source_url: https://wiki.genexus.com/commwiki/wiki?31296
genexus_version: "18"
---

# Camera external object

The Camera external object enables you to programmatically take photos and record videos using the device's camera.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

It does not have any.

## [Methods](#Methods)

### [TakePhoto method](#TakePhoto+method)

Takes a photo using the device's camera.

|  |  |
| --- | --- |
| **Return value** | [Image](https://wiki.genexus.com/commwiki/wiki?15204) |
| **Parameters** | None |

### [RecordVideo method](#RecordVideo+method)

Records a video using the device's camera. You can indicate (optionally)  the quality that the video will be recorded with, affecting the file size and transfer time over the network. If this parameter is not sent, the value used is the medium.

|  |  |
| --- | --- |
| **Return value** | [Video](https://wiki.genexus.com/commwiki/wiki?16608) |
| **Parameters** | [ VideoQuality ] based on the [CameraAPIQuality data type](https://wiki.genexus.com/commwiki/wiki?27012) |

## [Events](#Events)

It does not have any

## [Samples](#Samples)

```
Event 'RecordVideo'
  Composite
    &Video = Camera.RecordVideo()
    UploadVideo(&Video)
  EndComposite
EndEvent
```

```
Event 'TakePhoto'
  Composite
    &Image = Camera.TakePhoto()
    SaveImage(&Image)
  EndComposite
EndEvent
```

## [Considerations](#Considerations)

Android apps will ask for permission when they need it. For example, instead of giving an app access to your camera when you install it, you’ll be prompted the first time the app wants to access your camera.

`[imagen omitida: wiki id 42867]`

You can change the permissions that apps can access in the main Settings app on your device at any time. Keep in mind turning off permissions may cause apps on your device to lose functionality.

Check for more information [here](https://support.google.com/googleplay/answer/6270602?hl=en).

## [Scope](#Scope)

**Generators:**[Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

## [Availability](#Availability)

TakePhoto and RecordVideo methods are available for Angular as of [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396)

## [See also](#See+also)

[HowTo: Use Camera external object in GeneXus](https://wiki.genexus.com/commwiki/wiki?31298)


|  |
| --- |
| **Backlinks** |
| [Camera external object (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53919) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) |
| [HowTo: Use Camera external object in GeneXus](https://wiki.genexus.com/commwiki/wiki?31298) | [Purpose Strings properties group](https://wiki.genexus.com/commwiki/wiki?32755) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
