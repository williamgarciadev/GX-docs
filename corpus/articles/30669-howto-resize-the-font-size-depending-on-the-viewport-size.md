---
title: "HowTo: Resize the font size depending on the viewport size"
source_id: 30669
source_url: https://wiki.genexus.com/commwiki/wiki?30669
genexus_version: "18"
---

# HowTo: Resize the font size depending on the viewport size

[Viewport units](https://wiki.genexus.com/commwiki/wiki?30636) can be used on text to automatically change the font size depending on the viewport.

This could be very useful when you need to comply with [Accessibility for Web Applications](https://wiki.genexus.com/commwiki/wiki?30632) issues.

In this example, the font-size has been set in [vmax](https://www.w3.org/TR/css3-values/#Viewport-relative-lengths) [unit](https://www.w3.org/TR/css3-values/#Viewport-relative-lengths), creating the following responsive effect for the text:

`[imagen omitida: wiki id 32495]`

In GeneXus, the attribute's Class property is set to "AttributeBigFonts" class.

`[imagen omitida: wiki id 30670]`

The AttributeBigFonts has its [Label Class property](https://wiki.genexus.com/commwiki/wiki?28631,,) set to LabelBigFonts, which is a descendant class of Textblock. The LabelBigFonts Font-Size property is set to 2vmax, as shown in the picture below.

`[imagen omitida: wiki id 30671]`


|  |
| --- |
| **Backlinks** |
| [Using relative length units on the web](https://wiki.genexus.com/commwiki/wiki?30636) |

---
