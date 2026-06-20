---
title: "WorkflowGateway Data Type"
source_id: 27131
source_url: https://wiki.genexus.com/commwiki/wiki?27131
genexus_version: "18"
---

# WorkflowGateway Data Type

The WorkflowGateway Data Type represents a Workflow gateway, and it is provided by [Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240).

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
| Node | WorkflowNode | Read |  |

### [Methods](#Methods)

* **Load**

Allows loading a gateway.

Load(id) : Numeric

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | WorkflowGatewayInstanceId | Input | Gateway Id |

#### 

### [Availability](#Availability)

As from [GeneXus X Evolution 3 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?26959,,)
