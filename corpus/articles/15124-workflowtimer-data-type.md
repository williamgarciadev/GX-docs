---
title: "WorkflowTimer Data Type"
source_id: 15124
source_url: https://wiki.genexus.com/commwiki/wiki?15124
genexus_version: "18"
---

# WorkflowTimer Data Type

This data type represents a timer (in the context of an activity definition) and it is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | Numeric | Read | Identifier |
| Name | Character | Read | Activity name |
| ProcessDefinition | WorkflowProcessDefinition | Read | Process definition |
| ProcessDefinitionId | Numeric | Read | Identifier of the process definition |
| SuccesiveActivities | Collection (WorkflowActivity) | Read | Successive activities |
| Trigger | WorkflowBusinessEventTrigger | Read | Trigger |
| Target | WorkflowActivity | Read | Activity |
| InterruptsActivity | Boolean | Read |  |
| TimerType | WorkflowTimerType | Read |  |
| Attached | Boolean | Read |  |
| Node | WorkflowNode | Read |  |

### [Methods](#Methods)

* **Load**

Allows loading a Timer by Identifier.  
  
Load(ProcessDefinitionId,id)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | Movement | Description |
| 1 | ProcessDefinitionId | Numeric (WorkflowProcessDefinitionId) | Input | Process Definition identifier |
| 2 | Id | Numeric (WorkflowActivityId) | Input | Activity identifier |

* **LoadByName**

Allows loading a Timer by Name.  
  
LoadByName(Name)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | Movement | Description |
| 1 | Name | Character (WorkflowName) | Input | Timer name |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |

---
