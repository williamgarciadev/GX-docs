---
title: "HowTo: Use OAuth 2.0 endpoints to authenticate a Mini App from a Super App"
source_id: 56035
source_url: https://wiki.genexus.com/commwiki/wiki?56035
genexus_version: "18"
---

# HowTo: Use OAuth 2.0 endpoints to authenticate a Mini App from a Super App

This article describes the OAuth 2.0 Endpoints needed to authenticate a [Mini App](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,) from a [Super App](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50900,,).

Although the examples shown below use GAM, remember that [another IDP could be used depending on the case](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59284,,).

## [Methods for the user to authorize/deny data to be shared with the Mini App](#Methods+for+the+user+to+authorize%2Fdeny+data+to+be+shared+with+the+Mini+App)

`[imagen omitida: wiki id 56036]`

### [1. Access the Mini App](#1.+Access+the+Mini+App)

When trying to access the Mini App on the server from the device, check if the user already has the approved scopes of the data to be shared with the Mini App.

To do so, the method to use is:

```
&isOK= GAMUser.IsAllowedSharingDataWithOAuthApplication(&ClientID,&GAMErrorCollection)
```

If *&isOK = True* in the diagram, it exits at the bottom of the Rhombus 1.1 and triggers the Authentication Flow in the Mini App from a Super App (Step 5).

If *&isOK = False* in the diagram, it exits from the left corner of Rhombus 1.1 and the list of data to be shared with the Mini App should be displayed (Step 2).

### [2. Display a list of Data to be shared with the Mini App](#2.+Display+a+list+of+Data+to+be+shared+with+the+Mini+App)

```
&GAMApplication = GAMApplication.GetByClientId(&ClientID, &GAMErrorCollection)

//These are the application properties with the required scopes
&GAMApplication.ClientAllowGetUserDataREST
&GAMApplication.ClientAllowGetUserAdditionalDataREST
&GAMApplication.ClientAllowGetUserRolesREST
&GAMApplication.ClientAllowGetSessionInitialPropertiesREST
&GAMApplication.ClientAllowGetSessionApplicationDataREST
&GAMApplication.ClientAllowAdditionalScopeREST
```

You have to build an end user-friendly string.

View all the scopes enabled to share: [GAM - OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603).

### [3. Allow/Deny the Scopes to the Mini App](#3.+Allow%2FDeny+the+Scopes+to+the+Mini+App)

The screen that is displayed to the user must have an "Allow" and "Deny" button; depending on that the following services must be called to the server:

Deny:

```
&isOK= GAMUser.SetDenySharingDataWithOAuthApplication(&ClientID,&GAMErrorCollection)
```

Allow:

```
&isOK= GAMUser.SetAllowSharingDataWithOAuthApplication(&ClientID, &GAMErrorCollection)
```

If the user chooses "Deny" in the diagram, it exits from the left corner of Rhombus 3.1, returns control to the Application, and does not access the Mini App (Step 4).

If the user chooses "Allow" in the diagram, it exits from the bottom corner of Rhombus 3.1 and triggers the Authentication Flow in the Mini App from a Super App (Step 5).

### [4. Deny Scopes](#4.+Deny+Scopes)

If the user decides to Deny the requested scopes, the Authentication Flow ends here.

### [5. Local Access Token](#5.+Local+Access+Token)

If the Authentication Flow has been triggered in a Mini App from the Super App, the JSON of the Access Token must be returned (the same as in Step 5).

## [Authentication flow in a Mini App from a Super App](#Authentication+flow+in+a+Mini+App+from+a+Super+App)

To start this flow, the *GAMRepository.GetMiniAppAccessToken* method is exposed.

```
&GAMOAuth20AccessToken = GAMRepository.GetMiniAppAccessToken(&ClientID, &GAMSession, &GAMErrorCollection)
```

`[imagen omitida: wiki id 56039]`

### [1. Sign-in](#1.+Sign-in)

The Super App generates an access\_code and calls the Mini App's sign-in service.

The endpoint is: https://<miniapp>/virtual\_dir/oauth/gam/signin

#### [**POST**](#POST)

#### [Headers:](#Headers%3A)

Content-Type: application/x-www-form-urlencoded

#### [Parms:](#Parms%3A)

oauth: miniapp  
client\_id: Application's Client ID  
client\_secret: Application's Client Secret  
code: Retrieved from IDP (SuperApp)

**Note**: oauth: miniapp must be the first parameter.

**POSTMAN Example:**

`[imagen omitida: wiki id 56043]`

`[imagen omitida: wiki id 56044]`

#### [Response (Step 4 in the Diagram)](#Response+%28Step+4+in+the+Diagram%29)

```
{
   "access_token":"7032f1fd-e7a9-48bc-b9db-88a35b121b09!3964ab5e6ab7d771c6c5744122eaac8da2363a041fbfa96828441cd4a2b4c19d1319bb0dc775aa",
   "token_type": "Bearer",
   "expires_in": 1800,
   "refresh_token": "",
   "scope": "user_email+user_first_name+user_last_name",
   "user_guid": "139f4332-3f40-47b0-8fb4-ee7b3dbddc4f"
}
```

**Note**: The scopes received are those configured in the Mini App application on the Super App Server; i.e. the scopes specified by the Super App owner.

The following screen shows the Mini App Configuration at the Super App Server.

`[imagen omitida: wiki id 56045]`

When selected, the property *&GAMApplication.ClientDoNotShareUserIDs* **(Do not share user IDs?)** indicates that the user identifiers (UserGUID and UserExternalID) will not be shared with the Mini App. In this case, GAM will generate a unique identifier for each Mini App (this comes in the external\_id).

Also, the property *&GAMApplication.ClientAllowRemoteRESTAuthentication* **(Allow REST v2.0 authentication?)** must be selected to enable the REST OAuth v2.0 services. When enabling this option, you must select the scopes based on the user information you want to share with the Mini App.

To view the scopes that can be shared, follow this link: [GAM - OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603).

### [2. Access Token](#2.+Access+Token)

The Mini App requests an access\_token from the Super App Server using the access\_code received.

The endpoint is: https://<superapp>/<virtual\_dir>/oauth/gam/v2.0/access\_token

**POST**

#### [Headers:](#Headers%3A)

Content-Type: application/x-www-form-urlencoded

#### [Parms:](#Parms%3A)

code: The same code as the First Step  
client\_id: Application's Client ID  
client\_secret: Application's Client Secret  
Grant\_type: authorization\_code

**POSTMAN Example:**

`[imagen omitida: wiki id 56046]`

#### [Response](#Response)

```
{
   "access_token":"ae47229f-e133-42d1-87e0-c5ac59e51edf!65nKKCceSct11IEYKTOLkcdpvtRpm0CS3gV3qeCaigxNIaVf5doQ6y36fmCab2BVkZfq3v9nPizP8o",
   "expires_in": 0,
   "refresh_token": "",
   "scope": "user_email+user_first_name+user_last_name",
   "token_type": "Bearer",
   "user_guid": "139f4332-3f40-47b0-8fb4-ee7b3dbddc4f"
}
```

With the access\_token obtained, the MiniApp asks for the User Information.

### [3. User Information](#3.+User+Information)

The endpoint is: https://<superapp>//virtual\_dir/oauth/gam/v2.0/userinfo

#### [Headers:](#Headers%3A)

Content-Type: application/x-www-form-urlencoded  
Authorization: Access\_Token  
  
**POSTMAN Example:**

`[imagen omitida: wiki id 56047]`

#### [Response](#Response)

```
{
    "guid": "",
    "email": "testuser@genexus.com",
    "verified_email": true,
    "first_name": "test",
    "last_name": "user",
    "external_id": "8dfeee37-4d00-4fad-8fee-26fe71cd8ea7",
    "custominfo": "{\"City\":\"Canelones\",\"Country\":\"Uruguay\"}",
    "attributes": [
        {
            "Id": "EmployeeID",
            "IsMultiValue": false,
            "Value": "123100"
        }
    ]
}
```


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
