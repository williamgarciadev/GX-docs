---
title: "HowTo: Set the style of a read-only Attribute/Variable control using DSO"
source_id: 49906
source_url: https://wiki.genexus.com/commwiki/wiki?49906
genexus_version: "18"
---

# HowTo: Set the style of a read-only Attribute/Variable control using DSO

This article explains how to give a specific style to a read-only Attribute/Variable control using a [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375).

Consider a variable named &copyright that is inserted in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) to display a copyright text.

Since the variable should not be editable, its Readonly property is set to True.

`[imagen omitida: wiki id 55735]`

In addition, the &copyright variable has its [Class property](https://wiki.genexus.com/commwiki/wiki?8741) configured with a class named MinorText which is defined in the Styles section of a Design System object created in the KB and [associated with the Web Panel](https://wiki.genexus.com/commwiki/wiki?48696).

The definition of the MinorText class in the Styles section of the Design System object is as follows:

```
.MinorText
    {
        background-color: $colors.Grey01;
        color: $colors.OnSurface;
        font-size: 20px;
        font-family: AbhayaLibre-Bold;
        gx-readonly-class: Readonly;
    }

    .Readonly
    {
        background-color: yellow;
    }
```

Note that the MinorText class contains the [gx-readonly-class property](https://wiki.genexus.com/commwiki/wiki?48092) configured with another class (which is defined by you and in this case has been named ".Readonly").

At runtime, you will see the following:

`[imagen omitida: wiki id 55737]`

However, if the Attribute/Variable control had its Readonly property set to False (which is the default value), at runtime you would see the following:

`[imagen omitida: wiki id 55736]`

In conclusion, given an Attribute/Variable control that has its Class property = MinorText and also has:

* Its Readonly property = False: The **background-color property** of the MinorText class is taken into account.
* Its Readonly property = True: The **gx-readonly-class property** of the MinorText class is taken into account (and the assigned class has its own **background-color property**configured).

### [See Also](#See+Also)

[DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707)


|  |
| --- |
| **Backlinks** |
| [Comparison between Theme and Design System objects](https://wiki.genexus.com/commwiki/wiki?48985) | [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) | [gx-readonly-class property](https://wiki.genexus.com/commwiki/wiki?48092) |
| [Readonly Class Comparison between Theme and Design System Object](https://wiki.genexus.com/commwiki/wiki?49912) |

---
