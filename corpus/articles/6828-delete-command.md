---
title: "Delete command"
source_id: 6828
source_url: https://wiki.genexus.com/commwiki/wiki?6828
genexus_version: "18"
---

# Delete command

Deletes the record(s) in the Base Table associated with the group where this command is specified.

### [Syntax](#Syntax)

**Delete**

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)

### [Description](#Description)

This command is used to delete records in the [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) associated with the group where the **Delete command** itself is specified.

This command can only be used in a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) defined in a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293). The deletion is executed at the exact moment it is found, unless the For each command has a [Blocking clause](https://wiki.genexus.com/commwiki/wiki?4837). In this last case, the current deletion will happen when the entire block is completed and the Delete command is sent to the DBMS for a bulk deletion.  

**Notes:**

* **Referential Integrity** is NOT automatically checked when the Delete command is specified.

  + If the Delete command is specified in a group that has nested groups, data in the current group can still be used in the inner nested groups despite having been physically deleted.
* Remember to delete the inner levels first, before the outer levels. This avoids any possible cancellations or locks.

### [Samples](#Samples)

Given the [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

```
PurchaseOrder
{
  PurchaseOrderId*
  PurchaseOrderDate
  SupplierId
  PurchaseOrderAmount
}

PurchaseOrderDetail
{
  PurchaseOrderId*
  PurchaseOrderDetailId*
  PurchaseOrderDetailQuantity
  PurchaseOrderDetailPrice
  PurchaseOrderDetailAmount
}
```

1) In the following example, purchase order lines are deleted before the purchase order header. So, there would be no purchase order lines left without a header if the program were to cancel.

```
For each PurchaseOrder           //As the base trn is PurchaseOrder the deletion will be perfomed in the PurchaseOrder table
   For each PurchaseOrderDetail  //As the base trn is PurchaseOrderDetail the deletion will be perfomed in the PurchaseOrder table
         Delete
   Endfor
   Delete
EndFor
```

To learn how to improve the throughput of bulk deletions, see [Blocking clause in a 'For each' command](https://wiki.genexus.com/commwiki/wiki?4837) or the general concept on [Blocking Data Updates](https://wiki.genexus.com/commwiki/wiki?5572).

2) The following example, deletes a specific purchase order received by parameter.

```
Procedure Rule:
Parm(&PurchaseOrderId);

Procedure Source:
For each PurchaseOrder   //As the base trn is PurchaseOrder the deletion will be perfomed in the PurchaseOrder table 
    where PurchaseOrderId=&PurchaseOrderId
    For each PurchaseOrderDetail //As the base trn is PurchaseOrderDetail the deletion will be perfomed in the PurchaseOrder table 
        Delete 
    Endfor 
    Delete 
EndFor
```

### [See Also](#See+Also)

[Database update through procedures](https://wiki.genexus.com/commwiki/wiki?6826)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Updating with procedure-specific commands. Introduction](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/updating-with-procedure-specific-commands-introduction-6104731)


|  |
| --- |
| **Backlinks** |
| [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Category:Database update through procedures](https://wiki.genexus.com/commwiki/wiki?6826) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
| [Logically Deleted Attribute property](https://wiki.genexus.com/commwiki/wiki?37091) | [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) |

---
