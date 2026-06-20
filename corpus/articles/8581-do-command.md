---
title: "Do command"
source_id: 8581
source_url: https://wiki.genexus.com/commwiki/wiki?8581
genexus_version: "18"
---

# Do command

Calls a local subroutine defined in the same object.

### [Syntax](#Syntax)

**Do** **‘***SubroutineName***’**  
  
**Where:**  
  
*SubroutineName*  
      Name of the subroutine to call.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829).  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917).

### [Description](#Description)

This command calls a local [subroutine](https://wiki.genexus.com/commwiki/wiki?24767) defined in the same object.

All the object variables are available to be used by the subroutine so, parameter-passing is not allowed. Also, instantiated attributes (loaded with values) are available to be used by the subroutine.

### [Samples](#Samples)

Consider the following code defined, for example, inside a Procedure Source or inside an object Event:

```
...
If &ConfirmedTicket  //Boolean variable
   Do 'PrintTicket'  //The 'PrintTicket' subroutine is called
EndIf
...

Sub 'PrintTicket'
    ...              // Subroutine code
EndSub
```

### [See Also](#See+Also)

[Sub command](https://wiki.genexus.com/commwiki/wiki?8586)  
[What is a subroutine?](https://wiki.genexus.com/commwiki/wiki?24767)


|  |
| --- |
| **Backlinks** |
| [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) | [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) |
| [Sub command](https://wiki.genexus.com/commwiki/wiki?8586) | [What is a subroutine?](https://wiki.genexus.com/commwiki/wiki?24767) |

---
