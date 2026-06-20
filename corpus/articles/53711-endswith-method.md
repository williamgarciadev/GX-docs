---
title: "EndsWith method"
source_id: 53711
source_url: https://wiki.genexus.com/commwiki/wiki?53711
genexus_version: "18"
---

# EndsWith method

Returns True if an expression ends with a specific string, or False if it doesn't.

### [Syntax](#Syntax)

*CharacterExpression***.EndsWith**(*ParmCharacter*)

**Where:**  
  
*CharacterExpression* Attribute,variable, or character [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) on which the search will be done. It must be based on the Character data type, Varchar or LongVarchar data type.

*ParmCharacter*  Is the character or string that will be compared to the *CharacterExpression*'s last part.

**Type Returned:**  
Boolean

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

This method compares a given string to the end of a character expression. It will return True if there´s a match and False if there isn´t.

**Note**: The comparison between characters is case sensitive (i.e.:  'a' is different from 'A').

### [Samples](#Samples)

```
&Character= "EndsWith method test" 
&Boolean=&Character.EndsWith("m") // Returns False
```

```
&Character= "EndsWith method test" 
&Boolean=&Character.EndsWith("t") // Returns True
```

```
&Character= "EndsWith method test"
&Boolean=&Character.EndsWith("test") // Returns True
```

### [See Also](#See+Also)

[StartsWith method](https://wiki.genexus.com/commwiki/wiki?53700)  
[Contains method](https://wiki.genexus.com/commwiki/wiki?53708)  
[LastIndexOf method](https://wiki.genexus.com/commwiki/wiki?12697)  
[Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530)


|  |
| --- |
| **Backlinks** |
| [CharAt method](https://wiki.genexus.com/commwiki/wiki?53716) | [Contains method](https://wiki.genexus.com/commwiki/wiki?53708) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |
| [StartsWith method](https://wiki.genexus.com/commwiki/wiki?53700) |

---
