---
title: "Permission Access Type"
source_id: 20603
source_url: https://wiki.genexus.com/commwiki/wiki?20603
genexus_version: "18"
---

# Permission Access Type

The Access Type of a permission defines the permission level available: Allow, Restricted, and Deny. It's assigned at different levels:

* Application level.   
  Each of the [GAM Permissions](https://wiki.genexus.com/commwiki/wiki?15912) of the Repository has an Access Type defined at GAM Application level, where a Default Access Type for each permission is defined. See [Update GAM Application Permissions](https://wiki.genexus.com/commwiki/wiki?20590).
* At role level.  
  When GAM Permissions are assigned to [roles](https://wiki.genexus.com/commwiki/wiki?17569), they are defined with an Access Type. See [Update GAM Role Permissions](https://wiki.genexus.com/commwiki/wiki?20593).
* Permissions are granted to the user.  
  When GAM Permissions are assigned to users, they are defined with an Access Type. See [Update GAM User Permissions](https://wiki.genexus.com/commwiki/wiki?20583).

The Access Type of a permission defined at all levels will be used to determine the final permissions for each user.

A permission Access Type at Application level is a *default access type* and is overridden by the Access Type of the same permission in some role the user is associated with. In turn, the Access Type of the permission which is granted directly to the user overrides the Access Type of the permission at Role level.

This document explains the meaning of permission Access Type depending on where the permission is defined.

### [Default Access Type of a permission at Application level](#Default+Access+Type+of+a+permission+at+Application+level)

The Access type of a permission (specified at Application level) is the default value. It means that this is the access type of this permission for any user unless there is an exception that overrides this default.

#### [**Restricted:**](#Restricted%3A)

It implies that only users who have this permission granted with Access Type = Allow or have some role where this permission is allowed, have the corresponding rights. That is to say, the user doesn't have this permission by default.

**Example:**

1.  In the following figure, the permission associated with the selection list for customers is restricted. The list of Application permissions can be seen using the [GAM Backend](https://wiki.genexus.com/commwiki/wiki?15935).

`[imagen omitida: wiki id 17620]`

Figure 1.

2. Since the user has not been granted this permission and has no roles where this permission is "allowed", the execution on the selection list for customers will fail with an Authorization error.

`[imagen omitida: wiki id 17621]`

Figure 2.

#### **Allow:**

This access type enables the permission to everyone by default. Users who have this permission granted with Access Type = restricted or denied, or have some role where the permission is restricted or denied, won't have this permission.

**Example:**

1. In the following figure, the permission associated with the selection list for products (gx0010\_Execute permission) has "Default Access Type"= Allow.

`[imagen omitida: wiki id 17616]`

Figure 3.

2. This means that the user who has "RoleSample" has access rights to execute object gx0010, even though "RoleSample" doesn't have gx0010\_Execute permission. See figure 4 where the user roles are shown, and figure 5 where the permissions of this role are listed.

`[imagen omitida: wiki id 17617]`

Figure 4.

`[imagen omitida: wiki id 17618]`

Figure 5.

As a consequence of what was previously explained, the user has the permission gx0010\_Execute.

### [Access Types of permissions at Role level](#Access+Types+of+permissions+at+Role+level)

#### [**Allow:**](#Allow%3A)

A user who has a role with a permission of Access Type = Allow will have this permission unless he has been given this permission with Access Type = Deny, or has another role where the same permission is denied.

#### [**Deny:**](#Deny%3A)

A user who has a role with a permission of Access Type = Deny won't have this permission, regardless if the permission is allowed at application level (by default) or if he has another role where the permission is allowed. The only way in which the user can be granted this permission is with Access Type = Allow.

#### [**Restricted:**](#Restricted%3A)

If a permission is restricted to a user's role, he doesn't have this permission unless the user is granted this permission with Access Type = Allow or has another role where the same permission is allowed.

### [Access Types of permissions assigned to the user](#Access+Types+of+permissions+assigned+to+the+user)

The permissions assigned to the user have precedence over the permissions assigned through user roles. That means, for example, that if a user has a permission that has been directly assigned to him, which has Access Type = Allow, this permission overrides any permission which has Access Type = Deny at role level for any role the user is associated with.

### [Summary](#Summary)

The following figure provides a graphical explanation of how Role permissions are given to users depending on the Access Type of these permissions. In this case, we are not considering if the user has permissions directly assigned to him.

| Permission  Default Access Type  Application level | Permission  Access Type  Role level | Behavior | Permission  Access Type Role level | Behavior | Permission  Access Type Role level | Behavior |
| --- | --- | --- | --- | --- | --- | --- |
| Allow | Allow (only one role) | Has permission | Allow (at least one role)  &  Restricted (any roles) | Has permission | Deny (at least one role)  &  Restricted or Allow (any roles) | Has No permissions |
|  | Restricted (only one role) | Has No permission |
| Deny (only one role) | Has No permission |  | |
| No roles with this permission | Has permission |  | | | |
| Restricted | Allow (only one role) | Has permission | Allow (at least one role)  &  Restricted (any roles) | Has permission | Deny (at least one role)  &  Restricted or Allow (any roles) | Has No permissions |
|  | Restricted (only one role) | Has No permission |
| Deny (only one role) | Has No permission |  | |
| No roles with this permission | Has No permission |  | | | |


|  |
| --- |
| **Backlinks** |
| [GAM - Grouping of permissions](https://wiki.genexus.com/commwiki/wiki?18536) | [GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912) | [GAM - Permissions Created by the User](https://wiki.genexus.com/commwiki/wiki?29723) |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Add a Permission to a Role using GAM](https://wiki.genexus.com/commwiki/wiki?17963) | [HowTo: Implement GAM permissions in Transaction's Modes](https://wiki.genexus.com/commwiki/wiki?18046) | [HowTo: Manage permissions to execute WW Lists and Panels](https://wiki.genexus.com/commwiki/wiki?18064) |
| [HowTo: Permissions in SD Applications, CRUD Restricted](https://wiki.genexus.com/commwiki/wiki?17935) | [HowTo: Permissions in SD Applications, WW and CRUD Restricted](https://wiki.genexus.com/commwiki/wiki?17943) | [Permissions Over a User Action in SD Objects](https://wiki.genexus.com/commwiki/wiki?18173) | [Update GAM User Permissions](https://wiki.genexus.com/commwiki/wiki?20583) |

---
