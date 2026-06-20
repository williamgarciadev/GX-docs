---
title: "Base Control Type property"
source_id: 40586
source_url: https://wiki.genexus.com/commwiki/wiki?40586
genexus_version: "18"
---

# Base Control Type property

Specifies the "base control type" to which your user control belongs.

### [Values](#Values)

|  |  |
| --- | --- |
| **Button** | The "base control type" of the user control is Button. |
| **CheckBox** | The "base control type" of the user control is CheckBox. |
| **ComboBox** | The "base control type" of the user control is ComboBox. |
| **Edit** | The "base control type" of the user control is Edit. |
| **ErrorViewer** | The "base control type" of the user control is ErrorViewer. |
| **Grid** | The "base control type" of the user control is Grid. |
| **Group** | The "base control type" of the user control is Group. |
| **HorizontalRule** | The "base control type" of the user control is HorizontalRule. |
| **HyperLink** | The "base control type" of the user control is HyperLink. |
| **Image** | The "base control type" of the user control is Image. |
| **ListBox** | The "base control type" of the user control is ListBox. |
| **None** | No "base control type" is set. |
| **RadioButton** | The "base control type" of the user control is RadioButton. |
| **Section** | The "base control type" of the user control is Section. |
| **Tab** | The "base control type" of the user control is Tab. |
| **Table** | The "base control type" of the user control is Table. |
| **TextBlock** | The "base control type" of the user control is TextBlock. |

### [Scope](#Scope)

**Objects:** [User Control](https://wiki.genexus.com/commwiki/wiki?39356)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

To create a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) that mimics the behavior of some of the standard controls provided by your Base Library, use this user control property in order to choose the base control type.

When you select Button as Base Type for your control, the following properties will be inherited:

* Caption (to set the button caption)
* OnClickEvent (to define the event associated with the click event)

#### [How do you specify when the OnClickEvent is raised and where the Caption is used?](#How+do+you+specify+when+the+OnClickEvent+is+raised+and+where+the+Caption+is+used%3F)

Use {{OnClickEvent}} in the HTML tag where you want to raise the event. And just use {{Caption}} as any other user-defined property to define a caption.

For example, in the Screen Template tab of your [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) set the following:

```
<div {{OnClickEvent}} > {{Caption}} </div>
```

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |

---
