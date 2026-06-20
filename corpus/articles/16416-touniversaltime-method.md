---
title: "ToUniversalTime method"
source_id: 16416
source_url: https://wiki.genexus.com/commwiki/wiki?16416
genexus_version: "18"
---

# ToUniversalTime method

Converts a DateTime value to Coordinated Universal Time (UTC), assuming that the DateTime to convert to is the server's time zone.

### [Syntax](#Syntax)

*DateTime-expression*.**ToUniversalTime**()

**Where:**

*DateTime-expression*Is a DateTime [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) to which the method applied converts to Coordinated Universal Time (UTC).

**Type returned:**  
DateTime

### [Scope](#Scope)

**Data Types:**

[DateTime](https://wiki.genexus.com/commwiki/wiki?7370)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Samples](#Samples)

```
&MeetingInUTC = &MeetingDateTime.ToUniversalTime()
```

```
&MeetingInUTC = &MeetingDateTime.AddDays(5).ToUniversalTime()
```

### [See Also](#See+Also)

[Coordinated Universal Time](http://en.wikipedia.org/wiki/Coordinated Universal Time) (UTC)  
[The TimeZone problem](https://wiki.genexus.com/commwiki/wiki?22135)  
[DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218)  
[TimeZone support - Compatibility considerations](https://wiki.genexus.com/commwiki/wiki?20834,,)  
[DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370)


|  |
| --- |
| **Backlinks** |
| [Toc:TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) |

---
