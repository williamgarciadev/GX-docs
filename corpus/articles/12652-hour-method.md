---
title: "Hour method"
source_id: 12652
source_url: https://wiki.genexus.com/commwiki/wiki?12652
genexus_version: "18"
---

# Hour method

Returns a numeric value representing the time in 24-hour format.

### [Syntax](#Syntax)

*DateTime-expression.***Hour(****)**  
  
**Type Returned:**  
Numeric(2)

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Cobol, RPG, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

When given a DateTime argument, this method returns a numeric value representing the time in 24-hour format.

### [Samples](#Samples)

```
If &HappyTime.Hour() > 20
   &TxtHour = "Is the After-eight time!"
EndIf 
```

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[Hour function](https://wiki.genexus.com/commwiki/wiki?8415)  
[Minute method](https://wiki.genexus.com/commwiki/wiki?12650)  
[Second method](https://wiki.genexus.com/commwiki/wiki?12651)


|  |
| --- |
| **Backlinks** |
| [Hour function](https://wiki.genexus.com/commwiki/wiki?8415) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Minute method](https://wiki.genexus.com/commwiki/wiki?12650) |
| [Second method](https://wiki.genexus.com/commwiki/wiki?12651) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) |

---
