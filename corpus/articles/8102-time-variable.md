---
title: "Time variable"
source_id: 8102
source_url: https://wiki.genexus.com/commwiki/wiki?8102
genexus_version: "18"
---

# Time variable

Stores the current time in hh:mm:ss format.

**Data Type:**  
Character (8)

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)

### [Description](#Description)

The &Time [standard variable](https://wiki.genexus.com/commwiki/wiki?7386) contains the value of the [Time function](https://wiki.genexus.com/commwiki/wiki?8470) stored at the beginning of the program.  
  
In case it’s used in a Procedure header, the time will be displayed every time the header is evaluated, and not when the page is printed.

### [Samples](#Samples)

Consider the Invoice Transaction:

```
Invoice
{
  InvoiceId*
  InvoiceDate
  InvoiceTime
  ....
  InvoiceAmount
}
```

#### [Transaction Rules:](#Transaction+Rules%3A)

```
InvoiceTime = &Time if on BeforeInsert;
```

The &Time variable is evaluated at the beginning of the Transaction so the recorded time corresponds to that moment.

If the Time() function is used:

```
InvoiceTime = Time() on BeforeInsert;
```

The assigned value corresponds to the moment in which the rule is evaluated.

### [See Also](#See+Also)

[Built-in Variable List](https://wiki.genexus.com/commwiki/wiki?7386)  
[Time function](https://wiki.genexus.com/commwiki/wiki?8470)  
[Systime function](https://wiki.genexus.com/commwiki/wiki?8494)


|  |
| --- |
| **Backlinks** |
| [Dashboard widgets](https://wiki.genexus.com/commwiki/wiki?36779) | [ServerTime function](https://wiki.genexus.com/commwiki/wiki?8492) | [Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386) |
| [Systime function](https://wiki.genexus.com/commwiki/wiki?8494) | [Tabs offered in Panel and Work With objects](https://wiki.genexus.com/commwiki/wiki?16847) | [Time function](https://wiki.genexus.com/commwiki/wiki?8470) |

---
