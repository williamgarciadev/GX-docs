---
title: "OAuth mobile service"
source_id: 45320
source_url: https://wiki.genexus.com/commwiki/wiki?45320
genexus_version: "18"
---

# OAuth mobile service

It's a REST service to obtain an OAuth 2.0 authorization token.

Endpoints:

* [1. Access Token](https://wiki.genexus.com/commwiki/wiki?45320)
* [2. Refresh Token](https://wiki.genexus.com/commwiki/wiki?45320)

## [1. Access Token](#1.+Access+Token)

The endpoint is: https://<domain>/<virtual\_directory>**/oauth/access\_token**

### [When using One-Factor Authentication](#When+using+One-Factor+Authentication)

#### [Endpoint](#Endpoint)

**POST**

https://<domain>/<virtual\_directory>**/oauth/access\_token**

#### [**Body:**](#Body%3A)

**client\_id:** Client ID of the application.  
**grant\_type:** Authentication type name.  
**scope:** Scope of the user account you wish to access. Check possible Scopes: [OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603)  
**username:** Username of the account you wish to access.  
**password:** Password of the account you wish to access.

#### [**Sample:**](#Sample%3A)

```
&addstring = "client_id=be47d883307446b4b93fea47f9264f88&grant_type=GAMLocal&scope=gam_user_data&username=test&password=test"

&getstring = &urlbase + "/oauth/access_token"  

&httpclient.AddHeader("Content-Type", "application/x-www-form-urlencoded")
&httpclient.AddString(&addstring)
&httpclient.Execute("POST", &getstring)

&httpstatus = &httpclient.StatusCode // &httpstatus is defined as a Numeric(X.0) variable where 4<X<=9 
&result = &httpclient.ToString() //&result is defined as a LongVarChar variable
```

#### [Response](#Response)

```
{    
     "access_token": "ae47229f-e133-42d1-87e0-c5ac59e51edf!a90817ee94932e905b6fada72bf83dbef4605e2bacbe850f6a684bb3a7b072a6860b2ee76d20d6",     
     "token_type": "Bearer",     
     "expires_in": 180,     
     "refresh_token": "001mebXeCSJY0Pb9nMsBoVIYAvbwAhbHw5FqK1e",     
     "scope": "FullControl+gam_user_info",     
     "user_guid": "eeb8bc39-b7dc-4169-8eb7-ffee95386876" 
}
```

### [When using Two-Factor Authentication](#When+using+Two-Factor+Authentication)

#### [Endpoint](#Endpoint)

**POST**

https://<domain>/<virtual\_directory>**/oauth/access\_token**

**First step**

**client\_id:** Client ID of the application.  
**grant\_type:** Authentication type name.  
**scope:** Scope of the user account you wish to access. Check possible Scopes: [OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603)  
**username:** Username of the account you wish to access.  
**password:** Password of the account you wish to access.  
**additional\_Parameters:** Both OTPStep and UseTwoFactorAuthentication are necessary.

#### [**Sample:**](#Sample%3A)

```
&addstring = 'client_id=be47d883307446b4b93fea47f9264f88&grant_type=GAMLocal&scope=gam_user_data&username=test&password=test&additional_parameters="AuthenticationTypeName":"Local","OTPStep":"1","Repository":"","UseTwoFactorAuthentication":"false","Properties":[{}]}'

&getstring = &urlbase + "/oauth/access_token"
&httpclient.AddHeader("Content-Type", "application/x-www-form-urlencoded")
&httpclient.AddString(&addstring)
&httpclient.Execute("POST", &getstring)

&httpstatus = &httpclient.StatusCode //&httpstatus is defined as a Numeric(X.0) variable where 4<X<=9
&result = &httpclient.ToString() //&result is defined as a LongVarChar variable
```

**First step response**

The first step returns status code 202 and error 410:

```
{
   "error": {
       "code": "410",
       "message": "To enter app, the second authentication factor must be validated."
    }
}
```

**Second Step**

**client\_id:** Client ID of the application.  
**grant\_type:** Authentication type name.  
**scope:** Scope of the user account you wish to access. Check possible Scopes: [OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603)  
**username:** Username of the account you wish to access.  
**password=**OTP\_Value.  
**additional\_Parameters:** Both OTPStep and UseTwoFactorAuthentication are necessary.

#### [**Sample**:](#Sample%3A)

```
&addstring = 'client_id=be47d883307446b4b93fea47f9264f88&grant_type=GAMLocal&scope=gam_user_data&username=test&password=OTP_Value&additional_parameters="AuthenticationTypeName":"Local","OTPStep":"2","Repository":"","UseTwoFactorAuthentication":"true","Properties":[{}]}'

&getstring = &urlbase + "/oauth/access_token"
&httpclient.AddHeader("Content-Type", "application/x-www-form-urlencoded")
&httpclient.AddString(&addstring)
&httpclient.Execute("POST", &getstring)

&httpstatus = &httpclient.StatusCode //&httpstatus is defined as a Numeric(X.0) variable where 4<X<=9
&result = &httpclient.ToString() //&result is defined as a LongVarChar variable
```

**Second Step response**

```
{
    "access_token": "72fef4c4-bb13-418b-9eee-92cbc18ed846!9153eaf0277241ef38de08ea5a7adf47d08ed29144e90c2ab46da38bb02a441b21273ee3ac56e4",
    "token_type": "Bearer"
    "expires_in": 0,
    "refresh_token": "",
    "scope": "FullControl",
    "user_guid": "63d9f144-f4e1-4f9e-a49e-ba0a12892544"
}
```

### [When using a One-Time Password](#When+using+a+One-Time+Password)

#### [Endpoint](#Endpoint)

**POST**

http://<domain>/<virtual\_directory>**/oauth/access\_token**

**First Step**

#### [**Body:**](#Body%3A)

**client\_id:** Client ID of the application.  
**grant\_type:** Authentication type name.  
**scope:** Scope of the user account you wish to access. Check possible Scopes: [OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603)  
**username:** Username of the account you wish to access.  
**password:** Password of the account you wish to access.

#### [**Sample:**](#Sample%3A)

```
&addstring = 'client_id=be47d883307446b4b93fea47f9264f88&grant_type=GAMLocal&scope=gam_user_data&username=test&password=test&additional_parameters="AuthenticationTypeName":"Local","Repository":"","Properties":[{}]}'

&getstring = &urlbase + "/oauth/access_token"
&httpclient.AddHeader("Content-Type", "application/x-www-form-urlencoded")
&httpclient.AddString(&addstring)
&httpclient.Execute("POST", &getstring)

&httpstatus = &httpclient.StatusCode //&httpstatus is defined as a Numeric(X.0) variable where 4<X<=9
&result = &httpclient.ToString() //&result is defined as a LongVarChar variable
```

**First step response**

#### [The first step returns status code 202 and error 400](#The+first+step+returns+status+code+202+and+error+400)

```
{
   "error": {
       "code": "400",
       "message": "An email was sent with your access code"
    }
}
```

#### [**Second step**](#Second+step)

**client\_id:** Client ID of the application.  
**grant\_type:** Authentication type name.  
**scope:** Scope of the user account you wish to access. Check possible Scopes: [OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603)  
**username:** Username of the account you wish to access.  
**password=**OTP\_Value.

#### [Sample](#Sample)

```
&addstring = 'client_id=be47d883307446b4b93fea47f9264f88&grant_type=GAMLocal&scope=gam_user_data&username=test&password=OTP_Value&additional_parameters="AuthenticationTypeName":"Local","Repository":"","Properties":[{}]}'

&getstring = &urlbase + "/oauth/access_token"
&httpclient.AddHeader("Content-Type", "application/x-www-form-urlencoded")
&httpclient.AddString(&addstring)
&httpclient.Execute("POST", &getstring)

&httpstatus = &httpclient.StatusCode //&httpstatus is defined as a Numeric(X.0) variable where 4<X<=9
&result = &httpclient.ToString() //&result is a variable based on the LongVarchar data type.
```

Second Step response

```
{
    "access_token": "72fef4c4-bb13-418b-9eee-92cbc18ed846!9153eaf0277241ef38de08ea5a7adf47d08ed29144e90c2ab46da38bb02a441b21273ee3ac56e4",
    "token_type": "Bearer"
    "expires_in": 0,
    "refresh_token": "",
    "scope": "FullControl",
    "user_guid": "63d9f144-f4e1-4f9e-a49e-ba0a12892544"
}
```

## [2. Refresh Token](#2.+Refresh+Token)

The endpoint is: https://<domain>/<virtual\_directory>**/oauth/access\_token  
  
POST**  
**Headers:**

**Content-Type:**Type of the content that will be returned. Use application/x-www-form-urlencoded

**Body:**

**client\_id:** Client ID of the application, required.  
**client\_secret:** Client Secret of the application, required.  
**grant\_type:** must be "refresh\_token.", required.  
**refresh\_token:** refresh\_token received when requesting the access\_token obtained in Step 2, required.

**POSTMAN Example:**

`[imagen omitida: wiki id 51041]`

`[imagen omitida: wiki id 51042]`

**Response:**

In response, you will receive a JSON with the following format:

```
{
    "access_token": "85a3006c-0606-41d2-980e-223f88463ec2!b1b3e778247c870560d49d17ffd514a2a8467747208b1cf4a641780a267466bc65fba8034c9bbc",
    "token_type": "Bearer",
    "expires_in": 180,
    "refresh_token": "002b9ec850f78b845d883779fa52c91a01",
    "scope": "gam_user_data",
    "user_guid": "139f4332-3f40-47b0-8fb4-ee7b3dbddc4f"
}
```

**When to call the Refresh Token**

When a Rest service is called and the access token has expired, 401 and Error 103 are returned. If this happens and there is a [Refresh Token](https://wiki.genexus.com/commwiki/wiki?45320) saved, it can be used as detailed above; otherwise, a new [Access Token](https://wiki.genexus.com/commwiki/wiki?45320) must be requested.

**POSTMAN Example:**

`[imagen omitida: wiki id 50293]`

**Response:**

In response, you will receive a JSON with the following format:

```
{
    "error": {
        "code": "103",
        "message": "Token expired, log in again."
    }
}
```


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864) | [HowTo: Develop Secure REST Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?15918) |
| [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) | [HowTo: Use Postman to access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?50055) | [OAuth mobile service](https://wiki.genexus.com/commwiki/wiki?45320) |
| [Userinfo GAM Service](https://wiki.genexus.com/commwiki/wiki?45316) |

---
