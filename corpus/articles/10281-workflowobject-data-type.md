---
title: "WorkflowObject Data Type"
source_id: 10281
source_url: https://wiki.genexus.com/commwiki/wiki?10281
genexus_version: "18"
---

# WorkflowObject Data Type

This Data Type represents a generic Workflow object and it is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Type | Numeric (WorkflowObjectType) | Read | Type of object |

### [Methods](#Methods)

* **ToProcessInstance**

Converts the object in a process instance.

ToProcessInstance(): WorkflowProcessInstance

* **ToDocumentInstance**

Converts the object in a document instance.

ToDocumentInstance(): WorkflowDocumentInstance

* **ToWorkitem**

Converts the object in a workitem.

ToWorkitem(): WorkflowWorkitem

* **ToProcessDefinition**

Converts the object in a process definition.

ToProcessDefinition(): WorkflowProcessDefinition

* **ToApplicationData**

Converts the object to application data.

ToApplicationData(): WorkflowApplicationData

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) | [WorkflowDataChangeEvent Data Type](https://wiki.genexus.com/commwiki/wiki?10278) |

---
