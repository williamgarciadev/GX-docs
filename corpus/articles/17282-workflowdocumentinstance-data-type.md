---
title: "WorkflowDocumentInstance Data Type"
source_id: 17282
source_url: https://wiki.genexus.com/commwiki/wiki?17282
genexus_version: "18"
---

# WorkflowDocumentInstance Data Type

This data type provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350) represents a document instance.

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | [WorkflowDocumentInstanceId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Identifier |
| Version | [WorkflowVersion](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Version |
| Name | [WorkflowDescription](https://wiki.genexus.com/commwiki/wiki?15734) | Read/ Write | Name |
| Created | DateTime | Read | Date and time of creation |
| Updated | DateTime | Read | Date and time of last update |
| Comments | [WorkflowComment](https://wiki.genexus.com/commwiki/wiki?15734) | Read/ Write | Comments |
| State | [WorkflowDocumentInstanceState](https://wiki.genexus.com/commwiki/wiki?15734) | Read | State |
| CheckedOutBy | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Read | The user that has locked the document |
| CheckedOutAt | DateTime | Read | Date and time when the document was locked |
| DocumentDefinition | [WorkflowDocumentDefinition](https://wiki.genexus.com/commwiki/wiki?10260) | Read | Document Definition |
| DocumentDefinitionId | [WorkflowDocumentDefinitionId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Document Definition Identifier |
| Author | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Read | Author |
| Error | [WorkflowError](https://wiki.genexus.com/commwiki/wiki?10283) | Read | Error |
| DigitalSignature | [WorkflowDigitalSignature](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Digital Signature |
| Versions | WorkflowDocumentInstance (Collection) | Read | Document Instance Versions |
| ExtendedAttributes | WorkflowAttribute (Collection) | Read | List of extended attributes |

### [Methods](#Methods)

* **Read**

This method allows recovering a document.

Read (user, workitem, targetDirectory): character

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| user | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | User who want to access the document |
| workitem | [WorkflowWorkitem](https://wiki.genexus.com/commwiki/wiki?11731) (opcional) | Input | Allows to register the workitem between the operation |
| targetDirectory | Character (opcional) | Input | Directory where the document will be copied |

* **CheckIn**

 This method allows logging into a previously locked document and check in the right to Write.

CheckIn (user, workitem, file)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| user | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | User that want to check in the document |
| workitem | [WorkflowWorkitem](https://wiki.genexus.com/commwiki/wiki?11731) | Input | Allows to register the workitem between the operation |
| file | Character | Input | Complete path to the document |

* **CheckInWithSignature**

This method allows logging into a previously locked document and check in the right to Write.

CheckIn (user, workitem, file, signature, base64Certificate)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| user | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | User that want to check in the document |
| workitem | [WorkflowWorkitem](https://wiki.genexus.com/commwiki/wiki?11731) | Input | Allows to register the workitem between the operation |
| file | Character | Input | Complete path to the document |
| signature | Character | Input | Digital signature |
| base64Certificate | Character | Input | base 64 encoded certicate |

* **CheckOut**

This method allows recovering a document, check out the right to Write.

CheckOut (workitem, targetDirectory): file

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| user | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | User that wants to recover and block the document |
| workitem | [WorkflowWorkitem](https://wiki.genexus.com/commwiki/wiki?11731) | Input | Allows to register the workitem between the operation |
| targetDirectory | Character | Input | Directory to copy the document |

#### 

* **UndoCheckOut**

This method allows undoing the check out on the right to Write that was previously done to a document.

UndoCheckOut (user)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| user | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | User the wants to unblock the document |

#### 

* **Load**

This method allows loading a document instance from its id and version

Load (id,version)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| id | [WorkflowDocumentInstanceId](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Workflow document instance id |
| version | [WorkflowVersion](https://wiki.genexus.com/commwiki/wiki?15734) | Input | Workflow version id |

#### 

* **Share**

This method allows sharing a document instance with another process instance.

Share(processinstance)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| processinstance | [WorkflowProcessInstance](https://wiki.genexus.com/commwiki/wiki?11702,,) | Input | Process Instance to share the document |

#### 

* **Remove**

This method allows removing the user document.

Remove (user)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| user | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | User´s document to be removed. |

* **AddAttribute**

 This method allows adding an attribute

Addattribute (attribute)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| attribute | [WorkflowAttribute](https://wiki.genexus.com/commwiki/wiki?10271) | Input | Attribute to be added. |

* **RemoveAttribute**

 This method allows removing an attribute

Removeattribute (attribute)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| attribute | [WorkflowAttribute](https://wiki.genexus.com/commwiki/wiki?10271) | Input | Attribute to be removed. |

 

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |

---
