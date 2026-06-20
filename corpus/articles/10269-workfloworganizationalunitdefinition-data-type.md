---
title: "WorkflowOrganizationalUnitDefinition Data Type"
source_id: 10269
source_url: https://wiki.genexus.com/commwiki/wiki?10269
genexus_version: "18"
---

# WorkflowOrganizationalUnitDefinition Data Type

This Data Type, that is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350), represents the definition of an organizational unit.

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Name | Character | Read | Name |
| Description | Character | Read | Description |
| Propagable | Boolean | Read | Organizational Unit Type |
| Error | WorkflowError | Read | Error |

### [Methods](#Methods)

* **AddOrganizationalUnit**

This method allows adding organizational units.

AddOrganizationalUnit(name, description) : OrganizationalUnit

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Name | Character | Input | Name |
| Description | Character | Input | Description |

* **GetOrganizationalUnitByName**

This method returns an organizational unit by name.

GetOrganizationalUnitByName(Character name): OrganizationalUnit

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Name | Character | Input | Name |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) | [WorkflowOrganizationalModel data type](https://wiki.genexus.com/commwiki/wiki?10266) | [WorkflowRestrictionDefinition Data Type](https://wiki.genexus.com/commwiki/wiki?12192) |

---
