---
title: "Use Domain Descriptions property"
source_id: 47098
source_url: https://wiki.genexus.com/commwiki/wiki?47098
genexus_version: "18"
---

# Use Domain Descriptions property

Uses domain descriptions instead of the actual values from the database for the attribute.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Query](https://wiki.genexus.com/commwiki/wiki?9026)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)

### [Description](#Description)

For attributes based on a domain with enumeration values, it is possible to indicate through this property whether to use the domain enumeration descriptions instead of the actual values of the attribute stored in the data base.

This property is valid only for attributes but not for expressions involving these attributes. It can be used in attributes returned by the query itself or in attributes used to order the result of the query.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

Suppose there is an attribute *CustomerSex* based on a Domain as follows:

```
1: Male
2: Female
```

`[imagen omitida: wiki id 47187]`

The property enable to use and order by database values or enumerated descriptions.

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,).
