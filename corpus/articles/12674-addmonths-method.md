---
title: "AddMonths method"
source_id: 12674
source_url: https://wiki.genexus.com/commwiki/wiki?12674
genexus_version: "18"
---

# AddMonths method

Adds a given number of months to a given date.

### [Syntax](#Syntax)

*Date*| *DateTime***.AddMonths(***Numeric-*e*xpression***)**  
  
**Where:**  
  
*Date*| *DateTime*  
     Is an attribute or variable based on the Date/DateTime data type, to which the method will add a certain number of months.

*Numeric-expression*  
     Is the number of months added to the given Date | DateTime.

**Type returned:**  
Date | DateTime

### [Scope](#Scope)

**Data Types:**

[Date](https://wiki.genexus.com/commwiki/wiki?7373), 
[DateTime](https://wiki.genexus.com/commwiki/wiki?7370)

### [Description](#Description)

Returns a value that results from adding a number of months to a given date or date with time.

The result data type will be the same as the given original value (Date or DateTime).

If the numeric expression is negative, the months are subtracted from the given date.

### [Samples](#Samples)

```
&ExpirationDate = &Today.AddMonths(1)    //This line can be included, for example, in a Procedure Source or in an Event
```

```
Event 'Calculates Expiration DateTime'
   &Now=Now()                            //&Now is a variable based on the DateTime data type
   &ExpirationDateTime = &Now.AddMonths(1)          
Endevent
```

### [See Also](#See+Also)

[AddMth function](https://wiki.genexus.com/commwiki/wiki?8314)  
[AddYears method](https://wiki.genexus.com/commwiki/wiki?12673)  
[AddDays method](https://wiki.genexus.com/commwiki/wiki?8313)


|  |
| --- |
| **Backlinks** |
| [AddMth function](https://wiki.genexus.com/commwiki/wiki?8314) | [AddYears method](https://wiki.genexus.com/commwiki/wiki?12673) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |
|

---
