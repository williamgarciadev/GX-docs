---
title: "Rendering Mode property in Images"
source_id: 23135
source_url: https://wiki.genexus.com/commwiki/wiki?23135
genexus_version: "18"
---

# Rendering Mode property in Images

Indicates how to draw an image.

### [Values](#+Values)

|  |  |
| --- | --- |
| **Automatic (Default)** | The image behaves differently depending on the context in which it is used. When used in the toolbar, tabs, or buttons, it behaves as if the "Template" value was selected. Otherwise, it behaves as if the "Original" value was chosen. |
| **Original** | The image will be drawn as it is (using all the color channels and the alpha channel). |
| **Template** | Only the alpha channel of the image will be used and the 100% opaque pixels will be painted with the [Key Color](https://wiki.genexus.com/commwiki/wiki?23130). |

### [Scope](#Scope)

**Objects:**[Image object](https://wiki.genexus.com/commwiki/wiki?23387)

### [Description](#Description)

[Image object](https://wiki.genexus.com/commwiki/wiki?23387)s have two modes to be drawn: Original and Template.

There is also a third mode called Automatic that works depending on the context.

### [Run-time/Design-time](#Run-time%2FDesign-time)

This property applies only at design time.

### [Sample](#Sample)

|  |  |
| --- | --- |
| Original | Template |
|  |  |

### [Availability](#Availability)

Rendering Mode is available for iOS as of [GeneXus X Evolution 2 Upgrade 4](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22626,,) for iOS 7.

### [See Also](#See+Also)

[iOS 7 Overview](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?23121,,)


|  |
| --- |
| **Backlinks** |
| [DesignOps - FAQ and Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46880) | [Category:Image object](https://wiki.genexus.com/commwiki/wiki?23387) |

---
