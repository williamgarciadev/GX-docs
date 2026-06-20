---
title: "WorkflowPriorityChangeEvent Data Type"
source_id: 10277
source_url: https://wiki.genexus.com/commwiki/wiki?10277
genexus_version: "18"
---

# WorkflowPriorityChangeEvent Data Type

This Data Type, provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350), represents an event corresponding to a change of priority. It inherits all the properties of the Event object.

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| OldPriority | Numeric (WorkflowPriority) | Read | Priority before the change |
| NewPriority | Numeric (WorkflowPriority) | Read | Priority after the change |
| Id | Numeric | Read | Identifier |
| Source | Character (WorkflowEventSource) | Read | Component responible for the event triggering |
| Target | WorkflowObject | Read | Object associated to the event |
| TargetType | Numeric (WorkflowObjectType) | Read | Type of object associated to the event |
| User | WorkflowUser | Read | User that triggers the event |
| TimeStamp | DateTime | Read | Date and time of creation |
| Type | Numeric | Read | EventType |

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


|  |
| --- |
| **Backlinks** |
| [On priority change property](https://wiki.genexus.com/commwiki/wiki?11480) | [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |

---
