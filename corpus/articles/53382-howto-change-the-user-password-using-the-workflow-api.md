---
title: "HowTo: Change the user password using the Workflow API"
source_id: 53382
source_url: https://wiki.genexus.com/commwiki/wiki?53382
genexus_version: "18"
---

# HowTo: Change the user password using the Workflow API

This article gives details on how to change the user password using the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

You may do this by defining and executing the following code, for example inside a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) user event:

```
&WorkflowServer.Connect(&UserName, &ActualPassword)
&WorkflowOrganizationalModel = &WorkflowServer.GetOrganizationalModel()
&WorkflowUser=&WorkflowOrganizationalModel.GetUserByName(&UserName)
&WorkflowUser.ChangePassword(&ActualPassword,&NewPassword)
commit
return
```

Where the data types variables are the following:

```
&WorkflowServer – WorkflowServer
&WorkflowOrganizationalModel – WorkflowOrganizationalModel
&WorkflowUser – WorkflowUser
&UserName – WorkflowName
&ActualPassword – WorkflowPassword
&NewPassword – WorkflowPassword
```

For further information about the Workflow API, go to [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
