---
title: "Silverlight Photo Gallery User Control"
source_id: 5707
source_url: https://wiki.genexus.com/commwiki/wiki?5707
genexus_version: "18"
---

# Silverlight Photo Gallery User Control

[Download here](http://marketplace.genexus.com/viewproduct.aspx?13)

`[imagen omitida: wiki id 5865]`

**Control Description**

The PhotoGallery control provides an elegant way of displaying and interacting with pictures using Silverlight technology.

The control was extended to manage Ajax events that are handled from GeneXus code (server side) allowing you to work with the currently selected image.

**Using the control**

The control loads an SDT called PhotoData where you can specify the photos (collection) that will be displayed by the control. Each item (PhotosData.PhotosDataItem) of the PhotosData collection has the following properties:

* Id: this is an internal ID useful for identifying the image when handling the control's PhotoChanged events
* Image: this is the url of the full-size image
* Description: this is a text that will be displayed under the picture

**Example**

```
PhotoData {
PhotoDataItem Input &i=1 to 16
{ Id = trim(&i.ToString())
Image = "PhotoGallery/sampleImages/photo" + trim(&i.ToString()) + ".jpg"
Description = "photo" + trim(&i.ToString()) 
} }
```

**Control properties**

|  |  |
| --- | --- |
| Width | Sets the width of the control |
| Height | Sets the height of the control |
| Title | Title of the PhotoGallery |
| SelectedPhotoId | ID of the Selected Photo |
| DataBindings |  |
| ImagesData | PhotosDATA SDT with all the images to be displayed. |

**Control Events**

Every time you change the current photo an event to the server is triggered, allowing you to know what image is currently being displayed. This can be accomplished using the SelectedPhotoId as follows:

```
Event photoGallery1.PhotoChanged
     textBlock.Caption = "Selected photo Id " + photoGallery1.SelectedPhotoId 
EndEvent
```

**To Install It**

Please visit: [Default Installation Instructions for User Controls](https://wiki.genexus.com/commwiki/wiki?5920).

Contact information

Please send feedback to: [acimas@genexus.com](mailto:acimas@genexus.com)
