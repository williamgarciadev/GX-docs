---
title: "Today variable"
source_id: 8873
source_url: https://wiki.genexus.com/commwiki/wiki?8873
genexus_version: "18"
---

# Today variable

Stores the current date.

**Data Type:**  
Date

### [Scope](#Scope)

**Objects:**  [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)

### [Description](#Description)

It's a [standard variable](https://wiki.genexus.com/commwiki/wiki?7386) that stores the current (Today) date value. The format of the date issued by this variable depends on the language used by the application (language configuration parameter).

**iSeries:** This variable returns the start date of the JOB, not the SYSTEM DATE. This allows you to run a job with a date different from the current one and use this date in the program.

See also the [Sysdate function](https://wiki.genexus.com/commwiki/wiki?8493) if you want to use the actual SYSTEM DATE.

If &Today is used in a Procedure header, it prints the job's date. The result could be different from the one obtained using the function Sysdate if the job's attributes are changed (the dates may be different). The value returned by [Today function](https://wiki.genexus.com/commwiki/wiki?8334) is the same as using &Today variable.

**PC:** If &Today is used in a Procedure header, it’s evaluated whenever the header is printed (once per page). It is equivalent to use Sysdate and Today.

### [Samples](#Samples)

Consider the Invoice Transaction:

```
Invoice
{
  InvoiceId*
  InvoiceDate
  ....
  InvoiceAmount
}
```

#### [Transaction Rules:](#Transaction+Rules%3A)

```
InvoiceDate = &Today if Insert;
```

The variable &Today is evaluated at the beginning of the Transaction, so the date assigned to the attribute corresponds to that day.

Using the Today function:

```
InvoiceDate = &Today if Insert;
```

The date corresponds to the moment the rule is evaluated.

If the program continues executing from one day to another, the values may be different.

### [See Also](#See+Also)

[Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386)  
[Sysdate function](https://wiki.genexus.com/commwiki/wiki?8493)  
[Systime function](https://wiki.genexus.com/commwiki/wiki?8494)


|  |
| --- |
| **Backlinks** |
| [Dashboard widgets](https://wiki.genexus.com/commwiki/wiki?36779) | [Category:Object functions](https://wiki.genexus.com/commwiki/wiki?6877) | [Standard Variables List](https://wiki.genexus.com/commwiki/wiki?7386) |
| [Tabs offered in Panel and Work With objects](https://wiki.genexus.com/commwiki/wiki?16847) |

---
