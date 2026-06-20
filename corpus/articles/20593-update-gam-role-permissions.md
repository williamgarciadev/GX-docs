---
title: "Update GAM Role Permissions"
source_id: 20593
source_url: https://wiki.genexus.com/commwiki/wiki?20593
genexus_version: "18"
---

# Update GAM Role Permissions

You can add [Permissions](https://wiki.genexus.com/commwiki/wiki?15912) to [Roles](https://wiki.genexus.com/commwiki/wiki?17569) using the [Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) (see [HowTo: Add a Permission to a Role using GAM](https://wiki.genexus.com/commwiki/wiki?17963)), or programmatically using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535).

In this article, you see how to do it programmatically.

GAMRole object, which is part of [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) Library, has methods to add, update, and delete Permissions to the Role, which we explain below.

### [AddPermission Method of GAMRole Object](#AddPermission+Method+of+GAMRole+Object)

#### [Syntax](#Syntax)

GAMRole.AddPermission(in:GAMPermission,out:GAMError Collection) : Boolean

#### [Example](#Example)

In this example, you will learn how to create a new Role, and add a Permission to the Role (the permission needs to exist in any Application). See [Update GAM Application Permissions](https://wiki.genexus.com/commwiki/wiki?20590) for more information on how to add Permissions to [applications](https://wiki.genexus.com/commwiki/wiki?15910).

So in this example, assume that the Permission already exists in some Application.

```
&Application.Load(&ApplicationID) //&Application is GAMApplication data type
//First create a new Role (if it doesn´t exist)
&GAMRole = new()
&GAMRole.Name= 'TestRol2'
&GAMRole.Description  = 'TestRol2'
&GAMRole.SecurityPolicyId = &SecurityPolicyId
&GAMRole.Save()
```

```
If &GAMRole.Success()
   &RoleId = &GAMRole.Id
   //&PermissionGUID is the GUID of the Permission I want to add to the Role
   &GAMPermission.ApplicationId = &ApplicationId //&GAMPermission is GAMPermission type.
   &GAMPermission.GUID = &PermissionGUID
   &GAMPermission.Type = GAMPermissionAccessType.Allow //Posible values are Allow, Deny and Restricted
   &isok =  &GAMRole.AddPermission(&GAMPermission,&Errors)
   if &isok
      commit
   else
      For &Error in &Errors
          Msg(Format(!"%1 (GAM%2)", &Error.Message, &Error.Code))
      EndFor
   Endif
Endif
```

### [Note](#Note)

There are other methods in GAMRole object used to update and delete GAM Permissions, like DeletePermission, DeletePermissionById, and UpdatePermission.  
You can edit the GAMRole object in order to see the methods available:

`[imagen omitida: wiki id 20594]`


|  |
| --- |
| **Backlinks** |
| [GAM - Roles](https://wiki.genexus.com/commwiki/wiki?17569) | [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) | [HowTo: Add a Permission to a Role using GAM](https://wiki.genexus.com/commwiki/wiki?17963) |
| [Permission Access Type](https://wiki.genexus.com/commwiki/wiki?20603) | [Update GAM User Permissions](https://wiki.genexus.com/commwiki/wiki?20583) |

---
