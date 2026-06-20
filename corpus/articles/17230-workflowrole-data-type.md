---
title: "WorkflowRole Data Type"
source_id: 17230
source_url: https://wiki.genexus.com/commwiki/wiki?17230
genexus_version: "18"
---

# WorkflowRole Data Type

This data type represents a functional role within the organization, and it is provided by the [Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | [WorkflowRoleId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Identifier |
| Name | [WorkflowName](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Name |
| hasParent | Boolean | Read | Indicates if it is subordinated to another role |
| hasChildren | Boolean | Read | Indicates if it has subordinated roles |
| Parent | [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,) | Read | Parent Role |
| Users | Collection ([WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,)) | Read | Associated users |
| Children | Collection ([WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,)) | Read | Subordinated roles |
| Error | [WorflowError](https://wiki.genexus.com/commwiki/wiki?10283) | Read | Error |
| GUID | [WorflowGUID](https://wiki.genexus.com/commwiki/wiki?15734) | Read | GUID |

### [Methods](#Methods)

* **AddChild**

 This method allows subordinating the specified role to the current role.

 AddChild (child)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| child | [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,) | Input | Role to be subordinated |

* **RemoveChild**

This method allows removing the subordinating relationship between the specified role and the current role.

RemoveChild (child)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| child | [WorkflowRole](https://wiki.genexus.com/commwiki/wiki?10267,,) | Input | Role with which the subordinating relationship will be removed |

* **AddUser**

 Adds the specified user to the collection of users associated to the role.

 AddUser (user)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| user | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | User to be associated to the role |

* **RemoveUser**

 Removes the specified user from the collection of users associated to the role.

 RemoveUser (user)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| user | [WorkflowUser](https://wiki.genexus.com/commwiki/wiki?10268,,) | Input | User to be dissociated from the role |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [GXflow - GAM Integration](https://wiki.genexus.com/commwiki/wiki?18454) | [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |
| [WorkflowOrganizationalModel data type](https://wiki.genexus.com/commwiki/wiki?10266) |

---
