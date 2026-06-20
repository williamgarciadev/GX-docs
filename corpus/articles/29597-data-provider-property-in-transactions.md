---
title: "Data Provider property in Transactions"
source_id: 29597
source_url: https://wiki.genexus.com/commwiki/wiki?29597
genexus_version: "18"
---

# Data Provider property in Transactions

Creates a Data Provider object associated with the Transaction containing in its source the Transaction structure declared. You have to complete the desired data to be assigned to the Transaction attributes.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** Transaction

### [Description](#Description)

This property is offered under the **'Data'** properties group available for [Transactions](https://wiki.genexus.com/commwiki/wiki?1908):

`[imagen omitida: wiki id 31319]`

Default value: False.

When the **Data Provider** propertyvalue is set to True:

1. GeneXus creates a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) (named: TransactionName\_DataProvider) with the Transaction structure in its source so that you can quickly fill the desired data to be loaded into the Transaction attributes:  
     
   `[imagen omitida: wiki id 32406]`

           The previous Data Provider could be completed with fixed data or with attributes, to load all the available promotions.

       2. The [Used To property](https://wiki.genexus.com/commwiki/wiki?29584) is added to the group, as shown below:   
  
            `[imagen omitida: wiki id 29587]`

            It is important to read about the [Used to property](https://wiki.genexus.com/commwiki/wiki?29584) because it works together with the Data Provider property, in order to implement the whole behavior.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?27605,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Automatic data population associated with Transactions](https://wiki.genexus.com/commwiki/wiki?32706) | [Automatic data population associated with Transactions - FAQ](https://wiki.genexus.com/commwiki/wiki?31018) | [Toc:Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062) |
| [Dynamic Transactions Samples](https://wiki.genexus.com/commwiki/wiki?36273) | [Dynamic Transactions that receive parameters](https://wiki.genexus.com/commwiki/wiki?36732) | [Dynamic Transactions that update data](https://wiki.genexus.com/commwiki/wiki?28656) |
| [Populate Data property](https://wiki.genexus.com/commwiki/wiki?46340) | [Update Policy property](https://wiki.genexus.com/commwiki/wiki?29599) | [Used to property](https://wiki.genexus.com/commwiki/wiki?29584) |

---
