---
title: "WorkflowDataChangeEvent Data Type"
source_id: 10278
source_url: https://wiki.genexus.com/commwiki/wiki?10278
genexus_version: "18"
---

# WorkflowDataChangeEvent Data Type

This Data Type represents an event corresponding to the change of an application data. It inherits all the properties of the Event object and it is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| DataName | Character | Read | Application Data name |
| OldValue | Character | Read | Value before the change |
| NewValue | Character | Read | Value after the change |
| Id | Numeric | Read | Identifier |
| Source | Character | Read | Component responible for the event triggering |
| Target | [WorkflowObject Data Type](https://wiki.genexus.com/commwiki/wiki?10281) | Read | Object associated with the event |
| TargetType | Numeric | Read | Type of object associated with the event |
| TimeStamp | DateTime | Read | Date and time of the creation |
| Type | Numeric | Read | Event type |
| User | [WorkflowUser Data Type](https://wiki.genexus.com/commwiki/wiki?17273) | Read | User that triggers the event |

### [Methods](#Methods)

* **Load**

Allows loading an event.

Load(id) : Numeric

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | Numeric | Input | Event Id |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)  
[Workflow Event Data Type](https://wiki.genexus.com/commwiki/wiki?10275)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |

---
