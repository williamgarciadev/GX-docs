---
title: "Design System Style Rules"
source_id: 47472
source_url: https://wiki.genexus.com/commwiki/wiki?47472
genexus_version: "18"
---

# Design System Style Rules

There’s a set of rules (beginning with the @ sign) that you can use for structuring [Styles](https://wiki.genexus.com/commwiki/wiki?47379). They let you:

●    Compose [classes](https://wiki.genexus.com/commwiki/wiki?49309)

For example, declare that the H1 class consists of the style of the H1\_Negative and Margin-Sides classes, in addition to the specific properties defined for it (only color here):

```
.H1
      {
          @include H1_Negative Margin-Sides;
          color: $colors.Black;
      }
```

See [Include style rule](https://wiki.genexus.com/commwiki/wiki?49353).

●    Import Tokens or styles (or both) from other [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375)s.

For example, declare that you are going to import both Tokens and Styles from the DSO named TravelAgency into the current one:

```
styles TravelAgencyFrontendExtended
{
    @import TravelAgency;
}
```

See [Import style rule](https://wiki.genexus.com/commwiki/wiki?49346).

●    Vary the style of a class according to the screen size.

For example, when the screen width is less than 768px, the H1\_Negative class has a font-size of 26px:

```
@media screen and (max-width:767px)
{
    .H1_Negative {
        font-size: 26px;
    }
}
```

Note that this relates precisely to [CSS Media Queries](https://www.w3schools.com/css/css3_mediaqueries.asp).   
See [Media style rule](https://wiki.genexus.com/commwiki/wiki?49344).

●    Incorporate a non-default source

For example, to use the AbhayaLibre-bold family, which is not a default font, in some token or class.

```
@font-face
{
    font-family: AbhayaLibre-Bold; 
    src: gx-file(AbhayaLibre-Bold_ttf);
}
.H1_Negative
{
    color: #FFFFFF;
    font-size: $fontSizes.H1;
    font-family: AbhayaLibre-Bold;
}
```

See [Font-face style rule](https://wiki.genexus.com/commwiki/wiki?49338).

### [Availabilty](#Availabilty)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).


|  |
| --- |
| **Backlinks** |
| [Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49323) | [Design System Class Properties (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55682) | [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) |
| [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) | [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) | [Font-face style rule](https://wiki.genexus.com/commwiki/wiki?49338) | [Import style rule](https://wiki.genexus.com/commwiki/wiki?49346) |
| [Include style rule](https://wiki.genexus.com/commwiki/wiki?49353) | [Include style rule (GeneXus 18 Upgrade 1)](https://wiki.genexus.com/commwiki/wiki?53833) | [Media style rule](https://wiki.genexus.com/commwiki/wiki?49344) | [Structuring classes in Design System](https://wiki.genexus.com/commwiki/wiki?49292) |

---
