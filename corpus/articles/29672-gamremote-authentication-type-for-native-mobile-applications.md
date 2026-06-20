---
title: "GAMRemote Authentication type for Native mobile applications"
source_id: 29672
source_url: https://wiki.genexus.com/commwiki/wiki?29672
genexus_version: "18"
---

# GAMRemote Authentication type for Native mobile applications

This guide details the steps to configure the [GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355) specifically for Native Mobile applications.

### [Prerequisites](#Prerequisites)

Ensure you have completed the configuration steps for both the client and server as described in the [GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355).

After completing the configuration steps, you need to consider the following:

### [How to login](#How+to+login)

The login is called by coding the following in the GAMSDLogin object (the login object in the client):

On GeneXus 15 and later versions

```
Event 'LoginRemote'
    Composite
        &LoginExternalAdditionalParameters = new()
        &LoginExternalAdditionalParameters.AuthenticationTypeName    = !"ip_new" //Use only when there is more than one GAMRemote authentication type 
        GeneXus.SD.Actions.LoginExternal(GAMAuthenticationTypes.GAMRemote, &User, &Password, &LoginExternalAdditionalParameters)
        Return
    EndComposite
Endevent
```

In previous versions the code should be:

```
Event 'LoginRemote'
    Composite
        SDActions.LoginExternal("gamremote","","")
        Return
    EndComposite
Endevent
```

When the user taps on the "LoginRemote" action, he is redirected to the gamremotelogin object (that executes on the server side).

`[imagen omitida: wiki id 29659]`

### [Logout](#Logout)

Logging out from the client does not log out from the server.

### [Availability](#Availability)

Since [GeneXus X Evolution 3 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?29463,,).


|  |
| --- |
| **Backlinks** |
| [GAM - GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [Multi-tenant GAM applications using Single Sign On](https://wiki.genexus.com/commwiki/wiki?30495) |

---
