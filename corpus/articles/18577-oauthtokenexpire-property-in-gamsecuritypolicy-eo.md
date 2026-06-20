---
title: "OauthTokenExpire property in GAMSecurityPolicy EO"
source_id: 18577
source_url: https://wiki.genexus.com/commwiki/wiki?18577
genexus_version: "18"
---

# OauthTokenExpire property in GAMSecurityPolicy EO

Configures the time in minutes that the access\_token will remain active.

### [Syntax](#Syntax)

*&GAMSecurityPolicy.**OauthTokenExpire*** *= Number\_Minutes*

**Where:**

*&GAMSecurityPolicy*  Is a variable based on the GAMSecurityPolicy data type.

*Number\_Minutes*  
  Number in minutes that the access\_token will remain active.

### [Description](#Description)

This property allows configuring the time in minutes that the access\_token will remain active.

By default, it is set to 0; this means that the token never expires.

In order to connect to a secure application, the final user will need to know an authorized username / password. These credentials will be used in conjunction with the client\_id downloaded to the device when the application is installed, to establish the first connection to the server application (see [HowTo: Develop Secure REST Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?15918) for details).

When the user tries to connect to the application, a login is presented to him/her. The first time he tries to connect, a POST is done to the server, using username, password, and client\_id. Then, the HTTP Response returns an access\_token which will be used all over the connection from now on.

This access\_token is stored in the device and can either remain unchanged while the user is connected or be reset regularly depending on the value of the **OauthTokenExpire** **property** of the GAMSecurityPolicy [External Object](https://wiki.genexus.com/commwiki/wiki?5669).

The access\_token stores in the device cache, and while it's valid (the user does not log out) the final user will not be presented with the login again.

The local session is destroyed when the user logs out the application, and the local cache of the device is destroyed.

**Note**: When using the GAM Backoffice, this property is shown with the description "Token expiration (minutes)".

### [Samples](#Samples)

The GAMExampleEntrySecurityPolicy [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) is an example where this property is used.

To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMSecurityPolicy.OauthTokenExpire  = &OauthTokenExpire
```

Notes:

1. The criteria of time expiration for Token expiration is different from the web session expiration timeout. The latter is time of inactivity, the former is elapsed time.  
2. **Token expiration (minutes)** property is not considered for auto-registered users.

### [See Also](#See+Also)

[OauthTokenMaximumRenovations property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?19324)  
[Security Session Management in Applications using GAM](https://wiki.genexus.com/commwiki/wiki?16338)


|  |
| --- |
| **Backlinks** |
| [Enable Biometrics property](https://wiki.genexus.com/commwiki/wiki?43466) | [GAM - Auto-register anonymous users - How it works](https://wiki.genexus.com/commwiki/wiki?19909) | [GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) |
| [GAM - Security Policies (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58087) | [GAM architecture for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?14978) | [GetSTSAuthorizationAccessToken method of GAMRepository Object](https://wiki.genexus.com/commwiki/wiki?43218) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) |
| [HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864) | [OAuth Token expire (minutes) GAM Security Policy property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58155) | [OauthTokenMaximumRenovations property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?19324) |
| [Secure Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?16052) | [Security Session Management in Applications using GAM](https://wiki.genexus.com/commwiki/wiki?16338) |

---
