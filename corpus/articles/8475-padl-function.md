---
title: "PadL function"
source_id: 8475
source_url: https://wiki.genexus.com/commwiki/wiki?8475
genexus_version: "18"
---

# PadL function

Builds a character expression from a different one, by adding a specific character N times, or blanks to the left.

### [Syntax](#Syntax)

**Padl(***Str*, *Len* [,*FillChar*]**)**

**Where:**  
  
*Str*  
   Is the character [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) from which you want to add left blanks or with the FillChar if indicated.

*Len*  
   Is the numeric expression that indicates the length of the returned string.

*FillChar*  
   Is the character to be added on the left of ‘Str’. It is an optional parameter, if it is not specified, then blanks will be added.

**Type returned:**  
Character

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Returns a character string, aligned on the right, which is the result of concat the specified ‘FillChar’, ‘len’ times on the left of the ‘Str’  specified for the function.

### [Samples](#Samples)

```
PadL(“My string”, 14) = “     My string”
PadL(“My string”, 14, ‘*’) = “*****My string”
```

### [See Also](#See+Also)

[PadLeft method](https://wiki.genexus.com/commwiki/wiki?12705)  
[PadR function](https://wiki.genexus.com/commwiki/wiki?8476)  
[Trim function](https://wiki.genexus.com/commwiki/wiki?8424)  
[LTrim function](https://wiki.genexus.com/commwiki/wiki?8423)  
[RTrim function](https://wiki.genexus.com/commwiki/wiki?8425)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [PadLeft method](https://wiki.genexus.com/commwiki/wiki?12705) | [PadR function](https://wiki.genexus.com/commwiki/wiki?8476) | [PadRight method](https://wiki.genexus.com/commwiki/wiki?12706) |
| [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) |

---
