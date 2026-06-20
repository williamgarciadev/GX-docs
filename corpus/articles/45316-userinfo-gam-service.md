---
title: "Userinfo GAM Service"
source_id: 45316
source_url: https://wiki.genexus.com/commwiki/wiki?45316
genexus_version: "18"
---

# Userinfo GAM Service

It's a REST service to obtain the user's information.

Through the service /oauth/gam/userinfo it is possible to obtain the user's information.  
Before running the service, authentication is required. To this end, you must obtain an OAuth 2.0 token through the service [access\_token](https://wiki.genexus.com/commwiki/wiki?45320). The service is then invoked through the GET or POST methods.

### [Endpoint](#Endpoint)

$ServerURL/oauth/gam/userinfo

### [Configuration](#Configuration)

For this to work, a certain configuration is needed at the level of the [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910) where the service is configured:

`[imagen omitida: wiki id 51916]`

* &GAMApplication.ClientAllowRemoteAuthentication = True. (Although GAM requests that a ClientCallbackURL and a ClientLocalLoginURL be indicated, they will not be used in this case.)
* &GAMApplication.ClientAllowGetUserRoles = True. (If you want to get the user's roles.)
* &GAMApplication.ClientAllowGetUserAdditionalData = True. (To obtain the [dynamic attributes of the user.](https://wiki.genexus.com/commwiki/wiki?19639,,))

### [GET](#GET)

In this case, the authentication token (&access\_token) goes in the header.

```
&method = !"GET"
&headername = "Authorization"
&headervalue = "OAuth " + &access_token

&getstring = &urlbase + "/oauth/gam/userinfo"

&httpclient.AddHeader(&headername, &headervalue)
&httpclient.AddHeader("GeneXus-Agent","SmartDevice Application")
&httpclient.Execute(&method, &getstring)

&httpstatus = &httpclient.StatusCode
&result = &httpclient.toString()
```

### [POST](#POST)

In this case, the authentication token (&access\_token) goes in the body.

```
&method = !"POST"

&getstring = &urlbase + "/oauth/gam/userinfo"

&httpclient.AddHeader("GeneXus-Agent", "SmartDevice Application")
&httpclient.AddVariable(!"access_token", &access_token)
&httpclient.Execute(&method, &getstring)

&httpstatus = &httpclient.StatusCode
&result = &httpclient.toString()
```

### [Response](#Response)

```
{
    "guid":"139f4332-3f40-47b0-8fb4-ee7b3dbddc4f",
    "username":"admin",
    "email":"admin",
    "verified_email":true,
    "first_name":"Administrator",
    "last_name":"User",
    "external_id":"",
    "birthday":"2000-01-01",
    "gender":"N",
    "url_image":"https://",
    "url_profile":"",
    "phone":"+598",
    "address":".",
    "city":".",
    "state":".",
    "post_code":".",
    "language":"Eng",
    "timezone":".",
    "CustomInfo":"",
    "roles":["is_gam_administrator"]
}
```


|  |
| --- |
| **Backlinks** |
| [GAM - Authentication flow with an external OAuth2.0 provider, using a JavaScript Frontend](https://wiki.genexus.com/commwiki/wiki?52539) | [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Use GAM as an OAuth 2.0 provider](https://wiki.genexus.com/commwiki/wiki?45493) |

---
