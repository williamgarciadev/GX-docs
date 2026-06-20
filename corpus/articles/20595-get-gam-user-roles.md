---
title: "Get GAM User Roles"
source_id: 20595
source_url: https://wiki.genexus.com/commwiki/wiki?20595
genexus_version: "18"
---

# Get GAM User Roles

The GAMUser object of the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) Library provides methods to obtain the user's [Roles](https://wiki.genexus.com/commwiki/wiki?17569).

They are as follows:

* (Boolean) GAMUser.CheckRole(String: RoleName)
* (Boolean) GAMUser.CheckRoleById(Numeric: RoleId)
* (Boolean) GAMUser.CheckRoleByGUID(GUID: RoleGUID)
* (Boolean) GAMUser.CheckRoleByExternalId(String: RoleExternalId)

The following methods of the GAMRepository object are the same as the previous ones:

* (Boolean) GAMRepository.CheckRole(String: RoleName)
* (Boolean) GAMRepository.CheckRoleById(Numeric: RoleId)
* (Boolean) GAMRepository.CheckRoleByGUID(GUID: RoleGUID)
* (Boolean) GAMRepository.CheckRoleByExternalId(String: RoleExternalId)

These methods return true when the role is associated with the user or when the role is a descendant of a role associated with the user.

### [Sample](#Sample)

The following code is present in the Start Event of the GAMMasterpage object:

```
If GAMUser.CheckRoleByExternalId(!"is_gam_administrator")
        Header1.Object= GAMHeader.Create(ContHolder1.Pgmname)
        //OK
    Else
        GAMExampleNotAuthorized.Link()
    Endif
```

### [Other methods available:](#Other+methods+available%3A)

* GetRoles Method

Returns a collection of Roles which have been associated with the User.

#### [Syntax](#Syntax)

GAMUser.GetRoles(out:GAMError Collection): GAMRole Collection

* GetAllRoles Method

Returns a collection of Roles which have been associated with the User and their descendants.

#### [Syntax](#Syntax)

GAMUser.GetRoles(out:GAMError Collection): GAMRole Collection

### [Note](#Note)

These methods do not consider the [Require Access Permissions Application Property](https://wiki.genexus.com/commwiki/wiki?18512). That is, you can manage roles in your application but not permissions because they are independent of each other.

### [See Also](#See+Also)

[HowTo: Get all users which have a given set of Roles](https://wiki.genexus.com/commwiki/wiki?21268)


|  |
| --- |
| **Backlinks** |
| [HowTo: Get all users which have a given set of Roles](https://wiki.genexus.com/commwiki/wiki?21268) | [Restricted access to GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?18495) |

---
