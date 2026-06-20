---
title: "HowTo: Signout from a SSO applications not using GAM (GeneXus 18 Upgrade 12)"
source_id: 60831
source_url: https://wiki.genexus.com/commwiki/wiki?60831
genexus_version: "18"
---

# HowTo: Signout from a SSO applications not using GAM (GeneXus 18 Upgrade 12)

This article is related to [HowTo: Implement SSO for applications that do not use GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?28089,,).

Here you will find the two ways that an application has to do Logout:

1. How to logout from the Client Application.
2. How to do the Logout when it is started from the [Identity Provider](https://wiki.genexus.com/commwiki/wiki?37038) side.

## [1. How to notify the Identity Provider when my application sign out](#1.+How+to+notify+the+Identity+Provider+when+my+application+sign+out)

First of all, make sure you already implemented the [Single Sign On](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?28089,,)

To implement the Single Logout (SLO) your application must be logged in using Single Sign On with GAM Identity Provider.

**After your logout, redirect to:**

The Endpoint is: https://gamidentityprovider.com/<virtual\_dir>**/oauth/gam/signout.**

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

http://gamidentityprovider.com/<virtual\_dir>/**oauth/gam/signout?client\_id**=<client\_id>**&redirect\_uri**=<redirect\_uri>**&token**=<access\_token>**&state**=<random\_alphanumeric>

You must validate that the value of the state is the same as the one sent to the IDP Server.

### [Sample code](#Sample+code)

```
&redirect_uri = !"http://mydomain/myapplication/sampleobjectname.aspx" // URL after single logout
&state = GUID.NewGuid().ToString() // You must save this value.
&WebSession.Set(IdentityProviderParameters.State,&state)
&Token = &WebSession.Get(IdentityProviderParameters.RemoteToken) //Where you stored the provided access_token by the IDP.

&EncodedURL = EncodeUrl.Udp(&redirect_uri) // (1)

&url = format(!"https://gamidentityprovider.com/<virtual_dir>/oauth/gam/signout?client_id=%1&redirect_uri=%2&token=%3&state=%4", 
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

## [2. How to Implement a service for GAM Identity Provider to notify the Sign out](#2.+How+to+Implement+a+service+for+GAM+Identity+Provider+to+notify+the+Sign+out)

It is a service that will call the GAM Identity Provider when one of the applications that logged in SSO now launches a sign out.

You have to implement a service that handle and receive the following parameters: **client\_id, redirect\_uri, token and state**.

**client\_id:** My Client ID Application.  
**redirect\_uri:** The encoded redirection URL to be called by the Identity Provider afterwards single logout.  
**token:** My access\_token to finish.  
**state:** Server state.  
**repository:**Repository GUID when using GAM Multitenant, optional.  
**key:** String with encrypted parameters when your application uses "Private Encryption Key" (&GAMApplication.ClientEncryptionKey) property, optional.

In this service, you will delete your application's WebSession, and redirect to the Identity Provider. 

The Endpoint is: https://gamidentityprovider.com/<virtual\_dir>**/oauth/gam/signout.**

**GET**

**Parms:**

**client\_id:** Application Client ID, required.  
**redirect\_uri:** The same URL value received for the service, required.  
**token:** access\_token. Return the same value received for the service, required.  
**state:** Return the same value received for the service, required.  
**first\_call=0**, required.

You must specify your service URL at **Custom Single Logout URLs** (&GAMApplication.ClientSingleLogoutCustomURLsSLO) property in the Client Application within the Identity Provider's Backoffice.

If this property is empty, by default the SLO URL is the same as the callback URL, but the /oauth/gam/signout service is called.

See more about these properties in [Identity Provider Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37038).

### [Sample code](#Sample+code)

```
/ Rules (Parameters)
Parm(in:&client_id, in:&redirect_uri, in:&token, in:&state, in:&key, in:&repository);

// Validate if the parameters are encrypted
if not &Key.IsEmpty()
    &AppCliEncKey     = GetRemoteKey() // your code here
    &ResponseEnc     = Decrypt64(&Key, &AppCliEncKey)
    &aParametersEnc = &ResponseEnc.SplitRegEx(!"&")
    If &aParametersEnc.Count = 3
        &i = 1
        Do while &i <= &aParametersEnc.Count
            &Text = &aParametersEnc.item(&i)  // simple parsing
            &VarReg   = &Text.SplitRegEx(!"=")
            If &VarReg.Count > 1
                Do Case
                    Case &VarReg.item(1).Trim() = "redirect_uri"
                        &OriginalLogoutURL = &VarReg.item(2).Trim()
                    Case &VarReg.item(1).Trim() = "token"
                        &TokenToFinish = &VarReg.item(2).Trim()
                    Case &VarReg.item(1).Trim() = "state"
                        &GAMTokenState = &VarReg.item(2).Trim()
                EndCase
            Endif
            &i = &i + 1
        EndDo
    endif
Endif                        

If not &State.IsEmpty() 
    If not &Token.isEmpty()
        &WebSession.Destroy()
    Endif
Endif

// IDP server redirection
&GAMIDPURL = !"https://gamidentityprovider.com/<virtual_dir>/oauth/gam/signout"

If not &Key.IsEmpty()
   &GAMIPEncryptionKey = !"1234" //You must use the encryption key stored in the IDP server for your application.
   &Parameters = Format(!"redirect_uri=%1&token=%2&state=%3&first_call=0",
                 &redirect_uri.Trim(),// %1
                 &token.Trim(), // %2
                 &state.Trim()) // %3
   &Key = Encrypt64(&Parameters, &GAMIPEncryptionKey)

   &url = format(!"%1?client_id=%2&Key=%3",
          &GAMIDPURL.Trim(), // %1
          &client_id.Trim(), // %2
          &Key.Trim()) // %3
Else
    &url = format(!"%1?client_id=%2&redirect_uri=%3&token=%4&state=%5&first_call=0",
           &GAMIDPURL.Trim(), // %1
           &client_id.Trim(), // %2
           &redirect_uri.Trim(),// %3
           &token.Trim(), // %4
           &state.Trim()) // %5
Endif

If not &repository.IsEmpty()
   &url += "&repository="+&repository
Endif

link(&url)
```

**Notes:**

* The response is parsed to get parameters.
* The local session is destroyed (your code here).
* The Identity Provider (/oauth/gam/signout) is called using the parameters provided and your credentials.

### [Considerations for the Environment configuration](#Considerations+for+the+Environment+configuration)

#### [**C#**](#C%23)

If the client application is generated with C#, you need to add the following lines to the web.config file under the rules section:

```
<!--GXIGNORE_START-->
<rule name="GXGamCallback" stopProcessing="true">
  <match url="^oauth/gam/signout$" />
  <action type="Rewrite" url="alogoutresponse.aspx" />
</rule>
<!--GXIGNORE_END-->
```

where "logoutresponse" references the GeneXus procedure in charge of the processing.

#### [**Java**](#Java)

If the client application is generated with Java, you need to add the following lines to the web.xml file in the WEB-INF directory of the client web app:

```
<servlet>
  <servlet-name>GAMOAuthCallback</servlet-name>
  <servlet-class>alogoutresponse</servlet-class>                                                                         
</servlet>
<servlet-mapping>
  <servlet-name>GAMOAuthCallback</servlet-name>
  <url-pattern>/oauth/gam/signout</url-pattern>
</servlet-mapping>
```

### [Availability](#Availability)

This behavior is available since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27605,,).

### [See Also](#See+Also)

[Single Sign On in applications using GAM](https://wiki.genexus.com/commwiki/wiki?25385)  
[GAM - GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355)
