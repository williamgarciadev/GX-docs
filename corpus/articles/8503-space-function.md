---
title: "Space function"
source_id: 8503
source_url: https://wiki.genexus.com/commwiki/wiki?8503
genexus_version: "18"
---

# Space function

Returns a string filled with blank characters.

### [Syntax](#Syntax)

**Space(** *Att | **&**Var | Const* **)**

**Where:**  
  
*Att | **&**Var | Const*  
     The argument can be a numeric Attribute, User Variable or Constant. It specifies the number of spaces returned by the Space function.

**Type Returned:**  
Character

### [Scope](#Scope)

**Objects****:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), , [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Ruby (up to GeneXus X Evolution 3) , Visual Basic (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Returns a character string with as many blank spaces as indicated by its argument.

**Note**: In the iSeries, the receiving attribute or variable is completely filled with spaces, regardless of the value given to the argument.

### [Samples](#Samples)

* The attribute Attlen5 is defined as C(5).

```
Attlen5 = Space(5)
```

 Assigns a string of 5 blank characters to attribute Attlen5.

* The following is equivalent to the above in the iSeries, since the value of the argument is not taken into account when the attribute Attlen5 is defined as C(5).

```
Attlen5 = Space(1)
```


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |

---
