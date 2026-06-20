---
title: "Substring method"
source_id: 12713
source_url: https://wiki.genexus.com/commwiki/wiki?12713
genexus_version: "18"
---

# Substring method

Returns a substring from a given string.

### [Syntax](#Syntax)

*String.***Substring(***n1* [, *n2*]**)**

**Where:**  
  
*String*  
   Is an attribute or variable based on the Character/VarChar/LongVarChar data type.

*n1* and *n2*  
   Must be numeric expressions.

**Type Returned:**  
Character

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

This method returns a substring from a given string.

#### [**Considerations**](#Considerations)

If *n2* = 0 an empty string is returned.  
Omitting *n2* is equivalent to setting it to *CharacterExpression*.length() - *n1* + 1.

#### [Constraints (not apply to .NET, Java)](#Constraints+%28not+apply+to+.NET%2C+Java%29)

* 1 <= *CharacterExpression*length <= 255
* 0 < *n1* <= *CharacterExpression*length
* *n2* >= 0

### [Samples](#Samples)

```
&Txt = '1234567890'
&Substr = &Txt.Substring(5,2)  //&Substr = '56'
```

### [Availability](#Availability)

Omitting *n2* is possible since [GeneXus 15 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?36355,,).

### [See Also](#See+Also)

[Concat function](https://wiki.genexus.com/commwiki/wiki?8352)  
[Str function](https://wiki.genexus.com/commwiki/wiki?7474)


|  |
| --- |
| **Backlinks** |
| [CharAt method](https://wiki.genexus.com/commwiki/wiki?53716) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Substr function](https://wiki.genexus.com/commwiki/wiki?8527) |

---
