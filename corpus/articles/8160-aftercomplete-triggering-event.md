---
title: "AfterComplete Triggering event"
source_id: 8160
source_url: https://wiki.genexus.com/commwiki/wiki?8160
genexus_version: "18"
---

# AfterComplete Triggering event

AfterComplete is used to trigger a rule after processing all Transaction data; that is, the first level and all subordinated levels. It can be used in environments with or without Transactional Integrity control.

In environments with Transactional Integrity Control, the rules conditioned by an AfterComplete event are triggered after the LUW (Logical Unit of Work) is completed.

In GeneXus, the structure of a Transaction establishes the scope of the LUW. This one is defined as the data entry of the first level and subordinated levels. The Confirm Transactions property, allows the inclusion of a request for confirmation of the LUW. A Commit is performed in case of an affirmative answer. Otherwise, a Rollback is performed, eliminating the operations performed on the database within the LUW. The events conditioned by the AfterComplete event are executed, only if the LUW is confirmed.

In environments without Transactional Integrity, this function is equivalent to other Triggering Events. For example, in a single level Transaction, it is equivalent to: AfterInsert, AfterUpdate, AfterDelete. In case of a multi-level Transaction, it is equivalent to: AfterLevel of the last level of the Transaction (that is: just before it starts the first level of a new LUW).

### [**Syntax**](#Syntax)

[Any valid Transaction rule](https://wiki.genexus.com/commwiki/wiki?8213)  [ IF *condition* ][ **ON AfterComplete**];

Where:

*condition*  
          Is any valid logic condition

### [Example](#Example)

To call a report for print after entering an invoice, if the environment supports Transactional Integrity control, we would want to print the invoice after ensuring the LWU is complete.

Invoice Transaction

```
InvoiceId*
CustomerId
  (ProductId*
   InvoiceLineQuantity
   . . . 
   InvoiceLineAmount)
InvoiceAmount
```

```
PrintInvoice.Call(InvoiceId) On AfterComplete;
```

### [Note](#Note)

In the iSeries and web interfaces, the rule will always be executed after validating the whole transaction.

### [Scope](#Scope)

Objects: [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)

Purpose

To indicate the completion of a Logical Work Unit.

### [Compatibility](#Compatibility)

The After(TRN) function is maintained for backward compatibility reasons. We highly recommend using the AfterComplete event instead. For further information see Triggering Events.

#### [See Also](#See+Also)

[After function](https://wiki.genexus.com/commwiki/wiki?8321)  
[After Trn event](https://wiki.genexus.com/commwiki/wiki?8045)  
[Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213)  
[Triggering events for rules in Transactions](https://wiki.genexus.com/commwiki/wiki?6840)


|  |
| --- |
| **Backlinks** |
| [After Action Triggering event](https://wiki.genexus.com/commwiki/wiki?8284) | [After function](https://wiki.genexus.com/commwiki/wiki?8321) | [After Trn event](https://wiki.genexus.com/commwiki/wiki?8045) |
| [Transaction Rules Syntax](https://wiki.genexus.com/commwiki/wiki?6868) | [Category:Triggering events for rules in Transactions](https://wiki.genexus.com/commwiki/wiki?6840) |

---
