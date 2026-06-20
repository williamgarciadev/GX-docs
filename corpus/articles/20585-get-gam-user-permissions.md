---
title: "Get GAM User Permissions"
source_id: 20585
source_url: https://wiki.genexus.com/commwiki/wiki?20585
genexus_version: "18"
---

# Get GAM User Permissions

There exist three methods in order to get the [Permissions](https://wiki.genexus.com/commwiki/wiki?15912) of a given user, which we detail below.

### [GetPermissions Method](#GetPermissions+Method)

It returns a collection of GAMPermission Object of the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) library, which corresponds to all the permissions which have been granted to the user directly (not through roles). See [Update GAM User Permissions](https://wiki.genexus.com/commwiki/wiki?20583) for more information about adding permissions to a user.

### [Syntax](#Syntax)

&GAMUser.GetPermissions(in:GAMPermissionFilter,out:GAMError Collection): GAMPermission Collection

### [Sample](#Sample)

```
//Set the Filters for the GetPermissions method
&GAMPermissionFilter.ApplicationId = &ApplicationId
&GAMPermissionFilter.AccessType = GAMPermissionAccessType.Convert(&GAMPermissionAccessType) //&GAMPermissionAccessType is character(1). Valid values are: A (Allow),D (Deny), R (Restricted)
&GAMPermissions = &User.GetPermissions(&GAMPermissionFilter,&errors) //&GAMPermissions is GAMPermission Collection, &User is GAMUser 

for &GAMPermission in &GAMPermissions

    &GAMPermissionGUID = &GAMPermission.GUID
    &GAMPermissionName = &GAMPermission.Name
 
endfor
do 'display errors'

sub 'display errors'
for &error in &errors
  msg(&error.Code.ToString() + ' ' + &error.Message)
endfor
endsub
```

**Note**

The valid values for &GAMPermissionFilter.AccessType given to GetPermissions method are: A (Allow), D (Deny), R (Restricted).

### [GetAllPermissions Method](#GetAllPermissions+Method)

It returns a collection of GAMPermission Object, which corresponds to all the permissions associated to the user (through roles or directly to the User), which fulfill the GAMPermissionFilter conditions.

### [Syntax](#Syntax)

&GAMUser.GetAllPermissions(in:GAMPermissionFilter,out:GAMError Collection): GAMPermission Collection

### [Example](#Example)

Similar to the previous example, in this case the only valid values for the GAMPermissionFilter.AccessType are Allow and Deny.

```
//Set the Filters for the GetAllPermissions method
&GAMPermissionFilter.ApplicationId = &ApplicationId
&GAMPermissionFilter.AccessType = GAMPermissionAccessType.Convert(&GAMPermissionAccessType) //Only A (Allow) or D (Deny)
&GAMPermissions = &User.GetAllPermissions(&GAMPermissionFilter,&errors)

for &GAMPermission in &GAMPermissions
   &GAMPermissionGUID = &GAMPermission.GUID
   &GAMPermissionName = &GAMPermission.Name
endfor
do 'display errors'
```

**Note**

The valid values for &GAMPermissionFilter.AccessType given to GetAllPermissions method are: A (Allow), D (Deny)

### [GetUnassigned Permissions Method](#GetUnassigned+Permissions+Method)

It returns a collection of GAMPermission Object, which corresponds to all the permissions which the user has through the associaton to a role only.

### [Syntax](#Syntax)

&GAMUser.GetUnAssignedPermissions(in:GAMPermissionFilter,out:GAMError Collection): GAMPermission Collection

### [Sample](#Sample)

```
//Set the Filters for the GetUnassignedPermissions method

&GAMPermissionFilter.ApplicationId = &ApplicationId
&GAMPermissionFilter.AccessType = GAMPermissionAccessType.Convert(&GAMPermissionAccessType) //Valid values are: A (Allow),D (Deny), R (Restricted)

&GAMPermissions = &User.GetUnassignedPermissions(&GAMPermissionFilter,&errors)

for &GAMPermission in &GAMPermissions
   &GAMPermissionGUID = &GAMPermission.GUID
   &GAMPermissionName = &GAMPermission.Name
endfor
do 'display errors'
```

**Note**

The valid values for &GAMPermissionFilter.AccessType given to GetUnassignedPermissions method are: A (Allow), D (Deny), R (Restricted).


|  |
| --- |
| **Backlinks** |
| [GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912) | [Update GAM User Permissions](https://wiki.genexus.com/commwiki/wiki?20583) |

---
