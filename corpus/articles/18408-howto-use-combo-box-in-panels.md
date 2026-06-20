---
title: "HowTo: Use Combo Box in Panels"
source_id: 18408
source_url: https://wiki.genexus.com/commwiki/wiki?18408
genexus_version: "18"
---

# HowTo: Use Combo Box in Panels

A Combo box is a control used in both Web and Native Mobile applications. It is used to show a group of possible values for a variable or attribute.

This tutorial explains how to use a Combo Box in Native Mobile applications, with a simple example.

### [Properties](#Properties)

|  |  |
| --- | --- |
| [Auto Grow](https://wiki.genexus.com/commwiki/wiki?20204) | If this property is True, then the field will adjust the length of the attribute. |
| [Values](https://wiki.genexus.com/commwiki/wiki?8819) | Definition of all the possible values for the attribute/variable, each value is defined as a pair (String:Numeric). The String represents the information that will be displayed to the user when selecting or viewing this attr/var. Each item is defined as a pair separated with a colon (":"), and the different items are separated by a comma. For example, if you want to define the values for three different countries (Brazil, Argentina and Uruguay), you will have: Brazil:1, Argentina:2, Uruguay:3 (the value 0 is used for the empty item so setting the EmptyItem = True and defining the property Values = Brazil:0, Argentina:1, Uruguay:2, is a wrong definition and will have unexpected results). |
| **EmptyItem** | It enables to set an empty option for this field. |
| **EmptyItemText** | It defines the information that will be displayed for the EmptyItem when EmptyItem = True. |

### [Samples](#Samples)

For this example, a [Domain](https://wiki.genexus.com/commwiki/wiki?7221) called "Enum" will be defined as follows:

`[imagen omitida: wiki id 32542]`

The definition of the values in the domain is made in the [Enum Values property](https://wiki.genexus.com/commwiki/wiki?7379), as shown in the next image:

`[imagen omitida: wiki id 32543]`

In the images above, you can see that the properties of a Combo Box can be defined directly in the domain. All you have to do later is define the variable/attribute with *Type = Enum*. Also, an EmptyItem was defined to the domain, so a value "No Country" is shown when the combo is used.

The [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) to be used for this example is the next one, with the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974) applied (see [Applying Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975)).

`[imagen omitida: wiki id 32544]`

Set the ComboBoxTutorialBoolean attribute property [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) = ComboBox (also note that when the ComboBoxTutorialEnum attribute is defined, it takes all the properties defined by the domain Enum).

GeneXus should define the Values property automatically, as seen in the next image:

`[imagen omitida: wiki id 32545]`

All done! All you have to do now is hit F5 and see the results.

[**Android**](https://wiki.genexus.com/commwiki/wiki?14453) **Snapshot**

`[imagen omitida: wiki id 18426]`

####


|  |
| --- |
| **Backlinks** |
| [HowTo: Use Radio Button in Panels](https://wiki.genexus.com/commwiki/wiki?18434) |

---
