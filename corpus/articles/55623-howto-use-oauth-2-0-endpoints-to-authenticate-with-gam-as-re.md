---
title: "HowTo: Use OAuth 2.0 Endpoints to authenticate with GAM as REST IDP Server"
source_id: 55623
source_url: https://wiki.genexus.com/commwiki/wiki?55623
genexus_version: "18"
---

# HowTo: Use OAuth 2.0 Endpoints to authenticate with GAM as REST IDP Server

This article describes the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) Endpoints in order to explain authentication with GAM as IDP using OAuth 2.0 REST services.

Unlike the article [HowTo: Use GAM as an OAuth 2.0 provider](https://wiki.genexus.com/commwiki/wiki?45493) where this concept is applied within GAM itself, this article explains how it can be used by any external client.

OAuth 2.0 REST service flow with GAM Endpoints as IDP (Identity Provider):

`[imagen omitida: wiki id 55624]`

## [Endpoints](#Endpoints)

The possible endpoints to authenticate with GAM as IDP are as follows:

### 1. Access Token 2. User Info 3. Refresh Token

### 1. Access Token

access\_token: Sends the user credentials to get a new Token.

#### [Endpoint](#Endpoint)

http://<domain-url>/<base-url>/oauth/gam/v2.0/access\_token

#### [POST](#POST)

#### [Headers](#Headers)

Content-Type: application/x-www-form-urlencoded. Type of content that will be returned.

#### Body in Postman

|  |  |  |
| --- | --- | --- |
| Tag | Value | Description |
| \*client\_id |  | Application Client ID. |
| \*client\_secret |  | Application Client Secret. |
| \*grant\_type | password | In this case, it must be ‘password’. |
| \*scope | gam\_user\_data+gam\_user\_roles | Scope of the user account you want to access. |
| \*username |  | Username of the user to be authenticated. |
| \*password |  | Password of the user to be authenticated. |
| authentication\_type\_name | local | Authentication type name; by default, it uses the default Authentication Type of the Repository. |
| initial\_properties |  | User custom properties array. |
| repository |  | Only use if the IDP is multitenant. |
| request\_token\_type | OAuth | Determines the token type to return and, based on that, the Security Policy to be applied. By default it is OAuth, and the other possible value is Web. |

additional\_parameters:  Use if you want to get more user information.

Check possible Scopes: [OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603).

#### [Initial Properties Example](#Initial+Properties+Example)

```
 [{"Id":"Company","Value":"GeneXus"},{"Id":"Branch","Value":"Uruguay"}]
```

#### [Postman Example](#Postman+Example)

`[imagen omitida: wiki id 55628]`

#### [Response](#Response)

```
{
    "access_token": "ae47229f-e133-42d1-87e0-c5ac59e51edf!c0f5aadd56fb7e1305e7c7abac8ee497d8d640ab446af07149fba8b2a3cad8321ad3c052dd65a7@SSORT!ae47229f-e133-42d1-87e0-c5ac59e51edf!0c6fe15b76f14f5b8a0805c1b6c20",
    "token_type": "Bearer",
    "expires_in": 0,
    "refresh_token": "",
    "scope": "gam_user_data+gam_user_roles+session_initial_prop",
    "user_guid": "736c85fa-5123-437d-a528-93471d3bae42"
}
```

This response follows the GAMOAuth20AccessToken External Object structure.

**Note**: To receive a refresh token, you must change the default value of the property Maximum OAuth token renewals in GAM Security Policies, and set the time that this Token will take to expire.

### [2. User Info](#2.+User+Info)

userinfo: Send the access\_token obtained in the previous request and get the user info depending on the scopes you have indicated.

#### [Endpoint](#Endpoint)

http://<domain-url>/<base-url>/oauth/gam/v2.0/userinfo

#### [GET](#GET)

#### [Headers](#Headers)

Content-Type: application/x-www-form-urlencoded. Type of content that will be returned.

Authorization: access\_token obtained.

#### [Postman example](#Postman+example)

`[imagen omitida: wiki id 55632]`

#### [Response](#Response)

```
{
    "guid": "492c664b-8831-4efb-8618-0c8e86e75446",
    "username": "admin",
    "email": "admin@example.com",
    "verified_email": true,
    "first_name": "Administrator",
    "last_name": "User",
    "external_id": "",
    "birthday": "2000-01-01",
    "gender": "N",
    "url_image": "https://",
    "url_profile": "",
    "phone": "+598",
    "address": ".",
    "city": ".",
    "state": ".",
    "post_code": ".",
    "language": "Eng",
    "timezone": ".",
    "application_data": "",
    "CustomInfo": "",
    "roles": [
        "is_gam_administrator"
    ]
}
```

This response follows the GAMOAuth20UserInfo External Object structure.

### [3. Refresh Token](#3.+Refresh+Token)

access\_token: In this case, you send a refresh token to get a new Token.

#### [Endpoint](#Endpoint)

http://<domain-url>/<base-url>/oauth/gam/v2.0/access\_token

#### [GET](#GET)

Headers

Content-Type: application/x-www-form-urlencoded. Type of content that will be returned.

|  |  |  |
| --- | --- | --- |
| Tag | Value | Description |
| \*client\_id |  | Application Client ID. |
| \*client\_secret |  | Application Client Secret. |
| \*grant\_type | refresh\_token | In this case, it must be “refresh\_token”. |
| \*refresh\_token |  |  |

Postman Example: `[imagen omitida: wiki id 55633]`

#### [Response](#Response)

```
{
    "access_token": "ae47229f-e133-42d1-87e0-c5ac59e51edf!f5b06a969d6ca0a6824318bad9fddd3d72913c1e9118ff9d34a4d117c2f6caa749586f4fee99f2@SSORT!ae47229f-e133-42d1-87e0-c5ac59e51edf!0c6fe15b76f14f5b8a0805c1b6c20-IDP",
    "token_type": "Bearer",
    "expires_in": 6000,
    "refresh_token": "002iKhdKkZ5Xa1el62k2elnwQ24sg0fxwM8rYZc",
    "scope": "gam_user_data+gam_user_additional_data+gam_session_initial_prop+gam_user_roles",
    "user_guid": "492c664b-8831-4efb-8618-0c8e86e75446"
}
```

### [See Also](#See+Also)

[HowTo: Use GAM as an OAuth 2.0 provider](https://wiki.genexus.com/commwiki/wiki?45493)  
[GAM - OAuth 2.0 Endpoints to use GAM as Web IDP Server](https://wiki.genexus.com/commwiki/wiki?49817)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Use API Key to request services from an application](https://wiki.genexus.com/commwiki/wiki?56104) |

---
