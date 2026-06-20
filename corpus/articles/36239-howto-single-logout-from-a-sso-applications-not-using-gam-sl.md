---
title: "HowTo: Single Logout from a SSO applications not using GAM (SLO)"
source_id: 36239
source_url: https://wiki.genexus.com/commwiki/wiki?36239
genexus_version: "18"
---

# HowTo: Single Logout from a SSO applications not using GAM (SLO)

This article is related to [HowTo: Implement SSO for applications that do not use GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?28089,,).

Here you will find the two ways that an application has to do Logout:

1. How to logout from the Client Application.
2. How to do the Logout when it is started from the [Identity Provider](https://wiki.genexus.com/commwiki/wiki?37038) side.

## [1. How to notify the Identity Provider when my application SLO](#1.+How+to+notify+the+Identity+Provider+when+my+application+SLO)

First of all, make sure you already implemented the [Single Sign On](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?28089,,)

To implement the Single Logout (SLO) your application must be logged in using Single Sign On with GAM Identity Provider.

**After your logout, redirect to:**

The Endpoint is: https://<idp\_domain>/<virtual\_dir>**/oauth/gam/signout.**

**GET**

**Parms:**

**client\_id:** Application Client ID, required.  
**redirect\_uri**: The encoded redirection url to be called by the Identity Provider afterwards single logout, required.  
**token:** access\_token. This access\_token it's provided by the Identity Provider when your application Sign In, required.  
**state:** Random string that stores the status before the request, optional.

It's important to check that your redirect\_uri it's included at **Valid URLs after Single Logout** (&GAMApplication.ClientSingleLogoutValidURLsAfterSLO) property in the Client Application within the Identity Provider's Backoffice.

If &GAMApplication.ClientSingleLogoutValidURLsAfterSLO is empty, all URLs will be valid.

See more about these properties in [Identity Provider Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37038).

The URL result will look like follows:

https://<idp\_domain>/<virtual\_dir>/**oauth/gam/signout?client\_id**=<client\_id>**&redirect\_uri**=<redirect\_uri>**&token**=<access\_token>**&state**=<random\_alphanumeric>

You must validate that the value of the state is the same as the one sent to the IDP Server.

### [Sample code](#Sample+code)

```
&redirect_uri = !"http://mydomain/myapplication/sampleobjectname.aspx" // URL after single logout
&state = GUID.NewGuid().ToString() // You must save this value.
&WebSession.Set(IdentityProviderParameters.State,&state)
&Token = &WebSession.Get(IdentityProviderParameters.RemoteToken) //Where you stored the provided access_token by the IDP.

&EncodedURL = EncodeUrl.Udp(&redirect_uri) // (1)

&url = format(!"https://<idp_domain>/<virtual_dir>/oauth/gam/signout?client_id=%1&redirect_uri=%2&token=%3&state=%4", 
       &ClientId.Trim(), // %1
       &EncodedURL.Trim(),// %2 
       &Token.Trim(), // %3
       &state.Trim()) // %4
    
link(&url)
```

The execution of the URL (&url) checks in the GAM Identity Provider if there is a valid session. If so, the session is finished. Afterwards, the URL specified in the redirect\_uri parameter is executed by a GET HTTP.

**Notes:**

(1) - The code associated to the EncodeUrl Procedure is the following:

```
&URLEncoded = urlencode(&UrlToEncode)
```

Make sure to change the [Standard Functions property at Object level](https://wiki.genexus.com/commwiki/wiki?8013) to: allow non-standard functions.

## [2. How to Implement a service for GAM Identity Provider to notify the SLO](#2.+How+to+Implement+a+service+for+GAM+Identity+Provider+to+notify+the+SLO)

It is a service that will call the GAM Identity Provider when one of the applications that logged in SSO now launches a sign out.

You have to implement a service that handle and receive the following parameters: **client\_id, redirect\_uri, token and state**.

**client\_id:** My Client ID Application.  
**redirect\_uri:** The encoded redirection URL to be called by the Identity Provider afterwards single logout.  
**token:** My access\_token to finish.  
**state:** Server state.

In this service, you will delete your application's WebSession, and redirect to the URL specified in the redirect\_uri parameter.  
  
For example, in case you received **redirect\_uri=https://<domain>/<virtual\_dir>/oauth/gam/signout**, the request will the following

**GET**

https://<domain>/<virtual\_dir>/oauth/gam/signout

**Parms:**  
  
**state:** Return the same value received for the service, required.  
  
You must specify your service URL at **Custom Single Logout URLs** (&GAMApplication.ClientSingleLogoutCustomURLsSLO) property in the Client Application within the Identity Provider's Backoffice.

If this property is empty, by default the SLO URL is the same as the callback URL, but the /oauth/gam/signout service is called.

See more about these properties in [Identity Provider Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37038).

### [See Also](#See+Also)

[Single Sign On in applications using GAM](https://wiki.genexus.com/commwiki/wiki?25385)  
[GAM - GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355)


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |
| [HowTo: Signout from a SSO applications not using GAM (GeneXus 18 Upgrade 12)](https://wiki.genexus.com/commwiki/wiki?60831) |

---
