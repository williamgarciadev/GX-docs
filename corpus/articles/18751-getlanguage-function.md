---
title: "GetLanguage function"
source_id: 18751
source_url: https://wiki.genexus.com/commwiki/wiki?18751
genexus_version: "18"
---

# GetLanguage function

Returns the currently active Language object Name (not the Description).

### [Syntax](#Syntax)

**GetLanguage()**

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

GeneXus allows the same application to be generated in multiple languages. You can read more about this topic at [GeneXus Application Localization](https://wiki.genexus.com/commwiki/wiki?6330).

The GetLanguage() function returns the currently active [Language object](https://wiki.genexus.com/commwiki/wiki?7258) Name.

### [Samples](#Samples)

The most common use is to set a variable with the currently active Language object Name as in the following example.

```
Event Start
    &ActiveLanguageName = GetLanguage() 
    ...
EndEvent
```

### [See Also](#See+Also)

[Language object](https://wiki.genexus.com/commwiki/wiki?7258)  
[SetLanguage function](https://wiki.genexus.com/commwiki/wiki?18757)


|  |
| --- |
| **Backlinks** |
| [ClientInformation external object](https://wiki.genexus.com/commwiki/wiki?31271) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Table of contents:GeneXus Application Localization](https://wiki.genexus.com/commwiki/wiki?6330) | [SetLanguage function](https://wiki.genexus.com/commwiki/wiki?18757) | [SetLanguage function (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54431) |

---
