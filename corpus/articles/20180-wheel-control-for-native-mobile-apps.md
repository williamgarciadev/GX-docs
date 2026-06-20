---
title: "Wheel Control for Native Mobile apps"
source_id: 20180
source_url: https://wiki.genexus.com/commwiki/wiki?20180
genexus_version: "18"
---

# Wheel Control for Native Mobile apps

The Wheel control allows selecting a value by swiping up and down and minimizing the use of the touch keyboard.

`[imagen omitida: wiki id 20181]`

It can be used to select different kinds of data:

* Numeric data
* Enumerated strings
* Dynamic information (like a dynamic combo box).

Conceptually a wheel can be used as you use a combo box. The main difference is that in general, you will use the wheel with low cardinality ranges or enumerated fields.

### [**Properties**](#Properties)

When the data type associated is Numeric there are some specific properties to set.

|  |  |  |
| --- | --- | --- |
| **Property** | **Type** | **Description** |
| *Cyclic* | Boolean | After the highest value, the lowest value is shown. |
| *Step* | Character | It might be an integer or a decimal value. In case it is a decimal value, the control shows a wheel with two components: the first for the integer part and the second for the decimal part. This has some restrictions:   * You shouldn't set a Step value that has an integer part and a decimal part. For example, you shouldn't set a step of 1.5. Use decimals only with an integer part of 0. * You shouldn't set a Step value that doesn't add up to the unit. For example, if you set a Step value of 0.3, the decimal part will show the values 0, 3, 6 and 9 only. You should use values such as 0.1, 0.2, 0.5, 0.25, etc. |
| *Minimum Value* | Character | Indicates the minimum value. |
| *Maximum Value* | Character | Indicates the maximum value. |
| *Initial Value* | Character | Indicates the initial value. It's a temporary property that will be removed once we add support for the default rule in Transactions. |

### [**Notes**](#Notes)

* On Android generator, the *Cycle*, *Step*, *Minimum Value* and *Maximum Value* properties cannot be set at run-time (there are design-time properties).  
  For more information, refer to [SAC#34598](https://www.genexus.com/es/developers/websac?data=34598;;)

### [**Scope**](#Scope)

|  |  |
| --- | --- |
| **Level:** | Attribute/Variable, Numeric and Enumerated Domains |
| **Generators:** | Apple, Android |


|  |
| --- |
| **Backlinks** |
| [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945) | [Data Source From property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55489) | [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396) |
| [HowTo: Use the Data Source From property](https://wiki.genexus.com/commwiki/wiki?22948) | [HowTo: Using the Data Source From property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55521) | [Invite Message property](https://wiki.genexus.com/commwiki/wiki?19697) |

---
