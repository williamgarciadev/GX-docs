---
title: "Numeric values in the RTL interface for Apple"
source_id: 54480
source_url: https://wiki.genexus.com/commwiki/wiki?54480
genexus_version: "18"
---

# Numeric values in the RTL interface for Apple

When using numeric values in an Edit control, it is automatically transformed to a string using the [NSNumberFormatter class](https://developer.apple.com/documentation/foundation/nsnumberformatter) using the current language locale. It means that by default Arabic numbers will be displayed in a read-only interface. To display characters in another language, use a String variable and format it with the desired language. The following example shows the default LTR interface on the left side and the same one in RTL mode; notice the mirroring of the numbers and presentation changes.

`[imagen omitida: wiki id 42506]`


|  |
| --- |
| **Backlinks** |
| [Toc:Getting ready for Right-to-Left Development](https://wiki.genexus.com/commwiki/wiki?42322) |

---
