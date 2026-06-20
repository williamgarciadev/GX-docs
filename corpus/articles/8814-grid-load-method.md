---
title: "Grid Load method"
source_id: 8814
source_url: https://wiki.genexus.com/commwiki/wiki?8814
genexus_version: "18"
---

# Grid Load method

Loads a new line to the Grid.

### [*Syntax*](#Syntax)

*Grid***.load()**

### [Scope](#Scope)

**Objects:** [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)  
**Controls:** [Grid control](https://wiki.genexus.com/commwiki/wiki?24817)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Samples](#Samples)

```
Event Grid1.Load
    For each InvCode
        &InvCode = InvCode
        &InvDat = InvDate
        &Type = "INV"
         …
        grid1.Load( ) 
    EndFor
EndEvent
```

This method is very useful when you have more than one Grid in the form. In this case, you need to specify to which Grid the line is loaded:

*Grid1***.Load( )** or *Grid2***.Load( )**  
  
**Notes:**

* For Win applications, this method applies to the Grid.Load Event.
* In case of Web applications, the Load method is allowed in user events. See[Load Command and Load Method in User Events](https://wiki.genexus.com/commwiki/wiki?22555) for more details.
* For SD applications, this method is not offered nor allowed. You only can use the [Load command](https://wiki.genexus.com/commwiki/wiki?8196) .

### [See Also](#See+Also)

[Load command](https://wiki.genexus.com/commwiki/wiki?8196)


|  |
| --- |
| **Backlinks** |
| [Load command](https://wiki.genexus.com/commwiki/wiki?8196) | [Load Command and Load Method in User Events](https://wiki.genexus.com/commwiki/wiki?22555) |

---
