---
title: "How to manage user data using the Workflow API"
source_id: 53728
source_url: https://wiki.genexus.com/commwiki/wiki?53728
genexus_version: "18"
---

# How to manage user data using the Workflow API

This article explains how to create, update and delete users with [Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240).

### [How to create a new user](#How+to+create+a+new+user)

To create a new user, you execute the following code:

```
&WorkflowServer.Connect('WFADMINISTRATOR','WFADMINISTRATOR')
&WorkflowOrganizationalModel=&WorkflowServer.GetOrganizationalModel()
&WorkflowOrganizationalModel.AddUser(&WorkflowUserId,&WorkflowUserName,&WorkflowUserEmail,&WorkflowUserPassword)
Commit
```

Where the data type variables are:

```
&WorkflowServer – WorkflowServer
&WorkflowOrganizationalModel – WorkflowOrganizationalModel
&WorkflowUserId – WorkflowUserId
&WorkflowUserName – WorkflowName
&WorkflowUserEmail – WorkflowUserEmail
&WorkflowUserPassword – WorkflowUserPasword
```

### [How to update a user’s information](#How+to+update+a+user%E2%80%99s+information)

To update a user’s information, you execute the following code:

```
&WorkflowServer.Connect('WFADMINISTRATOR','WFADMINISTRATOR')
&WorkflowOrganizationalModel=&WorkflowServer.GetOrganizationalModel()
&workflowUser=&WorkflowOrganizationalModel.GetUserById(&id)
if &workflowUser.Name <> &WorkflowUserName
    &workflowUser.Name = &WorkflowUserName
endif
if &workflowUser.Email <> &WorkflowUserEmail
    &workflowUser.Email = &WorkflowUserEmail
endif
if &workflowUser.isBlocked <> &WorkflowUserBlocked
    if &workflowUserBlocked = True
        &workflowUser.Block()
    else
        &workflowUser.Unblock()
    endif
endif
Commit
```

Where the data type variables are:

```
&WorkflowServer – WorkflowServer
&WorkflowOrganizationalModel – WorkflowOrganizationalModel
&WorkflowUser – WorkflowUser
&Id – WorkflowUserId
&WorkflowUserName – WorkflowName
&WorkflowUserEmail – WorkflowUserEmail
&WorkflowUserBlocked – Boolean
```

### [How to delete a user](#How+to+delete+a+user)

To delete a user, you execute the following code:

```
&WorkflowServer.Connect('WFADMINISTRATOR','WFADMINISTRATOR')
&WorkflowOrganizationalModel=&WorkflowServer.GetOrganizationalModel()
&WorkflowUser=&WorkflowOrganizationalModel.GetUserByName(&WorkflowUserName)
&WorkflowOrganizationalModel.RemoveUser(&WorkflowUser)
Commit
```

Where the data type variables are:

```
&WorkflowServer – WorkflowServer
&WorkflowOrganizationalModel – WorkflowOrganizationalModel
&WorkflowUser – WorkflowUser
&WorkflowUserName – WorkflowName
```
