---
title: "AddRange method"
source_id: 57654
source_url: https://wiki.genexus.com/commwiki/wiki?57654
genexus_version: "18"
---

# AddRange method

Adds the elements of the specified collection at a given position in the collection to which the method is applied.

### [Syntax](#Syntax)

*&VarCollection1.AddRange(&VarCollection2 [,Numeric Index])*

**Where:**

*&VarCollection1*  
         The collection to which elements will be added.

*&VarCollection2*  
         Contains a collection of items to be added to the collection to which the method is applied.

*Numeric Index*  
          This optional parameter indicates the position where the elements have to be added in the collection to which the method is applied. If this parameter is not provided, the elements will be added at the end.

**Type returned:**  
*Boolean*

### [Scope](#Scope)

**Generator:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604) [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

If the Numeric Index parameter is 0 or 1, the specified collection is added at the front of the collection.

### [Samples](#Samples)

### [**1)**](#1%29+)

```
// &NumericCollection1 = (1, 2, 3)
// &NumericCollection2 = (4, 5, 6)

&isOK = &NumericCollection1.AddRange(&NumericCollection2)
```

The result is that &NumericCollection1 contains (1, 2, 3, 4, 5, 6) and &isOK is true.

```
2)
// &NumericCollection1 = (1, 2, 3)
// &NumericCollection2 = (4, 5, 6)
&isOK = &NumericCollection1.AddRange(&NumericCollection2, 2)
```

The result is that &NumericCollection1 contains (1, 4, 5, 6, 2, 3) and &isOK is true.

**3)**

```
// &NumericCollection1 = (1, 2, 3)
// &NumericCollection2 = (4, 5)
&isOK = &NumericCollection1.AddRange(&NumericCollection2, 1)
```

The result is that &NumericCollection1 contains (4, 5, 1, 2, 3) and &isOK is true.

**4)**

```
// &NumericCollection1 = (1, 2, 3)
// &NumericCollection2 = (4, 5)
&isOK = &NumericCollection1.AddRange(&NumericCollection2 , 10)
```

The result is that &NumericCollection1 is not modified and &isOK is false. The operation fails because the specified position does not exist. The same behavior occurs if the Numerical index parameter = -10.

**5)**

```
// &NumericCollection1 = ()
// &NumericCollection2 = (4, 5)
&isOK = &NumericCollection1.AddRange(&NumericCollection2, 1)
```

The result is that &NumericCollection1 contains (4, 5) and &isOK is true.

**6)**

```
// &NumericCollection1 = ()
// &NumericCollection2 = ()
&isOK = &NumericCollection1.AddRange(&NumericCollection2, 1)
```

 The result is that there are no elements to add and &NumericCollection1 is empty and &isOK is true.

### [See Also](#See+Also)

[RemoveRange method](https://wiki.genexus.com/commwiki/wiki?57655)  
[Set method in Collections](https://wiki.genexus.com/commwiki/wiki?57662)


|  |
| --- |
| **Backlinks** |
| [AddRange method (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58261) | [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) | [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243) |
| [RemoveRange method](https://wiki.genexus.com/commwiki/wiki?57655) | [RemoveRange method (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58260) | [Set method in Collections](https://wiki.genexus.com/commwiki/wiki?57662) | [Set method in Collections (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58262) |

---
