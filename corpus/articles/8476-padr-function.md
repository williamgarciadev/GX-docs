---
title: "PadR function"
source_id: 8476
source_url: https://wiki.genexus.com/commwiki/wiki?8476
genexus_version: "18"
---

# PadR function

Builds a character expression from another one, by adding a specific character N times, or blanks to the right.

### [Syntax](#Syntax)

**PadR(***Str*, *Len*[,*FillChar*]**)**

**Where:**  
  
*Str*  
   Is the character expression from which you want to add right blanks or the FillChar if indicated.

*Len*  
   Is the numeric expression that indicates the length of the returned string.

*FillChar*  
   Is the caracter that is added to the right side of ‘Str’. It is an optional parameter, if it is not specified then blanks will be added.

**Type returned:**  
Character

### [Scope](#Scope)

**Objects:**  [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Returns a character string, aligned to the right, which is the result of concat the specified ‘FillChar’ , ‘len’ times to the right side of the ‘Str’  specified to the function.

### [Samples](#Samples)

```
PadR(“My string”, 14) = “My string     ”
PadR(“My string”, 14, ‘*’) = “My string*****”
```

**Note:**All trailing spaces from the original string will be removed before applying the function. The implementation of the function is similar to the following:

```
PadR(string text, int size, string fill)
  return Left(RTrim(text) + Replicate(fill, size), size);
```

### [See Also](#See+Also)

[PadRight method](https://wiki.genexus.com/commwiki/wiki?12706)  
[PadLeft method](https://wiki.genexus.com/commwiki/wiki?12705)  
[PadL function](https://wiki.genexus.com/commwiki/wiki?8475)  
[Trim function](https://wiki.genexus.com/commwiki/wiki?8424)  
[LTrim function](https://wiki.genexus.com/commwiki/wiki?8423)  
[RTrim function](https://wiki.genexus.com/commwiki/wiki?8425)


|  |
| --- |
| **Backlinks** |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [PadL function](https://wiki.genexus.com/commwiki/wiki?8475) | [PadLeft method](https://wiki.genexus.com/commwiki/wiki?12705) |
| [PadRight method](https://wiki.genexus.com/commwiki/wiki?12706) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) |

---
