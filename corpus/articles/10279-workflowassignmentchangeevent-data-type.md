---
title: "WorkflowAssignmentChangeEvent Data Type"
source_id: 10279
source_url: https://wiki.genexus.com/commwiki/wiki?10279
genexus_version: "18"
---

# WorkflowAssignmentChangeEvent Data Type

This Data Type, provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350), represents an event corresponding to a change in an activity assignment. It inherits all the properties of the Event object.

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| AssignmentType | Numeric (WorkflowAssignmentType) | Read | Type of assignment change |
| Id | Numeric | Read | Identifier |
| OldUser | WorkflowUser | Read | User assigned before the change |
| NewUser | WorkflowUser | Read | User assigned after the change |
| OldRole | WorkflowRole | Read | Role assigned before the change |
| NewRole | WorkflowRole | Read | Role assigned after the change |
| Source | Character (WorkflowEventSource) | Read | Component responsible for the event triggering |
| Target | WorkflowObject | Read | Object associated to the event |
| TargetType | Numeric (WorkflowObjectType) | Read | Type of object associated to the event |
| TimeStamp | DateTime | Read | Date and time of the creation |
| Type | Numeric | Read | Event type |
| User | WorkflowUser | Read | User |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)  
[Workflow Event Data Type](https://wiki.genexus.com/commwiki/wiki?10275)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |

---
