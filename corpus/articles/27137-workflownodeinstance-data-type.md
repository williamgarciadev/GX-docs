---
title: "WorkflowNodeInstance Data Type"
source_id: 27137
source_url: https://wiki.genexus.com/commwiki/wiki?27137
genexus_version: "18"
---

# WorkflowNodeInstance Data Type

This data type represents a Workflow node instance. It is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

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
| Node | WorkflowNode | Read |  |
| NodeId | WorkflowNodeId | Read |  |
| ProcessInstance | WorkflowProcessInstance | Read |  |
| ProcessInstanceId | WorkflowProcessInstanceId | Read |  |
| Successors | WorkflowNodeInstance | Read |  |
| Predecessors | WorkflowNodeInstance | Read |  |

### [Methods](#Methods)

* **Load**

Allows loading a workflow node instance.

Load(id) : Numeric

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | WorkflowGatewayInstanceId | Input | Gateway Id |

#### 

### [Availability](#Availability)

As from [GeneXus X Evolution 3 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?26959,,)


|  |
| --- |
| **Backlinks** |
| [Workflow Server Data Type](https://wiki.genexus.com/commwiki/wiki?11671) | [WorkflowBusinessEventInstance Data Type](https://wiki.genexus.com/commwiki/wiki?12190) | [WorkflowProcessInstance Data Type](https://wiki.genexus.com/commwiki/wiki?17771) |
| [WorkflowWorkitem Data Type](https://wiki.genexus.com/commwiki/wiki?11731) |

---
