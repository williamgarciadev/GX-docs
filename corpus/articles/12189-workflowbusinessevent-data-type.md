---
title: "WorkflowBusinessEvent Data Type"
source_id: 12189
source_url: https://wiki.genexus.com/commwiki/wiki?12189
genexus_version: "18"
---

# WorkflowBusinessEvent Data Type

This Data Type represents an event corresponding to a [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486). It inherits all the properties of the Event object and is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | [WorkflowActivityId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Identifier |
| Name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Activity name |
| ProcessDefinitionId | [WorkflowProcessDefinitionId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Identifier of the process definition |
| ProcessDefinition | [WorkflowProcessDefinition](https://wiki.genexus.com/commwiki/wiki?11698,,) | Read | Process definition |
| SuccesiveActivities | Collection ([WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?10263,,)) | Read | Successive activities |
| Trigger | [WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?15734) | Read |  |
| Target | [WorkflowActivity Data Type](https://wiki.genexus.com/commwiki/wiki?17229) | Read |  |
| Attached | Boolean | Read |  |
| GUID | [WorkflowGUID](https://wiki.genexus.com/commwiki/wiki?15734) | Read |  |
| InterruptsActivity | Boolean | Read | Indicates if the event interrupts an Activity |
| Node | [WorkflowNode Data Type](https://wiki.genexus.com/commwiki/wiki?27136) | Read | Node |
| Type | Numeric | Read | Event Type |

### [Methods](#Methods)

* **Load**

Loads a BusinessEvent.  
  
Load(ProcessDefinitionId,id)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | ProcessDefinitionId | [WorkflowProcessDefinitionId](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Process Definition Id |
| 2 | Id | [WorkflowActivityId](https://wiki.genexus.com/commwiki/wiki?15734) | Input |  |

* **LoadByName**

Loads a BusinessEvent by name.  
  
Load(Name)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | Name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Business Process Name |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) | [WorkflowActivity Data Type](https://wiki.genexus.com/commwiki/wiki?17229) | [WorkflowProcessDefinition Data Type](https://wiki.genexus.com/commwiki/wiki?17239) |

---
