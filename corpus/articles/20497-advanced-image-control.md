---
title: "Advanced Image Control"
source_id: 20497
source_url: https://wiki.genexus.com/commwiki/wiki?20497
genexus_version: "18"
---

# Advanced Image Control

Images are very common in applications, and the users of these apps are used to being able to manipulate them. For example, zoom in/out, scroll inside the image, copy the image, etc.

[GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) has a control that enables this behavior for our images in a Smart Device application.

### [Using the control](#Using+the+control)

On the [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) (WWSD) or [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) (SDPanel), select the node which has the image attribute or variable. For example, the Section(General) node inside the Detail node of the WorkWithDevicesProperty (the WWSD applied to the Property transaction, a transaction created to handle the houses and appartments in sale or rent by a real estate), we change the width of the row corresponding to the front image of the property, and then change the [Control Type](https://wiki.genexus.com/commwiki/wiki?9550) of that attribute:

`[imagen omitida: wiki id 20498]`

### [Properties](#Properties)

|  |  |
| --- | --- |
| **Enable Zoom** | True/False. If this property is true, the user can zoom in/out on the image. |
| **Max Zoom** | Indicates how much you can enlarge an image. (Percentage). |
| **Max Zoom Relative To** | Indicates how much you can enlarge an image with reference to the original size of it or the size of the controller. (Percentage) |
| **Enable Copy To Clipboard** | If this property is true, the user can copy the image to the clipboard (Only for iOS, see image below). |

`[imagen omitida: wiki id 20499]`


|  |
| --- |
| **Backlinks** |
| [Category:Control Types](https://wiki.genexus.com/commwiki/wiki?20402) | [Enable Copy To Clipboard property](https://wiki.genexus.com/commwiki/wiki?46557) | [Enable Copy To Clipboard property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57272) |
| [Enable Zoom property](https://wiki.genexus.com/commwiki/wiki?46466) | [Enable Zoom property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57238) |
| [Max Zoom property](https://wiki.genexus.com/commwiki/wiki?46472) | [Max Zoom property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57273) | [Max Zoom Relative To property](https://wiki.genexus.com/commwiki/wiki?46574) | [Max Zoom Relative To property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57252) |
| [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Zoom Outside Control property](https://wiki.genexus.com/commwiki/wiki?43486) | [Zoom Outside Control property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57270) |

---
