---
title: "TrimStart method"
source_id: 12720
source_url: https://wiki.genexus.com/commwiki/wiki?12720
genexus_version: "18"
---

# TrimStart method

Returns a specified character expression with all leading blanks removed.

### [Syntax](#Syntax)

*character-expression****.*TrimStart( )**  
  
**Where:**  
  
*character-expression*  
   Is the character
[expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) from which you want to trim all leading blanks.

**Type Returned:**  
Character

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), RPG, Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This method returns the character string that results from removing the leading blanks from a character [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) *String*.

**Note**: In Cobol for iSeries this function is ignored, because the string's length is fixed.

### [Samples](#Samples)

```
&Text = &Var.TrimStart()
// &Var = "    My character expression" 
// &Text: “My character expression”
```

### [See Also](#See+Also)

[Trim method](https://wiki.genexus.com/commwiki/wiki?12718)  
[TrimEnd method](https://wiki.genexus.com/commwiki/wiki?12719)  
[Trim function](https://wiki.genexus.com/commwiki/wiki?8424)  
[LTrim function](https://wiki.genexus.com/commwiki/wiki?8423)


|  |
| --- |
| **Backlinks** |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Trim function](https://wiki.genexus.com/commwiki/wiki?8424) | [Trim method](https://wiki.genexus.com/commwiki/wiki?12718) |
| [TrimEnd method](https://wiki.genexus.com/commwiki/wiki?12719) |

---
