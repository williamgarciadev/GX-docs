---
title: "IndexOf method"
source_id: 12696
source_url: https://wiki.genexus.com/commwiki/wiki?12696
genexus_version: "18"
---

# IndexOf method

Searches for a string within another one.

### [Syntax](#Syntax)

*str1**.*****IndexOf(***str2*[, *start-position* ]**)**

**Where:**  
  
*str**1*  
    String on which the search will be done. It may be based on the Character data type, Varchar or LongVarchar data type.

*str**2*  
    Searched string. It may be based on the Character data type, Varchar or LongVarchar data type.

*start-position*  
    Optional. It indicates the search start position. It must be a positive number (fixed value or variable).

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

The IndexOf method searches for a string within another one.

It returns the position (integer index starting in 1) of the *str1* string where the *str2* string was found. It searches from front to back.

The starting position is an optional parameter in the search. If it is omitted, the starting position will be position 1 of the *str1* string. It must be a positive number. If it is 0, the method returns 0.

**Notes:**

* The comparison between characters is case sensitive (i.e.:  'a' is different from 'A').
* If *str1* is empty or the length is shorter than *str**2*, the method returns 0, since the search cannot be carried out.
* If *str2* is empty, it returns s*tart-position*if it was initialized; otherwise, it returns 1.

### [Samples](#Samples)

```
&str1 ="StrSearch function tests"
&Number = &str1.IndexOf("j")    // Returns 0 ("j" not found)
&Number = &str1.IndexOf("a")    // Returns 6
&Number = &str1.IndexOf("e", 7) // Returns 21
```

### [See Also](#See+Also)

[IndexOf method - SDT Collection](https://wiki.genexus.com/commwiki/wiki?44905)  
[StrReplace function](https://wiki.genexus.com/commwiki/wiki?8505)


|  |
| --- |
| **Backlinks** |
| [Contains method](https://wiki.genexus.com/commwiki/wiki?53708) | [LastIndexOf method](https://wiki.genexus.com/commwiki/wiki?12697) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |
| [StartsWith method](https://wiki.genexus.com/commwiki/wiki?53700) | [StrSearch function](https://wiki.genexus.com/commwiki/wiki?8529) |

---
