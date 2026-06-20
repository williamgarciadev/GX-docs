---
title: "CharAt method"
source_id: 53716
source_url: https://wiki.genexus.com/commwiki/wiki?53716
genexus_version: "18"
---

# CharAt method

Returns the character that is located on a specific place of an expression.

### [Syntax](#Syntax)

*Character***.****CharAt**(*Number*)  
  
******Where:******  
  
*Character* Attribute, variable, or [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) on which the search will be done. It must be based on the Character data type, Varchar or LongVarchar data type.

*Number*  Is the position of the requested character. It may be a fixed number, an attribute, a variable, or a numeric expression.

**Type Returned:**  
Character

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

This method returns the character that is placed in the required position.

### [Samples](#Samples)

```
&Txt="abcdefghijk"
&Character=&Txt.CharAt(5) // &Character="e"
```

### [See Also](#See+Also)

[EndsWith method](https://wiki.genexus.com/commwiki/wiki?53711)  
[StartsWith method](https://wiki.genexus.com/commwiki/wiki?53700)  
[Substring method](https://wiki.genexus.com/commwiki/wiki?12713)  
[Contains method](https://wiki.genexus.com/commwiki/wiki?53708)  
[Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530)


|  |
| --- |
| **Backlinks** |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |

---
