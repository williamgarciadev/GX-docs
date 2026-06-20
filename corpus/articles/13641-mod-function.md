---
title: "Mod function"
source_id: 13641
source_url: https://wiki.genexus.com/commwiki/wiki?13641
genexus_version: "18"
---

# Mod function

Returns the remainder of dividing the first parameter (dividend) by the second (divisor). The reminder is always an integer.

### [Syntax](#Syntax)

**Mod(***dividend*, *divisor***)**

**Where:**  
*dividend*  
    Numeric value used as the dividend.

*divisor*  
    Numeric value used as the divisor.

**Notes:**

* If divisor is 0, the function fails and the applicacion cancels.
* The result has the same sign as the dividend.
* Both dividend and divisor may be decimal values, but the returned value is always an integer.

**Type returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7387,,)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), Ruby (up to GeneXus X Evolution 3), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Visual FoxPro (up to GeneXus X Evolution 3)

### [Samples](#Samples)

```
&Int = Mod(5, 3)    // Result: 2
&Int = Mod(-5, 3)   // Result: -2
&Int = Mod(4, 2)    // Result: 0
&Int = Mod(7, 2.5)  // Result: 2
&Int = Mod(5, -3)   // Result: 2
```


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |

---
