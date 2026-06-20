---
title: "WorkflowStateChangeEvent Data Type"
source_id: 10276
source_url: https://wiki.genexus.com/commwiki/wiki?10276
genexus_version: "18"
---

# WorkflowStateChangeEvent Data Type

This Data Type represents an event corresponding to a state change, it inherits all the properties of the Event object. It is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| OldState | Character ([WorkflowWorkitemState](https://wiki.genexus.com/commwiki/wiki?11306), [WorkflowProcessInstanceState](https://wiki.genexus.com/commwiki/wiki?11306), [WorkflowProcessDefinitionState](https://wiki.genexus.com/commwiki/wiki?11306)) | Read | Status previous to the change |
| NewState | Character ([WorkflowWorkitemState](https://wiki.genexus.com/commwiki/wiki?11306), [WorkflowProcessInstanceState](https://wiki.genexus.com/commwiki/wiki?11306), [WorkflowProcessDefinitionState](https://wiki.genexus.com/commwiki/wiki?11306)) | Read | State after the change |
| Id | Numeric | Read | Identifier |
| Source | Character (WorkflowEventSource) | Read | Component responsible for the event triggering |
| Target | WorkflowObject | Read | Object associated to the event |
| Target Type | Numeric (WorkflowObjectType) | Read | Type of object associated to the event |
| TimeStamp | DateTime | Read | Date and time of the creation |
| Type | Numeric | Read | Event type |
| User | WorkflowUser | Read | User |

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
[Workflow Enumerated Domains](https://wiki.genexus.com/commwiki/wiki?11306)


|  |
| --- |
| **Backlinks** |
| [On state change property](https://wiki.genexus.com/commwiki/wiki?11483) | [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |

---
