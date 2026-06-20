---
title: "HowTo: Assign/unassign a user role using the Workflow API"
source_id: 53383
source_url: https://wiki.genexus.com/commwiki/wiki?53383
genexus_version: "18"
---

# HowTo: Assign/unassign a user role using the Workflow API

This article is useful if you need to assign/unassign a user role using [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

To do this, you can define and execute the following code in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916).

```
Event Start
    &WorkflowServer.Connect(&UserName, &UserPassword)
Endevent

Event 'AssignRole'
    &WorkflowOrganizationalModel = &WorkflowServer.GetOrganizationalModel()
    &WorkflowUser = &WorkflowOrganizationalModel.GetUserByName(&UserName)
    &WorkflowRole = &WorkflowOrganizationalModel.GetRoleByName(&RoleName)
    &WorkflowUser.AssignRole(&WorkflowRole)
    commit
    return
Endevent

Event 'UnassignRole'
    &WorkflowOrganizationalModel = &WorkflowServer.GetOrganizationalModel()
    &WorkflowUser = &WorkflowOrganizationalModel.GetUserByName(&UserName)
    &WorkflowRole = &WorkflowOrganizationalModel.GetRoleByName(&RoleName)
    &WorkflowUser.UnassignRole(&WorkflowRole)
    commit
    return
Endevent
```

Where the data types variables are the following:

```
&WorkflowServer – WorkflowServer
&WorkflowOrganizationalModel – WorkflowOrganizationalModel
&WorkflowUser – WorkflowUser
&WorkflowRole – WorkflowRole
&UserName – Character(100)
&UserPassword – Character(30)
&RoleName – Character(100)
```

For further information about the Workflow API, go to [API](https://wiki.genexus.com/commwiki/wiki?51350).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
