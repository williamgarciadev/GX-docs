---
title: "Month function"
source_id: 8379
source_url: https://wiki.genexus.com/commwiki/wiki?8379
genexus_version: "18"
---

# Month function

Returns the numeric month identifier in a given date.

### [Syntax](#Syntax)

**Month(***Date-Expression* | *Datetime-Expression***)**

**Type Returned:**  
Numeric(2)

A null value (0) is returned if the received parameter is null.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Samples](#Samples)

1)

```
&Month = Month(CToD('01/01/08')) // Result &Month: 1
&Month = Month(Now()) // Result &Month: 2 If Now() = 25/02/08 10:30
```

2)

Suppose you need to define a list of all the Customers whose birthdays are in the current month (in this example, the current month is October).

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Customer
{
   CustomerId*
   CustomerName
   CustomerDateOfBirth
   CustomerEmail
}
```

Create a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) and define the following in its Layout:

`[imagen omitida: wiki id 32812]`

Next, in the Source section of the Procedure object, include the following code:

```
Print printBlock1
For each Customer
    Where Month(CustomerDateofBirth) = Month(&Today)
        Print printBlock2
EndFor
```

The [Today variable](https://wiki.genexus.com/commwiki/wiki?8873) (&Today), shown above, is a pre-defined GeneXus variable that stores the current date.

The following image shows the list at runtime:

`[imagen omitida: wiki id 32814]`

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[Month method](https://wiki.genexus.com/commwiki/wiki?12647)  
[Year function](https://wiki.genexus.com/commwiki/wiki?8380)  
[Day function](https://wiki.genexus.com/commwiki/wiki?8376)


|  |
| --- |
| **Backlinks** |
| [Date expressions](https://wiki.genexus.com/commwiki/wiki?24212) | [Day function](https://wiki.genexus.com/commwiki/wiki?8376) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Month method](https://wiki.genexus.com/commwiki/wiki?12647) |
| [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) | [Year function](https://wiki.genexus.com/commwiki/wiki?8380) |

---
