---
title: "HowTo: Use Radio Button in Panels"
source_id: 18434
source_url: https://wiki.genexus.com/commwiki/wiki?18434
genexus_version: "18"
---

# HowTo: Use Radio Button in Panels

A Radio Button is a control used in Web and Native Mobile applications to show a group of possible values for an attribute or variable.

This tutorial explains how to use a Radio Button in Native Mobile applications.

### [**Properties**](#Properties)

|  |  |
| --- | --- |
| [Auto Grow](https://wiki.genexus.com/commwiki/wiki?20204) | If this property is set to True, the field will adjust the length of the attribute. |
| [Values](https://wiki.genexus.com/commwiki/wiki?8819) | Definition of all the possible values for the attribute/variable; each value is defined as a pair (String: Numeric). The String represents the information that will be displayed to the user when selecting or viewing this attribute/variable. Each item is defined as a pair separated by a colon (":"), and the different items are separated by a comma (","). For example, the values for three different countries (Brazil, Argentina and Uruguay) are defined in this way: Brazil:1, Argentina:2, Uruguay:3. The value 0 is used for the empty item, so setting EmptyItem = True and defining the property Values = Brazil:0, Argentina:1, Uruguay:2 is an incorrect definition and will have unexpected results. |
| [RadioDirection](https://wiki.genexus.com/commwiki/wiki?8818) | Decides whether the values will be shown horizontally or vertically. |
| [ControlTitle](https://wiki.genexus.com/commwiki/wiki?8736) | Used to define a title to the control (this property is not supported yet). |
| **EmptyItem** | Enables setting an empty option for this field. |
| **EmptyItemText** | Defines the information that will be displayed for the EmptyItem when EmptyItem = True. |

### [**Samples**](#Samples)

For this example, a [domain](https://wiki.genexus.com/commwiki/wiki?7221) called "Enum" will be defined as follows:

`[imagen omitida: wiki id 55741]`

The definition of the values in the domain is made in the [Enum Values property](https://wiki.genexus.com/commwiki/wiki?7379), as shown in the following image:

`[imagen omitida: wiki id 55742]`

In the images above, you can see that the properties of a Combo Box can be defined directly in the domain. All you have to do later is define the attribute/variable with *Type = Enum*. Also, an EmptyItem was defined for the domain, so a "No Country" value should be shown when the combo is used.

The Transaction to be used for this example is the following, with the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974) applied (see [Applying Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975)):

```
ComboBoxTutorial                 
{                                   
    ComboBoxTutorialId*         
    ComboBoxTutorialEnum 
    ComboBoxTutorialBoolean    
}
```

Set the ComboBoxTutorialBoolean attribute property [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) = Radio Button. Note that when the ComboBoxTutorialEnum attribute is defined, it takes all the properties defined by the Enum domain.

GeneXus should define the [Values property (for Check Boxes, List Boxes and Radio Buttons)](https://wiki.genexus.com/commwiki/wiki?8819) automatically, as seen in the following image:

`[imagen omitida: wiki id 55743]`

All done! All you have to do now is press F5 and see the results.

### [[Android](https://wiki.genexus.com/commwiki/wiki?14453) Snapshot](#com.gxwiki.wiki%3F14453%2CCategory%253AAndroid%2Bplatform+Android+Snapshot)

`[imagen omitida: wiki id 59819]`

### [Apple Snapshots](#Apple+Snapshots)

The following combinations of properties illustrate the visual outcomes displayed in the user interface:

**1) Visual Result: Table View**

|  |  |
| --- | --- |
| **Property** | **Value** |
| Control Direction | Vertical |
| Auto Grow | True |

This style presents the Radio Buttons in a vertical list, where each option behaves like a row in a table. It is ideal for long lists of options.

`[imagen omitida: wiki id 59828]`

**2) Visual Result: Segmented Control**

|  |  |
| --- | --- |
| **Property** | **Value** |
| Control Direction | Horizontal |
| Auto Grow | False |

In this case, the Radio Buttons are displayed in a horizontal row and occupy a fixed space. This style is useful for options where the number of buttons is limited and a more compact appearance is desired.

`[imagen omitida: wiki id 59829]`

**3) Visual Result: Pop-up Button**

|  |  |
| --- | --- |
| **Property** | **Value** |
| Control Direction | Horizontal |
| Auto Grow | True |

or

|  |  |
| --- | --- |
| **Property** | **Value** |
| Control Direction | Vertical |
| Auto Grow | False |

With this configuration, although the direction is vertical, the control does not automatically expand. This can result in a fixed Pop-up button that displays options in a more compact format.

`[imagen omitida: wiki id 59830]`

### See Also

[HowTo: Use Combo Box in Panels](https://wiki.genexus.com/commwiki/wiki?18408)
