---
title: "HowTo: Authenticate to Office 365 using GAM"
source_id: 39166
source_url: https://wiki.genexus.com/commwiki/wiki?39166
genexus_version: "18"
---

# HowTo: Authenticate to Office 365 using GAM

**Warning**: This sample shows how to use GAM with Office 365 as an external OAuth 2.0 provider. GeneXus does not support the configuration of this external system. Samples, screenshots, parameters, and/or locations may change over time.

Since the introduction of [OAuth 2.0 Authentication](https://wiki.genexus.com/commwiki/wiki?39484) in [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746), it is possible to authenticate to a broader set of providers. This article explains what to do in GAM backend, to authenticate to Office 365. For more information on how to configure Azure, see [Application Registration in Azure Active Directory](https://wiki.genexus.com/commwiki/wiki?42055).

### [Authentication Type](#Authentication+Type)

Add a new OAuth 2.0 authentication type in the [Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) and set the associated basic parameters:

* Name (you will use this name later in the code to log in)
* Function (Only Authentication is supported)
* Enabled (Yes|No)
* Description: friendly description
* Small image name
* Big image name
* Impersonate

You need to fill in detailed information in the following tabs:

* General: to identify the OAuth 2.0 application.
* Authorization: headers associated with the authorization request and response.
* Token: service URL to handle token information.
* User Information: service URL to handle user data.

Configuration at GAM backend

```
General:
Client ID:     client_id        Value: <clientid>
Client Secret: client_secret    Value: <clientsecret>
Redirect URL:  redirect_uri     Value: https://<server>/webapp

Authorization:
URL: https://login.windows.net/common/oauth2/authorize
Response type TAG:  response_type      Value: code
Scope TAG:          scope              Value: https://graph.microsoft.com/user.read
State TAG:          state
Include ClientID and RedirectURL
Response:
Access code TAG: code
Error description TAG: message

Token:
URL: https://login.windows.net/common/oauth2/token
Header Cotent type: Content-type      Value: application/x-www-form-urlencoded
Grant type:         grant_type        Value: authorization_code
Include = All
Aditional Parameters:  resource=https://graph.microsoft.com
Response:
Access token TAG: access_token
Token type TAG: token_type
Expires in TAG: expires_in
Error description TAG: message
Validate external token = False

User Information:
URL:  https://graph.microsoft.com/v1.0/me
Method: Get
Header Content type: Content-type      Value: application/json;charset=utf-8
Do not include anything
Email TAG: mail
External ID TAG: id
Name TAG:  userPrincipalName
First name TAG: givenName
Last name TAG: surname
Language TAG: preferredLanguage
Error description TAG: message
```

### [How to use it from the code](#How+to+use+it+from+the+code)

Use the LoginOauth20 method from the GAM Repository external object, detailing your OAuth 2.0 configuration name. For example, if you set 'Office365' for the previous configuration:

```
Event 'Login'
  GAMRepository.LoginOauth20(!"Office365") // Authentication Type Name must match the backend definition
EndEvent
```

### [Logout](#Logout)

If you want to force a logout from the Identity provider, you will need to invoke the following URL with your desired callback url:

```
https://login.windows.net/common/oauth2/logout?post_logout_redirect_uri=<my_callback_URL>
```

### [Troubleshooting](#Troubleshooting)

In case of any error, enable the [GAM trace](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?25395,,) to get more information on the error.

### [AADSTS90002](#AADSTS90002)

```
AADSTS90002: Tenant organizations not found. This may happen if there are no active subscriptions for the tenant. Check with your subscription administrator.
```

Check your Azure server-side configuration as it seems the URL configured in GAM is wrong.

### [AADSTS50011](#AADSTS50011)

```
AADSTS50011: The reply url specified in the request does not match the reply urls configured for the application: 'GUID'.
```

Verify your Endpoint URLs are correctly configured and match the location of your GAM application. Go to the Azure portal \ Azure Active Directory application; select your application and check the associated endpoints.

`[imagen omitida: wiki id 42057]`

### [AADSTS70001](#AADSTS70001)

```
AADSTS70001: Application 'GUID' is disabled.
```

Check your Azure application is correctly configured.

### [AADSTS70002](#AADSTS70002)

```
AADSTS70002: Error validating credentials. AADSTS50012: Invalid client secret is provided
```

Review the password settings on the Azure application configuration site and update your GAM configuration.

### [AADSTS50020](#AADSTS50020)

```
Message: AADSTS50020: We are unable to issue tokens from this api version for a Microsoft account. Please contact the application vendor as they need to use version 2.0 of the protocol to support this.
```

Review the following Azure registered Application endpoint and the associated configuration within GAM.

* OAuth 2.0 token endpoint
* OAuth 2.0 authorization endpoint

### [Considerations](#Considerations)

OAuth 2.0 authentication is available in GAM since [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?38845,,).

### [See Also](#See+Also)

[Application Registration in Azure Active Directory](https://wiki.genexus.com/commwiki/wiki?42055)  
[HowTo: Authenticate to Microsoft Entra ID using GAM](https://wiki.genexus.com/commwiki/wiki?48906)  
[GAM - OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484)


|  |
| --- |
| **Backlinks** |
| [Application Registration in Azure Active Directory](https://wiki.genexus.com/commwiki/wiki?42055) | [GAM - OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484) | [GAM - OAuth 2.0 Authentication Type (GeneXus 18 Upgrade 10 or prior)](https://wiki.genexus.com/commwiki/wiki?59831) |
| [GAM - OAuth 2.0 Authentication Type (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60769) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
