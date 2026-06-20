---
title: "Val function"
source_id: 8528
source_url: https://wiki.genexus.com/commwiki/wiki?8528
genexus_version: "18"
---

# Val function

Converts a number in character format into numeric format.

### [Syntax](#Syntax)

**Val(***character-expression***)**

**Where:**  
  
*character-expression*  
    Is any valid [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) that can involve constants, functions, methods, [variables](https://wiki.genexus.com/commwiki/wiki?7375), [attributes](https://wiki.genexus.com/commwiki/wiki?7240), [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441). The result must match the character data type.

**Type Returned:**  
Numeric N(18.2)

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

This function converts the numbers of a character expression into a numeric type. It processes the numbers in the character expression from left to right until a non-numeric character is encountered. If the first character of the character expression is not a number, the result of Val function will be 0.

### [Samples](#Samples)

```
&Result = Val('-123.35')         // Result is -123.35
&Result = Val(STR(123.35, 6, 2)) // Result is 123.35
&Result = Val('ABC')             // Result is 0 (*)
&Result = Val('12A')             // Result is 12 (*)
&WebSesNbr = Val(&SessionId)     // where &WebSesNbr is N(10.0) and &SessionId is C(30)
```

(\*) Converting alphanumerics to numerics is not supported when the method is evaluated in the DBMS (see [Server Side Functions/Methods](https://wiki.genexus.com/commwiki/wiki?11572) or SAC 42709).

### [See Also](#See+Also)

[ToNumeric method](https://wiki.genexus.com/commwiki/wiki?12717)  
[ToString method](https://wiki.genexus.com/commwiki/wiki?7090)  
[Str function](https://wiki.genexus.com/commwiki/wiki?7474)


|  |
| --- |
| **Backlinks** |
| [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [Str function](https://wiki.genexus.com/commwiki/wiki?7474) |
| [ToNumeric method](https://wiki.genexus.com/commwiki/wiki?12717) |

---
