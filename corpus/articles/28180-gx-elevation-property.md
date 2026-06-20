---
title: "gx-elevation property"
source_id: 28180
source_url: https://wiki.genexus.com/commwiki/wiki?28180
genexus_version: "18"
---

# gx-elevation property

Configures the shadows cast by controls.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

This property is available in Native Mobile applications for these controls: Attribute/Variable, [Button](https://wiki.genexus.com/commwiki/wiki?6011), [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Group](https://wiki.genexus.com/commwiki/wiki?6570), [Image](https://wiki.genexus.com/commwiki/wiki?5939), [Tab](https://wiki.genexus.com/commwiki/wiki?25623), [Table](https://wiki.genexus.com/commwiki/wiki?6001), [Text Block](https://wiki.genexus.com/commwiki/wiki?5948).

It accepts positive numerical values to indicate how much shadow to show.  
By default, its value is empty (semantically, it represents 0).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at runtime and at design time.

### [Samples](#Samples)

The example below is based on customized buttons.

First, in your Design System object define the following in the .Button class created to give style to your buttons:

```
.Button
        {
           border-style: solid;
           border-color: 14BBCC;
           border-width: 1dip;
           border-radius: 60dip;
           background-color: 14BBCC;
           gx-elevation: 20;
         }
```

In this case the gx-elevation value chosen is 20.

Next, after dragging the Button Control from the Toolbox to an Abstract Layout of a Panel or Work With, set the following:

Width = 40   
Height = 40  
Image = <an\_add\_to\_cart\_icon>  
Class = <class\_previously\_created>

With this configuration, the button will have a rounded look with a small icon inside it.

Finally, after defining the Elevation property, the effects achieved are shown in the following table:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Value** | **by default** | **5** | **10** | **20** |
|  | **Effect** |  |  |  |  |

**Notes:**

* This property is available for Android 5.0 or higher.
* To see the effect, the background color should be opaque.
* The space for the control and its shadow must be smaller than its container cell.
* If there are controls inside a [Canvas](https://wiki.genexus.com/commwiki/wiki?22452) with Elevation and [ZOrder](https://wiki.genexus.com/commwiki/wiki?22510) properties set, the difference between two controls with the same ZOrder is their Elevation.
* To change the elevation at runtime, change the Design System Class. For instance, if you have set the Button class for a button control, you can type:

  ```
  Button1.Class = StyleClass:ButtonWithElevation
  ```

  where ButtonWithElevation is a Design System Class with its Elevation property set.

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [See Also](#See+Also)

[HowTo: Adding Material Design to Android applications](https://wiki.genexus.com/commwiki/wiki?31004)  
[Design System Object](https://wiki.genexus.com/commwiki/wiki?47375)  
[Grid control](https://wiki.genexus.com/commwiki/wiki?24817)


|  |
| --- |
| **Backlinks** |
| [Attribute theme-class](https://wiki.genexus.com/commwiki/wiki?37646) | [Button theme-class for Smart Devices](https://wiki.genexus.com/commwiki/wiki?37647) |
| [Grid Theme class](https://wiki.genexus.com/commwiki/wiki?37657) | [HowTo: Adding Material Design to Android applications](https://wiki.genexus.com/commwiki/wiki?31004) | [Slider Theme class](https://wiki.genexus.com/commwiki/wiki?42294) |

---
