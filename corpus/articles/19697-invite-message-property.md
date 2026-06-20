---
title: "Invite Message property"
source_id: 19697
source_url: https://wiki.genexus.com/commwiki/wiki?19697
genexus_version: "18"
---

# Invite Message property

Sets a message that will be shown for the field to invite the user to enter specific data.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [Description](#Description)

This property allows entering a text that will be shown for the field to inform the kind of information that is expected.

In text boxes, this is generally solved by placing a gray text inside the text box that disappears when the focus is on it or when a value is entered.

The property is used when the control is not read-only.

#### [**Considerations**](#Considerations)

* In order to show the invite message for Numeric attribute/variable definitions, you must ensure that their [Picture property](https://wiki.genexus.com/commwiki/wiki?36522) has the 'ZZZZ' value.  
  Otherwise, the value 0 is displayed instead of the invite message.
* The **Invite Message property** is only generated if, at the environment level, the [HTML Document Type property](https://wiki.genexus.com/commwiki/wiki?13517) is set to HTML5.
* For the Native Mobile generator, when the **Invite Message property** has the same value as the [Caption property](https://wiki.genexus.com/commwiki/wiki?4633), and the [Label Position property](https://wiki.genexus.com/commwiki/wiki?34141) is None, the label won't be displayed. Only the invite message will be shown.

Since [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396), this property is taken into account for [Wheel Control for Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?20180).

### [Samples](#Samples)

In the following example, you can see the **InviteMessage property** of the CustomerName attribute filled with the text “Enter your name”:

`[imagen omitida: wiki id 53871]`

The result at runtime is as follows:

`[imagen omitida: wiki id 53872]`

There are cases where this may be used as an alternative to labels.

`[imagen omitida: wiki id 19699]`


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396) | [InviteMessage property (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53870) | [Label Position property](https://wiki.genexus.com/commwiki/wiki?34141) |

---
