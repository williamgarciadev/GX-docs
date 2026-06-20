---
title: "Contains method"
source_id: 53708
source_url: https://wiki.genexus.com/commwiki/wiki?53708
genexus_version: "18"
---

# Contains method

Returns True if a character expression contains a specific string, or False if it doesn't.

### [Syntax](#Syntax)

*CharacterExpression***.Contains(***ParmCharacter***)**

**Where:**  
  
*CharacterExpression* Attribute*,*variable, or character [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) on which the search will be done. It must be based on the Character data type, Varchar or LongVarchar data type.

*ParmCharacter*  Is the character or string that will be compared to the *CharacterExpression*'s characters.

**Type Returned:**  
Boolean

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

This method searches for a specific string within a character expression. It will return True if there´s a match and False if there isn´t.

**Note**: The comparison between characters is case sensitive (i.e.:  'a' is different from 'A').

### [Samples](#Samples)

```
&Character= "Contains method test" 
&Boolean=&Character.Contains("f") // Returns False
```

```
&Character= "Contains method test" 
&Boolean=&Character.Contains("i") // Returns True 

&Character= "Contains method test"
&Boolean=&Character.Contains("ins ") // Returns True
```

### [See Also](#See+Also)

[EndsWith method](https://wiki.genexus.com/commwiki/wiki?53711)  
[StartsWith method](https://wiki.genexus.com/commwiki/wiki?53700)  
[IndexOf method](https://wiki.genexus.com/commwiki/wiki?12696)  
[Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530)


|  |
| --- |
| **Backlinks** |
| [CharAt method](https://wiki.genexus.com/commwiki/wiki?53716) | [EndsWith method](https://wiki.genexus.com/commwiki/wiki?53711) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |
| [StartsWith method](https://wiki.genexus.com/commwiki/wiki?53700) |

---
