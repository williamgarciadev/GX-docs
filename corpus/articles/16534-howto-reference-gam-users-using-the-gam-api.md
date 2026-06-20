---
title: "HowTo: Reference GAM users using the GAM API"
source_id: 16534
source_url: https://wiki.genexus.com/commwiki/wiki?16534
genexus_version: "18"
---

# HowTo: Reference GAM users using the GAM API

This document explains the best way to identify [GAM Users](https://wiki.genexus.com/commwiki/wiki?22082). The User Identity can be obtained in different ways:

### [1. Get the User GUID.](#1.+Get+the+User+GUID.)

There are different ways to get the User GUID.

The following is a static method. The static methods refer to the currently logged in user:

```
&UserIdentification = GAMUser.GetId()       //&UserIdentification is GAMGUID Data Type
```

Another way is to use the active session:

```
&GAMSession= GAMSession.Get(&GAMErrors)     //&GAMErrors is Collection of GAMError Data Type
&User = &GAMSession.User                    //&User is GAMUser Data Type
&UserIdentification = &User.GetId()         //&UserIdentification is GAMGUID Data Type
```

Very similar would be:

```
&UserIdentification = &GAMSession.User.GUID
```

Information of the user can be obtained from these variables.

There are other ways which can be used to get the User identity

### [2. Get the User nick (the name used to log in).](#2.+Get+the+User+nick+%28the+name+used+to+log+in%29.)

As GAM supports many authentication types, the UserName is not a unique key in GAM Users table. If the application will support only one type of authentication, it can be used.

```
&UserNick = GAMUser.GetName()      //&UserNick is GAMUserIdentification Data Type
```

### [3. Get the User Login string.](#3.+Get+the+User+Login+string.)

UserLogin is a string which contains Namespace\AuthenticationType\UserName, for example: miapp\local\jhon.

UserLogin is a unique key in GAM Users table, because it identifies the user in each Authentication Type.

```
&GAMSession= GAMSession.Get(&GAMErrors)
&User = &GAMSession.User
&Userlogin = &User.GetLogin()     //&Userlogin is GAMUserLogin Data Type
```

### [4. Get the externalId of the user.](#4.+Get+the+externalId+of+the+user.)

GAM Users can be mapped to users in the application database, by the externalId attribute.

When a new user is created using [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), or the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535), you can specify the externalId of the GAM User, which maps to the User Identification in the Users table of the application Database.

```
&GAMUser.externalId = &UserIdentification
```

When you need to do the opposite operation, that means, get the user identification who is logged in, you first need to get the externalId of the user:

```
&UserIdentification = GAMUser.GetExternalId()
```

See [HowTo: Mapping Application Users to GAM Users - Using ExternalID GAMUser property](https://wiki.genexus.com/commwiki/wiki?16565) for an example of use of externalId GAM User attribute.

### [See Also](#See+Also)

[GAM API](https://wiki.genexus.com/commwiki/wiki?16535)


|  |
| --- |
| **Backlinks** |
| [GAM - Auto-register anonymous user - Panel usage example](https://wiki.genexus.com/commwiki/wiki?19911) | [GAM - Repository](https://wiki.genexus.com/commwiki/wiki?17568) | [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Filter data by user using the GAM API](https://wiki.genexus.com/commwiki/wiki?15387) | [HowTo: Map Application Users to GAM - Adding a secondary attribute referencing the GAMUser](https://wiki.genexus.com/commwiki/wiki?19643) | [HowTo: Map Application Users to GAM Users](https://wiki.genexus.com/commwiki/wiki?16552) |
| [HowTo: Map Application Users to GAM Users - Using ExternalID GAMUser property](https://wiki.genexus.com/commwiki/wiki?16565) |

---
