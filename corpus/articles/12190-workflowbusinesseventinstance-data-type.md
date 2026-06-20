---
title: "WorkflowBusinessEventInstance Data Type"
source_id: 12190
source_url: https://wiki.genexus.com/commwiki/wiki?12190
genexus_version: "18"
---

# WorkflowBusinessEventInstance Data Type

This Data Type represents an event corresponding to a [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486) instance. It inherits all the properties of the Event object. It is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | [WorkflowActivityId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Identifier |
| Created | DateTime | Read | Created DateTime |
| Ended | DateTime | Read | Ended DateTime |
| State | [WorkflowBusinessEventInstanceState](https://wiki.genexus.com/commwiki/wiki?15734) | Read | State |
| ProcessDefinition | [WorkflowProcessDefinition](https://wiki.genexus.com/commwiki/wiki?11698,,) | Read | Process definition |
| ProcessDefinitionId | [WorkflowProcessDefinitionId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Identifier of the process definition |
| BusinessEvent | [WorkflowBusinessEvent](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Business Event |
| BusinessEventId | [WorkflowBusinessEventId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Business Event Id |
| ProcessInstance | [WorkflowProcessInstance](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Process Instance |
| ProcessInstanceId | [WorkflowProcessInstanceId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Process Instance Id |
| Error | [WorkflowError](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Error Code |
| NodeInstance | [WorkflowNodeInstance Data Type](https://wiki.genexus.com/commwiki/wiki?27137) | Read | Node Instance |

### [Methods](#Methods)

* **Load**

Allows loading a BusinessEvent.  
  
Load(ProcessDefinitionId,id)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | Movement | Description |
| 1 | ProcessDefinitionId | [WorkflowProcessDefinitionId](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Process Definition Id |
| 2 | Id | [WorkflowActivityId](https://wiki.genexus.com/commwiki/wiki?15734) | Input |  |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) | [WorkflowProcessInstance Data Type](https://wiki.genexus.com/commwiki/wiki?17771) |

---
