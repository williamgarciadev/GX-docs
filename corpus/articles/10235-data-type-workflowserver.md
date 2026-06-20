---
title: "Data Type WorkflowServer"
source_id: 10235
source_url: https://wiki.genexus.com/commwiki/wiki?10235
genexus_version: "18"
---

# Data Type WorkflowServer

The Server object represents a session with the Workflow engine. It provides the context for the interaction with the Workflow engine, acting as an input point to the other objects.

| Note |
| --- |
| WorkflowServer Data Type methods require the user to have the administrator role |

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Session | Character | Read | Session |
| AutoCommit | Boolean | Write | = TRUE allows properties/methods so requiring to perform transactional control = FALSE allows delegating transactional control to the applications |
| AutoRebuildWorklists | Boolean | Write | = TRUE allows that, when the organizational model is modified, the engine automatically rebuilds involved users worklists = FALSE the engine does not rebuild worklists automatically |
| Error | WorkflowError | Read | Error code |
| Connected User | WorkflowUser | Read | Returns the user connected to the engine |
| LastListCount | Numeric | Read | Returns the number of records in the last call to a List method ignoring paging filters if any. Not applicable for all List methods, available since [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,). |

#### Methods

* **Connect**

A valid session to interact with the Workflow engine is obtained.  
Connect (user, password)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | Movement | **Description** |
| 1 | user | Character | Input | UserId |
| 2 | password | Character | Input | User Password |

* **Disconnect**

Ends the connection created with the connect method.  
Disconnect ()

* **ListProcessDefinitions**  
  This method returns a collection with the process definitions matching the specified filter.

ListProcessDefinitions (filter): Collection (WorkflowProcessDefinition)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | Movement | **Description** |
| 1 | Filter | WorkflowFilter Filtros válidos: Name, User | Input | Filter |

* **ListProcessDefinitionsOrderBy**

This method returns a collection with the process definitions matching the specified filter in the specified order.

ListProcessDefinitions (filter, order) : Collection (WorkflowProcessDefinition)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Pasaje** | **Descripción** |
| 1 | Filter | WorkflowFilter Filtros válidos: Name, User | Input | Filter |
| 2 | Order | Numeric (WorkflowOrder.ID\_ASC,  WorkflowOrder.ID\_DESC,  WorkflowOrder.NAME\_ASC,  WorkflowOrder.NAME\_DESC) | Input | Order |

* **ListActivities**

This method returns a collection with the activities matching the specified filter.

ListActivities (filter) : Collection (WorkflowActivity)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Pasaje** | **Descripción** |
| 1 | Filter | WorkflowFilter Filtros válidos: ProcessDefinition, Name, Role, User | Input | Filter |

* **ListActivitiesOrderBy**

This method returns a collection with the activities matching the specified filter in the specified order.

ListActivitiesOrderBy (filter, order) : Collection (WorkflowActivity)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Pasaje** | **Descripción** |
| 1 | Filter | WorkflowFilter Filtros válidos: ProcessDefinition, Name, Role, User | Input | Filter |
| 2 | Order | Numeric (WorkflowOrder.ID\_ASC,  WorkflowOrder.ID\_DESC,  WorkflowOrder.NAME\_ASC,  WorkflowOrder.NAME\_DESC) | Input | Order |

* **ListProcessInstances**

This method returns a collection with the process instances matching specified filter.  
The LastListCount property is updated with the total number of records ignoring paging filters if any.

ListProcessInstances (filter) : Collection (WorkflowProcessInstance)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | filter | WorkflowFilter Valid Filters: From, To, ProcessDefinition, User, Priority, WithWarning, Subject, State, OrganizationalUnit, SetOrganizationalUnit, ApplicationDataName, ApplicationDataValue, SetApplicationData | Input | Filter |

* **ListProcessInstancesOrderBy**

This method returns a collection with the process instances matching the specified filter in the specified order.  
The LastListCount property is updated with the total number of records ignoring paging filters if any.

ListProcessInstances (filter, order) : Collection (WorkflowProcessInstance)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | Movement | **Description** |
| 1 | Filter | WorkflowFilter Filtros válidos: From, To, ProcessDefinition, User, Priority, WithWarning, Subject, State, Organizational Unit, SetOrganizationalUnit, ApplicationDataName, ApplicationDataValue, SetApplicationData | Input | Filter |
| 2 | Order | Numeric (WorkflowOrder.ID\_ASC,  WorkflowOrder.ID\_DESC,  WorkflowOrder.CREATED\_ASC,  WorkflowOrder.CREATED\_DESC,  WorkflowOrder.PRIORITY\_ASC,  WorkflowOrder.PRIORITY\_DESC,  WorkflowOrder.STATE\_ASC,  WorkflowOrder.STATE\_DESC,  WorkflowOrder.WITH\_WARNING\_ASC,  WorkflowOrder.WITH\_WARNING\_DESC,  WorkflowOrder.SUBJECT\_ASC,  WorkflowOrder.SUBJECT\_DESC,  WorkflowOrder.ENDED\_ASC,  WorkflowOrder.ENDED\_DESC) | Input | Order |

* **ListWorkitems**

This method returns a collection of Workitems matching the specified filters.  
The LastListCount property is updated with the total number of records ignoring paging filters if any.

ListWorkitems (filter) : Collection (WorkflowWorkitem)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | Filter | WorkflowFilter Filtros válidos: From, To, ProcessInstance, Subject, ProcessDefinition, Activity, User, Priority, WithWarning, State, OrganizationalUnit, SetOrganizationalUnit, ApplicationDataName, ApplicationDataValue, SetApplicationData | Input |  |

* **ListWorkitemOrderBy**

This method returns a collection of Workitems matching the specified filter in the specified order.  
The LastListCount property is updated with the total number of records ignoring paging filters if any.

ListWorkitems (filter, order) : Collection (WorkflowWorkitem)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | Filter | WorkflowFilter Filtros válidos: From, To, ProcessInstance, Subject, ProcessDefinition, Activity, User, Priority, WithWarning, State, Organizational Unit, SetOrganizationalUnit, ApplicationDataName, ApplicationDataValue, SetApplicationData | Input | Filter |
| 2 | Order | Numeric (WorkflowOrder.ID\_ASC,  WorkflowOrder.ID\_DESC,  WorkflowOrder.CREATED\_ASC,  WorkflowOrder.CREATED\_DESC,  WorkflowOrder.PRIORITY\_ASC,  WorkflowOrder.PRIORITY\_DESC,  WorkflowOrder.STATE\_ASC,  WorkflowOrder.STATE\_DESC,  WorkflowOrder.WITH\_WARNING\_ASC,  WorkflowOrder.WITH\_WARNING\_DESC,  WorkflowOrder.SUBJECT\_ASC,  WorkflowOrder.SUBJECT\_DESC,  WorkflowOrder.ENDED\_ASC,  WorkflowOrder.ENDED\_DESC) | Input | Order |

* **GetProcessDefinitionById**

This method returns a Process Definition type object whose Id coincides with the specified one.

GetProcessDefinitionById (id) : WorkflowProcessDefinition)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | Id | Numeric | Input | Process definition identifier |

* **GetProcessInstanceById**

This method returns a Process Instance type object whose identifier coincides with the specified one.

GetProcessInstanceById (id) : WorkflowProcessInstance

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | id | Numeric | Input | Identificador de la instancia de proceso |

**GetWorkitemById**

This method returns a Workitem type object whose identifier coincides with the specified one.

GetWorkitemById (id) : WorkflowWorkitem

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | id | Numeric | Input | workitem identifier |

**GetActivityById**

This method returns an Activity type object whose identifier (of both Process and Activity) coincides with the specified one.

GetActivityById (processDefinitionId, activityId) : WorkflowActivity

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | processDefinitionId | Numeric | Input | process defintion identifier |
| 2 | activityId | Numeric | Input | Activity identifier |

**GetProcessDefinitionByName**

This method returns the first Process Definition type object whose name coincides with the specified one.

GetProcessDefinitionByName (name) : WorkflowProcessDefintion

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | Name | Character | Input | process definition name |

**GetActivityByName**

This method returns the first Activity type object whose name coincides with the specified one.

GetActivityByName (name) : WorkflowActivity

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | name | Character | Input | activity name |

**GetProcessInstanceBySubject**

This method returns the first Process Instance type object whose subject coincides with the specified one.

GetProcessInstanceSubject ( subject) : WorkflowProcessInstance

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | subject | Character | Input | process instance subject |

* **GetOrganizationalModel**

This method returns the Organizational Model object.

GetOrganizationalModel () : WorkflowOrganizationalModel

* **Get EventRepository**

This method returns the Event Repository object.

GetEventRepository () : Workflow Event Repository

* **GetDocumentRepository**

This method returns the Document Repository object.

* **ListCalendars**

This method returns the list of calendars matching the established filter.

ListCalendars (filter) : Collection (WorkflowCalendar)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | filter | WorkflowFilter | Input | Filter |
