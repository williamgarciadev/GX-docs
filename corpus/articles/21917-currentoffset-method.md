---
title: "CurrentOffset method"
source_id: 21917
source_url: https://wiki.genexus.com/commwiki/wiki?21917
genexus_version: "18"
---

# CurrentOffset method

Returns the current difference, in minutes, between [CTZ](https://wiki.genexus.com/commwiki/wiki?22005) and [UTC](https://wiki.genexus.com/commwiki/wiki?21994,,).

### [Syntax](#Syntax)

&varCurrentOffset = DateTime**.CurrentOffset()**

**Type Returned:**  
 Numeric  
     Is the difference in minutes between [CTZ](https://wiki.genexus.com/commwiki/wiki?22005) and [UTC](https://wiki.genexus.com/commwiki/wiki?21994,,).

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

This is a static function of DateTime data type. Note that ‘DateTime’ is neither a variable nor an attribute; it’s the name of the [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) to which the method is applied.

### [Samples](#Samples)

```
&varCurrentOffset = DateTime.CurrentOffset()
```

If the application is run from a browser or a device in Uruguay, the variable &varCurrentOffset will be loaded with -180; this is the difference in minutes between Uruguay and UTC when Daylight Savings Time is not in effect. If the application was run when Daylight Savings Time was used, the result would be: 120.

### [See Also](#See+Also)

[Enabling TimeZone Support](https://wiki.genexus.com/commwiki/wiki?22147)  
[DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218)  
[GetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21915)  
[SetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21893)  
[FromTimeZone method](https://wiki.genexus.com/commwiki/wiki?21916)


|  |
| --- |
| **Backlinks** |
| [FromTimeZone method](https://wiki.genexus.com/commwiki/wiki?21916) | [GetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21915) | [SetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21893) |
| [Toc:TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) |

---
