---
title: "Title property"
source_id: 7234
source_url: https://wiki.genexus.com/commwiki/wiki?7234
genexus_version: "18"
---

# Title property

Determines the title of a control.

### [Syntax](#Syntax)

**control.** Title = Value   

Type returned: Text

**Where:**

*control*

The control name.

*Value*

A character to be assigned.

### [Description](#Description)

In columns is used to determine the title of the grid’s columns at execution time (Column title). In attributes is used in flat structures, such as first level of a Transaction, descriptions of variables in Prompts and report titles. When using a chart associated to a [Query object](https://wiki.genexus.com/commwiki/wiki?9026) or [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) it specifies the chart title (supported since [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,)).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [Samples](#Samples)

```
Gridcol1.Title = 'Description'
```

### [Scope](#Scope)

**Objects:** Procedure, Transaction, Web Panel  
**Controls:** Grid


|  |
| --- |
| **Backlinks** |
| [Category:Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802) | [Description property](https://wiki.genexus.com/commwiki/wiki?7446) |
| [Full Text Search example 1](https://wiki.genexus.com/commwiki/wiki?6024) | [HowTo: Use Charts Control](https://wiki.genexus.com/commwiki/wiki?16106) | [Query Object Compatibility](https://wiki.genexus.com/commwiki/wiki?11032) | [Query Object Properties](https://wiki.genexus.com/commwiki/wiki?18471) |
| [QueryViewer control properties](https://wiki.genexus.com/commwiki/wiki?32920) |

---
