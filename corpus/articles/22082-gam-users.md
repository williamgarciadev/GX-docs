---
title: "GAM - Users"
source_id: 22082
source_url: https://wiki.genexus.com/commwiki/wiki?22082
genexus_version: "18"
---

# GAM - Users

GAM users are stored in the User table of the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) Database.

The credential information stored in the User table depends on the [Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) used in GAM:

* For [Local Authentication Type](https://wiki.genexus.com/commwiki/wiki?20703), user credentials are stored in the GAM User table. This is the only case in which they are accessible by GAM.
* For [External Authentication Type](https://wiki.genexus.com/commwiki/wiki?21755), [Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208), [Google Authentication Type](https://wiki.genexus.com/commwiki/wiki?29013) or [Facebook Authentication Type](https://wiki.genexus.com/commwiki/wiki?29007), the user credentials belong to the external identity providers.

Depending on the application model design, user information may reside entirely in the GAM User table, or in another table within the application. In that case, you must map the information so that GAM can properly enforce security, even if user data is stored outside the GAM tables.  
See [HowTo: Map Application Users to GAM Users](https://wiki.genexus.com/commwiki/wiki?16552) for details.

### [User identity](#User+identity)

Each user is identified by a GUID in the GAM User Table. Additionally, the combination of "User Namespace (UserNameSpace) \ Authentication Type (UserAuthTypeName) \User Name (UserName)" forms a [Candidate Key](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?2199,,).

When a user is created, they are assigned the [Repository Namespace](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18678,,) of the repository in which they are defined.

Users can also be referenced by other properties such as their name, login, or nickname. For more information, see: [HowTo: Reference GAM users using the GAM API](https://wiki.genexus.com/commwiki/wiki?16534).

### [Adding users](#Adding+users+)

Although the Database may support case sensitivity, GAM does not support case sensitivity for usernames. If you try to insert a user named "John" (capitalized) while another user with the username "john" already exists, an error will be returned: Username already exists. (GAM49).

### [Deleting users](#Deleting+users)

You can logically delete a user using the Delete method:

```
&GAMUser.Load(&GAMGUID)
    if &GAMUser.Success()
        &GAMUser.delete()
    endif
endif
```

To restore (undelete) a user, use the corresponding method:

```
&GAMUser.Load(&GAMGUID)
    if &GAMUser.Success()
        &isOK = &GAMUser.UnDelete(&GAMErrors)
        if &IsOK
          commit
        else
           //Display GAM Errors
       endif
endif
```

Another option is physical deletion. In this case, the user and all related data are permanently removed from the database:

```
&GAMUser.Load(&GAMGUID)
     if &GAMUser.Success()
        &isOK = &GAMUser.PhysicalDelete(&GAMErrors)
           if &isOK
             commit
           else
              //Process GAM Errors
           endif
     endif
```

For more information, see: [How to revoke tokens from external IDPs](https://wiki.genexus.com/commwiki/wiki?51085).

### [GAMUser external object](#GAMUser+external+object)

The GAMUser external object, which is imported when GAM is activated or updated, is used to manage GAM Users in the application.

It is part of the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) and allows handling user properties and performing different operations.

For examples of how to use the GAM API to manage user relations, refer to the following links:

* [Update GAM User Permissions](https://wiki.genexus.com/commwiki/wiki?20583)
* [Update GAM Role Permissions](https://wiki.genexus.com/commwiki/wiki?20593)

See the [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993) distributed, in particular the GAMExampleWWUsers and GAMExampleEntryUser objects to get more examples.

### [User relation to [Roles](https://wiki.genexus.com/commwiki/wiki?17569), [Repository](https://wiki.genexus.com/commwiki/wiki?17568) and [Permissions](https://wiki.genexus.com/commwiki/wiki?15912)](#User+relation+to+com.gxwiki.wiki%3F17569%2CGAM%2B-%2BRoles+Roles%2C+com.gxwiki.wiki%3F17568%2CGAM%2B-%2BRepository+Repository+and+com.gxwiki.wiki%3F15912%2CGAM%2B-%2BPermissions+Permissions)

* A User is a strong entity, uniquely identified by a GUID (used as the Primary Key).  
  Considering that GAM can include more than one repository (see [Multiple Repositories Scenarios](https://wiki.genexus.com/commwiki/wiki?18682)), a user can be enabled in multiple repositories, as long as the user's namespace matches the [Repository Namespace](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18678,,) where they are enabled. See [Users enabled or disabled in the GAM Repository](https://wiki.genexus.com/commwiki/wiki?21042).
* Users are associated with Roles in a Repository (a user can have multiple Roles per Repository), following the [Role Based Access Control (RBAC)](https://wiki.genexus.com/commwiki/wiki?17808) approach.
* Additionally, users can also be directly related to Permissions.

### [User properties](#User+properties)

The User table structure allows storing UserFirstName, UserLastName, UserBirthday, UserGender, UserPhone, etc. If you need to store other information in addition to the information provided by the User table structure, you can extend the User table properties using an OAV-based approach. See [Extensibility of GAM entity properties](https://wiki.genexus.com/commwiki/wiki?19634) and [HowTo: GAM User table extensibility - multivalued attributes](https://wiki.genexus.com/commwiki/wiki?21315).

### [GAM Initialization and admin user](#GAM+Initialization+and+admin+user)

When GAM is activated for the first time ([Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) is set to TRUE), the user "admin" is created for prototyping purposes. You can login using the "admin" user in the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) in order to start working, and then create new users for your application. See [GAM - Getting Started](https://wiki.genexus.com/commwiki/wiki?19946) for more details.

### [See Also](#See+Also)

[GAM Deploy Tool - Import Users](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22017,,)  
[HowTo: Filter data by user using the GAM API](https://wiki.genexus.com/commwiki/wiki?15387)  
[GAM Web Backoffice - Users section](https://wiki.genexus.com/commwiki/wiki?60983)


|  |
| --- |
| **Backlinks** |
| [Checkpermission method of GAMRepository Object](https://wiki.genexus.com/commwiki/wiki?20599) | [GAM - How to revoke tokens from external IDPs](https://wiki.genexus.com/commwiki/wiki?51085) | [GAM - Repository](https://wiki.genexus.com/commwiki/wiki?17568) |
| [GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) | [Category:GAM - Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) | [GAM Web Backoffice - Users section](https://wiki.genexus.com/commwiki/wiki?60983) |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Reference GAM users using the GAM API](https://wiki.genexus.com/commwiki/wiki?16534) |

---
