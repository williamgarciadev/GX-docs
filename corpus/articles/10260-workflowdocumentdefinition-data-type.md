---
title: "WorkflowDocumentDefinition Data Type"
source_id: 10260
source_url: https://wiki.genexus.com/commwiki/wiki?10260
genexus_version: "18"
---

# WorkflowDocumentDefinition Data Type

This Data Type represents a document definition, it is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | Numeric | Read | Identifier |
| Name | Character | Read | Name |
| Error | WorkflowError | Read | Error |
| FileExtension | Character | Read | Document file extension |
| hasTemplate | Boolean | Read | It indicates if the document has a template |
| MimeType | Character | Read | It indicates the format of the document |

### [Methods](#Methods)

* **CreateInstance**

CreateInstates a new document instance associated to the specified workitem.

CreateInstance (workitem, name): WorkflowDocumentInstance

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| workitem | WorkflowWorkitem | Input | Workitem |
| name | Character | Input | Document name to be created |

* **CreateInstanceFromFile**

This method creates a new instance of the document associated to the workitem specified, based on a specific file.

CreateInstanceFromFile (workitem, name, file): WorkflowDocumentInstance

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| workitem | WorkflowWorkitem | Input | Workitem |
| name | Character | Input | Document name to be created |
| file | Character | Input | Complete path to the file |

* **Load**

This method allows loading a document definition from its Id.

Load (Id)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | WorkflowDocumentDefinitionId | Input | Document Definition identifier |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) | [WorkflowActivity Data Type](https://wiki.genexus.com/commwiki/wiki?17229) | [WorkflowDocumentInstance Data Type](https://wiki.genexus.com/commwiki/wiki?17282) |
| [WorkflowProcessDefinition Data Type](https://wiki.genexus.com/commwiki/wiki?17239) |

---
