---
title: "WorkflowContext Data Type"
source_id: 12187
source_url: https://wiki.genexus.com/commwiki/wiki?12187
genexus_version: "18"
---

# WorkflowContext Data Type

This oData Type represents the workflow context and gives information about the execution context. It is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| ProcessDefinition | [WorkflowProcessDefinition](https://wiki.genexus.com/commwiki/wiki?11698,,) | Read | Task Process Definition |
| Workitem | [WorkflowWorkitem](https://wiki.genexus.com/commwiki/wiki?11731) | Read | Task Workitem |
| ProcessInstance | [WorkflowProcessInstance](https://wiki.genexus.com/commwiki/wiki?11702,,) | Read | Task Process Instance |

### [Methods](#Methods)

* **Load**

 Allows loading workflow context.

Load (processDefinitionId,processInstanceId,workitemId)

* **CheckRights**

 Allows to check if a Workflow Web Session exists and if the user has permissions to execute the workitem.

CheckRights () : WorkflowError

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow API](https://wiki.genexus.com/commwiki/wiki?51350) | [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |

---
