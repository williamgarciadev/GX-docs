---
title: "Scroll Factor property"
source_id: 29874
source_url: https://wiki.genexus.com/commwiki/wiki?29874
genexus_version: "18"
---

# Scroll Factor property

Indicates the Scroll Factor of a Table or Canvas regarding the control it is attached to.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [Canvas](https://wiki.genexus.com/commwiki/wiki?22452), [Table](https://wiki.genexus.com/commwiki/wiki?6001)

### [Description](#Description)

This property is available for [Table](https://wiki.genexus.com/commwiki/wiki?6001) and [Canvas](https://wiki.genexus.com/commwiki/wiki?22452) controls included in [Panels](https://wiki.genexus.com/commwiki/wiki?24829) and [Work With patterns and Work With objects](https://wiki.genexus.com/commwiki/wiki?15974).

The default value for this property is 1; it indicates the default behavior of the control (scrolling pixel by pixel). A different value gives the illusion of depth to the end user when they move multiple layers at different speeds.

The relationship between the control that contains the table and the table itself is as follows: if the control shifts N-pixels, the table with the Scroll Factor property set to M shifts N\*M-pixels.

*Note*: It is frequently used with the [Zoom Factor property](https://wiki.genexus.com/commwiki/wiki?29876) to simulate a [Parallax Effect](https://en.wikipedia.org/wiki/Parallax_scrolling).

### [See Also](#See+Also)

[Scroll Attachment property](https://wiki.genexus.com/commwiki/wiki?29875)


|  |
| --- |
| **Backlinks** |
| [Scroll Attachment property](https://wiki.genexus.com/commwiki/wiki?29875) | [Scroll behavior properties group](https://wiki.genexus.com/commwiki/wiki?31174) | [Zoom Factor property](https://wiki.genexus.com/commwiki/wiki?29876) |

---
