---
title: "Json Null Serialization property"
source_id: 36980
source_url: https://wiki.genexus.com/commwiki/wiki?36980
genexus_version: "18"
---

# Json Null Serialization property

Selects whether a null value should be serialized as empty or not at all.

### [Values](#Values)

|  |  |
| --- | --- |
| **Empty** | The null value of an SDT member will be serialized as an empty item. |
| **JSON null** | The null value of an SDT member will be serialized as null. |
| **No Property** | The null value of an SDT member isn't serialized at all. |

### [Scope](#Scope)

**Objects:** [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021)

### [Description](#Description)

The purpose of this property is to determine how to serialize a structure or member of a [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) to a JSON when that structure or member is empty.

It can be serialized as an empty item or list, or not serialized at all.

The property applies to structures or members of a Structured Data Type. The default value for members that are items is 'Empty' and for others is 'No Property'.

Note: Since [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/wiki?40782,,), this property applies also to items.

### [Samples](#Samples)

Suppose that you have an SDT where there is a member (b) which is a collection.

`[imagen omitida: wiki id 37036]`

If b has **Json** **Null Serialization property** set to empty, the result of doing &SDT1.toJson will be :

```
{"a":1,"b":[]}
```

If b has **Json**  **Null Serialization property** set to No Property, the resulting JSON will be:

```
{"a":1}
```

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?36778,,).

### [See Also](#See+Also)

[XML Null Serialization property (SDT)](https://wiki.genexus.com/commwiki/wiki?14497)
