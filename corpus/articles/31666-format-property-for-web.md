---
title: "Format property (for Web)"
source_id: 31666
source_url: https://wiki.genexus.com/commwiki/wiki?31666
genexus_version: "18"
---

# Format property (for Web)

Indicates if the contents of the control must be interpreted as text or as HTML code.

### [Syntax](#Syntax)

**control.** Format

### [Values](#Values)

|  |  |
| --- | --- |
| **Text** | The content of the control will be interpreted as text. Leading spaces are ignored. Two or more spaces are interpreted as only one. This is the default value. |
| **HTML** | The content of the control will be interpreted as HTML code. |
| **Raw HTML** | The same as HTML, but the content will not appear within the SPAN tag. Use this option when you need to add HTML and you do not want to apply any style to it. It is used on the Web. |
| **Text with meaningful spaces** | It’s the same as “Text,” except that leading spaces and spaces in the middle of a sentence are shown as they are. In the case of “Text” value, two or more spaces are interpreted as only one. It is used on the Web. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** Attribute/Variable, [Button](https://wiki.genexus.com/commwiki/wiki?6011), [Text Block](https://wiki.genexus.com/commwiki/wiki?5948)

### [Description](#Description)

In the case of Attributes, the format property of the controls associated with the Attribute will inherit the value of this property (which can be modified using the Format property of the control).

This property is enabled only when the Read-only property is enabled and can be used at design and execution time.

#### [Considerations](#Considerations)

When using the RawHTML option, and when executing a User Event it is not possible to modify its value.  
RawHTML option means that the developer is in charge of the code in the control. GeneXus does not include the content of a container; later on, GX cannot locate it at runtime. If you need to change its value in a User Event, use the HTML option.

### [Samples](#Samples)

A Text Block contains the string "<b>Hello</b>".  
If the Format property has the ‘HTML’ value, you will view the text Hello in ‘Bold’ at runtime, like this: **Hello**  
If the property has the ‘Text’ value, you will view the whole string, including the HTML tags, like this: <b>Hello</b>

Control.Format = 1    // HTML format

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Extended Data Types Read-Only property](https://wiki.genexus.com/commwiki/wiki?2565)  
[TitleFormat Property](https://wiki.genexus.com/commwiki/wiki?8785,,)  
[Format property](https://wiki.genexus.com/commwiki/wiki?46309)


|  |
| --- |
| **Backlinks** |
| [Attribute/Variable control properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8133) | [Default HTML Format (TextBlocks only) property](https://wiki.genexus.com/commwiki/wiki?9083) | [Format property](https://wiki.genexus.com/commwiki/wiki?46309) |
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |
| [Text Block properties](https://wiki.genexus.com/commwiki/wiki?9908) |

---
