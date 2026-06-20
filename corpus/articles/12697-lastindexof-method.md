---
title: "LastIndexOf method"
source_id: 12697
source_url: https://wiki.genexus.com/commwiki/wiki?12697
genexus_version: "18"
---

# LastIndexOf method

Searches for a string within a string in reverse order and returns the found position counting from the beginning (unless the start position is indicated).

### [Syntax](#Syntax)

*str**1***.LastIndexOf(***str**2* [ , *start-position* ] **)**  
  
**Where:**  
  
*str**1*  
    String on which the search will be done. It may be an attribute or variable based on the Character/VarChar/LongVarChar data type.

*str**2*  
    Search string. It may be a fixed value, an attribute or variable based on the Character/VarChar/LongVarChar data type.

*start-position*Optional. It indicates the search start position. It must be a positive number.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This method searches for a string within a string in reverse order. If the last parameter is omitted, it searches from the first position of the *str**1*. If the search is not successful, it returns 0.

**Notes:**

* The *start-position* parameter must be a positive number. It indicates the initial position of the search within the *str**1*.  If it is 0, both functions return to 0.
* The comparison between characters is case sensitive; i.e.:  'a' is different from 'A'.
* If *str**1* is empty or the length is shorter than *str**2*, both functions return 0, since the search cannot be carried out.
* If *str**2* is empty, it returns *start-position* if it was initialized. Otherwise, it returns 1.

### [Samples](#Samples)

```
&str1 = "Of LastIndexOf test"
&Nbr=&str1.LastIndexOf("e")      //&Nbr= 17
&Nbr=&str1.LastIndexOf("In")     //&Nbr= 8
&Nbr=&str1.LastIndexOf("Last")   //&Nbr= 4
&Nbr=&str1.LastIndexOf("O")      //&Nbr= 13
&Nbr=&str1.LastIndexOf("Of")     //&Nbr= 13
&Nbr=&str1.LastIndexOf("Of",1)   //&Nbr= 1
```

### [See Also](#See+Also)

[IndexOf method](https://wiki.genexus.com/commwiki/wiki?12696)  
[StrSearchRev function](https://wiki.genexus.com/commwiki/wiki?8507)  
[StrReplace function](https://wiki.genexus.com/commwiki/wiki?8505)


|  |
| --- |
| **Backlinks** |
| [EndsWith method](https://wiki.genexus.com/commwiki/wiki?53711) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [StrSearchRev function](https://wiki.genexus.com/commwiki/wiki?8507) |

---
