---
title: "Security Session Management in Applications using GAM"
source_id: 16338
source_url: https://wiki.genexus.com/commwiki/wiki?16338
genexus_version: "18"
---

# Security Session Management in Applications using GAM

The purpose of this document is to briefly explain the main concepts around session management used by this kind of application.

There are two types of "sessions" used for solving security mechanisms, depending on the type of application (referring to applications using GAM):

### [Web Sessions](#Web+Sessions)

In Web applications, "web sessions" are used to store all the information needed to solve authentication problems (remain authenticated as long as the session does not expire).

Read about how to change the Web Session timeout at [WebSessionTimeOut property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?58396).

### [Local Session for Native Mobile](#Local+Session+for+Native+Mobile)

In Native Mobile applications, there is a "local session" stored in the device (the client tier) with the access\_token that enables communication with [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) and requires authentication (see [Secure Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?16052) for more information).  
Unlike web applications, where authentication is checked via web sessions only, native mobile applications cache a "local session" that stores the access\_token which makes communication possible between the application installed on the device and the REST web services residing on the server. In this case, the authorization mechanism is based on [OAuth](http://oauth.net/).

#### [Behavior of a "local session"](#Behavior+of+a+%22local+session%22)

To connect to a secure Native Mobile application, the end user will need an authorized username/password. These credentials will be used together with the [Client Id and Client Secret information](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?21454,,) downloaded to the device when the application is installed, to establish the first connection to the server application.

When the user tries to connect to the application, a login prompt is displayed. The first time the user tries to connect, a POST is made to the server using their username, password, client\_id, and client\_secret, and the HTTP Response returns an access\_token which will be used during the connection.

This access\_token is stored in the device and can either remain unchanged while the user is connected or be reset regularly depending on the value of the [OauthTokenExpire property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?18577).  
The access\_token is stored in the device cache, and while it's valid (the user does not log out) the end user will not be prompted to log in again.

The local session is deleted when the user logs out from the application.

### [**Notes:**](#Notes%3A)

1. The time expiration criteria for [OAuth Token Expire](https://wiki.genexus.com/commwiki/wiki?18577) is different from the [web session expiration timeout](https://wiki.genexus.com/commwiki/wiki?58396). They are related to elapsed time and idle time, respectively.

2. Remember that all the Security Policies and Repository configuration can be done through the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535).  
  
**Sample**

The following code creates a Security Policy and sets its SessionTimeout and OAuth Token Expire.

```
&GAMSecurityPolicy.Id = &Id  //&GAMSecurityPolicy is GAMSecurityPolicy Type
&GAMSecurityPolicy.Name     = "TESTSecurityPolicy"
&GAMSecurityPolicy.WebSessionTimeOut   = 10 
&GAMSecurityPolicy.OauthTokenExpire  = 15
&GAMSecurityPolicy.Save()
If &GAMSecurityPolicy.Success()
  commit
Else
  &GAMErrors = &GAMSecurityPolicy.GetErrors() //&GAMErrors is GAMError collection type
  For &GAMError in &GAMErrors 
   Msg(Format("%1 (GAM%2)", &GAMError.Message, &GAMError.Code))
  EndFor
Endif
```

### [See Also](#See+Also)

[Secure Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?16052)  
[Anonymous Sessions in GAM - Web Applications](https://wiki.genexus.com/commwiki/wiki?16414)


|  |
| --- |
| **Backlinks** |
| [GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) | [GAM - Security Policies (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58087) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |
| [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [HowTo: Have an SSO behavior by using SAML Authentication](https://wiki.genexus.com/commwiki/wiki?44887) |
| [OAuth Token expire (minutes) GAM Security Policy property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58155) | [OauthTokenExpire property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?18577) | [WebSessionTimeOut property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?58396) |

---
