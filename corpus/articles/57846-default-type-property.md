---
title: "Default Type property"
source_id: 57846
source_url: https://wiki.genexus.com/commwiki/wiki?57846
genexus_version: "18"
---

# Default Type property

Sets the default data type to be used when no other data type is specified.

### [Scope](#Scope)

**Objects:** [External Object](https://wiki.genexus.com/commwiki/wiki?5669)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

When defining a variable of External Object type that includes one or more [Type nodes](https://wiki.genexus.com/commwiki/wiki?57997), a data type must be selected from the list available for each defined Type. If no data type is specified, the variable will automatically use the value set in the Default Type property.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Suppose you define an External Object called GenericDictionary with the structure shown in the image:

`[imagen omitida: wiki id 57999]`

As you can see in the following image, VarChar has been set as Default Type for TypeValue.

`[imagen omitida: wiki id 58003]`

When you define a GenericDictionary type variable, the default value of TypeValue is VarChar.

`[imagen omitida: wiki id 58002]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

No action is required to apply the corresponding changes when the property value is configured.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).


|  |
| --- |
| **Backlinks** |
| [External Object Types Node](https://wiki.genexus.com/commwiki/wiki?57997) | [External Objects with Type property 'Native Object'](https://wiki.genexus.com/commwiki/wiki?6148) |

---
