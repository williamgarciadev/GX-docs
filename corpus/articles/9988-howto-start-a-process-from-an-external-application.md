---
title: "HowTo: Start a Process from an External Application"
source_id: 9988
source_url: https://wiki.genexus.com/commwiki/wiki?9988
genexus_version: "18"
---

# HowTo: Start a Process from an External Application

Suppose you need to start a process instance every day in the morning, the steps to follow will be the following:

### [Step 1.](#Step+1.)

Create a Genexus Procedure with the [Main program](https://wiki.genexus.com/commwiki/wiki?7407) property in 'Yes', [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) with the 'Command line' value and the following source code:

```
&server.connect('<User_Name>','<User_Password>')
&process = &server.GetProcessDefinitionByName('<process_name>')
&procInstance = &process.CreateInstance()
&procInstance.Subject = '<process_instance_subject>' //optional, by default is the process definition name 
&procInstance.Start()
commit
```

Where the data types variables are the following:

```
&server         - WorkflowServer
&process        - WorkflowProcessDefinition
&procInstance   - WorkflowProcessInstance
```

**Note**: <User\_Name> must be an administrator user.

### [Step 2.](#Step+2.)

Create a *.bat* file with the following source code:

```
cd <path file>
a<procedure_name>.exe
```

For example:

```
cd C:\Models\GXFLOW_X_KB\CSharpModel\Web\bin
a<procedure_name>.exe
```

### [Step 3.](#Step+3.)

Include this *.bat* file into a windows scheduled task.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [HowTo: Start a GXflow process from outside the inbox](https://wiki.genexus.com/commwiki/wiki?4178) |

---
