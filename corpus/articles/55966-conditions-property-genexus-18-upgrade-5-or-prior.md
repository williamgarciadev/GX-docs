---
title: "Conditions property (GeneXus 18 Upgrade 5 or prior)"
source_id: 55966
source_url: https://wiki.genexus.com/commwiki/wiki?55966
genexus_version: "18"
---

# Conditions property (GeneXus 18 Upgrade 5 or prior)

Defines filter(s) to be taken into account when navigating records that will be loaded in the Grid / Grid Free Style.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058)

### [Description](#Description)

A condition is a logical expression (its evaluation is True or False) that may include attributes, constant values, variables, functions, and other expressions. Attributes must belong to the [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029) of the [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) where the condition is applied.

**Note**:  
This property applies to the individual [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) / [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058) for which it is defined. It must not be confused with the *Conditions tab* of the GeneXus object (whose aim is to apply filters to the whole object: form, all the Grids, etc.).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Consider a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) containing the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

```
Neighborhood
{ 
   NeighborhoodId*
   NeighborhoodName
}

Property
{
   PropertyId*
   PropertyName
   PropertyPhoto
   NeighborhoodId
   NeighborhoodName
}
```

Suppose you include a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) in a [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132) as shown below.

The Conditions property defined is a filter that indicates that the Properties you want to retrieve from the Property table to be loaded in the Grid are those that belong to NeighborhoodId = 1.

`[imagen omitida: wiki id 36884]`

Although this example shows a Grid in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), it could be a Grid in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).

### [See Also](#See+Also)

[Orders and Filters in Grids of Panels](https://wiki.genexus.com/commwiki/wiki?24805)  
[Conditional Orders and Filters](https://wiki.genexus.com/commwiki/wiki?12566)
