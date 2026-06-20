---
title: "Attribute-checkbox class for Design System objects"
source_id: 52932
source_url: https://wiki.genexus.com/commwiki/wiki?52932
genexus_version: "18"
---

# Attribute-checkbox class for Design System objects

Attribute-checkbox is a class that inherits properties from the Attribute class, but applies specifically to controls whose [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) = Check Box.

When generating the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974), this class allows those Attributes whose [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) = Check Box to be automatically assigned this specific class.

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

Now, suppose that if the Attribute/Variable is a Check box, you want the borders not to be displayed, and the left padding to be 0, so that it looks as shown below:

`[imagen omitida: wiki id 52946]`

The class to be defined is as follows:

```
        .attribute-checkbox {
            @include Attribute;
            border-style: none;
            padding-left: 0dip;
        }
```

### [See Also](#See+Also)

[Design System Class](https://wiki.genexus.com/commwiki/wiki?49309)
