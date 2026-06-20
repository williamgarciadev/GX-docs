---
title: "HowTo: Block a user using the Workflow API"
source_id: 53521
source_url: https://wiki.genexus.com/commwiki/wiki?53521
genexus_version: "18"
---

# HowTo: Block a user using the Workflow API

This article shows how to block a user using the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

To do so, execute the following code:

```
&WorkflowOrganizationalModel= &WorkflowServer.GetOrganizationalModel()
&WorkflowUser = &WorkflowOrganizationalModel.GetUserByName(&WorkflowUserName)
&WorkflowUser.Block()
Commit
```

Where the data type variables are as follows:

```
&WorkflowServer – WorkflowServer
&WorkflowOrganizationalModel – &WorkflowOrganizationalModel
&WorkflowUser – &WorkflowUser
&WorkflowUserName – &WorkflowName
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
