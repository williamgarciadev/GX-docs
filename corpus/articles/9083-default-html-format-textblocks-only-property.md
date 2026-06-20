---
title: "Default HTML Format (TextBlocks only) property"
source_id: 9083
source_url: https://wiki.genexus.com/commwiki/wiki?9083
genexus_version: "18"
---

# Default HTML Format (TextBlocks only) property

Sets the default value of the [Format property](https://wiki.genexus.com/commwiki/wiki?31666) for [Text Block control](https://wiki.genexus.com/commwiki/wiki?5948)s.

### [Values](#Values)

|  |  |
| --- | --- |
| **Text** | The default Format value for Text Blocks will be Text, so the content of the Text Block controls will be interpreted as text by default. |
| **HTML** | The default Format value for Text Blocks will be HTML, so the content of the Text Blocks controls will be interpreted as HTML code. |
| **RawHtml** | The default Format value for Text Blocks will be RawHTML, so the content of the Text Blocks will be interpreted in the same way as HTML, but the content will not appear between the tags <SPAN></SPAN>. You will not be able to modify the control value from a User Event. |
| **Text with meaningful spaces** | The default Format value for Text Blocks will be “Text with meaningful spaces” which is the same as “Text”, except that leading spaces and spaces in the middle of a sentence are shown as they are. In the case of “Text” value, two or more spaces will be interpreted as only one. |

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

Rebuild all objects

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Controls** | [Text Block control](https://wiki.genexus.com/commwiki/wiki?5948) in Transactions and Web Panels |
| **Languages** | .NET, .NET Framework, Java |
|  |  |

### [See also](#See+also)

[Format property (for Web)](https://wiki.genexus.com/commwiki/wiki?31666)


|  |
| --- |
| **Backlinks** |
| [Work With for Web Selection Node](https://wiki.genexus.com/commwiki/wiki?5640) |

---
