---
title: "Design System Classes writing styles"
source_id: 49363
source_url: https://wiki.genexus.com/commwiki/wiki?49363
genexus_version: "18"
---

# Design System Classes writing styles

Basically, it can be divided into 3 writing styles:

### [CSS](#CSS)

The format is completely compatible with a CSS style sheet.

Although it is not the optimal way to use it, it allows you to paste a CSS directly there and use it as the style sheet of the design system for Web applications.

```
Styles My_Style
{
  .HeaderContainer
  {
       background-color: #fafafb;
       border-radius: 0px;
       border-width: 1px;
       font-size: 16px;
  }
}
```

### [Pure](#Pure)

There are those who argue that in a design system, all the values of the decisions should be [Tokens](https://wiki.genexus.com/commwiki/wiki?47378). In this writing style, the property values are completely parameterized with Tokens.

```
Styles My_Style
{ 
   .HeaderContainer 
   { 
      background-color: $color.background; 
      border-radius: $radius.circle; 
      border-width: $border.thin; 
      font-size: $fontSizes.small; 
   }    
}
```

For this, you first have to define the corresponding Tokens.

### [Hybrid](#Hybrid)

This way of defining styles takes advantage of both previous possibilities by creating a hybrid sheet, where some properties are parameterized with Tokens while others simply have a fixed value.

```
Styles My_Style
{
   .HeaderContainer
   {
      background-color: #fafafb;
      border-radius: $radius.circle;
      border-width: 1px;
      font-size: $fontSizes.small;
   }
}
```

### [See Also](#See+Also)

[Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379)


|  |
| --- |
| **Backlinks** |
| [Design System Class](https://wiki.genexus.com/commwiki/wiki?49309) | [Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49323) | [Design System Class Properties (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55682) |
| [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) | [Design System Tokens](https://wiki.genexus.com/commwiki/wiki?47378) | [Design System Tokens Options](https://wiki.genexus.com/commwiki/wiki?49381) | [Font-face style rule](https://wiki.genexus.com/commwiki/wiki?49338) |
| [Import style rule](https://wiki.genexus.com/commwiki/wiki?49346) | [Include style rule](https://wiki.genexus.com/commwiki/wiki?49353) | [Include style rule (GeneXus 18 Upgrade 1)](https://wiki.genexus.com/commwiki/wiki?53833) | [Media style rule](https://wiki.genexus.com/commwiki/wiki?49344) |
| [Structuring classes in Design System](https://wiki.genexus.com/commwiki/wiki?49292) |

---
