---
title: "Image Gallery Control"
source_id: 5221
source_url: https://wiki.genexus.com/commwiki/wiki?5221
genexus_version: "18"
---

# Image Gallery Control

Provides an elegant way of displaying pictures and interacting with them.

It basically offers two different ways of displaying pictures, using either a Table or a Slider view. The "Table view" is based on [Lightbox Image Viewer 2.03](http://www.dynamicdrive.com/dynamicindex4/lightbox2/index.htm), which is an unobtrusive script used to overlay images, while the "Slider view" is based on [FrogJS](http://www.dynamicdrive.com/dynamicindex4/frogjs/index.htm), which is a sequential image gallery. Both controls were extended to manage Ajax events that are handled from GeneXus code(server-side) allowing you to work with the currently selected image.

|  |  |
| --- | --- |
|  |  |

### [Using the control](#Using+the+control)

The control loads an SDT called ImagesData, where you can specify the images (collection) that will be displayed by the control. Each item (ImagesData.ImagesDataItem) of the ImagesData collection has the following properties:

* Id: This is an internal ID useful for identifying the image when handling the ImageChanged event control.
* Thumbnail (optional): This is the URL of the thumbnail image.
* Image: this is the URL of the full-size image.
* Caption: This is a text that will be displayed under the picture.

Although the thumbnail is optional, when using the Slider view it is recommended that a thumbnail be provided, as this will achieve a better transition between images.

```
Sub 'ImageGalleryMenuSample'
   &imagesDataItem.Id = "1"
   &imagesDataItem.Thumbnail = "ImageGallery/sampleImages/imageth1.jpg"
   &imagesDataItem.Image = "ImageGallery/sampleImages/image1.jpg"
   &imagesDataItem.Caption = "Description 1"
   &imagesData.Add(&imagesDataItem)
   &imagesDataItem = new()
   &imagesDataItem.Id = "2"
   &imagesDataItem.Thumbnail = "ImageGallery/sampleImages/imageth2.jpg"
   &imagesDataItem.Image = "ImageGallery/sampleImages/image2.jpg"
   &imagesDataItem.Caption = "Description 2"
   &imagesData.Add(&imagesDataItem)
   &imagesDataItem = new()
   &imagesDataItem.Id = "3"
   &imagesDataItem.Thumbnail = "ImageGallery/sampleImages/imageth3.jpg"
   &imagesDataItem.Image = "ImageGallery/sampleImages/image3.jpg"
   &imagesDataItem.Caption = "Description 3"
   &imagesData.Add(&imagesDataItem)
EndSub
```

### [Control properties](#Control+properties)

|  |  |
| --- | --- |
| Width | Sets the control's width. |
| Height | Sets the control's height. |
| Type | Table / Slider. Sets whether images will be displayed using the table view or the slider view. |
| ***Appearance*** |  |
| LoadingImage | Sets the image that will be displayed while loading an image. |
| ThumbnailWidth | The width of the thumbnails. Applies only to ImagesDataItem, which doesn't specify a thumbnail. |
| ThumbnailHeight | The height of the thumbnails. Applies only to ImagesDataItem, which doesn't specify a thumbnail. |
| ***Appearance/Table*** | Applies only to the table view. |
| Rows | Sets the number of rows in the table. When set to 0, the control will create as many rows as necessary in order to display all the images loaded in the SDT. |
| Columns | Sets the number of columns in the table. |
| BorderWidth | Sets the table's width. |
| BorderColor | Sets the color of the table's border. |
| CellSpace | Sets the space of the table's cells. |
| CellPad | Sets the table's cell padding. |
| ResizeSpeed | Sets the speed in which images are resized. |
| ***DataBindings*** |  |
| ImagesData | ImagesDATA SDT with all the images to be displayed. |

### [Control Events](#Control+Events)

Every time you change the current image (either in the table view or in the slider), you trigger an event to the server that allows you to know which image is currently being displayed. This can be accomplished using the SelectedImageId as follows:

```
Event imageGallery1.ImageChanged
     textBlock.Caption = "The current image is " + imageGallery1.SelectedImageId 
EndEvent
```

As you can see, the SelectedImageId holds the id of the image currently being displayed. When using the slider, you can also use the SelectedImageId from other events to change the current image:

```
Event TextblockPrevious.Click
      &num = val(imageGallery1.SelectedImageId)
      &num-=1
      imageGallery1.SelectedImageId = &num.ToString() 
EndEvent
```

Event TextblockNext.Click       &num = val(imageGallery1.SelectedImageId)       &num+=1       imageGallery1.SelectedImageId = &num.ToString()   EndEvent

The code above forces the slider ImageGallery to show either the next or previous image in the sequence.

### [Considerations](#Considerations)

This User control is not compatible with [Responsive Web Design](https://wiki.genexus.com/commwiki/wiki?25135).


|  |
| --- |
| **Backlinks** |
| [Category:Common Controls](https://wiki.genexus.com/commwiki/wiki?5928) |

---
