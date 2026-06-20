---
title: "Workflow API"
source_id: 51350
source_url: https://wiki.genexus.com/commwiki/wiki?51350
genexus_version: "18"
---

# Workflow API

GeneXus BPM Suite provides an API that allows you to automate the interactions with the Workflow’s engine. This is done with the [Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) through the methods and properties of each one.

Since the GeneXus 18 upgrade 3, to use the Workflow API it is necessary to install the [GeneXusBPM module](https://wiki.genexus.com/commwiki/wiki?54058,,).

### [Most commonly used Workflow Data Types](#Most+commonly+used+Workflow+Data+Types)

These are some of the most commonly used Workflow Data Types and their main characteristics. If you are getting started with the Workflow API, you should learn about them.

#### [[WorkflowProcessDefinition](https://wiki.genexus.com/commwiki/wiki?17239)](#wiki%3F17239%2CWorkflowProcessDefinition%2BData%2BType+WorkflowProcessDefinition)

It represents a process definition (it is the equivalent of a diagram in the GeneXus IDE) and allows you to access some process properties, like name, version, tasks included, etc. It is also possible to create an instance of this process through the method CreateInstance().

#### [[WorkflowProcessInstance](https://wiki.genexus.com/commwiki/wiki?17771)](#wiki%3F17771%2CWorkflowProcessInstance%2BData%2BType+WorkflowProcessInstance)

It represents the execution of a process definition (it is the equivalent of a process instance in the GXflow inbox) and gives you information about this particular instance, like the subject, user owner, active workitems, etc. It is also possible to do almost the same you can do in the inbox, like suspend, abort or reactivate the process.

#### [[WorkflowActivity](https://wiki.genexus.com/commwiki/wiki?17229)](#wiki%3F17229%2CWorkflowActivity%2BData%2BType+WorkflowActivity)

It represents an activity in the context of a process definition (it is the equivalent of a task in the GeneXus IDE) and allows you to access the task properties. It is also possible to assign or unassign roles through the methods AssignRole() UnasassignRole().

#### [[WorkflowWorkitem](https://wiki.genexus.com/commwiki/wiki?11731)](#wiki%3F11731%2CWorkflowWorkitem%2BData%2BType+WorkflowWorkitem)

It represents the execution of an activity in the context of a process instance (it is the equivalent of a task in the GXflow inbox) and allows you to access information about this activity. It is also possible to do almost the same you can do in the inbox, like assign, delegate or complete the task.

#### [[WorkflowContext](https://wiki.genexus.com/commwiki/wiki?12187)](#wiki%3F12187%2CWorkflowContext%2BData%2BType+WorkflowContext)

It gives you information about the execution context and allows you to know the values of the actual WorkflowProcess, WorkflowInstance, and WorkflowWorkitem.

### [Special considerations](#Special+considerations)

There are a few things to consider when using Workflow Data Types.

Keep in mind that the [WorkflowServer](https://wiki.genexus.com/commwiki/wiki?11671) object is the entry point to the other Workflow Data Types, so before doing anything, you must perform a WorkflowServer.connect() to obtain a valid session to interact with the Workflow engine. Also, this object allows you to obtain information about the execution environment.

Be aware that when you are using any of the Workflow Data Types exclusively, GeneXus doesn’t commit automatically. Therefore, every time you use them to do an update you must commit the changes.

The Workflow API will skip the restrictions implemented, so, for example, it is possible to assign a task to a user with a role that doesn't have permission to be assigned to this task.

After you have created a new instance of the process with the WorkflowProcessDefinition.CreateInstance() method, you have to start it with the WorkflowProcessInstance.Start() method.

### [See also](#See+also)

[Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240)


|  |
| --- |
| **Pages** |
| [WorkflowAttribute Data Type](https://wiki.genexus.com/commwiki/wiki?10271) | [WorkflowDocumentRepository Data Type](https://wiki.genexus.com/commwiki/wiki?10272) |

---
