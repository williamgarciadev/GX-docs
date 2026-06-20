---
title: "HowTo: Authenticate to Microsoft Entra ID using GAM"
source_id: 48906
source_url: https://wiki.genexus.com/commwiki/wiki?48906
genexus_version: "18"
---

# HowTo: Authenticate to Microsoft Entra ID using GAM

**Warning**: This sample shows how to use GAM with Azure Active Directory as an external OAuth 2.0 provider. GeneXus does not support the configuration of this external system. Samples, screenshots, parameters, and/or locations may change over time.

This tutorial explains how to authenticate your users with [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id?) using GAM.

Basically, you need to use [OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484) and do some configurations on both sides—the Azure portal and the GAM's backend.

### [Configuration at the Microsoft Entra admin center](#Configuration+at+the+Microsoft+Entra+admin+center)

**1.** Define and register an application. See [this guide](https://learn.microsoft.com/en-us/graph/auth-register-app-v2) from Microsoft.

**2.** Get the app's Application Id, since you'll need it later on:

`[imagen omitida: wiki id 48910]`

**3.** Configure a Redirect URI. Go through the Authentication menu option (Panel on the left) and create a new Web platform. Then Add a Redirect URI of the form:

http://<server>:<port>/<BackendBaseURL>/oauth/gam/callback

`[imagen omitida: wiki id 48911]`

**4.** Go through Certificates and secrets, and create a new secret. You should copy the **value** of the secret, as it will be needed later.

`[imagen omitida: wiki id 48912]`

**5.** In the Permissions tab, verify that you have added the following (User.Read of Microsoft.graph):

`[imagen omitida: wiki id 48913]`

### [Configuration at GAM Backend](#Configuration+at+GAM+Backend)

There are two possible configuration options:

* Use a preset option for Microsoft Entra ID. Follow the article [HowTo: Configure OAuth 2.0 authentication with Microsoft Entra ID](https://wiki.genexus.com/commwiki/wiki?54371) to learn how to use it.
* Follow the steps below to configure it yourself:

**1.** Create a new [OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484) and define the basics: Name, Description, Images (optional), etc.

**2.** In the General tab, define the following:

`[imagen omitida: wiki id 52243]`

The Redirect URL is of the form:

http://<server>:<port>/<BackendBaseURL>/

**Note**: For the configuration of the following tabs, you'll need to check the Endpoints of your application in Microsoft Entra ID.

`[imagen omitida: wiki id 48915]`

**3.** In the Authorization tab:

```
URL: 
https://login.microsoftonline.com/{tenat}/oauth2/v2.0/authorize        
Response type TAG:  response_type      Value: code
Scope TAG:          scope              Value: https://graph.microsoft.com/user.read
State TAG:          state
Include ClientID and RedirectURL
Response:
Access code TAG: code
Error description TAG: error_description
```

In the URL, note the specification of the tenant inside the Microsoft Entra ID.

**4.** In the Token tab:

```
URL: https://login.microsoftonline.com/{tenat}/oauth2/v2.0/token
Header Content type: Content-type      Value: application/x-www-form-urlencoded
Grant type:         grant_type        Value: authorization_code
Include = All
Response:
Access token TAG: access_token
Token type TAG: token_type
Expires in TAG: expires_in
Scope TAG: scope
Error description TAG: error_description
Validate external token = False
```

**5.** In the User Information tab:

```
URL:  https://graph.microsoft.com/v1.0/me
Method: Get
Header Content type: Content-type      Value: application/json;charset=utf-8
Do not include anything
Email TAG: mail
External ID TAG: id
Name TAG:  userPrincipalName
First name TAG: givenName
Last name TAG: surname
Error description TAG: message
```

**Notes:**

* Under "User Information Tab", leave all the fields that are not specified in the configuration above empty.  
  For example: To solve the Error: "Code":284,"Message":"azuread account is not verified, first verify your azuread account".  
  Verify if the field "User Verified Email Tag" is empty.

* The login to Microsoft Entra may be done by entering the user credentials in your application, not in the ME-ID portal.  
  This is done by setting "Redirect to authenticate?" to FALSE.  
  In case of error GAM 280 AADSTS900144: The request body must contain the following parameter: 'scope'. Please refer to SAC 51934.

`[imagen omitida: wiki id 52244]`


|  |
| --- |
| **Backlinks** |
| [Application Registration in Azure Active Directory](https://wiki.genexus.com/commwiki/wiki?42055) | [GAM - OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484) | [GAM - OAuth 2.0 Authentication Type (GeneXus 18 Upgrade 10 or prior)](https://wiki.genexus.com/commwiki/wiki?59831) |
| [GAM - OAuth 2.0 Authentication Type (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60769) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Authenticate to Azure Active Directory using GAM (GeneXus 18 Upgrade 2 or pior)](https://wiki.genexus.com/commwiki/wiki?54393) | [HowTo: Authenticate to Azure Active Directory using GAM (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55881) |
| [HowTo: Authenticate to Office 365 using GAM](https://wiki.genexus.com/commwiki/wiki?39166) | [HowTo: Configure OAuth 2.0 authentication with Azure AD (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55882) | [HowTo: Configure OAuth 2.0 authentication with Microsoft Entra ID](https://wiki.genexus.com/commwiki/wiki?54371) |

---
