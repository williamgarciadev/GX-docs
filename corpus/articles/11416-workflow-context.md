---
title: "Workflow Context"
source_id: 11416
source_url: https://wiki.genexus.com/commwiki/wiki?11416
genexus_version: "18"
---

# Workflow Context

The Workflow Context is a data type that allows you to work with the process definition, process instance and workitem that are running. You can access them using the WorkflowContext variable this way:

```
&WorkflowProcessDefinition=&WorkflowContext.ProcessDefinition
&WorkflowProcessInstance=&WorkflowContext.ProcessInstance
&WorkflowWorkitem=&WorkflowContext.Workitem
```

As of GeneXus X, it is not necessary to add the parm rule with the three parameters in all the objects, it is only required when working with procedures associated with conditions.

If you want to use a procedure associated with a condition instead of the condition editor you have to define the following parm rule:

```
parm(in:&wfprocessdefinition,in:&wfprocessinstance,in:&wfworkitem,out:&conditioncode);
```

Where the variables are defined as follows:

```
&wfprocessdefinition - WorkflowProcessDefinition
&wfprocessinstance - WorkflowProcessInstance
&wfworkitem - WorkflowWorkitem
&conditioncode - Numeric(4.0)
```

### [Warning: you can't use the &WorkflowContext in procedures associated with conditionals, timers events and event handling properties.](#Warning%3A+you+can%27t+use+the+%26WorkflowContext+in+procedures+associated+with+conditionals%2C+timers+events+and+event+handling+properties.)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [HowTo: Get and Set a Relevant Data Value](https://wiki.genexus.com/commwiki/wiki?11720) |

---
