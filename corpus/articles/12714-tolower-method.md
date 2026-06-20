---
title: "ToLower method"
source_id: 12714
source_url: https://wiki.genexus.com/commwiki/wiki?12714
genexus_version: "18"
---

# ToLower method

Returns a specified character expression in lowercase letters.

### [Syntax](#Syntax)

*String***.ToLower(****)**

**Where:**  
  
*String* Is a character [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) based on the Character/VarChar/LongVarChar data type.

**Type Returned:**  
Character

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Ruby (up to GeneXus X Evolution 3),
Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Converts all uppercase letters (A - Z) in a character [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) to lowercase letters (a - z). All the other characters in the character expression remain unchanged.

**Note**: In Cobol and RPG for iSeries the character expression can be up to 256 bytes long.

### [Samples](#Samples)

By defining the following code in an Event:

```
&ArtistName = "Van Gogh, Vincent"
&TxtLower = &ArtistName.ToLower()
```

you will go from this:

```
&ArtistName = "Van Gogh, Vincent"
```

to this:

```
&TxtLower = "van gogh, vincent"
```

### [See Also](#See+Also)

[Lower function](https://wiki.genexus.com/commwiki/wiki?8464)  
[Upper Function](https://wiki.genexus.com/commwiki/wiki?8466)  
[ToUpper method](https://wiki.genexus.com/commwiki/wiki?12716)


|  |
| --- |
| **Backlinks** |
| [Lower function](https://wiki.genexus.com/commwiki/wiki?8464) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [ToUpper method](https://wiki.genexus.com/commwiki/wiki?12716) |

---
