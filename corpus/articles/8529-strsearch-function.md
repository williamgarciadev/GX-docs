---
title: "StrSearch function"
source_id: 8529
source_url: https://wiki.genexus.com/commwiki/wiki?8529
genexus_version: "18"
---

# StrSearch function

Searches for a string within another one.

### [Syntax](#Syntax)

**StrSearch(** *str1* , *str2*[, *start\_char* ] **)**;

**Where:**  
*str1*  
    String on which the search will be done. It may be of the [Character data type](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) or [LongVarChar data type](https://wiki.genexus.com/commwiki/wiki?7371).

*str2*  
    Search string. It may be of the Char, Varchar or Long varchar type.

*Start\_char*  
    Optional. It indicates the search start position. This variable is of the positive number type.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), Ruby (up to GeneXus X Evolution 3), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

StrSearch returns the position (integer index starting at 1) of the *Str1* string where the *Str2* string was found. It searches from front to back. The starting position in the search is optional. If it is omitted, then the starting position is the position 1 of the *Str1* string.

* The *Start\_Char* parameter is a positive number and indicates the initial position of the search within the *Str1*.  If it is 0, then the function return to 0.
* The comparison between characters is case-sensitive; i.e.:  'a' is different from 'A'.
* If *Str1* is empty or the length is shorter than *Str2*, then the function returns 0, since the search cannot be carried out.
* If *Str2* is empty, it returns *Start\_Char* if it was initialized. Otherwise, it returns 1.

### [Samples](#Samples)

```
&str1 ="StrSearch function tests"
StrSearch(&str1,"j")       // returns  0 (not found)  
StrSearch(&str1,"a" )      // returns  6
StrSearch(&str1, "e" , 7)  // returns 21
```

### [See Also](#See+Also)

[IndexOf method](https://wiki.genexus.com/commwiki/wiki?12696)  
[StrReplace function](https://wiki.genexus.com/commwiki/wiki?8505)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [Replace method](https://wiki.genexus.com/commwiki/wiki?12710) | [StrReplace function](https://wiki.genexus.com/commwiki/wiki?8505) |
| [StrSearchRev function](https://wiki.genexus.com/commwiki/wiki?8507) |

---
