---
title: "Sub command"
source_id: 8586
source_url: https://wiki.genexus.com/commwiki/wiki?8586
genexus_version: "18"
---

# Sub command

​Defines [local subroutines](https://wiki.genexus.com/commwiki/wiki?24767) that will be triggered when you call them, in the same object, with the [Do command](https://wiki.genexus.com/commwiki/wiki?8581).

Parameter-passing is not allowed. All the object variables are available to be used by the subroutine. Also, instantiated attributes (loaded with values) are available to be used by the subroutine.

### [Syntax](#Syntax)

**Sub** *'Subroutine-Name'*  
    *Code*  
**EndSub**

#### [**Where:**](#Where%3A)

*Subroutine-Name*  
    Name of the subroutine defined.

### [Scope](#Scope)

**Objects:** [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916).  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258).

### [Samples](#Samples)

As an example, consider the following code defined inside a Procedure Source or inside an object Event:

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

### See Also

[Do command](https://wiki.genexus.com/commwiki/wiki?8581)  
[What is a subroutine?](https://wiki.genexus.com/commwiki/wiki?24767)


|  |
| --- |
| **Backlinks** |
| [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) | [Do Case command](https://wiki.genexus.com/commwiki/wiki?31605) |
| [Do command](https://wiki.genexus.com/commwiki/wiki?8581) | [What is a subroutine?](https://wiki.genexus.com/commwiki/wiki?24767) |

---
