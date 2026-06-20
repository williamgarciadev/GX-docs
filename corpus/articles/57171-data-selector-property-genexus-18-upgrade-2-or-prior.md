---
title: "Data Selector property (GeneXus 18 Upgrade 2 or prior)"
source_id: 57171
source_url: https://wiki.genexus.com/commwiki/wiki?57171
genexus_version: "18"
---

# Data Selector property (GeneXus 18 Upgrade 2 or prior)

Indicates the name of a Data Selector object defined in the Knowledge Base.

### [Scope](#Scope)

**Objects:** [Data Selector](https://wiki.genexus.com/commwiki/wiki?5271)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058)

### [Description](#Description)

This property allows you to indicate the name of a [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) defined in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), in addition to the "none" value.

When you complete this property, the Data Selector definition is combined with the Grid that references it (or with the Data Selector that references it) to determine the resulting navigation, **which will be a combination of both (Data Selector definition + Grid definition or Data Selector definition + Data Selector definition)**.

When used in a Data Selector, the property value cannot generate a recursive reference either directly or indirectly.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Data Selectors in Grids](https://wiki.genexus.com/commwiki/wiki?5386)  
[Data Selectors in Aggregations](https://wiki.genexus.com/commwiki/wiki?5432)  
[Data Selectors in Data Providers](https://wiki.genexus.com/commwiki/wiki?6501)
