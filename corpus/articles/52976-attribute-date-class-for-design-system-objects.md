---
title: "Attribute-date class for Design System objects"
source_id: 52976
source_url: https://wiki.genexus.com/commwiki/wiki?52976
genexus_version: "18"
---

# Attribute-date class for Design System objects

Attribute-date is a class that inherits properties from the Attribute class, but applies specifically to those based on the [Date data type](https://wiki.genexus.com/commwiki/wiki?7373) / [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370).

When generating the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974), this class allows those Attributes whose [Data Type](https://wiki.genexus.com/commwiki/wiki?7232) is [Date](https://wiki.genexus.com/commwiki/wiki?7373) or [Date Time](https://wiki.genexus.com/commwiki/wiki?7370) to be automatically assigned this specific class.

### [Sample](#Sample)

First, create an Attribute class in the [Styles section](https://wiki.genexus.com/commwiki/wiki?47379) of your [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) with the desired general style for the attributes:

```
        .Attribute {
             gx-label-class: attribute__label;
             border-style: solid;
             border-color: #8592A6;
             border-width: 1dip;
             border-radius: 4dip;
             margin-left: 16dip;
             margin-right: 16dip;
             margin-bottom: 8dip;
             background-color: $colors.surface;
             padding-left: 8dip;
             padding-right: 8dip;
             gx-show-edit-text-line: false;
             color: #3D4854;
             gx-invite-message-color: #8592A6;
             font-size: 16dip;
             font-family: $fonts.primary-regular;  
       }
```

Now, suppose that for the Attribute/Variable whose [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) = Radio Button, you want the borders not to be displayed and to have a lower margin, as shown below:

`[imagen omitida: wiki id 52977]`

The class to be defined is as follows:

```
 .attribute-date {
          @include Attribute;
          border-style: none;
          margin-bottom: 7dip;
 }
```

### [See Also](#See+Also)

[Design System Class](https://wiki.genexus.com/commwiki/wiki?49309)
