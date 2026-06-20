---
title: "Minute method"
source_id: 12650
source_url: https://wiki.genexus.com/commwiki/wiki?12650
genexus_version: "18"
---

# Minute method

Returns a numeric value representing the minutes of a DateTime argument.

### [Syntax](#Syntax)

*DateTime-Expression***.Minute(****)**  
  
**Type Returned:**  
Numeric(2)

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

When given a DateTime argument, this method returns a numeric value representing its minutes.

### [Samples](#Samples)

```
If &DateTime.Minute() > 00
   &TxtMinute = "Past o'clock..."
EndIf
```

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[Minute function](https://wiki.genexus.com/commwiki/wiki?8416)  
[Hour method](https://wiki.genexus.com/commwiki/wiki?12652)  
[Second method](https://wiki.genexus.com/commwiki/wiki?12651)


|  |
| --- |
| **Backlinks** |
| [Hour method](https://wiki.genexus.com/commwiki/wiki?12652) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Minute function](https://wiki.genexus.com/commwiki/wiki?8416) |
| [Second method](https://wiki.genexus.com/commwiki/wiki?12651) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) |

---
