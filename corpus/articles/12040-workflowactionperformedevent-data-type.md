---
title: "WorkflowActionPerformedEvent Data Type"
source_id: 12040
source_url: https://wiki.genexus.com/commwiki/wiki?12040
genexus_version: "18"
---

# WorkflowActionPerformedEvent Data Type

This Data Type represents an event corresponding to the execution of a specific action. It is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350), and inherits all the properties of the Event object.

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| ActionPerformed | [WorkflowActionPerformed](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Action that was performed |
| Context | [WorkflowContext](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Context (workitem, process instance) associated to the action |
| Id | [WorkflowEventId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Id |
| TimeStamp | DateTime | Read | TimeStamp |
| Type | [WorkflowEventType](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Type |
| Source | [WorkflowEventSource](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Source |
| TargetType | [WorkflowObjectType](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Target Type |
| Target | [WorkflowObject](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Target |
| User | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?15734) | Read | User |

### [Methods](#Methods)

* **Load**

Allows loading an Action Performed Event by Identifier.

Load(Id)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | Movement | Description |
| 1 | Id | [WorkfloweventId](https://wiki.genexus.com/commwiki/wiki?15734) | Input |  |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)  
[Workflow Event Data Type](https://wiki.genexus.com/commwiki/wiki?10275)


|  |
| --- |
| **Backlinks** |
| [On action performed property](https://wiki.genexus.com/commwiki/wiki?11868) | [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |

---
