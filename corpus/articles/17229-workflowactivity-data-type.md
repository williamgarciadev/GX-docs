---
title: "WorkflowActivity Data Type"
source_id: 17229
source_url: https://wiki.genexus.com/commwiki/wiki?17229
genexus_version: "18"
---

# WorkflowActivity Data Type

This data type (provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350)) represents an activity in the context of a process definition (it is the equivalent of a task in the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272)).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | [WorkflowActivityId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Identifier |
| Node | [WorkflowNode Data Type](https://wiki.genexus.com/commwiki/wiki?27136) | Read | Node |
| Name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Activity name |
| GUID | [WorkflowGUID](https://wiki.genexus.com/commwiki/wiki?15734) | Read | GUID |
| ProcessDefinitionId | [WorkflowProcessDefinitionId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Identifier of the process definition |
| ProcessDefinition | [WorkflowProcessDefinition](https://wiki.genexus.com/commwiki/wiki?11698,,) | Read | Process definition |
| Class | [WorkflowActivityClass](https://wiki.genexus.com/commwiki/wiki?10294,,) | Read | Activity Class |
| isInitial | Boolean | Read | Indicates if the activity is initial |
| isFinal | Boolean | Read | Indicates if the activity is final |
| Subprocess | [WorkflowProcessDefinition](https://wiki.genexus.com/commwiki/wiki?11698,,) | Read | Definition of associated subprocess |
| Application | [WorkflowApplicationName](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Name of the associated Web application |
| Applications | [WorkflowActivityApplication](https://wiki.genexus.com/commwiki/wiki?15734) | Read |  |
| Roles | Collection ([WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,)) | Read | Roles associated to the activity |
| SuccesiveActivities | Collection ([WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?10263,,)) | Read | Successive activities |
| SuccessiveOptionalActivities | Collection ([WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?10263,,)) | Read | Successive Optional activities |
| ExtendedAttributes | Collection ([WorkflowAttribute](https://wiki.genexus.com/commwiki/wiki?10271)) | Read | Activity extended attributes |
| PreviewApplication | [WorkflowApplication](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Preview application associated to the activity |
| QueryApplication | [WorkflowApplication](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Query application associated to the activity |
| canDelegate | Boolean | Read | It indicates if the activity can be delegated |
| canCollaborate | Boolean | Read | It indicates if several users can collaborate to the execution of an activity |
| canWorkWithDocuments | Boolean | Read | It indicates if documents can be attached to the activity |
| isAdhoc | Boolean | Read | It indicates if an activity is ad hoc |
| isSelectableForAdhoc | Boolean | Read | It indicates if an activity can be selectable for ad hoc |
| DocumentDefinitions | Collection ([WorkflowDocumentDefinition](https://wiki.genexus.com/commwiki/wiki?10260)) | Read | Document Definitions associated to the activity |
| AttachedBusinessEvent | Collection ([WorkflowBusinessEvent](https://wiki.genexus.com/commwiki/wiki?12189)) | Read |  |
| AttachedTimers | Collection (WorkflowTimer) | Read |  |
| Error | [WorkflowError](https://wiki.genexus.com/commwiki/wiki?10283) | Read |  |

### Methods

* **AssignRole**

Assign a Role to the Activity.  
  
AssignRole(role)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | Movement | Description |
| 1 | role | [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,) | Input | Workflow Role |

* **UnAssignRole**

Unassign a Role to the Activity.  
  
UnAssignRole(role)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | Movement | Description |
| 1 | role | [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,) | Input | Workflow Role |

* **GetDocumentDefinitionAllowedActions**

This method allows recovering the actions allowed to a specified document.  
  
GetDocumentDefinitionAllowedActions(DocumentDefinition):Collection(WorkflowDocumentAction)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | Movement | Description |
| 1 | DocumentDefinition | [WorkflowDocumentDefinition](https://wiki.genexus.com/commwiki/wiki?10260) | Input | Workflow Document Definition |

* **GetDocumentDefinitionRequiredActions**

This method allows recovering the actions required to a specified document.  
  
GetDocumentDefinitionRequiredActions(DocumentDefinition):Collection(WorkflowDocumentAction)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | Movement | Description |
| 1 | DocumentDefinition | [WorkflowDocumentDefinition](https://wiki.genexus.com/commwiki/wiki?10260) | Input | Workflow Document Definition |

* ****Load****

Allows loading an Activity by Identifier.

           Load(ProcessDefinitionId,id)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ****Name**** | ****Type**** | **Movement** | **Description** |
| 1 | ProcessDefinitionId | [WorkflowProcessDefinitionId](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Process Definition Id |
| 2 | Id | [WorkflowActivityId](https://wiki.genexus.com/commwiki/wiki?15734) | Input |  |

* ****LoadByName****

Allows to load an Activity by Name.  
  
LoadByName(Name)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ****Name**** | ****Type**** | **Movement** | **Description** |
| 1 | Name | [Workflowname](https://wiki.genexus.com/commwiki/wiki?15734) | Input |  |

* ****LoadByGUID****

Allows loading an Activity by GUID.

LoadByGUID(GUID)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ****Name**** | ****Type**** | **Movement** | **Description** |
| 1 | GUID | [WorkflowGUID](https://wiki.genexus.com/commwiki/wiki?15734) | Input |  |

* ****GetPropertyValue****

Allows recovering the value of a property with the name it appears in the task in GeneXus.  
  
GetPropertyValue(Name):Character

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ****Name**** | ****Type**** | **Movement** | **Description** |
| 1 | Name | Character () | Input |  |

* ****GetApplicationByPlatformAndAction****

GetApplicationByPlatformAndAction(Platform, Action):WorkflowActivityApplication

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ****Name**** | ****Type**** | **Movement** | **Description** |
| **1** | **Platflorm** | **[WorkflowApplicationPlatform](https://wiki.genexus.com/commwiki/wiki?15734)** | **Input** |  |
| **2** | **Action** | **[WorkflowApplicationAction](https://wiki.genexus.com/commwiki/wiki?15734)** | **Input** |  |

* ****GetApplicationByName****

GetApplicationByName(Name):WorkflowActivityApplication

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ****Name**** | ****Type**** | **Movement** | **Description** |
| 1 | Platflorm | [WorkflowApplicationName](https://wiki.genexus.com/commwiki/wiki?15734) | Input |  |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow API](https://wiki.genexus.com/commwiki/wiki?51350) | [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) | [WorkflowBusinessEvent Data Type](https://wiki.genexus.com/commwiki/wiki?12189) |

---
