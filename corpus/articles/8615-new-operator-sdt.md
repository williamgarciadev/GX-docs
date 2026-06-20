---
title: "New operator (SDT)"
source_id: 8615
source_url: https://wiki.genexus.com/commwiki/wiki?8615
genexus_version: "18"
---

# New operator (SDT)

Returns a new initialized instance of a Structured Data Type (SDT) variable.

### [Syntax](#Syntax)

*&Var* = **New** *SDTName()*

*or*

&Var = **New()**  //The advantage of using this syntax is that if the SDT is renamed, the syntax remains valid.

#### [**Where:**](#Where%3A)

*&Var*  
   A variable based on a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021).

*SDTName()*  
   The name of a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) that is a collection or the name of an item in a collection (regardless of the variable's data type).

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects:** | [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) [Java](https://wiki.genexus.com/commwiki/wiki?12258) |

### [Description](#Description)

The operator should be used when adding elements to an SDT collection.   
The first New is implicit when defining a variable.  
  

**Note**: Consider defining a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) to write less code, automatically handle what the New operator does, and efficiently obtain a loaded variable based on an SDT.

### [Sample](#Sample)

See the first sample proposed in [Add method](https://wiki.genexus.com/commwiki/wiki?8657).

### [See Also](#See+Also)

[Clone Method](https://wiki.genexus.com/commwiki/wiki?8748)  
[Add method](https://wiki.genexus.com/commwiki/wiki?8657)


|  |
| --- |
| **Backlinks** |
| [Clone method - SDT](https://wiki.genexus.com/commwiki/wiki?8748) | [Implementing SDT collections](https://wiki.genexus.com/commwiki/wiki?6296) | [Structured Data Type methods](https://wiki.genexus.com/commwiki/wiki?24589) |

---
