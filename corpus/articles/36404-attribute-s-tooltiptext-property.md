---
title: "Attribute's Tooltiptext property"
source_id: 36404
source_url: https://wiki.genexus.com/commwiki/wiki?36404
genexus_version: "18"
---

# Attribute's Tooltiptext property

Assigns a text to be displayed when the cursor is placed over any part of a control.

### [Syntax](#Syntax)

**control.** TooltipText = Expression   

Type returned: Text

**Where:**  
*Control*  
    is the name of an attribute.

*Expression*  
    is the text to be displayed when the cursor is placed over any part of the control.

### [Description](#Description)

It is a brief description (usually a single line) of the content of an attribute which is displayed as a small window while the mouse pointer hovers over the corresponding item. This property can be changed at run-time.

### [Samples](#Samples)

```
&CustomerDetail.TooltipText = 'Type a customer’s detailed information here'
```

In this example, when the cursor is positioned over the *&CustomerDetail* control, the specified text ('*Type a customer's detailed information here*') will be displayed.

### [Scope](#Scope)

**Platforms:** Web(.Net, Java)  
**Controls:** Attribute

### [See Also](#See+Also)

[Tooltiptext property](https://wiki.genexus.com/commwiki/wiki?4840)
