---
title: "RemoveDiacritics method"
source_id: 24596
source_url: https://wiki.genexus.com/commwiki/wiki?24596
genexus_version: "18"
---

# RemoveDiacritics method

Returns the text without diacritical characters.

### [Syntax](#Syntax)

*String***.RemoveDiacritics()**

**Where:**

*String*Is an attribute or variable based on the Character/VarChar/LongVarChar data type.

**Type returned**  
Character

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Samples](#Samples)

```
&Text = "áéíóú"   
&TextNoDiacritics = &Text.RemoveDiacritics()   // Result: "aeiou"
if &TextNoDiacritics = 'aeiou'
     //Success evaluation
endif
```

### [Availability](#Availability)

This feature is available since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

**Note**: This method is useful in conditions evaluated on client side. On the server side this could be solved by the [DBMS](https://wiki.genexus.com/commwiki/wiki?24615), for example [SQL Server](http://stackoverflow.com/questions/3469401/sql-search-on-fields-containing-diacritics).

### [See Also](#See+Also+)

[Diacritic](http://en.wikipedia.org/wiki/Diacritic)


|  |
| --- |
| **Backlinks** |
| [GeneXus and Diacritics](https://wiki.genexus.com/commwiki/wiki?24615) |

---
