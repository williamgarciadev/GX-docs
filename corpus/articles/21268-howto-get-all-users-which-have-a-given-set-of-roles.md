---
title: "HowTo: Get all users which have a given set of Roles"
source_id: 21268
source_url: https://wiki.genexus.com/commwiki/wiki?21268
genexus_version: "18"
---

# HowTo: Get all users which have a given set of Roles

Given a set of [Roles](https://wiki.genexus.com/commwiki/wiki?17569), you can get all the users which have those roles, by using the GetUsersOrderBy method of the GAMRepository object which corresponds to the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535).

The GetUsersOrderBy method receives a parameter based on GAMUserFilter data type where you can specify the collection of roles (or just one role) that will be used to filter the GAM users returned.

`[imagen omitida: wiki id 45840]`

### [Samples](#Samples)

Define a variable *&GAMUserFilter* based on GAMUserFilter data type.

Add the roles to the Roles property of GAMUserFilter variable.

```
&GAMUserFilter.Roles.Add(&ID)//&ID is GAMKeyNumLong data type, and corresponds to the Id of the Role.
&GAMUserFilter.Roles.Add(&ID2)
&GAMUserFilter.SearchRolesInherited = TRUE // If you want to filter users who have this role inherited from another role.

For &GAMUser in GAMRepository.GetUsersOrderBy(&GAMUserFilter, GAMUserListOrder.UserName_Asc, &Errors) 
//&Erros is collection of GAMError
  &UserNAme = &GAMuser.Name
endfor
```

Note that you can also filter the users by just one role using the following code:

```
&GAMUserFilter.RoleId = &FilRol
&Users= GAMRepository.GetUsersOrderBy(&GAMUserFilter, GAMUserListOrder.None, &Errors)
```

Or get the users which have no roles:

```
&GAMUserFilter.WithoutRoles = true 
&Users= GAMRepository.GetUsersOrderBy(&GAMUserFilter, GAMUserListOrder.None, &Errors)
```

Additionally, you can combine the search filters and get

* Users with a role, and users with no roles.
* Users with a collection of roles and users with no roles.

Take a look at the GAMExampleWWUsers [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) object, which shows an example of how to use this API.

### [See Also](#See+Also)

[Get GAM User Roles](https://wiki.genexus.com/commwiki/wiki?20595)


|  |
| --- |
| **Backlinks** |
| [Get GAM User Roles](https://wiki.genexus.com/commwiki/wiki?20595) |

---
