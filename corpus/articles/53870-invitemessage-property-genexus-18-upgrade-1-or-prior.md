---
title: "InviteMessage property (GeneXus 18 Upgrade 1 or prior)"
source_id: 53870
source_url: https://wiki.genexus.com/commwiki/wiki?53870
genexus_version: "18"
---

# InviteMessage property (GeneXus 18 Upgrade 1 or prior)

Sets a message that will be shown for the field to invite the user to enter specific data.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?49815,,), [.NET Core](https://wiki.genexus.com/commwiki/wiki?49825,,)  
**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [Description](#Description)

The fields in forms include a label that is usually located to the left of the field.

In some cases, it is better to have a suggestion for filling in the field (such as during the entry of forms) or to show, by way of an example, the type of data or the format of the data to be loaded in it.

In text boxes, this is normally solved by placing a gray text inside the text box that vanishes upon being focused on or when a value is entered.

### [Samples](#Samples)

In the following image, you can see on the left, an attribute **InviteMessage property** filled with the text “Enter your name”. On the left side, you can see the result in runtime.

`[imagen omitida: wiki id 19698]`

There are cases where, despite not being their primary use, this may be used as an alternative to labels.

`[imagen omitida: wiki id 19699]`

### [[Notes](https://wiki.genexus.com/commwiki/wiki?19697)](#https%3A%2F%2Fwiki.genexus.com%2Fcommwiki%2Fservlet%2Fwiki%3F19697%2CInvite%2520Message%2520property%23Notes+Notes)

* In order to show the invite message for Numeric attributes/variables definition, you must ensure that its [Picture property](https://wiki.genexus.com/commwiki/wiki?36522) has 'ZZZZ' value.  
  Otherwise, the value 0 is displayed instead of the invite message.
* As of [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?33798,,), this property is also available for Image-based variables/attributes in Smart Device Generator. By default has the same value of [Label caption property](https://wiki.genexus.com/commwiki/wiki?28626) and it is shown above the editable image field (e.g. if it has a custom [Placeholder image](https://wiki.genexus.com/commwiki/wiki?20460))
* The invite message property is only generated if at the environment level, the [HTML Document Type property](https://wiki.genexus.com/commwiki/wiki?13517) is set: HTML5

**Warning**: For Smart Devices generator, when the Invite Message property has the same value as [Caption property](https://wiki.genexus.com/commwiki/wiki?4633), and [Label Position property](https://wiki.genexus.com/commwiki/wiki?34141) is None, the label won't be displayed but the invite message does.

The option is only available when the control is not read-only.
