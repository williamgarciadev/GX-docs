---
title: "Property Name property"
source_id: 57843
source_url: https://wiki.genexus.com/commwiki/wiki?57843
genexus_version: "18"
---

# Property Name property

Sets the name used to display the Type node of the External Object in the properties added to the External Object's type variables.

### [Scope](#Scope)

**Objects:** [External Object](https://wiki.genexus.com/commwiki/wiki?5669)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

When defining an External Object that includes one or more [Type nodes](https://wiki.genexus.com/commwiki/wiki?57997), it is essential to set the Property Name for each defined Type. This setting allows the name specified in Property Name to be visible in the properties of the External Object's type variables.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Suppose you define an External Object called GenericDictionary with the structure shown in the image:

`[imagen omitida: wiki id 57999]`

As you can see in the image below, the value Key has been set in the Property Name for TypeKey. Similarly, for TypeValue, Value has been set in the Property Name.

`[imagen omitida: wiki id 58000]` `[imagen omitida: wiki id 58003]`

When you define a variable of GenericDictionary type, the following is displayed:

`[imagen omitida: wiki id 58002]`

If you change the values of these properties, as shown in the image below:

`[imagen omitida: wiki id 58004]``[imagen omitida: wiki id 58005]`

You can see the following in the variable properties:

`[imagen omitida: wiki id 58006]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

No action is required to apply the corresponding changes when the property value is configured.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).


|  |
| --- |
| **Backlinks** |
| [External Object Types Node](https://wiki.genexus.com/commwiki/wiki?57997) | [External Objects with Type property 'Native Object'](https://wiki.genexus.com/commwiki/wiki?6148) |

---
