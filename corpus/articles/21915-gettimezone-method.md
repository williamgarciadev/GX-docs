---
title: "GetTimeZone method"
source_id: 21915
source_url: https://wiki.genexus.com/commwiki/wiki?21915
genexus_version: "18"
---

# GetTimeZone method

Obtains the [Current TimeZone](https://wiki.genexus.com/commwiki/wiki?22146) (CTZ).

### [Syntax](#Syntax)

&TimeZone = DateTime.**GetTimeZone()**

**Type Returned:**  
[Timezone Domains](https://wiki.genexus.com/commwiki/wiki?21989)

**Note**: The TimeZones domain doesn’t list all the possible Time Zone values. It may happen that the value returned by this method is not included in the domain.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

This is a static function of DateTime data type. Note that ‘DateTime’ is neither a variable nor an attribute; it’s the name of the DateTime data type to which the method is applied.

### [Samples](#Samples)

```
Event 'GetTZ'
   &Timezones = DateTime.GetTimeZone()
   msg(&Timezones.EnumerationDescription())
Endevent
```

When this is run in a browser in Uruguay, the following message will be displayed:

```
America/Montevideo
```

### [See Also](#See+Also)

[Enabling TimeZone Support](https://wiki.genexus.com/commwiki/wiki?22147)  
[DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218)  
[SetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21893)  
[FromTimeZone method](https://wiki.genexus.com/commwiki/wiki?21916)  
[CurrentOffset method](https://wiki.genexus.com/commwiki/wiki?21917)


|  |
| --- |
| **Backlinks** |
| [CurrentOffset method](https://wiki.genexus.com/commwiki/wiki?21917) | [FromTimeZone method](https://wiki.genexus.com/commwiki/wiki?21916) | [SetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21893) |
| [Toc:TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) |

---
