---
title: "Image manipulation API (GeneXus 18 Upgrade 5 or prior)"
source_id: 55714
source_url: https://wiki.genexus.com/commwiki/wiki?55714
genexus_version: "18"
---

# Image manipulation API (GeneXus 18 Upgrade 5 or prior)

The task of [image](https://wiki.genexus.com/commwiki/wiki?15204) manipulation is quite common in applications that handle images. Common actions include: resizing, scaling, rotating, cropping, flipping horizontally and vertically, etc.

To allow the performance of such actions on images, GeneXus has added certain functions to the Image data type.

## [**Properties**](#Properties)

### [**ImageWidth:** Numeric](#ImageWidth%3A+Numeric)

Read-only property. Returns the image width in pixels.

```
&width = &image.ImageWidth
```

### [**ImageHeight:** Numeric](#ImageHeight%3A+Numeric)

Read-only property. Returns the image height in pixels.

```
&height = &image.ImageHeight
```

### [**FileSize:** Numeric](#FileSize%3A+Numeric)

Read-only property. Returns the image's file size in bytes.

```
&fileSize = &image.FileSize
```

## [**Methods**](#Methods)

The following methods do not modify the original image, they always return a new image with the modifications.

### [**Resize**](#Resize)

Returns a new image by resizing the original image.

Parameters:

* **Width**: Numeric - width of the new image,
* **Height**: Numeric - height of the new image,
* **KeepAspect**: Boolean, when set to **True,** the image is resized using "fill keeping aspect". Otherwise, "fill" is used.

```
&resizedImage = &image.Resize(100, 100, true)
```

### [**Scale**](#Scale)

Returns a new image by scaling the original image to the specified percentage.

Parameters:

* **Percentage**: Numeric.

```
&scaledImage = &image.Scale(80)
```

### [**Rotate**](#Rotate)

Returns a new image by rotating the original image in the specified angle. Valid angles are 90, 180, and 270 degrees; other values are ignored.

Parameters:

* **Angle**: Numeric.

```
&rotatedImage = &image.Rotate(90)
```

### [**Crop**](#Crop)

Returns a new image by cropping a portion of the original image. The dimensions of the new image are determined from the square indicated by the parameters.

Parameters:

* **Left**: Numeric - left coordinate in pixels where the cropping begins.
* **Top**: Numeric - top coordinate in pixels where the cropping begins.
* **Width**: Numeric - width of the new image in pixels.
* **Height**: Numeric - height of the new image in pixels.

```
&croppedImage = &image.Crop(0, 0, 50, 50)
```

### [**FlipHorizontally**](#FlipHorizontally)

Returns a new image from the original image rotated horizontally.

```
&hFlippedImage = &image.FlipHorizontally()
```

### [**FlipVertically**](#FlipVertically)

Returns a new image from the original image rotated vertically.

```
&vFlippedImage = &image.FlipVertically()
```

## [**Availability**](#Availability+)

These properties and methods are available:

* For iOS since [GeneXus 16 upgrade 2](https://wiki.genexus.com/commwiki/wiki?41525,,).
* For Android since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,).
* For Web since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,).
* For Angular since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).

## [**Scope**](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550) |

## [**See also**](#See+also+)

[Image data type](https://wiki.genexus.com/commwiki/wiki?15204)
