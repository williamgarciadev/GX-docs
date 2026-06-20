---
title: "StartsWith method"
source_id: 53700
source_url: https://wiki.genexus.com/commwiki/wiki?53700
genexus_version: "18"
---

# StartsWith method

Returns True if a character expression starts with a specific string or False if it doesn't.

### [Syntax](#Syntax)

*CharacterExpression***.StartsWith(***ParmCharacter***)**

**Where:**  
  
*CharacterExpression* Attribute,variable, or character [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) on which the search will be done. It must be based on the Character data type, Varchar or LongVarchar data type.

*ParmCharacter*  Is the character or string that will be compared to the *CharacterExpression*'s beginning.

**Type Returned:**  
Boolean

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

This method compares a given string to a character expression's beginning. It will return True if there´s a match and False if there isn´t.

**Note**: The comparison between characters is case sensitive (i.e.:  'a' is different from 'A').

### [Samples](#Samples)

```
If &CardDigits.StartsWith(!"5579")
   &CardBank=!"Santander"
   &DiscountPercentage=15
endif
```

```
&Character=!"StartsWith method test"
&Boolean=&Character.StartsWith(!"m") // Returns False
```

```
&Character=!"StartsWith method test"
&Boolean=&Character.StartsWith(!"S") // Returns True
```

```
&Character=!"StartsWith method test"
&Boolean=&Character.StartsWith(!"Star") // Returns True
```

### [See Also](#See+Also)

[EndsWith method](https://wiki.genexus.com/commwiki/wiki?53711)  
[Contains method](https://wiki.genexus.com/commwiki/wiki?53708)  
[IndexOf method](https://wiki.genexus.com/commwiki/wiki?12696)  
[Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530)


|  |
| --- |
| **Backlinks** |
| [CharAt method](https://wiki.genexus.com/commwiki/wiki?53716) | [Contains method](https://wiki.genexus.com/commwiki/wiki?53708) | [EndsWith method](https://wiki.genexus.com/commwiki/wiki?53711) |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |

---
