---
title: "Offline Database Object conditions"
source_id: 23570
source_url: https://wiki.genexus.com/commwiki/wiki?23570
genexus_version: "18"
---

# Offline Database Object conditions

The Offline Database object's Conditions are used to define the filters that will be applied to the data before synchronizing with the devices.

Conditions are applied to the [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029) in order to guarantee data consistency in the Offline Database. This is because each condition is independent and GeneXus has the intelligence to determine the tables in which the filters need to be applied. The criterion is that if the condition can be evaluated in the extended table of a table, then the filter will be applied. This allows you not to worry about the referential integrity of the data that will be stored in the device.

### [Sample](#Sample)

Suppose you have defined the following Transactions:

```
Customer
{
    CustomerId*      (Autonumber property = Yes)
    CustomerName
    CustomerLastName
    CustomerPhone
    CustomerEmail
    CustomerLastAccountId
}
```

```
PurchaseOrder
{
    PurchaseOrderId*      (Autonumber property = Yes)
    PurchaseOrderDate
    CustomerId            
    CustomerName           
    PurchaseOrderTotal
}
```

When working with an Offline Database, make sure that the data remains consistent even when the device is disconnected from the server. This means avoiding situations where a PurchaseOrder exists in the device's database without a corresponding Customer.

GeneXus uses conditions to filter data during synchronization. For example, you can define a condition like:

```
CustomerStatus = CustomerStatus.Active;
```

This condition will:

1. **Filter the** **Customer** **table:** Only active customers will be synchronized to the device.
2. **Filter the PurchaseOrder table (where the CustomerId is a [foreign key](https://wiki.genexus.com/commwiki/wiki?22918)):** Only purchase orders associated with active customers will be synchronized.

By applying this condition, you guarantee that the device's database will only contain purchase orders for active customers, avoiding inconsistencies.

The [Offline Database Object Navigation Report](https://wiki.genexus.com/commwiki/wiki?23568) provides a visual representation of how conditions are applied to each table during synchronization. This report helps you understand which data will be synchronized to the device and how conditions are used to maintain data integrity.

**Total filtering (no records in a specific table in the device)**

In some cases, you may need to have a table in the local database because the application saves data to that table, but you don't want to bring any record from the server.  
In that case, one possible solution is to define a condition that will never evaluate to True.  
For example, if you don't want to receive any Purchase Order in the device, the following condition could be used:

```
PurchaseOrderID < 0;
```

### [Considerations](#Considerations)

* Note that the conditions are only applied for the synchronization process and not for the offline database itself.
* The developer must handle the local data created on the devices when they are not considered for synchronization.

### [See Also](#See+Also)

[Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509)  
[Offline Database Object events](https://wiki.genexus.com/commwiki/wiki?23566)  
[Offline Database Object Navigation Report](https://wiki.genexus.com/commwiki/wiki?23568)


|  |
| --- |
| **Backlinks** |
| [Automatic Offline Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22267) | [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [Category:Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) |
| [Offline Database Object events](https://wiki.genexus.com/commwiki/wiki?23566) | [Offline Database Object Navigation Report](https://wiki.genexus.com/commwiki/wiki?23568) | [Offline Database Object Table selection](https://wiki.genexus.com/commwiki/wiki?23561) | [Table of contents:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |
| [Offline Native Mobile synchronization granularity alternatives](https://wiki.genexus.com/commwiki/wiki?37109) | [KB:Sales](https://wiki.genexus.com/commwiki/wiki?23672) | [Synchronization.Receive method](https://wiki.genexus.com/commwiki/wiki?23603) |

---
