---
title: "Data Selector property"
source_id: 5361
source_url: https://wiki.genexus.com/commwiki/wiki?5361
genexus_version: "18"
---

# Data Selector property

Indicates the name of a Data Selector object defined in the Knowledge Base.

### [Scope](#Scope)

**Objects:** [Data Selector](https://wiki.genexus.com/commwiki/wiki?5271)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058), [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449)   
**Level:** [Work With Pattern Instance](https://wiki.genexus.com/commwiki/wiki?15974)

### [Description](#Description)

This property allows you to indicate the name of a [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) defined in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) or the "none" value.

When you complete this property, the Data Selector definition is combined with the Grid that references it (or with the Data Selector that references it) to determine the resulting navigation, **which will be a combination of both (Data Selector definition + Grid definition or Data Selector definition + Data Selector definition)**.

When used in a Data Selector, the property value cannot generate a recursive reference either directly or indirectly.

**Note:** This property is also available for the [Work With List Node](https://wiki.genexus.com/commwiki/wiki?15984) (because this node corresponds to the Grid associated with the WW List).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Data Selectors in Grids](https://wiki.genexus.com/commwiki/wiki?5386)  
[Data Selectors in Aggregations](https://wiki.genexus.com/commwiki/wiki?5432)  
[Data Selectors in Data Providers](https://wiki.genexus.com/commwiki/wiki?6501)  
[Data Selectors in For Each command](https://wiki.genexus.com/commwiki/wiki?5312)


|  |
| --- |
| **Backlinks** |
| [Composition (nesting) of Data Selectors](https://wiki.genexus.com/commwiki/wiki?5835) | [Data Selector property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57171) | [Data Selectors in Grids](https://wiki.genexus.com/commwiki/wiki?5386) |
| [Data Selectors in Grids (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57179) | [Using Data Selectors - Examples](https://wiki.genexus.com/commwiki/wiki?5384) |

---
