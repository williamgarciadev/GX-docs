---
title: "GetCookie function"
source_id: 6879
source_url: https://wiki.genexus.com/commwiki/wiki?6879
genexus_version: "18"
---

# GetCookie function

Returns a string with the cookie’s value.

### [Syntax](#Syntax)

**GetCookie(***character-expression***)**

**Where:**  
  
*character-expression*  
    Is the cookie’s name.

**Type Returned**:  
Character

### [Scope](#Scope)

**Objects**:
[Procedure](https://wiki.genexus.com/commwiki/wiki?6293),
[Transaction](https://wiki.genexus.com/commwiki/wiki?1908), 
[Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** 
[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258),
Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

It makes it possible to read a [cookie](https://wiki.genexus.com/commwiki/wiki?6322) and return a string with its value. If it doesn’t find the cookie (or can’t read it because it is disabled), it returns an empty string.

### [Samples](#Samples)

```
&UserIdChar = GetCookie(UserParameters.CookieName) // Or...
&UserIdChar = trim(GetCookie(UserParameters.CookieName))
```

### [See Also](#See+Also)

[SetCookie function](https://wiki.genexus.com/commwiki/wiki?6878)


|  |
| --- |
| **Backlinks** |
| [Cookie data type](https://wiki.genexus.com/commwiki/wiki?21582) | [Cookies in GeneXus](https://wiki.genexus.com/commwiki/wiki?6322) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [SetCookie function](https://wiki.genexus.com/commwiki/wiki?6878) |

---
