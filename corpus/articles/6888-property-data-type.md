---
title: "Property Data Type"
source_id: 6888
source_url: https://wiki.genexus.com/commwiki/wiki?6888
genexus_version: "18"
---

# Property Data Type

This data type is used when iterating through a [Properties](https://wiki.genexus.com/commwiki/wiki?6889,,) variable.

### [Properties](#Properties)

|  |  |
| --- | --- |
| Key | Returns the key of the property |
| Value | Returns the value of the property |

### [Iterating properties](#Iterating+properties)

In order to read all the properties stored in a Properties variable, the Property data type must be used as follows:

E.g.

```
for &Property in &myProperties
    msg(&Property.Key)
    msg(&Property.Value)
endfor
```

where *&myProperties* has [Properties Data Type](https://wiki.genexus.com/commwiki/wiki?31606).

### [Scope](#Scope)

**Objects:** [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916)  
**Languages:** Java, .NET, Ruby (up to GeneXus X Evolution 3)  
**Interfaces:** Web


|  |
| --- |
| **Backlinks** |
| [Category:Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [Properties Data Type](https://wiki.genexus.com/commwiki/wiki?31606) |

---
