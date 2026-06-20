---
title: "LTrim function"
source_id: 8423
source_url: https://wiki.genexus.com/commwiki/wiki?8423
genexus_version: "18"
---

# LTrim function

Returns the specified character expression without any blank spaces placed at the beginning of the expression.

### [Syntax](#Syntax)

**LTrim(***Character-expresssion***)**  
  
**Where:**  
  
*Character-expression*  
    Is the character [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) from which you want to trim blanks.

**Type returned:**  
Character

### [Scope](#Scope)

**Objects:**  [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

This function is especially useful for removing the blanks inserted when you use Str() function to convert a numeric value into a character string.

**Note**: In Cobol for iSeries the character expression can be up to 256 bytes long.

### [Sample](#Sample)

```
&Var = LTrim('   H e l l o')        // Result of &Var: “H e l l o”
```

### [See Also](#See+Also)

[Trim function](https://wiki.genexus.com/commwiki/wiki?8424)  
[RTrim function](https://wiki.genexus.com/commwiki/wiki?8425)  
[Trim method](https://wiki.genexus.com/commwiki/wiki?12718)  
[TrimEnd method](https://wiki.genexus.com/commwiki/wiki?12719)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [PadL function](https://wiki.genexus.com/commwiki/wiki?8475) | [PadLeft method](https://wiki.genexus.com/commwiki/wiki?12705) | [PadR function](https://wiki.genexus.com/commwiki/wiki?8476) |
| [PadRight method](https://wiki.genexus.com/commwiki/wiki?12706) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [RTrim function](https://wiki.genexus.com/commwiki/wiki?8425) | [Trim function](https://wiki.genexus.com/commwiki/wiki?8424) |
| [Trim method](https://wiki.genexus.com/commwiki/wiki?12718) | [TrimEnd method](https://wiki.genexus.com/commwiki/wiki?12719) | [TrimStart method](https://wiki.genexus.com/commwiki/wiki?12720) |

---
