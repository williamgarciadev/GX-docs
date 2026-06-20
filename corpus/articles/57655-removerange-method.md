---
title: "RemoveRange method"
source_id: 57655
source_url: https://wiki.genexus.com/commwiki/wiki?57655
genexus_version: "18"
---

# RemoveRange method

Removes a range of items from a collection starting at Index.

### [Syntax](#Syntax)

*&VarCollection1.RemoveRange(Numeric Index[, Numeric Count])*

**Where:**

*&VarCollection1*  
        The collection from which a range of elements will be removed.

*Numeric Index*  
        Indicates the Numeric Index where the removal of elements will start.

*Numeric Count*  
         This is an optional parameter that indicates how many items must be removed from the collection to which the method was applied, starting from the Numeric Index. If not specified, all items will be removed starting from the Numeric Index.

**Type Returned:**  
*Boolean*

### [Scope](#Scope)

**Generator:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604) [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Samples](#Samples)

**1)**

```
   //&NumericCollection1 = (1, 2, 3, 4, 5, 6)  
   &NumericCollection2 = &NumericCollection1.RemoveRange(3)
```

The result is:

&isOK= true   
&NumericCollection1 = (1, 2)

**2)**

```
  //&NumericCollection1 = [1, 2, 3, 4, 5, 6]
  &NumericCollection2 = &NumericCollection1.RemoveRange(3, 2)
```

The result is:

&isOK = true   
&NumericCollection1 = (1, 2, 5, 6)

### [See Also](#See+Also)

[AddRange method](https://wiki.genexus.com/commwiki/wiki?57654)  
[Set method in Collections](https://wiki.genexus.com/commwiki/wiki?57662)


|  |
| --- |
| **Backlinks** |
| [AddRange method](https://wiki.genexus.com/commwiki/wiki?57654) | [AddRange method (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58261) | [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) |
| [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243) | [RemoveRange method (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58260) | [Set method in Collections](https://wiki.genexus.com/commwiki/wiki?57662) | [Set method in Collections (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58262) |

---
