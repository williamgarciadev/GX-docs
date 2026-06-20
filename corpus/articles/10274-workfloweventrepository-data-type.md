---
title: "WorkflowEventRepository Data Type"
source_id: 10274
source_url: https://wiki.genexus.com/commwiki/wiki?10274
genexus_version: "18"
---

# WorkflowEventRepository Data Type

This Data Type represents the event's repository, it is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| EnableEvents | WorkflowBoolean | Read/Write | Permite habilitar/deshabilitar el disparo de eventos |
| Error | WorkflowError | Read | Error |

### [Methods](#Methods)

* **ListEvents**

This method returns a collection with all the events matching the specified filters.

ListEvents (filter): Collection (WorkflowEvent)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilterValid Filters: From, To, EventType, ObjectType, User | Input | Filter |

* **ListEventsOrderBy**

This method returns a collection with all the events matching the specified filters in the specified order.

ListEvents (filter, order): Collection (WorkflowEvent)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid Filters: From, To, EventType, ObjectType, User | Input | Filter |
| Order | Numeric (WorkflowOrder.ID\_ASC, WorkflowOrder.ID\_DESC, WorkflowOrder.TIMESTAMP\_ASC, WorkflowOrder.TIMESTAMP\_DESC, WorkflowOrder.USER\_ASC, WorkflowOrder.USER\_DESC, WorkflowOrder.TYPE\_ASC, WorkflowOrder.TYPE\_DESC, WorkflowOrder.SOURCE\_ASC, WorkflowOrder.SOURCE\_DESC, WorkflowOrder.OBJECT\_TYPE\_ASC, WorkflowOrder.OBJECT\_TYPE\_DESC, WorkflowOrder.TARGET\_ASC, WorkflowOrder.TARGET\_DESC) | Input | Order |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |

---
