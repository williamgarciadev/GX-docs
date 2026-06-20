---
title: "ToUpper method"
source_id: 12716
source_url: https://wiki.genexus.com/commwiki/wiki?12716
genexus_version: "18"
---

# ToUpper method

Returns a specified character expression in uppercase letters.

### [Syntax](#Syntax)

*String***.ToUpper(****)**

**Where:**  
  
*String*  
     Is a character [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) based on the Character/VarChar/LongVarChar data type.

**Type Returned:**  
Character

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Converts all lowercase letters (a - z) in a character [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) to uppercase letters (A - Z). All the other characters in the character expression remain unchanged.

**Note**: In Cobol and RPG for iSeries the character expression can be up to 256 bytes long.

### Samples

By defining the following code in an Event:

```
&ArtistName = "Van Gogh, Vincent"
&TxtUpper = &ArtistName.ToUpper()
```

you will go from this:

```
&ArtistName = "Van Gogh, Vincent"
```

to this:

```
&TxtUpper = "VAN GOGH, VINCENT"
```

### [See Also](#See+Also)

[ToLower method](https://wiki.genexus.com/commwiki/wiki?12714)  
[Lower function](https://wiki.genexus.com/commwiki/wiki?8464)


|  |
| --- |
| **Backlinks** |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [ToLower method](https://wiki.genexus.com/commwiki/wiki?12714) | [Upper function](https://wiki.genexus.com/commwiki/wiki?8466) |

---
