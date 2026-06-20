---
title: "Cols function"
source_id: 8349
source_url: https://wiki.genexus.com/commwiki/wiki?8349
genexus_version: "18"
---

# Cols function

Returns the number of columns defined for an array.

### [Syntax](#Syntax)

**Cols(**&*array()***)**  
  
**Type returned:**  
Numeric constant, the same used to define the array.

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), 
[Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

By using this function, the array's dimensions within the program source is avoided. Modifying the array's dimensions would only cause the corresponding modification throughout the model, but there would be no need to modify the program's source where the array is used.

### [Samples](#Samples)

The following example illustrates how to load a 2D-array whose elements are the sum of their bi-dimensional positions (row and column):

```
&I = 1
Do while &I <= rows(&m())
   &J = 1
   Do while &J <= Cols(&m())
      &m(&I,&J) = &I + &J
      &J += 1
   EndDo
   &I = &I + 1
EndDo
```

### [See Also](#See+Also)

[Rows Function](https://wiki.genexus.com/commwiki/wiki?8351)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [How to define Variables and Arrays](https://wiki.genexus.com/commwiki/wiki?7385) | [Rows function](https://wiki.genexus.com/commwiki/wiki?8351) |

---
