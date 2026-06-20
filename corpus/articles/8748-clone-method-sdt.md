---
title: "Clone method - SDT"
source_id: 8748
source_url: https://wiki.genexus.com/commwiki/wiki?8748
genexus_version: "18"
---

# Clone method - SDT

Creates a new memory area and copies the variable data on it.

### [Syntax](#Syntax)

**&***VarBasedOnSTD**1* = **&***VarBasedOnSTD2*.**Clone()**  
  
**Where:**   
  
**&***VarBasedOnSTD1,***&***VarBasedOnSTD2*  
    Are variables based on an [SDT](https://wiki.genexus.com/commwiki/wiki?10021) that can be collection or not.

### [Scope](#Scope)

**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This method must always be applied to a variable. The only exception is within the Add method. For example:

```
   &VarBasedOnSTDCollection1.add(&VarBasedOnSTDCollection2.clone())
```

#### Clone Method vs New Operator

The Clone method includes the creation of a new memory area (the same operation as the New operator performs) and the assignment of each SDT element value.

For example:

```
&VarBasedOnSTD1 = &VarBasedOnSTD2.clone()
```

is equivalent to:

```
&VarBasedOnSTD1 = New()
&VarBasedOnSTD1.element1=&VarBasedOnSTD2.element1
&VarBasedOnSTD1.element2=&VarBasedOnSTD2.element2
```

So, the advantage of using the **Clone** method, is that it not only creates a new memory area but also it makes an automatic copy of each SDT element and you don't need to make the assignments.

**Note**: the assignment **&***VarBasedOnSTD1 =* **&***VarBasedOnSTD2* simply redirects both variables to the same memory area, and both variables are modified just by modifying one.

### [Considerations](#Considerations)

* If there are substructures within the SDT (whether they are collections or not), a new instance of the substructure is not created with the Clone method (shallow copy). You must do an explicit New or Clone for each substructure.
* If there are “defined” substructures within the SDT that are not collections, the clone method is not enabled.

### [See Also](#See+Also)

[Add Method](https://wiki.genexus.com/commwiki/wiki?8657)  
[New operator (SDT)](https://wiki.genexus.com/commwiki/wiki?8615)  
[Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021)


|  |
| --- |
| **Backlinks** |
| [New operator (SDT)](https://wiki.genexus.com/commwiki/wiki?8615) | [Structured Data Type methods](https://wiki.genexus.com/commwiki/wiki?24589) |

---
