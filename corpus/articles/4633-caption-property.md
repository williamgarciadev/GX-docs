---
title: "Caption property"
source_id: 4633
source_url: https://wiki.genexus.com/commwiki/wiki?4633
genexus_version: "18"
---

# Caption property

Indicates the text to be displayed for a control.

### [Syntax](#Syntax)

**control.** Caption = Expression

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [Button](https://wiki.genexus.com/commwiki/wiki?6011), [Text Block](https://wiki.genexus.com/commwiki/wiki?5948)

### [Description](#Description)

The Caption property is used to indicate the text to be displayed for a control (or to obtain the assigned text).

Its value can be set either at design time or runtime.

For values that can be set at design time, see [Dynamic Property Values](https://wiki.genexus.com/commwiki/wiki?4835).

At runtime:

* Any character expression can be assigned to it.
* It may be used in:
  + The Start event of an object.
  + The Refresh event of an object.
  + User events defined in an object.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at runtime and at design time.

### [Samples](#Samples)

The following rules are defined in a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Form.Caption = 'My Form - Update' if update;
Form.Caption = 'My Form - Delete' if delete;
Form.Caption = 'My Form - Insert' if insert;
```

In this example, the Form's title will change depending on the current mode (insert, delete, or update).


|  |
| --- |
| **Backlinks** |
| [Button control](https://wiki.genexus.com/commwiki/wiki?6011) |
| [Button properties](https://wiki.genexus.com/commwiki/wiki?9916) | [Caption property for the Selection Node of a Work With for Web Pattern instance](https://wiki.genexus.com/commwiki/wiki?52694) | [Font All Caps property (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56518) | [Form Control](https://wiki.genexus.com/commwiki/wiki?14619) |
| [Group control](https://wiki.genexus.com/commwiki/wiki?6570) | [HowTo: Use Tab Control in Panels](https://wiki.genexus.com/commwiki/wiki?16800) | [HowTo: Use Textblock in Panels](https://wiki.genexus.com/commwiki/wiki?18491) |
| [Invite Message property](https://wiki.genexus.com/commwiki/wiki?19697) | [InviteMessage property (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53870) | [Text Block properties](https://wiki.genexus.com/commwiki/wiki?9908) | [text-transform property](https://wiki.genexus.com/commwiki/wiki?40682) |

---
