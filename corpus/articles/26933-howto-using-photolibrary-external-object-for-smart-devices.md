---
title: "HowTo: Using PhotoLibrary external object for Smart Devices"
source_id: 26933
source_url: https://wiki.genexus.com/commwiki/wiki?26933
genexus_version: "18"
---

# HowTo: Using PhotoLibrary external object for Smart Devices

The [PhotoLibrary external object](https://wiki.genexus.com/commwiki/wiki?39397) enables you to interact with the photo gallery of the device.

As the [HowTo: Use Camera external object in GeneXus](https://wiki.genexus.com/commwiki/wiki?31298) enables an app to interact with the photo camera of the device, this API allows the application to save or get an image or a video from the native photo gallery. This article focuses on what this API does and gives an example of how to use it in a Smart Device application.

### Code Sample 1: Working with videos

Create the following [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)

#### [*Events*](#Events)

```
Event 'save'
    photoLibrary.SaveVideo(&CompanyPresentationVideo)
Endevent

Event 'Choose'
    &CompanyPresentationVideo = photolibrary.ChooseVideo()
Endevent
```

**Variables:** &CompanyPresentationVideo is based on [Video data type](https://wiki.genexus.com/commwiki/wiki?16608).

### [Code Sample 2: Working with images](#Code+Sample+2%3A+Working+with+images)

There are three cases of different types of images for which the save method can be used.

* To save an image from the DB (attribute)
* To save an image from an URL (ImageVariable.FromURL(url))
* To save an image just taken with the camera (CameraAPI)

Create the following [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).

#### [*Layout*](#Layout)

`[imagen omitida: wiki id 19328]`

#### [*Events*](#Events)

```
Event Refresh
    &saveToLibFromWeb.FromURL('https://encrypted-tbn3.google.com/images?q=tbn:ANd9GcQ8n7HS90TxDvT4TcEphGN_AOxgwaOtUJ1rgM7f1puDi7851pcG1Q')
EndEvent

Event 'GetFromLibrary'
    &getFromLibrary = PhotoLibrary.ChooseImage()
Endevent

Event 'saveFromURL'
    PhotoLibrary.Save(&saveToLibFromWeb)
Endevent
```

#### [*Variables*](#Variables)

&saveToLibFromWeb and &getFromLibrary are based on [Image data type](https://wiki.genexus.com/commwiki/wiki?15204)

#### [*Execution*](#Execution)

When the ChooseImage method is invoked:  
`[imagen omitida: wiki id 19329]`    `[imagen omitida: wiki id 19330]`    `[imagen omitida: wiki id 19331]`

The Save method has no UI interaction to show, but the result of the execution is the image of the url saved on the device's photo gallery.  
`[imagen omitida: wiki id 19332]`

### [See also](#See+also)

* [PhotoLibrary external object](https://wiki.genexus.com/commwiki/wiki?39397)


|  |
| --- |
| **Backlinks** |
| [PhotoLibrary external object](https://wiki.genexus.com/commwiki/wiki?39397) |

---
