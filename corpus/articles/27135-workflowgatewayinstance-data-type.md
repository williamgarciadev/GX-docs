---
title: "WorkflowGatewayInstance Data Type"
source_id: 27135
source_url: https://wiki.genexus.com/commwiki/wiki?27135
genexus_version: "18"
---

# WorkflowGatewayInstance Data Type

This data type, that it is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350), represents a Workflow gateway instance.

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | WorkflowGatewayInstanceId | Read | Identifier |
| Created | DateTime | Read |  |
| Ended | DateTime | Read |  |
| State | WorkflowBusinessEventInstanceState | Read |  |
| ProcessDefinition | WorkflowProcessDefinition | Read |  |
| ProcessDefinitionId | WorkflowProcessDefinitionId | Read |  |
| Gateway | WorkflowGateway | Read |  |
| GatewayId | WorkflowGatewayId | Read |  |
| ProcessInstance | WorkflowProcessInstance | Read |  |
| ProcessInstanceId | WorkflowProcessInstanceId | Read |  |
| NodeInstance | WorkflowNodeInstance | Read |  |

### [Methods](#Methods)

* **Load**

Allows loading a workflow gateway instance.

Load(id) : Numeric

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | WorkflowGatewayInstanceId | Input | Gateway Id |

#### 

### [Availability](#Availability)

As from [GeneXus X Evolution 3 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?26959,,)
