---
title: "HowTo: Delegate a Workitem using the Workflow API"
source_id: 53549
source_url: https://wiki.genexus.com/commwiki/wiki?53549
genexus_version: "18"
---

# HowTo: Delegate a Workitem using the Workflow API

This article describes how to delegate a workitem using the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350). Take into account that when you delegate a task using the API, constraints are not checked. Therefore, it doesn't matter whether you set the task's properties to Allow delegation, Delegation mode, or Maximum length of delegation.

To do this, execute the following code:

```
&WorkflowOrganizationalModel=&WorkflowServer.GetOrganizationalModel()
&WorkflowUser = &WorkflowOrganizationalModel.GetUserByName(&userName)
&WorkflowWorkitem.Delegate(&WorkflowUser)
commit
```

Where the data types variables are as follows:

```
&WorkflowServer – WorkflowServer
&WorkflowOrganizationalModel – WorkflowOrganizationalModel
&WorkflowUser – WorkflowUser
&userName – WorkflowName
&WorkflowWorkitem – WorkflowWorkitem
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
