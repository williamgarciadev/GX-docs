---
title: "Year method"
source_id: 12648
source_url: https://wiki.genexus.com/commwiki/wiki?12648
genexus_version: "18"
---

# Year method

Returns the numeric year identifier of a given date. If the received parameter is null, zero (0) is returned.

### [Syntax](#Syntax)

*Date*| *DateTime.***Year()**

**Type returned:**  
Numeric N(4)

### [Scope](#Scope)

**Data Types:** [Date](https://wiki.genexus.com/commwiki/wiki?7373), [DateTime](https://wiki.genexus.com/commwiki/wiki?7370)

### [Samples](#Samples)

To obtain the current year and assign it to a variable:

```
&ThisYear = Today.Year()
```

A string displaying text next to the year:

```
&TxtYear = 'Year:' + str(&Today.Year())
```

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[Year function](https://wiki.genexus.com/commwiki/wiki?8380)  
[Month method](https://wiki.genexus.com/commwiki/wiki?12647)  
[Day method](https://wiki.genexus.com/commwiki/wiki?12646)


|  |
| --- |
| **Backlinks** |
| [Day method](https://wiki.genexus.com/commwiki/wiki?12646) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Month method](https://wiki.genexus.com/commwiki/wiki?12647) |
| [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) | [Year function](https://wiki.genexus.com/commwiki/wiki?8380) |

---
