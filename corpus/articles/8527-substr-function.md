---
title: "Substr function"
source_id: 8527
source_url: https://wiki.genexus.com/commwiki/wiki?8527
genexus_version: "18"
---

# Substr function

Returns a substring from a given string.

### [Syntax](#Syntax)

**Substr(***s1*, *n1*, *n2***)**

**Where:**  
  
*s1*  
   Must be a Character Expression.

*n1* and *n2*  
   Must be Numeric Expressions. If *n2* = 0 a null string is returned.

**Type Returned:**  
Character

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Returns a substring of S1 beginning at position N1, with a length of N2 characters.

Constraints (not applicable to .NET, Java or Ruby):

```
1 <= s1 length <= 255
0 < n1 <= s1 length
n2 >= 0
```

### [Samples](#Samples)

```
NoStr = SubStr('1234567890',5,2) // Result: NoStr = '56'
```

### [See Also](#See+Also)

[Substring method](https://wiki.genexus.com/commwiki/wiki?12713)  
[Concat function](https://wiki.genexus.com/commwiki/wiki?8352)  
[Str function](https://wiki.genexus.com/commwiki/wiki?7474)


|  |
| --- |
| **Backlinks** |
| [Concat function](https://wiki.genexus.com/commwiki/wiki?8352) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [Str function](https://wiki.genexus.com/commwiki/wiki?7474) |
|

---
