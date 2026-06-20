---
title: "WorkflowFilter Data Type"
source_id: 10282
source_url: https://wiki.genexus.com/commwiki/wiki?10282
genexus_version: "18"
---

# WorkflowFilter Data Type

In this Data Type, you specify the values to filter the objects loaded in the collections. It is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| User | WorkflowUser | Read/Write | User |
| Role | WorkflowRole | Read/Write | Role |
| Restriction (Deprecated) | WorkflowRestriction | Read/Write | Restriction |
| State | Character | Read/Write | State |
| ProcessDefinition | WorkflowProcessDefinition | Read/Write | Process Definition |
| ProcessInstance | WorkflowProcessInstance | Read/Write | Process Instance |
| Activity | WorkflowActivity | Read/Write | Activity |
| Subject | Character | Read/Write | Subject |
| Priority | Numeric (WorkflowPriority) | Read/Write | Priority |
| From | DateTime | Read/Write | Starting date |
| To | DateTime | Read/Write | Ending date |
| CreatedFrom | DateTime | Read/Write | Start creation date |
| CreatedTo | DateTime | Read/Write | End creation date |
| EndedFrom | DateTime | Read/Write | Start date of completion |
| EndedTo | DateTime | Read/Write | End date of completion |
| Name | Character | Read/Write | Name |
| EventType | Numeric (WorkflowEventType) | Read/Write | Event Type |
| ObjectType | Numeric (WorkflowObjectType) | Read/Write | Type of object |
| DocumentDefinition | WorkflowDocumentDefinition | Read/Write | Document Definition |
| WithWarning | WorkflowBoolean | Read/Write | With Warning |
| OrganizationalUnitDefinition | WorkflowOrganizationalUnitDefinition | Read/Write | Org. Unit Definition |
| OrganizationalUnit | WorkflowOrganizationalUnit | Read/Write | Org. Unit |
| Search | WorkFlowText | Read/Write | Search |
| ApplicationDataName | Character | Read/Write | Application Data Name |
| ApplicationDataValue | LongVarChar | Read/Write | Application Data Value |
| Limit | Numeric | Read/Write |  |
| Start | Numeric | Read/Write |  |

### [Methods](#Methods)

* **Clear**

This method allows initializing the value of the filter properties.  
Clear ()

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) | [WorkflowOrganizationalModel data type](https://wiki.genexus.com/commwiki/wiki?10266) |

---
