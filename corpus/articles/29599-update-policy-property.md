---
title: "Update Policy property"
source_id: 29599
source_url: https://wiki.genexus.com/commwiki/wiki?29599
genexus_version: "18"
---

# Update Policy property

Sets whether the Transaction will allow editing attribute values or not. Besides, if the Transaction has associated table(s), the "Read Only" value will not allow updating those tables through Procedures or other objects.

### [Values](#Values)

|  |  |
| --- | --- |
| **Read Only** | The Transaction will not allow editing attribute values. Besides, if the Transaction has associated table(s), you will not be able to update their attributes through procedures or any object. |
| **Updatable** | The Transaction will allow editing the attribute values. |

### [Scope](#Scope)

**Objects:** Transaction

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

**1)**Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

**MaritalStatus  
{**MaritalStatusId\*  
   MaritalStatusName  
**}**

Suppose its [Data Provider property in Transactions](https://wiki.genexus.com/commwiki/wiki?29597) = True and its [Used to property](https://wiki.genexus.com/commwiki/wiki?29584) = Populate data (the Data Provider's purpose is to populate). Thus, the Data Provider stores all the necessary data in the MaritalStatus physical table (as shown in the following image) and the objective is to keep those values unchanged:

`[imagen omitida: wiki id 29603]`

To this end, you have to set the Transaction **Update Policy** property to Read-Only. Thus, the attribute values will not be able to be updated by end users (because the Transaction form behavior will be read-only) nor by you through GeneXus objects.

**2)** Now, suppose a Country Transaction has its [Data Provider property](https://wiki.genexus.com/commwiki/wiki?29597) = True and its [Used to property](https://wiki.genexus.com/commwiki/wiki?29584) = Populate data, too. That Data Provider stores only some initial data in the Country physical table. So, it is reasonable to set the Update Policy property to **Updatable**, so that end users can add new countries and edit them.

`[imagen omitida: wiki id 31797]`

**3)** See the following example that uses this property to implement [Dynamic Transactions that update data](https://wiki.genexus.com/commwiki/wiki?28656).

**4)** Suppose a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) with an associated [Data View](https://wiki.genexus.com/commwiki/wiki?1914). If you want to be able to read the external table, but not to allow updating it (because it is done via API -referenced module or services-), you can set the Update Policy property to **Read Only**.

### [Availability](#Availability)

This property is available since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?27605,,).


|  |
| --- |
| **Backlinks** |
| [Dynamic Transactions that update data](https://wiki.genexus.com/commwiki/wiki?28656) | [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) |

---
