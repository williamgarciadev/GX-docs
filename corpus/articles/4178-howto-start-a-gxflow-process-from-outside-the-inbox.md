---
title: "HowTo: Start a GXflow process from outside the inbox"
source_id: 4178
source_url: https://wiki.genexus.com/commwiki/wiki?4178
genexus_version: "18"
---

# HowTo: Start a GXflow process from outside the inbox

In most cases, it is useful to start a process from outside the GXflow inbox. This article shows you the basics for doing it.

**Note**: the following code does not control for errors to avoid complexity.

```
//Connect to workflow and start the process
&WFsession.Connect('<user>', '<password>')
&process = &WFSession.GetProcessDefinitionByName('<the value of the qualified name property of the activity diagram>')
&processInstance = &process.CreateInstance()
&processInstance.Subject = '<set the subject for the inbox if you want>'

//Set your application data
&WFApplicationData = &processInstance.GetApplicationDataByName('<your application data name>')
&WFApplicationData.NumericValue = <the id of whatever you are processing in the workflow process>
&processInstance.Start()

//If you stop here, somebody can go to the inbox and the task will appear there, but if you want to run the first task now, you have to invoke it:
&activity = &process.GetActivityByName('<the name of your first task>')
&workItem = &processInstance.GetWorkitemByActivity(&activity) 
call(<your first activity object> ,&process,&processInstance,&workItem)
```

**Note:** in this case, it is necessary to perform a Commit to actually start the process. Be aware that when using any of the [Workflow APIs](https://wiki.genexus.com/commwiki/wiki?51350) exclusively, GeneXus doesn't commit automatically. So, performing a commit is always required in order for changes to take place. Also, take into consideration the [LUW](https://wiki.genexus.com/commwiki/wiki?2424), when using the Workflow Data Types, to properly manage data.

The variables are defined as follows:

```
&WFSession = WorkflowServer
&Process = WorkflowProcessDefinition
&WFApplicationData = WorkflowApplicationData
&Activity = WorkflowActivity
&processInstance = WorkflowProcessInstance
```

### [See Also](#See+Also)

[HowTo: Start a Process from an External Application](https://wiki.genexus.com/commwiki/wiki?9988)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
