---
title: "StrSearchRev function"
source_id: 8507
source_url: https://wiki.genexus.com/commwiki/wiki?8507
genexus_version: "18"
---

# StrSearchRev function

Searches for a string within a string in reverse order.

### [Syntax](#Syntax)

**StrSearchRev(** *str1***,** *str2* [ **,** *start\_char* ] **)**  
  
**Where:**  
  
*str1*  
    String on which the search will be done. It may be of the Char, Varchar or Long varchar type.  
  
*str2*  
    Search string. It may be of the Char, Varchar or Long varchar type.  
  
*Start\_char*  
    Optional. It indicates the search start position. This variable is of the positive number type.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

StrSearchRev returns the position of the *Str1* string where the *Str2*  string was found.  It searches from back to front. If the last parameter is omitted, it searches from the final position of the *Str1*, backwards.   
If the search is not successful, it returns to 0.

**Notes:**

* The StartChar parameter is  of the positive number type and indicates the initial position of the search within the Str1.  If 0, the function returns 0.
* The comparison between characters is case-sensitive; i.e.:  'a' is different from 'A'.
* If Str1 is empty or the length is shorter than Str2, the function returns 0, since the search cannot be carried out.
* If Str2 is empty, it returns StartChar if it was initialized; otherwise, it returns StrLen.

### [Samples](#Samples)

```
&str1 = "StrSearch function tests"
StrSearchrev(&str1, "a") //Returns 6
StrSearchrev(&str1, "fun" ,20)  //Returns 11
```

### [See Also](#See+Also)

[LastIndexOf method](https://wiki.genexus.com/commwiki/wiki?12697)  
[StrSearch function](https://wiki.genexus.com/commwiki/wiki?8529)  
[StrReplace function](https://wiki.genexus.com/commwiki/wiki?8505)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [LastIndexOf method](https://wiki.genexus.com/commwiki/wiki?12697) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) |

---
