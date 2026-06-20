---
title: "Scroll Attachment property"
source_id: 29875
source_url: https://wiki.genexus.com/commwiki/wiki?29875
genexus_version: "18"
---

# Scroll Attachment property

Specifies the scrolling behavior of a control on a screen.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [Canvas](https://wiki.genexus.com/commwiki/wiki?22452), [Table](https://wiki.genexus.com/commwiki/wiki?6001)

### [Description](#Description)

This property is available for [Table](https://wiki.genexus.com/commwiki/wiki?6001) and [Canvas](https://wiki.genexus.com/commwiki/wiki?22452) controls included in [Panels](https://wiki.genexus.com/commwiki/wiki?24829) and [WW](https://wiki.genexus.com/commwiki/wiki?15974).

Its value is a sequence of [Control Names](https://wiki.genexus.com/commwiki/wiki?8754) (eventually one) to which the [Scroll Factor](https://wiki.genexus.com/commwiki/wiki?29874) and [Zoom Factor](https://wiki.genexus.com/commwiki/wiki?29876) properties will be applied when any of these controls is scrolled by the end user in the application. By default, its value is "Parent", indicating the control in which it is embedded, but can be replaced by a sequence of Control Names separated by a semicolon.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

In [EventDay](https://wiki.genexus.com/commwiki/wiki?22550,,), suppose we want to apply this UI/UX feature to the list of speakers. For this example, we use iOS Generator.  
First, open the [List section](https://wiki.genexus.com/commwiki/wiki?15984) of the WorkWithDevicesSpeaker object.  
From the toolbox, drag a Table control (it can be a Canvas control, too) and drop it at the top of the Main Table, above the Speakers Grid. Inside the table, insert an Image object (previously loaded - or it can be an Attribute/Variable Image instead).

`[imagen omitida: wiki id 30537]`

Make sure that the following properties have been set as shown below:

* The Speakers Grid has the Auto Grow property set to True, allowing the user to scroll the grid in the entire panel.
* The Row Style property for the Table has an embedded image with 100% value to enlarge it when the Table grows.

The reason for that is that we want a parallax effect when we scroll down in the panel beyond the limits, creating a zoom effect on the image.  
Then, at the Table control level we must configure the [Scroll Factor](https://wiki.genexus.com/commwiki/wiki?29874) and [Zoom Factor](https://wiki.genexus.com/commwiki/wiki?29876) properties with 0.5 and 1 values, respectively; also, to indicate what control will be used as a reference we must set the Scroll Attachment property to MainTable.

`[imagen omitida: wiki id 30536]`

One last thing that we must ensure is that the Class associated with the [Image object](https://wiki.genexus.com/commwiki/wiki?23387) has the [Scale Type property](https://wiki.genexus.com/commwiki/wiki?23857) set to “Fill Keeping Aspect Ratio”. With this configuration, the image will be filled proportionally in its own container (in this case, the Table control in which it is embedded).

**Note:** Usually this is not necessary because it is provided by default in the SimpleiOS theme, but in [EventDay](https://wiki.genexus.com/commwiki/wiki?22550,,) sample it is associated with the EventGXiOS7 theme for iOS layouts, whose value for Image class in the Scale Type property has been set to a different value. For this reason, we create another Image class called “ImageScrollZoom” with “Scale Type property = Fill Keeping Aspect Ratio” (see Advanced Usage Example to know the effect achieved with other values).

`[imagen omitida: wiki id 30538]`

Finally, the application at runtime looks as follows:

`[imagen omitida: wiki id 30539]`

### [Advanced Usage Example](#Advanced+Usage+Example)

Stretched image

By keeping the same properties for the Table in which the Image is embedded, and changing the [Scale Type property](https://wiki.genexus.com/commwiki/wiki?51461,,) to “Fill” value in the associated class, we obtain the following effect:

|  |  |
| --- | --- |
|  | *Table level properties*   * Scroll Factor = 0.5 * Zoom Factor = 1 * Scroll Attachment = MainTable   *Image class theme level*   * Scale type = Fill |

Raise image  
A negative value in [Scroll Factor property](https://wiki.genexus.com/commwiki/wiki?29874) and Scale Type property with “Fill” value (at Image class theme level), cause that when you scroll down the attached control, the Table/Canvas will scroll in the other way, generating the effect that raises the image.

|  |  |
| --- | --- |
|  | *Table level properties*   * Scroll Factor = -1 * Zoom Factor = 3 * Scroll Attachment = MainTable   *Image class theme level*   * Scale type = Fill |

### [Availability](#Availability)

This property is available since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?27605,,).

### [See Also](#See+Also)

[Scroll Factor property](https://wiki.genexus.com/commwiki/wiki?29874)  
[Zoom Factor property](https://wiki.genexus.com/commwiki/wiki?29876)


|  |
| --- |
| **Backlinks** |
| [Motion Effect properties group](https://wiki.genexus.com/commwiki/wiki?30953) | [Scroll behavior properties group](https://wiki.genexus.com/commwiki/wiki?31174) | [Scroll Factor property](https://wiki.genexus.com/commwiki/wiki?29874) |
| [Zoom Factor property](https://wiki.genexus.com/commwiki/wiki?29876) |

---
