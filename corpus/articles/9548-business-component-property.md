---
title: "Business Component property"
source_id: 9548
source_url: https://wiki.genexus.com/commwiki/wiki?9548
genexus_version: "18"
---

# Business Component property

Allows the Transaction to be executed in a 'silent' mode (without showing its form) in order to update the database from any object.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

The great advantage that the use of a Business Component provides is that you can update the database from any GeneXus object, and the same controls that are performed when the [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) is executed will be done.

The default value for this property is False.   
  
When you set the Business Component property of a Transaction = True, a new data type named with the same name of the Transaction is created in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), and variables based on that new data type may be defined in any object.

For example, suppose you define the Customer Transaction as Business Component (by setting its Business Component property = True):

`[imagen omitida: wiki id 23116]`

Once you set this property to True, a Business Component data type named Customer is automatically created in the Knowledge Base. Then, you will be able to define in any object a variable based on the new data type, as the following image shows (in the example in a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)):

`[imagen omitida: wiki id 23117]`

The variables based on a Business Component data type (as &customer in this example), have got a set of [properties](https://wiki.genexus.com/commwiki/wiki?2276) that correspond to the Transaction attributes (so that you can assign them values).

Also, a set of [methods](https://wiki.genexus.com/commwiki/wiki?2277) is available to apply to Business Components variables (in order to execute operations in the database as insertions, updates, etc.).

Important: After assigning values to the properties of a Business Component variable and executing methods to update the database, it is necessary to write explicitly the [Commit command](https://wiki.genexus.com/commwiki/wiki?7964) in the code, wherever you consider that all the operations made to the database make a complete [Logical Unit of Work (LUW)](https://wiki.genexus.com/commwiki/wiki?7963).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

Suppose the Customer Transaction shown above contains defined the following rule:

`[imagen omitida: wiki id 23170]`

and assume the CustomerId attribute has got its [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798) set to True.

The following code (included in the events section of the Web Panel where the &customer variable is defined) is inserting a customer by assigning values to the &customer variable properties (it means, the customer attributes), then the [Save method](https://wiki.genexus.com/commwiki/wiki?23229) is applied to the variable, and finally, the commit command is executed:

```
Event 'Insert customer'

 &Customer=new() //in this case, the new operator can be omitted, but if more than one customer is inserted, it must be used
 &Customer.CustomerName = 'John'
 &Customer.CustomerLastName = 'Smith'
 &Customer.CustomerAddress = '165 Ocean Drive'
 &Customer.CustomerEmail = 'jsmith@hotmail.com'
 &Customer.Save()
 if &Customer.Success() 
   commit 
 else 
   msg(&Customer.GetMessages().ToJson()) 
 endif

EndEvent
```

**Several explanations related to the previous code:**

When the [Save method](https://wiki.genexus.com/commwiki/wiki?23229) is executed:  
- The default rule defined in the Customer transaction rule is triggered, so the CustomerAddedDate attribute is assigned.  
- The CustomerId attribute is autonumbered.  
- The CustomerPhone was not assigned, so, the attribute in the table will not contain a value (it will be empty).  
- If the Transaction had had the CountryId attribute and/or the CityId attribute as foreign keys, and you assign by error values to them that not exist in the corresponding tables, when the Save method try to record, it fails.  
- The mode changes to update, and the records keep instantiated in memory.  
- After applying a method to access the database, it is recommended always [handle the errors](https://wiki.genexus.com/commwiki/wiki?2279).

Since GeneXus 15 you can also use the [Insert method](https://wiki.genexus.com/commwiki/wiki?31695) instead of the Save method to solve the same customer insertion, as shown below:

```
Event 'Insert customer'

 &Customer=new() //in this case, the new operator can be omitted, but if more than one customer is inserted, it must be used 
 &Customer.CustomerName = 'John' 
 &Customer.CustomerLastName = 'Smith' 
 &Customer.CustomerAddress = '165 Ocean Drive' 
 &Customer.CustomerEmail = 'jsmith@hotmail.com' 
 if &Customer.Insert() 
  commit 
 else
  msg(&Customer.GetMessages().ToJson()) 
 endif 

EndEvent
```

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, rebuild all the [Transaction objects](https://wiki.genexus.com/commwiki/wiki?1908).


|  |
| --- |
| **Backlinks** |
| [Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719) | [Applying Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975) | [Assignment Command for variables](https://wiki.genexus.com/commwiki/wiki?8217) |
| [Automatic data population associated with Transactions - FAQ](https://wiki.genexus.com/commwiki/wiki?31018) | [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [Business Component - Publication as Web Service](https://wiki.genexus.com/commwiki/wiki?2282) | [Business Component Delete method](https://wiki.genexus.com/commwiki/wiki?23238) |
| [Business Component Fail method](https://wiki.genexus.com/commwiki/wiki?23402) | [Business Component GetMessages method](https://wiki.genexus.com/commwiki/wiki?23475) | [Business Component GetOldValues method](https://wiki.genexus.com/commwiki/wiki?23804) | [Business Component Insert method](https://wiki.genexus.com/commwiki/wiki?31695) |
| [Business Component InsertOrUpdate method](https://wiki.genexus.com/commwiki/wiki?31697) | [Business Component Mode method](https://wiki.genexus.com/commwiki/wiki?23790) | [Business Component RemoveByKey method](https://wiki.genexus.com/commwiki/wiki?31847) | [Business Component Save method](https://wiki.genexus.com/commwiki/wiki?23229) |
| [Business Component Success method](https://wiki.genexus.com/commwiki/wiki?23404) | [Business Component ToXml method](https://wiki.genexus.com/commwiki/wiki?23483) | [Business Component Update method](https://wiki.genexus.com/commwiki/wiki?31696) | [Business Component variables properties](https://wiki.genexus.com/commwiki/wiki?2276) |
| [Creating Unit Tests](https://wiki.genexus.com/commwiki/wiki?38337) | [Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279) | [GXScheduler User Control](https://wiki.genexus.com/commwiki/wiki?11583) |

---
