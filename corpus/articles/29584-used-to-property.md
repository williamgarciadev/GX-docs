---
title: "Used to property"
source_id: 29584
source_url: https://wiki.genexus.com/commwiki/wiki?29584
genexus_version: "18"
---

# Used to property

Defines the purpose of the Data Provider associated with the Transaction (it is offered only if the Data Provider property is set to True for the Transaction).

### [Values](#Values)

|  |  |
| --- | --- |
| **Populate data** | The Data Provider is executed to store content in the physical table(s) associated with the Transaction. |
| **Retrieve data** | The Data Provider is executed to retrieve data. No physical tables are created associated with this Transaction. The Transaction is Dynamic. |

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,)

### [Description](#Description)

This property is offered under the 'Data' properties group available for [Transactions](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), only if the [Data Provider property](https://wiki.genexus.com/commwiki/wiki?29597) (which is under the same group) is set to True.

It allows defining the [Data Provider associated with the Transaction](https://wiki.genexus.com/commwiki/wiki?29597) purpose.

The possible values of this property are:

**1. Populate Data**

If you set this value, the Data Provider is executed to store the content in the physical table(s) associated with the Transaction. To carry out the data storage, GeneXus sets automatically the transaction Business Component property = True. It is important to know that the operation that will be performed -through the transaction executed as a business component- is an “upsert”. In other words, an insertion will be tried, but if it fails because a duplicated key is found, an update will be performed.

The Data Provider may be executed several times, automatically:- every time a modification is detected in the physical table(s) it loads.  
- every time the Data Provider is specified/generated/compiled again as a result of changes made to it or to some of his direct dependencies.

The Data Provider execution is independent of the database creation/reorganization process. On the one hand, the tables are created/reorganized, and later, after each success build (F5), if it is necessary, the Data Provider is executed in order to populate. This is shown as "========== Populate Data started ========== " in the output.

This automatic behavior can be avoided by setting [Populate Data property](https://wiki.genexus.com/commwiki/wiki?46340) to False.

Because the Data Provider can be run several times, you have to define an idempotent behavior (regardless of the times the Data Provider is run, the result should be the same as if executed once).

For instance, the following example shows a case in which content will always be loaded once no matter how many times the Data Provider is executed:

`[imagen omitida: wiki id 29593]`

`[imagen omitida: wiki id 29602]`

That is because the identificatory values (MaritalStatusId) were explicitly filled. If MaritalStatusId were an autonumber key, a Unique Index on a Candidate Key (for example, for MaritalStatusName) should be defined, to avoid storing several records with the same content.

Besides being automatically executed whenever GeneXus detects it has to run it, you can also execute explicitly the MaritalStatus\_DataProvider as shown:

```
Event 'Initialize'
   &MaritalStatusCollection=MaritalStatus_DataProvider()
   if &MaritalStatusCollection.InsertOrUpdate()
     msg("Initialization SUCCESSFUL")
     commit
   else
     msg("Initialization ERROR")
   endif
Endevent
```

Note: Whenever you set the **Used To** property of a Transaction to Populate Data, GeneXus automatically sets the [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) of the Data Provider associated with the Transaction to True.

**2. Retrieve Data**

If you set this value, no physical tables are created associated with this Transaction and we say it is a [Dynamic Transaction](https://wiki.genexus.com/commwiki/wiki?28062).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Compatibility](#Compatibility)

The Retrieve Data option is available as of GeneXus 15.
The Populate Data option is available as of GeneXus 15 Upgrade 1.

### [Availability](#Availability)

This property is available since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,).


|  |
| --- |
| **Backlinks** |
| [Table of contents:Automatic data population associated with Transactions](https://wiki.genexus.com/commwiki/wiki?32706) | [Automatic data population associated with Transactions - FAQ](https://wiki.genexus.com/commwiki/wiki?31018) | [Data Provider property in Transactions](https://wiki.genexus.com/commwiki/wiki?29597) |
| [Deploy to GeneXus Prototyping Cloud - FAQ](https://wiki.genexus.com/commwiki/wiki?18292) | [Table of contents:Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062) | [Dynamic Transactions Samples](https://wiki.genexus.com/commwiki/wiki?36273) | [Dynamic Transactions that receive parameters](https://wiki.genexus.com/commwiki/wiki?36732) |
| [Dynamic Transactions that update data](https://wiki.genexus.com/commwiki/wiki?28656) | [Populate Data property](https://wiki.genexus.com/commwiki/wiki?46340) | [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) | [Update Policy property](https://wiki.genexus.com/commwiki/wiki?29599) |

---
