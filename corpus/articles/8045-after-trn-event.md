---
title: "After Trn event"
source_id: 8045
source_url: https://wiki.genexus.com/commwiki/wiki?8045
genexus_version: "18"
---

# After Trn event

This event is activated immediately after the Commit is executed.

### [Syntax](#Syntax)

Event After Trn  
        *Event\_code*  
EndEvent

**Where:**

*Event\_code*  
    Code defined inside the event.

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908)  
**Generators:** .NET, Java, RPG, Cobol

### [Description](#Description)

This event is activated once the Transaction has ended / completed a cycle. That is, right after executing the Commit.  
If in the same [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) there are rules defined with the [AfterComplete Triggering event](https://wiki.genexus.com/commwiki/wiki?8160), these are executed first and then the After Trn Event is executed.

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Invoice
{
   InvoiceId*
   InvoiceDate
   InvoiceDescription
   InvoiceTotalAmount
}
```

You may want to call a [PDF report](https://wiki.genexus.com/commwiki/wiki?13531) after executing the commit and, after that, close the Transaction screen and return to the calling GeneXus object:

```
Event After Trn
    ListInvoice(InvoiceId)  //The attributes that belong to the first level of the Transaction are available even after the commit 
    Return
EndEvent
```

### [See Also](#See+Also)

[AfterComplete Triggering event](https://wiki.genexus.com/commwiki/wiki?8160)


|  |
| --- |
| **Backlinks** |
| [AfterComplete Triggering event](https://wiki.genexus.com/commwiki/wiki?8160) | [Events in Transactions](https://wiki.genexus.com/commwiki/wiki?8042) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |

---
