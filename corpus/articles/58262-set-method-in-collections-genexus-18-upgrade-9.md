---
title: "Set method in Collections (GeneXus 18 Upgrade 9)"
source_id: 58262
source_url: https://wiki.genexus.com/commwiki/wiki?58262
genexus_version: "18"
---

# Set method in Collections (GeneXus 18 Upgrade 9)

Replaces the element that is in the specified position with the provided element. Returns true if the operation succeeds.

### [Syntax](#Syntax)

*&VarCollection1.Set(Numeric Index, Element)*

**Where:**

*&VarCollection1*  
           The collection to which the method is applied to replace the specified element in the specified position.

*Numeric Index*  
           Indicates the position in the collection where you want to replace the existing element with a new element.

*Element*  
           The new element you want to place in the position specified by the Numeric Index.

**Type Returned:**  
*Boolean*

### [Scope](#Scope)

**Generator:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Samples](#Samples)

**1)**

```
// &NumericCollection1 = ("one", "two", "three")
&isOk = &NumericCollection1.Set(1, "newone")
```

The result is &NumericCollection1 = ("newone", "two", "three")  &isOK=true.

**2)**

```
// &NumericCollection1 = ("one", "two", "three")
&isOk = &NumericCollection1.Set(10, "newone")
```

The result is &NumericCollection1 = ("one", "two", "three")  &isOK=false.

**3)**

```
// &NumericCollection1 = ("one", "two", "three")
&isOk = &NumericCollection1.Set(0, "newone")
```

The result is &NumericCollection1 = ("one", "two", "three")  &isOK=false.

### [Availability](#Availability)

This method is available since [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243).

### [See Also](#See+Also)

[AddRange method](https://wiki.genexus.com/commwiki/wiki?57654)  
[RemoveRange method](https://wiki.genexus.com/commwiki/wiki?57655)
