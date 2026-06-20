---
title: "ToDate method"
source_id: 14231
source_url: https://wiki.genexus.com/commwiki/wiki?14231
genexus_version: "18"
---

# ToDate method

Returns a Date data type corresponding to a given DateTime data type.

### [Syntax](#Syntax)

*DateTime-expression***.ToDate(****)**

**Where:**  
  
*DateTime-expression*Is a DateTime [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) to which the method will convert the data type.

**Type Returned:**  
Date

### [Scope](#Scope)

**Data Types:** [DateTime](https://wiki.genexus.com/commwiki/wiki?7370)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), 
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol

### [Samples](#Samples)

```
&Date = &DateTime.ToDate()
```

```
&Date = &DateTime.AddDays(5).ToDate()
```
