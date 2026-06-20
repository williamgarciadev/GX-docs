---
title: "Trim method"
source_id: 12718
source_url: https://wiki.genexus.com/commwiki/wiki?12718
genexus_version: "18"
---

# Trim method

Returns the specified character expression with all leading and trailing blanks removed.

### [Syntax](#Syntax)

*character-expression***.Trim(****)**

**Where:**

*character-expression*  
Is a character [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) based on the [Character](https://wiki.genexus.com/commwiki/wiki?6777) / [VarChar](https://wiki.genexus.com/commwiki/wiki?6778) / [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371) data type.

**Type Returned:**  
Character

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604),[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Returns a character [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) with all leading and trailing blanks removed.

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
&FinalText: 'My character expression'
```

### See Also

[Trim function](https://wiki.genexus.com/commwiki/wiki?8424)  
[TrimEnd method](https://wiki.genexus.com/commwiki/wiki?12719)  
[TrimStart method](https://wiki.genexus.com/commwiki/wiki?12720)  
[Rtrim Function](https://wiki.genexus.com/commwiki/wiki?8425)  
[Ltrim Function](https://wiki.genexus.com/commwiki/wiki?8423)


|  |
| --- |
| **Backlinks** |
| [LTrim function](https://wiki.genexus.com/commwiki/wiki?8423) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Trim function](https://wiki.genexus.com/commwiki/wiki?8424) |
| [TrimEnd method](https://wiki.genexus.com/commwiki/wiki?12719) | [TrimStart method](https://wiki.genexus.com/commwiki/wiki?12720) |

---
