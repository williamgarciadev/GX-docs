---
title: "Select Record from Prompt"
source_id: 13576
source_url: https://wiki.genexus.com/commwiki/wiki?13576
genexus_version: "18"
---

# Select Record from Prompt

GeneXus provides two browse facilities for the base table and Transaction foreign keys called Autoprompt and Prompt, respectively.

These options are triggered in different moments and in different ways:

**Generators:**    .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)  
**Autoprompt:**    Select Button  
**Prompt:**            F4

**Generators:**    RPG and Cobol for iSeries  
**Autoprompt:**   F16 (View)  
**Prompt:**           F4

There is an Autoprompt for each transaction level that allows you to view and select the desired base table record corresponding to the current level.

The prompt facility displays all possible values that may be assigned to foreign keys, enabling the user to select the desired value. This prompt facility can be used when a referential integrity check fails; here the user may want to view the foreign key's valid values to overcome this failure.

It is invoked by pressing the F4 key. In some cases, in a microcomputer environment, when the referential integrity check fails it asks the user whether it is to be invoked.

### [Example](#Example)

For example, in the Orders Transaction (see below) you can view all of the suppliers by pressing the F4 function key over SupplierCode. At the beginning of the selection screen you can enter Supplier Code or Supplier Name to jump to a particular position on the supplier list.

```
Orders
{
    PurchaseOrderNumber*
    PurchaseOrderDate
    SupplierCode
    SupplierName
    AnalystNumber
    AnalystName
    {
         ProductCode*
         ProductName
         PurchaseOrderQuantity
         PurchaseOrderPrice
         ProductPrice
    }
    PurchaseOrderTotal
}
```

### [See also](#See+also)

[Prompt](https://wiki.genexus.com/commwiki/wiki?21635)  
[Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863)
