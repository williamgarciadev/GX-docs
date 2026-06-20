---
title: "TrimEnd method"
source_id: 12719
source_url: https://wiki.genexus.com/commwiki/wiki?12719
genexus_version: "18"
---

# TrimEnd method

Returns a specified character expression with all trailing blanks removed.

### [Syntax](#Syntax)

*character-expression****.*TrimEnd( )**  
  
**Where:**  
  
*character-expression*  
   Is the character
[expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) from which you want to trim all trailing blanks.

**Type Returned**  
Character

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), RPG, Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Returns a character string that results from removing the trailing blanks from the character
[expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,).

**Note**: In Cobol for iSeries this function is ignored, because the string's length is fixed.

### [Samples](#Samples)

By defining the following code in an Event:

```
&Text = ' My character expression '
&FinalText = &Text.Trim()
```

you will go from this:

```
&Text = '   My character expression   '
```

to this:

```
&FinalText: '   My character expression'
```

### [See Also](#See+Also)

[Trim function](https://wiki.genexus.com/commwiki/wiki?8424)  
[LTrim function](https://wiki.genexus.com/commwiki/wiki?8423)  
[Trim method](https://wiki.genexus.com/commwiki/wiki?12718)  
[TrimStart method](https://wiki.genexus.com/commwiki/wiki?12720)


|  |
| --- |
| **Backlinks** |
| [LTrim function](https://wiki.genexus.com/commwiki/wiki?8423) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [RTrim function](https://wiki.genexus.com/commwiki/wiki?8425) |
| [Trim function](https://wiki.genexus.com/commwiki/wiki?8424) | [Trim method](https://wiki.genexus.com/commwiki/wiki?12718) | [TrimStart method](https://wiki.genexus.com/commwiki/wiki?12720) |

---
