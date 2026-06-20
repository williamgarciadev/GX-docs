---
title: "WorkflowNode Data Type"
source_id: 27136
source_url: https://wiki.genexus.com/commwiki/wiki?27136
genexus_version: "18"
---

# WorkflowNode Data Type

This data type represents a Workflow node, and it is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | WorkflowGatewayId | Read | Identifier |
| Name | WorkflowName | Read |  |
| ProcessDefinitionId | WorkflowProcessDefinitionId | Read |  |
| ProcessDefinition | WorkflowProcessDefinition | Read |  |
| GUID | WorkflowGUID | Read |  |
| Type | WorkflowGatewayType | Read |  |
| Predecessors | WorkflowNode | Read |  |
| Successors | WorkflowNode | Read |  |

### [Methods](#Methods)

* **Load**

Allows loading a node.

processDefinitionId : WorkflowProcessDefinitionId  
id : Numeric

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | WorkflowGatewayInstanceId | Input | Gateway Id |

#### 

* **LoadByName**

Allows loading a node.

name : WorkflowName

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | WorkflowGatewayInstanceId | Input | Gateway Id |

### [Availability](#Availability)

As from [GeneXus X Evolution 3 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?26959,,)


|  |
| --- |
| **Backlinks** |
| [Workflow Server Data Type](https://wiki.genexus.com/commwiki/wiki?11671) | [WorkflowActivity Data Type](https://wiki.genexus.com/commwiki/wiki?17229) | [WorkflowBusinessEvent Data Type](https://wiki.genexus.com/commwiki/wiki?12189) |
| [WorkflowProcessDefinition Data Type](https://wiki.genexus.com/commwiki/wiki?17239) |

---
