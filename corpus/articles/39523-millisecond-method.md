---
title: "MilliSecond method"
source_id: 39523
source_url: https://wiki.genexus.com/commwiki/wiki?39523
genexus_version: "18"
---

# MilliSecond method

Returns a numeric value representing the milliseconds of a DateTime data type argument.

### [Syntax](#Syntax)

*DateTime-expression***.Millisecond(****)**

**Where:**

*DateTime-expression*Is a DateTime [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) to which the method will convert to milliseconds.

**Type Returned:**  
Numeric(3)

### [Scope](#Scope)

**Data Types:**

[DateTime](https://wiki.genexus.com/commwiki/wiki?7370)  
**Generators:** 
[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258),
[Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Samples](#Samples)

```
&Milliseconds = &DateTime.Millisecond()
```

```
&Milliseconds = &DateTime.AddDays(5).Millisecond()
```

### [See Also](#See+Also)

[Precision property](https://wiki.genexus.com/commwiki/wiki?39306)  
[AddMilliseconds method](https://wiki.genexus.com/commwiki/wiki?39524)
