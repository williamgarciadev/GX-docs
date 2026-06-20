---
title: "WorkflowEvent Data Type"
source_id: 10275
source_url: https://wiki.genexus.com/commwiki/wiki?10275
genexus_version: "18"
---

# WorkflowEvent Data Type

This Data Type represents a generic Workflow event and it is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | Numeric | Read | Identifier |
| TimeStamp | DateTime | Read | Date and time of the creation |
| Type | Numeric | Read | Event Type |
| Source | Character (WorkflowEventSource) | Read | Component responsible for the event triggering |
| Target | WorkflowObject | Read | Object associated to the event |
| TargetType | Numeric (WorkflowObjectType) | Read | Type of object associated to the event |
| User | WorkflowUser | Read | User that triggers the event |

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
| [On deadline property](https://wiki.genexus.com/commwiki/wiki?11477) | [On new instance property](https://wiki.genexus.com/commwiki/wiki?11479) | [On resource non available property](https://wiki.genexus.com/commwiki/wiki?11481) |
| [On warning property](https://wiki.genexus.com/commwiki/wiki?11478) | [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) | [WorkflowActionPerformedEvent Data Type](https://wiki.genexus.com/commwiki/wiki?12040) | [WorkflowAssignmentChangeEvent Data Type](https://wiki.genexus.com/commwiki/wiki?10279) |
| [WorkflowDataChangeEvent Data Type](https://wiki.genexus.com/commwiki/wiki?10278) | [WorkflowStateChangeEvent Data Type](https://wiki.genexus.com/commwiki/wiki?10276) |

---
