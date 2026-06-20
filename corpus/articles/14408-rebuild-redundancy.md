---
title: "Rebuild Redundancy"
source_id: 14408
source_url: https://wiki.genexus.com/commwiki/wiki?14408
genexus_version: "18"
---

# Rebuild Redundancy

The formula attributes or those inferred by a foreign key may be defined as redundant. In some cases, GeneXus maintains these redundancies automatically and in other instances it is necessary to explicitly update them. For such instances there is the 'Rebuild Redundancy' utility, which allows updating some of the redundancies defined in a KB.

One case where redundancies are not automatically updated is where the data that is part of the redundant formula is updated in a New-EndNew of a procedure.

Example:

In the following transaction:

a\*  
b  
c = b + 2

where **c** is a formula and is defined as redundant attribute, upon running Create Database, the table corresponding to this transaction is created with fields **a**, **b** and **c**. One case where redundancies are automatically updated is upon executing this transaction. When the values are loaded in attributes **a** and **b**, the **c** attribute is automatically calculated and recorded.

Supposing that there is a procedure for entering records in this table as follows:

```
New
   a = 1
   b = 1
EndNew // c is not referenced

New
   a = 2
   b = 2
EndNew
```

After executing this procedure, the table will have the following two records:

 a   b   c  
--- --- ---  
 1   1   0  
 2   2   0

At this stage, for updating the c field of the table the 'Rebuild Redundancy' must be executed and the table will have the following records:

 a   b   c  
--- --- ---  
 1   1   3  
 2   2   4

Another case requiring the execution of this utilitarian is where a reorganization is done consisting of the addition of an attribute defined as formula that is also established as redundant.

Example:

With the transaction

a\*  
b

by adding the attribute **c = b + 2**, and defining it as redundant. The **c** attribute created will remain in the reorganized table, but with its initial value. For loading this field with the **b+2** values or each record it will be necessary to execute the utility.

The program executed from this utilitarian is 'gxlred' which calls all redundancy programs called <tablename>loadredundancy, like, for example: invoiceloadredundancy.

For executing this call outside GeneXus it is possible to program in some object of the application and add a button to call an event with  call('gxlred') .

```
Event 'MyEvent'
       call("gxlred")
       commit  
Endevent
```

In previous GeneXus versions, this option was located in the Win Developer Menu.

#### [See Also](#See+Also)

[Redundant property - Attribute](https://wiki.genexus.com/commwiki/wiki?6661)  
[SAC #50774 - GXLRED - java.lang.ClassNotFoundException](https://www.genexus.com/developers/websac?data=50774)
