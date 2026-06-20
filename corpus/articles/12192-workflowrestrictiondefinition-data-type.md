---
title: "WorkflowRestrictionDefinition Data Type"
source_id: 12192
source_url: https://wiki.genexus.com/commwiki/wiki?12192
genexus_version: "18"
---

# WorkflowRestrictionDefinition Data Type

**Deprecated**: Since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066). Replaced by [WorkflowOrganizationalUnitDefinition Data Type](https://wiki.genexus.com/commwiki/wiki?10269).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Name | Character | Read | Name |
| Description | Character | Read | Description |
| Type | [WorkflowRestrictionDefinitionType](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Type |
| Values | Collection (Character) | Read | Values |

### [Methods](#Methods)

* **AddValue**

Allows to add a new value.  
  
AddValue (value)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | value | Character | Input | Value |

* **RemoveValue**

Allows removing a new value.  
  
RemoveValue (value)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Name** | **Type** | **Movement** | **Description** |
| 1 | value | Character | Input | Value |


|  |
| --- |
| **Backlinks** |
| [WorkflowOrganizationalModel data type](https://wiki.genexus.com/commwiki/wiki?10266) |

---
