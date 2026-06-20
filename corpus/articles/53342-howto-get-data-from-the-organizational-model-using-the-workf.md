---
title: "HowTo: Get data from the Organizational Model using the Workflow API"
source_id: 53342
source_url: https://wiki.genexus.com/commwiki/wiki?53342
genexus_version: "18"
---

# HowTo: Get data from the Organizational Model using the Workflow API

This article describes how to get data from the Organizational Model using the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

You can get a list of the organization's users, roles or organizational units and displayed in a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) Grid by defining and executing the following code:

`[imagen omitida: wiki id 53504]`

```
Event Start
     &WorkflowServer.Connect(<UserName>,<Password>)
Endevent

Event Grid.Refresh
    &WorkflowOrganizationalModel = &WorkflowServer.GetOrganizationalModel()
    &WorkflowUsers = &WorkflowOrganizationalModel.ListUsers(&WorkflowFilter)
Endevent

Event GridUsers.Load
        for &Workflowuser in &workflowUsers
            &UserId = &Workflowuser.Id
            &UserName = &Workflowuser.Name
            GridUsers.Load()
        endfor
Endevent
```

Where the data types variables are:

```
&WorkflowServer – WorkflowServer
&WorkflowOrganizationalModel – WorkflowOrganizationalModel
&WorkflowFilter – WorkflowFilter
&WorkflowUsers – WorkflowUser (Collection)
&WorkflowUser – WorkflowUser
&UserId – VarChar(40)
```

You can get a list of roles or organizational units with the following methods:

* &WorkflowOrganizationalModel.ListRoles(&WorkflowFilter)
* &WorkflowOrganizationalModel.ListOrganizationalUnitDefinitions(&WorkflowFilter)

You can also get a specific user or role with the following code:

```
&WorkflowServer.Connect(<UserName>,<Password>)
&WorkflowOrganizationalModel = &WorkflowServer.GetOrganizationalModel()
&Workflowuser = &WorkflowOrganizationalModel.GetUserByName(&UserName)
```

Where the data types variables are:

```
&WorkflowServer – WorkflowServer
&WorkflowOrganizationalModel – WorkflowOrganizationalModel
&WorkflowUser – WorkflowUser
&UserName – Character(25)
```

To get a specific role or organizational unit you can use the following methods:

* &WorkflowOrganizationalModel.GetRoleByName(&RoleName)
* &WorkflowOrganizationalModel. GetOrganizationalUnitByName (&OrganizationalUnitName)

For further information about the Workflow API, go to [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
