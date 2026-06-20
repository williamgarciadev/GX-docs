---
title: "WorkflowOrganizationalUnit Data Type"
source_id: 10270
source_url: https://wiki.genexus.com/commwiki/wiki?10270
genexus_version: "18"
---

# WorkflowOrganizationalUnit Data Type

This Data Type represents an instance of an organizational unit. That is an organizational unit that has an instantiated value, and it is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Name | Character | Read | Name |
| Description | Character | Read | Description |
| OrganizationalUnitDefinitionName | Character | Read | Definition Name |
| OrganizationalUnitDefinition | WorkflowOrganizationalUnitDefinition | Read | Definition |
| Error | WorkflowError | Read | Error |
| Users | Collection (only includes user Id and name) | Read | Users who belong to the Organizational Unit |

### [Methods](#Methods)

* **AddUser**

 This method allows adding a user to an organizational unit.

 AddUser(user)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| User | WorkflowUser | Input | User |

* **RemoveUser**

 This method allows removing a user from an organizational unit.

 RemoveUser(user)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| User | WorkflowUser | Input | User |

* **Load**

These methods allow loading an organizational unit, from its name and the definition name.

 Load(definitionName, name)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| definitionName | Character | Input | Organizational Unit Definition name |
| name | Character | Input | Organizational Unit name |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) | [WorkflowOrganizationalModel data type](https://wiki.genexus.com/commwiki/wiki?10266) | [WorkflowProcessInstance Data Type](https://wiki.genexus.com/commwiki/wiki?17771) |
| [WorkflowRestriction Data Type](https://wiki.genexus.com/commwiki/wiki?12191) | [WorkflowUser Data Type](https://wiki.genexus.com/commwiki/wiki?17273) |

---
