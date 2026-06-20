---
title: "Workflow Server Data Type"
source_id: 11671
source_url: https://wiki.genexus.com/commwiki/wiki?11671
genexus_version: "18"
---

# Workflow Server Data Type

The Server Data Type represents a session with the Workflow engine. It provides the context for the interaction with the Workflow engine, acting as an input point to the other objects.

This Data Type is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Session | Character | Read | Session |
| AutoCommit (deprecated) (\*) | Boolean | Write | = TRUE allows properties/methods so requiring to perform transactional control = FALSE allows delegating transactional control to the applications |
| AutoRebuildWorklists | Boolean | Write | = TRUE allows that, when the organizational model is modified, the engine automatically rebuilds involved users worklists = FALSE the engine does not rebuild worklists automatically |
| Connected User | WorkflowUser | Read | Returns the user connected to the engine |
| Error | WorkflowError | Read | Error code |
| Settings | WorkflowSettings (Collection) | Read | Returns the collection of workflow server settings. |

#### [(\*) Since X version apis does not commit by default.](#%28*%29+Since+X+version+apis+does+not+commit+by+default.)

### [Methods](#Methods)

* **Connect**

A valid session to interact with the Workflow engine is obtained.

Connect (user, password)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| User | Character | Input | User Id |
| Password | Character | Input | User Password |

* **Disconnect**

Ends the connection created with the connect method.

Disconnect ()

* **Load**

Loads a WorkfllowSession.

Load(Session)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Session | [WorkflowSession](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Workflow session |

* **ThrowSignal**

This method throws a signal which reaches all the actives [Signal Intermediate Events](https://wiki.genexus.com/commwiki/wiki?12196)

ThrowSignal()

* **ListProcessDefinitionsOrderBy**

This method returns a collection with the process definitions matching the specified filter in the specified order.

ListProcessDefinitions (filter, order) : Collection (WorkflowProcessDefinition)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: Name, User | Input | Filter |
| Order | Numeric (WorkflowOrder.ID\_ASC, WorkflowOrder.ID\_DESC, WorkflowOrder.NAME\_ASC, WorkflowOrder.NAME\_DESC) | Input | Order |

* **ListProcessDefinitions**

This method returns a collection with the process definitions matching the specified filter.

ListProcessDefinitions (filter): Collection (WorkflowProcessDefinition)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: Name, User | Input | Filter |

* **ListActivitiesOrderBy**

This method returns a collection with the activities matching the specified filter in the specified order.

ListActivitiesOrderBy (filter, order) : Collection (WorkflowActivity)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: ProcessDefinition, Name, Role, User | Input | Filter |
| Order | Numeric (WorkflowOrder.ID\_ASC, WorkflowOrder.ID\_DESC, WorkflowOrder.NAME\_ASC, WorkflowOrder.NAME\_DESC) | Input | Order |

### [Sample](#Sample)

```
&workflowserver = new()
&workflowserver.Connect(!"WFADMINISTRATOR", !"WFADMINISTRATOR")

&workflowerror = &workflowserver.Error
If &workflowerror.Code > 0
    msg(format(!"code:%1 %2", &workflowerror.Code, &workflowerror.Message),Status)
    return
EndIf
&ProcessDefinition = &workflowserver.GetProcessDefinitionByName(!"SampleName")
&Filter.ProcessDefinition = &ProcessDefinition
&Activities = &workflowserver.ListActivitiesOrderBy(&Filter, WorkFlowOrder.NAME_ASC) // Order by Task Name
for &Activity in &Activities
  msg(format(!"%2 %1", &Activity.Name, &Activity.Id), status)
endfor
```

* **GetActivityById**

This method returns an Activity type object whose identifier (of both Process and Activity) coincides with the specified one.

GetActivityById (processDefinitionId, activityId) : WorkflowActivity

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| ProcessDefinitionId | Numeric | Input | Process defintion identifier |
| ActivityId | Numeric | Input | Activity identifier |

* **GetActivityByName**

This method returns the first Activity type object whose name coincides with the specified one.

GetActivityByName (name) : WorkflowActivity

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Name | Character | Input | Activity name |

* **GetActivityByGUID**

This method returns the Activity type object whose GUID coincides with the specified one.

GetActivityByGUID (name) : WorkflowActivity

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| GUID | Charcter | Input | Activity GUID |

* **GetBusinessEventById**

This method returns a Business event type object whose identifier coincides with the specified one.

GetBusinessEventById (id, ProcessDefinitionId): WorkflowBusinessEvent

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | Numeric | Input | Business event identifier |
| ProcessDefinitionId | Numeric | Input | Process defintion identifier |

* **GetBusinessEventByName**

This method returns the first Business Event type object whose name coincides with the specified one.

GetBusinessEventById (name): WorkflowBusinessEvent

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Name | Character | Input | Business event name |

* **GetBusinessEventInstanceById**

This method returns a Business Event Instance type object whose identifier coincides with the specified one.

GetBusinessEventById (id): WorkflowBusinessEventInstance

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | Numeric | Input | Business event instance identifier |

* **GetDocumentRepository**

This method returns the Document Repository object.

GetDocumentRepository () : WorkflowDocumentRepository

* **GetEventRepository**

This method returns the Event Repository object.

GetEventRepository () : Workflow Event Repository

* **GetOrganizationalModel**

This method returns the Organizational Model object.

GetOrganizationalModel () : WorkflowOrganizationalModel

* **GetProcessDefinitionById**

This method returns a Process Definition type object whose Id coincides with the specified one.

GetProcessDefinitionById (id) : WorkflowProcessDefinition)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | Numeric | Input | Process definition identifier |

* **GetProcessDefinitionByName**

This method returns the first Process Definition type object whose name coincides with the specified one.

GetProcessDefinitionByName (name) : WorkflowProcessDefintion

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Name | Character | Input | Process definition name |

* **GetProcessDefinitionByGUID**

This method returns a Process Definition type object whose GUID coincides with the specified one.

GetProcessDefinitionByGUID (GUID) : WorkflowProcessDefinition)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| GUID | Character | Input | Process definition |

* **GetProcessInstanceById**

This method returns a Process Instance type object whose identifier coincides with the specified one.

GetProcessInstanceById (id) : WorkflowProcessInstance

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | Numeric | Input | Process instance identifier |

* **GetProcessInstanceBySubject**

This method returns the first Process Instance type object whose subject coincides with the specified one.

GetProcessInstanceSubject ( subject) : WorkflowProcessInstance

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Subject | Character | Input | Process instance subject |

* **GetWorkitemById**

This method returns a Workitem type object whose identifier coincides with the specified one.

GetWorkitemById (id) : WorkflowWorkitem

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | Numeric | Input | Workitem identifier |

* **ListActivities**

This method returns a collection with the activities matching the specified filter.

ListActivities (filter) : Collection (WorkflowActivity)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: ProcessDefinition, Name, Role, User | Input | Filter |

* **ListBusinessEventInstances**

This method returns a collection with the business event instances matching the specified filter.

ListBusinessEventInstances (filter) : Collection (WorkflowEventInstance)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: User, ProcessDefinition, ProcessInstance, Subject, CreatedFrom, CreatedTo, EndedFrom, EndedTo | Input | Filter |

* **ListBusinessEventInstancesOrderBy**

This method returns a collection with the business event instances matching the specified filter in the specified order.

ListBusinessEventInstances (filter,order) : Collection (WorkflowEventInstance)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: User, ProcessDefinition, ProcessInstance, Subject, CreatedFrom, CreatedTo, EndedFrom, EndedTo | Input | Filter |
| Order |  | Input | Order |

* **ListBusinessEvents**

This method returns a collection with the business event matching the specified filter.

ListBusinessEvent (filter) : Collection (WorkflowEvent)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: User, ProcessDefinition, ProcessInstance, Subject, CreatedFrom, CreatedTo, EndedFrom, EndedTo | Input | Filter |

* **ListBusinessEventOrderBy**

This method returns a collection with the business event matching the specified filter in the specified order.

ListBusinessEventsOrderBy (filter,order) : Collection (WorkflowEvent)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: User, ProcessDefinition, ProcessInstance, Subject, CreatedFrom, CreatedTo, EndedFrom, EndedTo | Input | Filter |
| Order |  | Input | Order |

* **ListCalendars**

This method returns the list of calendars matching the established filter.

ListCalendars (filter) : Collection (WorkflowCalendar)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: Name, Calendar | Input | Filter |

* **ListCalendarsOrderBy**

This method returns the list of calendars matching the specified filter in the specified order.

ListCalendarsOrderBy(filter,order) : Collection (WorkflowCalendar)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter | Input | Filter |
| Order | WorkflowFilter Valid filters: Name, Calendar | Input | Order |

* **ListProcessInstances**

This method returns a collection with the process instances matching specified filter.

ListProcessInstances (filter) : Collection (WorkflowProcessInstance)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: From, To, ProcessDefinition, User, Priority, WithWarning, Subject, State, Relevant Data | Input | Filter |

* **ListProcessInstancesOrderBy**

This method returns a collection with the process instances matching the specified filter in the specified order.

ListProcessInstances (filter, order) : Collection (WorkflowProcessInstance)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: From, To, ProcessDefinition, User, Priority, WithWarning, Subject, State | Input | Filter |
| Order | Numeric (WorkflowOrder.ID\_ASC, WorkflowOrder.ID\_DESC, WorkflowOrder.CREATED\_ASC, WorkflowOrder.CREATED\_DESC, WorkflowOrder.PRIORITY\_ASC, WorkflowOrder.PRIORITY\_DESC, WorkflowOrder.STATE\_ASC, WorkflowOrder.STATE\_DESC, WorkflowOrder.WITH\_WARNING\_ASC, WorkflowOrder.WITH\_WARNING\_DESC, WorkflowOrder.SUBJECT\_ASC, WorkflowOrder.SUBJECT\_DESC, WorkflowOrder.ENDED\_ASC, WorkflowOrder.ENDED\_DESC) | Input | Order |

* **ListWorkitems**

This method returns a collection of Workitems matching specified filter.

ListWorkitems (filter) : Collection (WorkflowWorkitem)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: From, To, ProcessInstance, Subject, ProcessDefinition, Activity, User, Priority, WithWarning, State, Relevant Data | Input | Filter |

* **ListWorkitemOrderBy**

This method returns a collection of Workitems matching the specified filter in the specified order.

ListWorkitems (filter, order) : Collection (WorkflowWorkitem)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: From, To, ProcessInstance, Subject, ProcessDefinition, Activity, User, Priority, WithWarning, State | Input | Filter |
| Order | Numeric (WorkflowOrder.ID\_ASC, WorkflowOrder.ID\_DESC, WorkflowOrder.CREATED\_ASC, WorkflowOrder.CREATED\_DESC, WorkflowOrder.PRIORITY\_ASC, WorkflowOrder.PRIORITY\_DESC, WorkflowOrder.STATE\_ASC, WorkflowOrder.STATE\_DESC, WorkflowOrder.WITH\_WARNING\_ASC, WorkflowOrder.WITH\_WARNING\_DESC, WorkflowOrder.SUBJECT\_ASC, WorkflowOrder.SUBJECT\_DESC, WorkflowOrder.ENDED\_ASC, WorkflowOrder.ENDED\_DESC) | Input | Order |

* **ListConnectedUsers**

This method returns a collection with the users that are connected to the engine matching the specified filter.

ListConnectedUsers(filter) : Collection (WorkflowUser)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: Name, User | Input | Filter |

* **ListConnectedUsersOrderBy**

This method returns a collection with the users that are connected to the engine matching the specified filter in the specified order.

ListConnectedUsersOrderBy(filter,order) : Collection (WorkflowUser)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: Name, User | Input | Filter |
| Order | Numeric (WorkflowOrder.USER\_ASC ,WorkflowOrder.USER\_DESC ,WorkflowOrder.NAME\_ASC ,WorkflowOrder.NAME\_DESC ) | Input | Order |

* **ListNodeInstances**

This method returns a collection with the Node Instances matching the specified filter.

ListNodeInstances (filter) : Collection (WorkflowNodeInstance)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: ProcessDefinition, ProcessIntance, From, To | Input | Filter |

* **ListNodeInstancesOrderBy**

This method returns a collection with the Node Instances matching the specified filter in the specified order.

ListNodeInstancesOrderBy(filter,order) : Collection (WorkflowNodeInstance)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: ProcessDefinition, ProcessIntance, From, To, Node | Input | Filter |
| Order | Numeric (WorkflowOrder.ID\_ASC, WorkflowOrder.ID\_DESC, WorkflowOrder.CREATED\_ASC, WorkflowOrder.CREATED\_DESC, WorkflowOrder.ENDED\_ASC, WorkflowOrder.ENDED\_DESC) | Input | Order |

* **ListNodes**

This method returns a collection with the Nodes matching the specified filter.

ListNodes (filter) : Collection (WorkflowNode)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: Name, Process Definition | Input | Filter |

* **ListNodesOrderBy**

This method returns a collection with the Nodes matching the specified filter in the specified order.

ListNodesOrderBy(filter,order) : Collection (WorkflowNode)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: Name, Process Definition | Input | Filter |
| Order | Numeric (WorkflowOrder.ID\_ASC, WorkflowOrder.ID\_DESC, WorkflowOrder.NAME\_ASC ,WorkflowOrder.NAME\_DESC | Input | Order |

* **GetSettingById**

This method returns a [Workflow Setting](https://wiki.genexus.com/commwiki/wiki?15084) whose identifier coincides with the specified one.

GetSettingById (Id) : WorkflowSetting

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | WorkflowSettingId | Input | Workflow Setting identifier |

#### 

* #### [**GetNodeById**](#GetNodeById)

This method returns a [Workflow Node](https://wiki.genexus.com/commwiki/wiki?27136) whose identifiers coincides with the specified.

GetNodeById (processDefinitionId,Id): WorkflowNode

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| processDefinitionId | [WorkflowProcessDefinitionId](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Workflow Process Definition identifier |
| Id | [WorkflowNodeId](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Workflow Node identifier |

#### 

* #### [**GetNodeByGUID**](#GetNodeByGUID)

This method returns the [Workflow Node](https://wiki.genexus.com/commwiki/wiki?27136) whose GUID coincides with the specified one.

GetNodeByGUID (GUID): WorkflowNode

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| GUID | Character | Input | Workflow Node GUID |

#### 

* #### [**GetNodeByName**](#GetNodeByName)

This method returns the first [Workflow Node](https://wiki.genexus.com/commwiki/wiki?27136)type object whose name coincides with the specified one.

GetNodeByName (name) : WorkflowNode

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| name | Character | Input | Workflow Node name |

#### 

* #### [**GetNodeInstanceById**](#GetNodeInstanceById)

This method returns a [WorkflowNodeInstance](https://wiki.genexus.com/commwiki/wiki?27137) object whose identifier coincides with the specified one.

GetNodeInstanceById(id) : WorkflowNodeIntance

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| id | [WorkflowNodeInstanceId](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Workflow Node Instance identifier |

* #### [**GetSettingsByGroup**](#GetSettingsByGroup)

This method returns a collection of WorkflowSettings according to the specified group.

GetSettingsByGroup(group) : Collection (WorkflowSettings)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| group | Numeric (WorkflowSettingGroup.DOCUMENT\_MANAGMENT ,WorkflowSettingGroup.APPLICATION ,WorkflowSettingGroup.LANGUAGE ,WorkflowSettingGroup.NOTIFICATIONS ,WorkflowSettingGroup.AUTHENTICATION ,WorkflowSettingGroup.SESSION\_MANAGMENT ,WorkflowSettingGroup.PASSWORD\_POLICY ,WorkflowSettingGroup.EVENT\_HANDLING ,WorkflowSettingGroup.PERFORMANCE ,WorkflowSettingGroup.COMPATIBILITY ,WorkflowSettingGroup.BUSINESS\_PROCESS\_DEPLOYMENT ,) | Input | Workflow Group |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [HowTo: Create a settings menu using the Workflow API](https://wiki.genexus.com/commwiki/wiki?54056) | [HowTo: Get data from the Workflow Server using the Workflow API](https://wiki.genexus.com/commwiki/wiki?53506) | [HowTo: List Workitems filtered by Status](https://wiki.genexus.com/commwiki/wiki?11439) |
| [Category:Workflow API](https://wiki.genexus.com/commwiki/wiki?51350) | [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) | [WorkflowUser Data Type](https://wiki.genexus.com/commwiki/wiki?17273) |

---
