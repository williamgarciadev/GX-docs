---
title: "Update GAM User Permissions"
source_id: 20583
source_url: https://wiki.genexus.com/commwiki/wiki?20583
genexus_version: "18"
---

# Update GAM User Permissions

[Permissions](https://wiki.genexus.com/commwiki/wiki?15912) can be associated to a GAM User through [Roles](https://wiki.genexus.com/commwiki/wiki?17569) or can be added to the user directly. The permissions added directly to the user have precedence over the others. See [Permission Access Type](https://wiki.genexus.com/commwiki/wiki?20603) for details.

In this paper you will see how to add (and delete) a Permission given to a User using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535).

### [AddPermission Method of GAMUser Object](#AddPermission+Method+of+GAMUser+Object)

#### [Syntax](#Syntax)

GAMUser.AddPermission(in:GAMPermission, out:GAMError Collection) : Boolean

#### [Example](#Example)

In this example, add to the user the permission named "webpanel1\_execute" with [Permission Access Type](https://wiki.genexus.com/commwiki/wiki?20603) = Allow.

The Permission to be added to the user needs to exist in any of the [Applications](https://wiki.genexus.com/commwiki/wiki?15910). First, you need to define a GAMApplicationPermission type variable in order to get the GUID of the Permission.  
Afterwards, define a GAMPermission type variable using the GUID obtained and the ApplicationId of the GAM Application.

The AddPermission Method of GAMUser receives the GAMPermission object and returns a collection of GAMError, as shown in the following code:

```
//&PermissionGUID is GAMGUID Data Type.
//&GAMPermission is GAMPermission Type.
```

```
&GAMPermission.GUID = &PermissionGUID
&GAMPermission.ApplicationId = &ApplicationId
&GAMPermission.Type = GAMPermissionAccessType.Allow
   
//&User is GAMUser Type.

&IsOK = &User.AddPermission(&GAMPermission, &Errors)
if &IsOK
  commit
else
  msg(&errors.Item(1).Message)
endif
```

### [DeletePermissionById Method of GAMUser Object](#DeletePermissionById+Method+of+GAMUser+Object)

Given the GAMUser object you can remove a permission by executing the DeletePermissionById GAMUser Method.  
You need to have the GUID of the Permission (as explained in the example above), and a collection of GAMError will be returned.

#### [Syntax](#Syntax)

GAMUser.DeletePermissionById(in:GAMKeyNumLong, in:GAMGUID, out:GAMError Collection) : Boolean

#### [Example](#Example)

```
//&user is GAMUser Type.

&IsOK = &user.DeletePermissionById(&ApplicationId,&PermissionGUID,&errors)
if &IsOK
  msg("Permiso borrado con éxito")
  commit
else
   msg(&errors.Item(1).Message)
endif
```

### [Note](#Note)

* There are other methods, like UpdatePermission and DeletePermission of GAMUser Object, with similar purposes.
* The way to know the list of permissions added directly to the user is by executing the GetPermissions method of GAM User object. See [Get GAM User Permissions](https://wiki.genexus.com/commwiki/wiki?20585) for more information on this topic.

### [See Also](#See+Also)

[Update GAM Application Permissions](https://wiki.genexus.com/commwiki/wiki?20590)  
[Update GAM Role Permissions](https://wiki.genexus.com/commwiki/wiki?20593)


|  |
| --- |
| **Backlinks** |
| [GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912) | [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) | [Get GAM User Permissions](https://wiki.genexus.com/commwiki/wiki?20585) |
| [Permission Access Type](https://wiki.genexus.com/commwiki/wiki?20603) |

---
