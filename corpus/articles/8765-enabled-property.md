---
title: "Enabled property"
source_id: 8765
source_url: https://wiki.genexus.com/commwiki/wiki?8765
genexus_version: "18"
---

# Enabled property

Determines whether the control is enabled or not.

### [Syntax](#Syntax)

**control.** enabled = value   

Type returned: Boolean

**Where**

*Control*

Is the name of a control inserted in the form, or the form itself in case of Win interfaces.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Description](#Description)

When disabled, it prevents the user from interacting with the control. This property only applies to the User interface.

It applies to the following Controls: Bitmaps, Buttons, Check Boxes, Combo Boxes, Dynamic Combo Boxes, Dynamic List Boxes, Edits, Forms, List Boxes, Radio Buttons, Texts Blocks.

### [Samples](#Samples)

Transaction rules

```
EvtBtn.Enabled = True If Update; // The button is disabled if in update mode (EvtBtn is button control).
Att2.Enabled = False If Not Null(Att1); // Attribute Att2 cannot be edited if attribute Att1 is not null.
```

WebPanel events

```
Event 'SampleEvent'
  If (&Variable.isEmpty())
    ControlName.Enabled = false
  else
    ControlName.Enabled = true
  EndIf
EndEvent
```

### [Scope](#Scope)

**Objects:** Transaction, Web Panel  
**Platforms:** Web(.Net, Java)

### [See Also](#See+Also)

[NoAccept rule](https://wiki.genexus.com/commwiki/wiki?6856)


|  |
| --- |
| **Backlinks** |
| [NoAccept rule](https://wiki.genexus.com/commwiki/wiki?6856) | [ReadOnly property](https://wiki.genexus.com/commwiki/wiki?8826) | [Tab Page Control for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?25638) |

---
