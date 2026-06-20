---
title: "Allow Collection property"
source_id: 57845
source_url: https://wiki.genexus.com/commwiki/wiki?57845
genexus_version: "18"
---

# Allow Collection property

Indicates whether the Type node of the External Object can be a collection.

### [Values](#Values)

|  |
| --- |
| **True** |
| **False** |

### [Scope](#Scope)

**Objects:** [External Object](https://wiki.genexus.com/commwiki/wiki?5669)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

When defining an External Object that contains one or more [Type nodes](https://wiki.genexus.com/commwiki/wiki?57997), you can specify whether each Type is a collection or not by setting the corresponding value in the Allow Collection property.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Suppose you define an External Object called GenericDictionary with the structure shown in the image:

`[imagen omitida: wiki id 57999]`

In the following image, you can see that TypeKey is not a collection.

`[imagen omitida: wiki id 58000]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

No action is required to apply the corresponding changes when the property value is configured.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).


|  |
| --- |
| **Backlinks** |
| [External Object Types Node](https://wiki.genexus.com/commwiki/wiki?57997) | [External Objects with Type property 'Native Object'](https://wiki.genexus.com/commwiki/wiki?6148) |

---
