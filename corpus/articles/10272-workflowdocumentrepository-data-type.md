---
title: "WorkflowDocumentRepository Data Type"
source_id: 10272
source_url: https://wiki.genexus.com/commwiki/wiki?10272
genexus_version: "18"
---

# WorkflowDocumentRepository Data Type

This Data Type, that it is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350), represents the document's repository.

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| EnableDocuments | Boolean | Read/Write | Allows enabling/disabling the use of documents |
| Error | WorkflowError | Read | Error |

### [Methods](#Methods)

* **ListDocumentDefinitions**

This method returns a collection with all the documents definitions matching the specified filters.

ListDocumentDefinitions (filter): Collection (WorkflowDocumentDefinition)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Filter | WorkflowFilter Valid filters: Name | Input | Filter |

* **ListDocumentDefinitionsOrderBy**

This method returns a collection with all the document definitions matching the specified filters in the specified order.

ListDocumentDefinitionsOrderBy (filter, order): Collection (WorkflowDocumentDefinition)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| filter | WorkflowFilter Valid filters: Name | Input | Filter |
| order | Numeric (WorkflowOrder.ID\_ASC  WorkflowOrder.ID\_DESC  WorkflowOrder.NAME\_ASC  WorkflowOrder.NAME\_DESC) | Input | Order |

* **ListDocumentInstances**

 This method returns a collection with all the document instances matching the specified filters.

 ListDocumentInstances (filter): Collection (WorkflowDocumentInstance)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| filter | WorkflowFilter Valid filters: From, To, Name, User, State, DocumentDefinition | Input | Filter |

* **ListDocumentInstancesOrderBy**

 This method returns a collection with all document instances matching the specified filters in the specified order.

 ListDocumentInstancesOrderBy (filter, order): Collection (WorkflowDocumentInstance)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| filter | WorkflowFilter Valid filters: From, To, Name, User, State, DocumentDefinition | Input | Filter |
| order | Numeric (WorkflowOrder.ID\_ASC,  WorkflowOrder.ID\_DESC,  WorkflowOrder.NAME\_ASC,  WorkflowOrder.NAME\_DESC,  WorkflowOrder.STATE\_ASC,  WorkflowOrder.STATE\_DESC,  WorkflowOrder.VERSION\_ASC,  WorkflowOrder.VERSION\_DESC,  WorkflowOrder.AUTHOR\_ASC,  WorkflowOrder.AUTHOR\_DESC,  WorkflowOrder.CREATED\_ASC,  WorkflowOrder.CREATED\_DESC,  WorkflowOrder.UPDATED\_ASC,  WorkflowOrder.UPDATED\_DESC, WorkflowOrder.DOCUMENT\_DEFINITION\_ASC, WorkflowOrder.DOCUMENT\_DEFINITION\_ASC) | Input | Order |

* **GetDocumentDefinitionById**

 These methods return a document definition by its Id.

 GetDocumentDefinitionById (id): WorkflowDocumentDefinition

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| id | Numeric | Input | Document Definition Identifier |

* **GetDocumentDefinitionByName**

 This method returns a document definition by its name.

 GetDocumentDefinitionByName (name): WorkflowDocumentDefinition

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| name | Character | Input | Document Definition Name |

* **GetDocumentInstanceById**

 This method returns a document instance by its Identifier.

 GetDocumentInstanceById(id, version): WorkflowDocumentInstance

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| id | Numeric | Input | Document Definition Identifier |
| Version | Numeric | Input | Document version. Cero value allows to get the last version available. |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |

---
