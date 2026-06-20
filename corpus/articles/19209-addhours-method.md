---
title: "AddHours method"
source_id: 19209
source_url: https://wiki.genexus.com/commwiki/wiki?19209
genexus_version: "18"
---

# AddHours method

Adds hours to a DateTime attribute or variable.

### [Syntax](#Syntax)

*Date* | *DateTime***.AddHours(***Numeric-expression***)**

**Where:**  
  
*Date* | *DateTime*Is an attribute or variable based on the Date/DateTime data type, to which the method will add a certain number of hours.

*Numeric-expression*  
     Is a Numeric [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) that indicates the number of hours to be added to the *Date | DateTime.*

**Type returned:**  
DateTime

### [Scope](#Scope)

**Data Types:**

[DateTime](https://wiki.genexus.com/commwiki/wiki?7370)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Samples](#Samples)

```
&AppointmentDateTime.AddHours(1)               //Adds 1 hours to &AppointmentDateTime variable
```

```
&AppointmentDateTime.AddHours(&HoursNmbr + 1)  //&HoursNmbr is a variable received as a parameter using the Parm rule.
```

### [See Also](#See+Also)

[AddMinutes method](https://wiki.genexus.com/commwiki/wiki?19205)  
[AddDays method](https://wiki.genexus.com/commwiki/wiki?8313)


|  |
| --- |
| **Backlinks** |
| [AddDays method](https://wiki.genexus.com/commwiki/wiki?8313) | [AddMinutes method](https://wiki.genexus.com/commwiki/wiki?19205) |

---
