---
title: "Workflow Enumerated Domains"
source_id: 11306
source_url: https://wiki.genexus.com/commwiki/wiki?11306
genexus_version: "18"
---

# Workflow Enumerated Domains

In this document, you can see the different values that a Workflow Enumerated domain can take.

### [WorkflowAccessLevel](#WorkflowAccessLevel)

|  |
| --- |
| **Values** |
| LOW |
| MEDIUM |
| HIGH |
| NULL |

### [WorkflowActionPerformed](#WorkflowActionPerformed)

|  |
| --- |
| **Values** |
| NEW |
| UPDATE |
| DELETE |
| READ |
| CHECK\_IN |
| CHECK\_OUT |
| UNDO\_CHECK\_OUT |

### [WorkflowActivityClass](#WorkflowActivityClass)

|  |
| --- |
| **Values** |
| NORMAL |
| BATCH |
| SUBPROCESS |
| EMBEDDED\_SUBPROCESS |
| ROUTE |

### [WorkflowAssignmentChangeType](#WorkflowAssignmentChangeType)

|  |
| --- |
| **Values** |
| FROM\_USER\_TO\_USER |
| FROM\_USER\_TO\_ROLE |
| FROM\_USER\_TO\_NA |
| FROM\_ROLE\_TO\_USER |
| FROM\_ROLE\_TO\_ROLE |
| FROM\_ROLE\_TO\_NA |
| FROM\_NA\_TO\_USER |
| FROM\_NA\_TO\_ROLE |

### [WorkflowDimension](#WorkflowDimension)

|  |
| --- |
| **Values** |
| SCALAR |
| VECTOR |

### [WorkflowDocumentInstanceState](#WorkflowDocumentInstanceState)

|  |
| --- |
| **Values** |
| OPEN\_CHECKED\_IN |
| OPEN\_CHECKED\_OUT |
| OPEN |
| CLOSED |

### [WorkflowEventSource](#WorkflowEventSource)

|  |
| --- |
| **Values** |
| DOCUMENT\_MANAGER |
| DATA\_MANAGER |
| RESOURCE\_MANAGER |
| PROCESS\_MANAGER |
| DEADLINE\_SCHEDULER |

### [WorkflowEventType](#WorkflowEventType)

|  |
| --- |
| **Values** |
| NEW\_INSTANCE |
| STATE\_CHANGE |
| PRIORITY\_CHANGE |
| ASSIGNMENT\_CHANGE |
| DATA\_CHANGE |
| WARNING |
| DEADLINE |
| ERROR |
| CONDITION\_NOT\_SATISFIED |
| RESOURCE\_NOT\_AVAILABLE |
| EXTERNAL |
| ACTION\_PERFORMED |

### [WorkflowOrder](#+WorkflowOrder)

|  |
| --- |
| **Values** |
| ID\_ASC |
| ID\_DESC |
| NAME\_ASC |
| NAME\_DESC |
| VERSION\_ASC |
| VERSION\_DESC |
| STATE\_ASC |
| STATE\_DESC |
| CREATED\_ASC |
| CREATED\_DESC |
| UPDATED\_ASC |
| UPDATED\_DESC |
| AUTHOR\_ASC |
| AUTHOR\_DESC |
| TYPE\_ASC |
| TYPE\_DESC |
| USER\_ASC |
| USER\_DESC |
| TIMESTAMP\_ASC |
| TIMESTAMP\_DESC |
| SUBJECT\_ASC |
| SUBJECT\_DESC |
| TARGET\_ASC |
| TARGET\_DESC |
| ACTIVITY\_ASC |
| ACTIVITY\_DESC |
| PROCESS\_DEFINITION\_ASC |
| PROCESS\_DEFINITION\_DESC |
| DOCUMENT\_DEFINITION\_ASC |
| DOCUMENT\_DEFINITION\_DESC |
| OBJECT\_TYPE\_ASC |
| OBJECT\_TYPE\_DESC |
| SOURCE\_ASC |
| SOURCE\_DESC |
| PRIORITY\_ASC |
| PRIORITY\_DESC |
| WITH\_WARNING\_ASC |
| WITH\_WARNING\_DESC |
| ENDED\_ASC |
| ENDED\_DESC |
| NONE |

### [WorkflowObjectType](#WorkflowObjectType+)

|  |
| --- |
| **Values** |
| WORKITEM |
| PROCESS\_DEFINITION |
| PROCESS\_INSTANCE |
| APPLICATION\_DATA |
| SERVER |
| DOCUMENT\_INSTANCE |
| DOCUMENT |

### [WorkflowPriority](#WorkflowPriority)

|  |
| --- |
| **Values** |
| LOW |
| NORMAL |
| HIGH |

### [WorkflowProcessDefinitionState](#WorkflowProcessDefinitionState)

|  |
| --- |
| **Values** |
| ENABLED |
| DISABLED |

### [WorkflowProcessInstanceState](#WorkflowProcessInstanceState)

|  |
| --- |
| **Values** |
| OPEN |
| OPEN\_RUNNING |
| OPEN\_NOTRUNNING |
| OPEN\_NOTRUNNING\_NONSTARTED |
| OPEN\_NOTRUNNING\_SUSPENDED |
| CLOSED |
| CLOSED\_ABORTED |
| CLOSED\_COMPLETED |
| CLOSED\_TERMINATED |

### [WorkflowRestrictionDefinitionType](#WorkflowRestrictionDefinitionType)

|  |
| --- |
| **Values** |
| SIMPLE |
| INHERITABLE |

### [WorkflowWorkitemState](#WorkflowWorkitemState)

|  |
| --- |
| **Values** |
| OPEN |
| OPEN\_ACTIVE |
| OPEN\_ACTIVE\_READY |
| OPEN\_ACTIVE\_ASSIGNED |
| OPEN\_ACTIVE\_INPROCESS |
| OPEN\_SUSPENDED |
| CLOSED |
| CLOSED\_COMPLETED |
| CLOSED\_ABNORMAL |
| CLOSED\_ABNORMAL\_ABORTED |
| CLOSED\_ABNORMAL\_CANCELED |
| CLOSED\_ABNORMAL\_DELEGATED |
| CLOSED\_ABNORMAL\_EXPIRED |
| CLOSED\_ABNORMAL\_INTERRUPTED |
| CLOSED\_ABNORMAL\_SKIPPED |
| CLOSED\_ABNORMAL\_TERMINATED |
| CLOSED\_ABNORMAL\_UNDONE |


|  |
| --- |
| **Backlinks** |
| [WorkflowStateChangeEvent Data Type](https://wiki.genexus.com/commwiki/wiki?10276) |

---
