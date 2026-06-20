---
title: "Transformations"
source_id: 23694
source_url: https://wiki.genexus.com/commwiki/wiki?23694
genexus_version: "18"
---

# Transformations

Transformations allow changing the shape, size, and/or position of an element on screen at runtime.

### [How do they work?](#How+do+they+work%3F)

Transformations are applied to elements in the UI through classes.

A transformation is created in the theme and associated with a class; then, the transformation is automatically applied to the elements that use that class. This makes it possible to transform elements both at design time and at runtime since classes can be assigned at any of these times.

### [How is a transformation created?](#How+is+a+transformation+created%3F)

Transformations are in the theme, grouped under the **Transformations node**. They are added and changed in the same way as classes, and then they are referenced by classes in their **Transformation** **property**.

`[imagen omitida: wiki id 37652]` `[imagen omitida: wiki id 37653]`

If a theme-class has a transformation and the [Animated property](https://wiki.genexus.com/commwiki/wiki?34111)enabled, the transformations will be animated -- to the extent that the platform supports it. Also, it's possible to indicate its [duration](https://wiki.genexus.com/commwiki/wiki?34112).

All transformations have the properties below, which allow defining the changes to be made when it is applied.

|  |  |
| --- | --- |
| **Property** | **Values** |
| **Name** | Name of the transformation |
| **Anchor Point X** | left,center,right,xx %,xx dip |
| **Anchor Point Y** | top,middle,bottom,xx %,xx dip |

The values of properties Anchor Point X and Anchor Point Y indicate the point at which the transformation functions start to be applied. In this way, points can be indicated such as {left, top} which is the same as {0%, 0%}, {center, middle} = {50%, 50%}, or any arbitrary value with percentages. The default value is always {center, middle} = {50%, 50%}.

**Note**: xx % values are relative to the initial size of the control when the transformation is applied.

### [Translate properties group](#Translate+properties+group)

Allows changing the position of an element on the screen.

|  |  |
| --- | --- |
| **Property** | **Values** |
| **Type** | TranslateBy / TranslateTo |
| **Value X** | xx %, xx dip |
| **Value Y** | xx %, xx dip |
| **Relative To** | Refer [here](23694#Relative+To+property'.html). |

The Type property indicates the reference framework to interpret the values:

* **TranslateBy**   
  Indicates that the control will be moved the distance calculated by value from the source point of the control.
* **TranslateTo**   
  Indicates that the movement is absolute to the point indicated by the values X/Y (and relative to).

Examples:  
- "*TranslateBy X 20% relative to form*" moves the control to the right 20% of the form width in relation to its original position.  
- "*TranslateTo X 20% relative to form*" will move the control (to the left or right) so that its left border is placed on the point located at 20% of the screen size.  
- TranslateTo and TranslateBy relative to control are equivalent.  
- The values for Value X and Value Y in a translation are percentages or dips. If the translation is to be made in only one coordinate, the other one must be set to zero.

### [Scale properties group](#Scale+properties+group)

When a control is scaled, the size of both control and content changes proportionally.

|  |  |
| --- | --- |
| **Property** | **Values** |
| **Value X** | xx %,  xx dip |
| **Value Y** | xx %,  xx dip |
| **Relative To** | Refer [here](23694#Relative+To+property'.html) |

The values for Value X and Value Y are percentages or dips. If the scaling is to be made in only one coordinate, the other one must be set to 100%.

### [Resize properties group](#Resize+properties+group)

When a control is resized, the size of it changes proportionally. Unlike Scale, the control's content remains unchanged (only changes the size of the control).

Resize the control at control level only (unlike Scale properties group).

|  |  |
| --- | --- |
| **Property** | **Values** |
| **Value X** | xx %,  xx dip |
| **Value Y** | xx %,  xx dip |
| **Relative To** | Refer [here](23694#Relative+To+property'.html) |

The values for Value X and Value Y are percentages or dips. If the scaling is to be made in only one coordinate, the other one must be set to 100%.

**Notes**:

* When *resizing* a control, may imply that certain contents are no longer displayed. On the other hand, when scaling a control, may distort it or make it loose definition.
* Angular doesn´t support it. CSS doesn't offer a native way of scaling an element without scaling its contents.

### [Rotate properties group](#Rotate+properties+group)

It indicates the angle of the rotation in degrees.

|  |  |
| --- | --- |
| **Property** | **Values** |
| **Angle** | xxx º |

### [Relative To property](#Relative+To+property)

This property indicates the size to be taken into account when the transformation is applied.

The values that can be used by this parameter are as follows:  
- Current control (default)  
- Parent control  
- Form  
This value applies to dimensions. However, it doesn't apply to angles.

For example, if I have a layout with a table of 400x300 which contains an image of 100x100, if I scale (100%, 100%) the image, the final size will be:  
- 100x100 if **Relative To property** is *Current control*  
- 400x300 if **Relative To property** is *Parent control*

**Note for Angular:**Only "Current Control" is supported. CSS only supports this value natively.

## [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

## See Also

* [RecursosUX](https://wiki.genexus.com/commwiki/wiki?23280,,) Sample


|  |
| --- |
| **Backlinks** |
| [Animated property](https://wiki.genexus.com/commwiki/wiki?34111) | [Animation Duration property (for Animation Theme class)](https://wiki.genexus.com/commwiki/wiki?34112) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |
| [Category:Theme object](https://wiki.genexus.com/commwiki/wiki?16595) | [Using Custom Fonts](https://wiki.genexus.com/commwiki/wiki?22781) |

---
