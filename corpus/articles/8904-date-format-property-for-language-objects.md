---
title: "Date format property (for Language Objects)"
source_id: 8904
source_url: https://wiki.genexus.com/commwiki/wiki?8904
genexus_version: "18"
---

# Date format property (for Language Objects)

Specifies the format in which all the dates will be accepted and displayed when generating applications using this language.

### [Values](#Values)

|  |  |
| --- | --- |
| **ANSI (Y/M/D)** | The date type format will be yy/mm/dd. When this value is used, dates are accepted and displayed in YMD format; two digits are always displayed. If you want to take into account the picture, use the ToFormattedString method. |
| **English** | mm/dd/yy |
| **Italian** | dd/mm/yy |
| **Portuguese** | dd/mm/yy |
| **Spanish** | dd/mm/yy |

### [Scope](#Scope)

**Objects:** Language

### [Description](#Description)

This property is offered for each Language object to allow selecting the date format associated with that language.

After that, when a certain [Language object](https://wiki.genexus.com/commwiki/wiki?7258) is set to be used, the dates are handled with the format that was set for it.

### [Samples](#Samples)

### [ANSI case](#ANSI+case)

```
&vCurrentDate = serverdate() // Picture is 9999/99/99
&vstr1 = &vCurrentDate.ToString() // assume the date is 2020/12/31
&vstr2 = &vCurrentDate.ToFormattedString()
//&vstr1 is 20/12/31
//&vstr2 is 2020/12/31
```

### [See Also](#See+Also)

[Date format property (for Date/DateTime attributes/variables)](https://wiki.genexus.com/commwiki/wiki?39441)  
[Date format in CTOD function property](https://wiki.genexus.com/commwiki/wiki?7632)  
[First year of 20th century property](https://wiki.genexus.com/commwiki/wiki?7631)  
[Time format property](https://wiki.genexus.com/commwiki/wiki?9227)


|  |
| --- |
| **Backlinks** |
| [Date format property (for Date/DateTime attributes/variables)](https://wiki.genexus.com/commwiki/wiki?39441) | [Decimal separator property](https://wiki.genexus.com/commwiki/wiki?7670) | [Category:Language object](https://wiki.genexus.com/commwiki/wiki?7258) |
| [Picture property](https://wiki.genexus.com/commwiki/wiki?36522) |

---
