---
title: "FontUnderline property"
source_id: 8780
source_url: https://wiki.genexus.com/commwiki/wiki?8780
genexus_version: "18"
---

# FontUnderline property

Determines the font style in the control with an Underline in it.

### [Syntax](#Syntax)

**control.** FontUnderline = value   

**Where:**  
  
*control*  
    Is the name of a control inserted in the form.

#### Values

|  |  |
| --- | --- |
| **0 (False)** | Turns off the formatting in that style. |
| **1 (True)** | Turns on the formatting in that style. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** Attribute/Variable (Control Type: Check Box, Combo Box, [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598), [Dynamic List Box](https://wiki.genexus.com/commwiki/wiki?7599), Edit, List Box, Radio Button)

### [Description](#Description)

It is only considered if the [FontStrikethru property](https://wiki.genexus.com/commwiki/wiki?8779) is set to 0 (disabled).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at runtime.

### [Samples](#Samples)

```
txtctrl.FontUnderline = 1
```

where txtctrl is the name of a text control.

### [See Also](#See+Also)

[FontItalic property](https://wiki.genexus.com/commwiki/wiki?8776)  
[FontName property](https://wiki.genexus.com/commwiki/wiki?8777)  
[FontBold property](https://wiki.genexus.com/commwiki/wiki?8775)  
[FontSize property](https://wiki.genexus.com/commwiki/wiki?8778)  
[FontStrikethru property](https://wiki.genexus.com/commwiki/wiki?8779)  
[HowTo: Format plain text programmatically](https://wiki.genexus.com/commwiki/wiki?31657)


|  |
| --- |
| **Backlinks** |
| [Font property](https://wiki.genexus.com/commwiki/wiki?8774) | [FontBold property](https://wiki.genexus.com/commwiki/wiki?8775) | [FontItalic property](https://wiki.genexus.com/commwiki/wiki?8776) |
| [FontName property](https://wiki.genexus.com/commwiki/wiki?8777) | [FontSize property](https://wiki.genexus.com/commwiki/wiki?8778) | [FontStrikethru property](https://wiki.genexus.com/commwiki/wiki?8779) |

---
