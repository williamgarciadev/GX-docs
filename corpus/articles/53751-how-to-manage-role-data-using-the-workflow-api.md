---
title: "How to manage role data using the Workflow API"
source_id: 53751
source_url: https://wiki.genexus.com/commwiki/wiki?53751
genexus_version: "18"
---

# How to manage role data using the Workflow API

This article explains how to create and delete roles using the [Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240).

### [How to create a new role](#How+to+create+a+new+role+)

To create a new role, you execute the following code:

```
&WorkflowServer.Connect('WFADMINISTRATOR','WFADMINISTRATOR')
&WorkflowOrganizationalModel=&WorkflowServer.GetOrganizationalModel()
&WorkflowOrganizationalModel.AddRole(&RoleName)
Commit
```

Where the data type variables are:

```
&WorkflowServer – WorkflowServer
&WorkflowOrganizationalModel – WorkflowOrganizationalModel
&RoleName – WorkflowName
```

### [How to delete a role](#How+to+delete+a+role)

To delete a role, you execute the following code:

```
&WorkflowServer.Connect('WFADMINISTRATOR','WFADMINISTRATOR')
&WorkflowOrganizationalModel=&WorkflowServer.GetOrganizationalModel()
&WorkflowRole=&WorkflowOrganizationalModel.GetRoleByName(&WorkflowRoleName)
&WorkflowOrganizationalModel.RemoveRole(&WorkflowRole)
Commit
```

Where the data type variables are:

```
&WorkflowServer – WorkflowServer
&WorkflowOrganizationalModel – WorkflowOrganizationalModel
&WorkflowRole – WorkflowRole
&WorkflowRoleName – WorkflowName
```
