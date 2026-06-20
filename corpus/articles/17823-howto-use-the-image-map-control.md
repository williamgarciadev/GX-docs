---
title: "HowTo: Use the Image Map Control"
source_id: 17823
source_url: https://wiki.genexus.com/commwiki/wiki?17823
genexus_version: "18"
---

# HowTo: Use the Image Map Control

The Image Map control lets you display a background image with regions identified by its coordinates {x, y} and a size. Each defined region can have an image to display on the coordinates defined for it, with an indicated size. Each region corresponds to one item of the list (grid). When a region is selected, the default action associated with it will be run.

This control applies to the [Grid control](https://wiki.genexus.com/commwiki/wiki?24817).

Suppose you are interested in representing the parts of a car:

`[imagen omitida: wiki id 23148]`

Start by defining the following [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) with the Work With pattern applied.

```
TRNImageMap
{
       TRNImageMapId*          Id
       TRNImageMapX            Numeric(4.0)
       TRNImageMapY            Numeric(4.0)
       TRNImageMapSize         Numeric(4.0)
       TRNImageMapImage        Image
       TRNImageMapInfo         VarChar(200)
}
```

Before continuing with this example, you may need to understand how this control works.

As already mentioned, this control lets you display a background image with regions identified by its coordinates. The coordinates start ({o,o} coordinate) in the upper left corner of the background image; the X-axis is horizontal to the background image and extends to the right; the Y-axis is vertical to the background image and extends downwards.

So, when you create a new [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) you need to define at least the following four attributes, as shown in the image:

* **X coordinate:** This will represent the *x* coordinate of the region where it will have its left upper corner. In the Transaction of the example, this attribute is *TRNImageMapX* and its type must be Numeric.
* **Y coordinate:** This will represent the *y* coordinate of the region where it will have its left upper corner. In the Transaction of the example, this attribute is *TRNImageMapY* and its type must be Numeric.
* **Size:** This will represent the size of the region. For example, if you define coordinates {0,0} and a size of 100, the region will be represented by the square defined by the points {0,0} and {100,100}. In the Transaction of the example, this attribute is *TRNImageMapSize* and its type must be Numeric.
* **Image:** This will be used to display an Image as a layout background on the region defined by the *x* and *y* coordinates and of the size defined. In the Transaction of the example, this attribute is *TRNImageMapImage* and its type must be Image.

**Note**: The attribute *TRNImageMapInfo* is not necessary; it will be used in this example to show information about the region when it's selected.

Once the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974) has been applied, you need to enable the Image Map control on the grid. To do so, open the List section, select the grid and set the [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) to Image Map.

`[imagen omitida: wiki id 46526]`

This will enable some other properties, as seen in the previous image:

|  |  |
| --- | --- |
| **Image Map properties** | **Description** |
| Image | Used for selecting the background image (\*). |
| Horizontal Coordinate Attribute | This is the attribute that represents the x coordinate for the upper left corner of each region. |
| Vertical Coordinate Attribute | This is the attribute that represents the y coordinate for the upper left corner of each region. |
| Size Attribute | This is the attribute that represents the size of each region. |

### [Image Map methods (\*)](#Image+Map+methods+%28*%29)

### [Syntax](#Syntax)

*Grid1*.**SetBackGroundImage**(*Image*)

**Where:**

*Grid1*  
      Is the control name of the Image Map grid

*Image*  
      Is a variable or attribute of [Image data type](https://wiki.genexus.com/commwiki/wiki?15204)

Continuing with the example, set the properties as follows:

|  |  |
| --- | --- |
| Image | carOutline (This image must be in the KB) |
| Horizontal Coordinate Attribute | TRNImageMapX |
| Vertical Coordinate Attribute | TRNImageMapY |
| Size Attribute | TRNImageMapSize |

Then, insert in the Grid's table, the image attribute that will be displayed as the background for each region.

The result must be as shown below:

`[imagen omitida: wiki id 46527]`

Now you are done, so press F5.

`[imagen omitida: wiki id 17828]`

Select one of the regions by tapping on the image that represents it, and see what happens.

`[imagen omitida: wiki id 17829]`

As you may have noticed, when you select a region, the default action will be run. In this case, the General section is shown.

In the example, three new car parts were created (records in a Transaction) and in the General section, all the attributes were deleted from the layout except for TRNImageMapInfo, because that's the only attribute wanted to be displayed.

### [Notes](#Notes)

* The coordinates are relative to the size of the background image. For example, if you have an image of 800x600 and coordinates {500, 200} for a region, and a resolution of 1024x768, the image of that region will be shown at {500\*1024/800, 200\*768/600} = {640, 256}.
* Images bigger than the device's resolution won't be displayed. For example, if you have a device with a resolution of 1024x768 and an image of 2048x1536, it won't be displayed.
* Since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?25073,,), to make it easier to position the items within the image when executing in the iPhone Simulator, if you tap anywhere on the image, the coordinates of the tapped point are logged in the Xcode console.

### [Other Methods](#Other+Methods)

#### [LongTap](#LongTap)

Triggered when the user performs a long-tap gesture on the image map.

Parameters:

* *&hCoord*, *&vCoord*: the horizontal and vertical coordinates of the long-tapped point. Coordinates are relative to the image's dimensions.

Example:

```
Event Grid1.LongTap(&hCoord, &vCoord)
    composite
        SavePoint(&hCoord, &vCoord)
    endcomposite
EndEvent
```

### [Restrictions](#Restrictions)

In Android, the zoom feature only works on devices with Android version 2.2 and later.

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Controls: Maps, Rating, Switch](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/controls-sd-maps-rating-sd-smart-grids-switch?p=3649)


|  |
| --- |
| **Backlinks** |
| [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) | [Category:Control Types](https://wiki.genexus.com/commwiki/wiki?20402) |
| [GeneXus Cognitive API - DetectFaces procedure](https://wiki.genexus.com/commwiki/wiki?40177) | [GeneXus Cognitive API - DetectObjects procedure](https://wiki.genexus.com/commwiki/wiki?40178) | [GeneXus Cognitive API - OCR procedure](https://wiki.genexus.com/commwiki/wiki?40180) |
| [Height Attribute property](https://wiki.genexus.com/commwiki/wiki?42199) | [Height Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42200) |
| [Horizontal Coordinate Attribute property](https://wiki.genexus.com/commwiki/wiki?42487) | [Horizontal Coordinate Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42488) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Rotation Attribute property](https://wiki.genexus.com/commwiki/wiki?42201) |
| [Rotation Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42202) | [Sample: GeneXus Cognitive API proof of concept](https://wiki.genexus.com/commwiki/wiki?40853) | [Size Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42483) | [SizeAttribute property](https://wiki.genexus.com/commwiki/wiki?42482) |
| [Vertical Coordinate Attribute property](https://wiki.genexus.com/commwiki/wiki?42485) | [Vertical Coordinate Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42486) | [Width Attribute property](https://wiki.genexus.com/commwiki/wiki?42197) | [Width Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42198) |

---
