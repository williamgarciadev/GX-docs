---
title: "WorkflowProcessDefinition Data Type"
source_id: 17239
source_url: https://wiki.genexus.com/commwiki/wiki?17239
genexus_version: "18"
---

# WorkflowProcessDefinition Data Type

This data type represents a process definition, that is the equivalent of a diagram in the GeneXus IDE. It is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | [WorkflowProcessDefinitioId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Identifier |
| Name | [WorkflowProcessName](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Process Name |
| Version | [WorkflowProcessVersion](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Process version |
| State | [WorkflowProcessDefinitionState](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Definition state |
| isMain | Boolean | Read | Indicates if it is main process |
| Calendar | [WorkflowCalendar](https://wiki.genexus.com/commwiki/wiki?11609) | Read | Calendar associated to the process |
| Activities | Collection ([WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?10263,,)) | Read | Activities making up the process definition |
| ExtendedAttributes | Collection (WorkflowAttribute) | Read | Process extended attributes |
| DocumentDefinitions | Collection [WorkflowDocumentDefinition](https://wiki.genexus.com/commwiki/wiki?10260) | Read | Document definitions associated to the process |
| States | Collection (WorkflowProcessDefinitionState) | Read | States that a process definition may have |
| Error | [WorkflowError](https://wiki.genexus.com/commwiki/wiki?10283) | Read | Error code |
| BusinessEvents | Collection ([WorkflowBusinessEvent](https://wiki.genexus.com/commwiki/wiki?12189)) | Read | Business Events |
| Description | [WorkflowDescription](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Process definition description |
| Created | DateTime | Read | Date of creation |
| Updated | DateTime | Read | Date of last update |
| GUID | [WorkflowGUID](https://wiki.genexus.com/commwiki/wiki?15734) | Read | GUID |
| ApplicationDataDefinitions | [WorkflowApplicationDataDefinition](https://wiki.genexus.com/commwiki/wiki?15734) (Collection) | Read | Application data defitinitions belonging to the Process Definition |
| Nodes | [WorkflowNode](https://wiki.genexus.com/commwiki/wiki?27136) (Collection) | Read | Nodes belonging to the Process Definition |

### [Methods](#Methods)

* **Load**

 Allows loading a process definition from the identifier.

Load (id)

* **LoadByName**

 Allows loading a process definition from the name.

LoadByName (name)

* **LoadByGUID**

Allows loading a process definition from the GUID

LoadByGUID(GUID)**Loa****LoadByName (name) Loa**

* **CreateInstance**

Creates a new process instance.

CreateInstance (): WorkflowProcessInstance

* **GetActivityById**

Returns an Activity type object whose identifier coincides with the specified one.

GetActivityById (id) : WorkflowActivity

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | Numeric | Input | Activity Identifier |

* **GetActivityByName**

Returns the first Activity type object whose name coincides with the specified one.

GetActivityByName (name): WorkflowActivity

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Name | [Workflowname](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Activity Name |

​​​​

* **GetNodeByName**

Returns the first Node type object whose name coincides with the specified one.

GetNodeByName (name): WorkflowNode

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Name | [Workflowname](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Node name |

* **GetNodeById**

Returns the first Node type object whose identifier coincides with the specified one.

GetNodeById (Id): WorkflowNode

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | [WorkflowId](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Node identifier |

* **ChangeState**

Changes the process state.

ChangeState (state)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| State | Character (WorkflowProcessDefinitionState) | Input | Process State |

* **Enable**

Changes the process state to enabled.

Enable ()

* **Disable**

Changes the process state to disabled.

Disable ()

* **GetBusinessEventById**

Returns a Business Event type object whose identifier coincides with the specified one.

GetBusinessEventById(id):WorkflowBusinessEvent

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | Numeric (WorkflowBusinessEventId) | Input | Business Event Identifier |

* **GetBusinessEventByName**

Returns the first Business Event type object whose name coincides with the specified one.

GetBusinessEventByName(name):WorkflowBusinessEvent

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Name | [Workflowname](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Business Event Name |

* **GetDocumentDefinitionAllowedActions**

Returns the allowed actions for the specified document.

GetDocumentDefinitionAllowedActions(DocumentDefinition):WorkflowDocumentAction

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| DocumentDefinition | [WorkflowDocumentDefinition](https://wiki.genexus.com/commwiki/wiki?10260) | Input | Business Event Name |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Date expression procedure property](https://wiki.genexus.com/commwiki/wiki?47342) | [Category:Workflow API](https://wiki.genexus.com/commwiki/wiki?51350) | [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |
| [WorkflowProcessInstance Data Type](https://wiki.genexus.com/commwiki/wiki?17771) |

---
