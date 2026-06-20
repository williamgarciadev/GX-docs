---
title: "Font-face style rule"
source_id: 49338
source_url: https://wiki.genexus.com/commwiki/wiki?49338
genexus_version: "18"
---

# Font-face style rule

Defines a font family other than the default ones and using it in both the Tokens and Styles of the Design System Object.

### [Syntax](#Syntax)

```
@font-face 
‘{‘
    font-family ':' <font_family_name> ';'
    src ':' <source_file> [, <source_file>]...';'
    [font-weight ':' <weight> ';']
    [font-style ':' <style> ';']
    [font-stretch ':' <separation> ';']
‘}’
```

View  [Design System Syntax conventions](https://wiki.genexus.com/commwiki/wiki?49363).

**Where:**

*font\_family\_name* Indicates the name of the font you are defining.

*source\_file* Indicates the source file of the font, which can be a URL or a reference to a file object (through the gx-file function).

*weight* Defines how bold the font is. Options: **normal**, **bold**, **100**, **200**, …, **900**

*style* Defines the font style. Options: **normal**, **italic**, **oblique**.

*separation* Defines the font spacing. Options: **normal**, **condensed**, **ultra-condensed**, **extra-condensed**, **semi-condensed**, **expanded**, **semi-expanded**, **extra-expanded**, **ultra-expanded**.

### [Samples](#Samples+)

```
Styles myStyle
{
       @font-face
       {
             font-family: AbhayaLibre-Bold;
             src: gx-file(AbhayaLibre-Bold-ttf);
       }
       .H1
       {
             color: #FFFFFF;
             font-family: AbhayaLibre-Bold;
             font-size: 95px;
       }
       .H2
       {
             color: $colors.OnSurface;
             font-family: $fonts.Title1;
             font-size: $fontSizes.H2;
       }
}

Tokens MyTokens
{
       #colors
       {
              OnSurface: #191819;
       }
       #fonts
       {
              Title1: AbhayaLibre-Bold;
       }
       #fontSizes
       {
               H2: 60px;
       }

}
```

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [See Also](#See+Also)

See the general topic [Design System Style Rules](https://wiki.genexus.com/commwiki/wiki?47472).  
[Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)


|  |
| --- |
| **Backlinks** |
| [Design Import option](https://wiki.genexus.com/commwiki/wiki?46882) | [Design Import option (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55439) | [Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49323) |
| [Design System Class Properties (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55682) | [Design System Style Rules](https://wiki.genexus.com/commwiki/wiki?47472) | [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) | [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |
| [DesignOps - Guide for developers](https://wiki.genexus.com/commwiki/wiki?46877) | [HowTo: Using web fonts in Web Themes](https://wiki.genexus.com/commwiki/wiki?22701) |

---
