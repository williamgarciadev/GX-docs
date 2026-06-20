---
title: "Design System Object - How to change an image according to the Design System Object option"
source_id: 48694
source_url: https://wiki.genexus.com/commwiki/wiki?48694
genexus_version: "18"
---

# Design System Object - How to change an image according to the Design System Object option

This article describes how to change the [Image object](https://wiki.genexus.com/commwiki/wiki?23387) named chatbot according to the Light or Dark color-scheme.

As you can see in the design, in Light mode it is red and in Dark mode it is green:

`[imagen omitida: wiki id 48644]`

For this, it is enough to define the variable image by Option in the definition of the image object itself in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836):

`[imagen omitida: wiki id 48645]`

The GeneXus Image object named Chatbot is varied by Style (DSO), image density, and color-scheme option.

`[imagen omitida: wiki id 48646]`

**Note:** since it is not yet possible to set which DSO design options will be the default values (in this case, the default color-scheme should be Light), it will not know which image to show in the layout and therefore the following will be displayed instead of the image:

`[imagen omitida: wiki id 48648]`

```
Event Start
    &Background_HeroImg = HomeHeroImage.GetInternalURI()
    HeroTitle.Caption = "Get ready to Explore"
    Textblock1.Caption = "The new age of <br/> EXPLORATION"
    &option = "Light"
    DesignSystem.SetOption("color-scheme", &option)
Endevent

Event &Background_HeroImg.Click
    &option = iif(&option = "Dark", "Light", "Dark")
    DesignSystem.SetOption("color-scheme", &option)
Endevent
```

[Here](https://wiki.genexus.com/commwiki/wiki?52496,,) you can download a ZIP file with an XPZ and the images for the chatbot.

### [See Also](#See+Also)

[GetInternalURI method](https://wiki.genexus.com/commwiki/wiki?52480)


|  |
| --- |
| **Backlinks** |
| [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) | [GetInternalURI method](https://wiki.genexus.com/commwiki/wiki?52480) | [Options property](https://wiki.genexus.com/commwiki/wiki?48091) |

---
