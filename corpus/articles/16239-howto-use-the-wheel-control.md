---
title: "HowTo: Use the Wheel Control"
source_id: 16239
source_url: https://wiki.genexus.com/commwiki/wiki?16239
genexus_version: "18"
---

# HowTo: Use the Wheel Control

Sometimes you need to navigate through the values a field can take. The wheel control has gained popularity with the touch screen interface and is widely used in such cases. You can scroll through an [Enumerated Domain](https://wiki.genexus.com/commwiki/wiki?2207) or Numeric values to select the value you want.

In this article, the most important concepts of the wheel control are explained and there is an example on how to use it.

This control applies to the following data types:

* [Numeric data type](https://wiki.genexus.com/commwiki/wiki?6793)
* [Enumerated Domains Methods and Properties](https://wiki.genexus.com/commwiki/wiki?9918)

### [Samples](#Samples)

The following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) will be used with the Work With pattern applied.

`[imagen omitida: wiki id 16240]`

The Transaction contains an attribute based on an [Enumerated Domain](https://wiki.genexus.com/commwiki/wiki?2207) (TrnCustomersEnumerated) and an attribute based on the Numeric data type (TrnCustomersNumWheel).

Enumerated Domain:

`[imagen omitida: wiki id 16241]`

To enable the control, go to the Section (General) under the [Detail node](https://wiki.genexus.com/commwiki/wiki?20433), and select the Edit layout. Select the Numeric attribute (TrnCustomersNumWheel) and change the [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) to Wheel.

`[imagen omitida: wiki id 46460]`

This will enable some other properties.

### [General Wheel properties](#General+Wheel+properties)

|  |  |
| --- | --- |
| **Notify Context Change** | This property is used for event handling. |
| **Display Style** | "Inline" or "As a picker" values. You can select how this control is seen. The default value is "As a picker". This property has an effect only in Apple devices. For Android devices, the wheel control is always displayed as a picker. This restriction is imposed by the platform itself. |
| **Cyclic** | You can enable this property if you want the last value to be continued by the first one. |

For Numeric based attributes:

|  |  |
| --- | --- |
| **Step** | The incrementation from one value to another. |
| **Min Value** | The minimum value the control will show to select. |
| **Max Value** | The maximum value the control will enable you to select. |

For the Enumerated attribute let's do the same:

|  |  |
| --- | --- |
| **Control type** | Wheel |

`[imagen omitida: wiki id 46462]`

There are no particular properties enabled, just the General Wheel control properties.

Done, press F5.

The following pictures show you the wheel control according to its attributes.

**Numeric as a Picker**:

`[imagen omitida: wiki id 16244]`

#### [**Enumerated As a picker**:](#Enumerated+As+a+picker%3A)

`[imagen omitida: wiki id 16245]`

#### [**Numeric Inline**:](#Numeric+Inline%3A)

`[imagen omitida: wiki id 16246]`

#### [**Numeric with decimals:**](#Numeric+with+decimals%3A)

The wheel control can also be applied to a field based on a numeric with decimals. For example:

`[imagen omitida: wiki id 16826]`

`[imagen omitida: wiki id 46463]`

When using decimals you can specify decimal step (in the example 0.02) and after deploying the application the control is displayed as follows:

`[imagen omitida: wiki id 16828]`

### [See Also](#See+Also)

[HowTo: Use MultiWheel Control](https://wiki.genexus.com/commwiki/wiki?20171)


|  |
| --- |
| **Backlinks** |
| [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) | [Category:Control Types](https://wiki.genexus.com/commwiki/wiki?20402) | [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945) |
| [Data Source From property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55489) | [GetDescriptionByKey Procedure Parameters property](https://wiki.genexus.com/commwiki/wiki?55468) | [GetDescriptionByKey Procedure property](https://wiki.genexus.com/commwiki/wiki?55413) | [HowTo: Use MultiWheel Control](https://wiki.genexus.com/commwiki/wiki?20171) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
