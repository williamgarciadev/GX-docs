---
title: "GAM - OpenID Connect Authentication Type"
source_id: 49183
source_url: https://wiki.genexus.com/commwiki/wiki?49183
genexus_version: "18"
---

# GAM - OpenID Connect Authentication Type

OpenID Connect (OIDC) is an authentication protocol that works with [OAuth 2.0](https://tools.ietf.org/html/rfc6749) by implementing authentication as an extension of the OAuth 2.0 authorization process. To use this extension, the app manager must include the openid scope in the Authorization Request when setting the authentication type. The information about the authentication performed is returned in a JSON Web Token (JWT) called ID Token.

Remember that:

* OAuth 2.0 authentication servers that implement OIDC are called OpenID Providers (OP).
* OAuth 2.0 client applications using OIDC are called Relying Parties (RP).

The current implementation of GAM makes it possible to authenticate an application against OAuth 2.0 identity providers because OIDC works with OAuth 2.0. Also, it allows you to authenticate an application against an OP by adding the above openid scope.

### [Configuration](#Configuration)

Read the document [OAuth 2.0 Authentication Type in GAM](https://wiki.genexus.com/commwiki/wiki?48575,,) about how OAuth 2.0 configuration —which is necessary for OIDC configuration— is divided.  
In addition, you need to install the modules *GeneXusJWT* and *SecurityAPICommons*to use the functionality that allows validating the ID Token in OpenID Connect.

#### [New Authorization Tab section](#New+Authorization+Tab+section+)

`[imagen omitida: wiki id 57653]`

There, the fields indicate the following:

* **Enable OpenID Connect Protocol?**: Enabling this option signals GAM that the OpenID Connect protocol will be used. Therefore, the developer in charge of configuring it doesn't need to add the openid scope, because it is added automatically. Additionally, the *OpenID Connect* section is displayed containing the fields described below.
* **Validate ID Token?**: Enabling this option will instruct GAM to validate the ID Token received (Issuer URL, token signature, claims, among other fields). Two fields required for token validation will also be displayed.
  + **Issuer URL**: The URL of the ID Token issuer must be added.
  + **Path to server certificate filename**: It is necessary to indicate the path to the issuer's certificate associated with the private key used to sign the token.
* **Allow only users with verified email?**: Enabling this option will only allow users with verified email addresses to access the application.

**Discovery URL**: Identity Provider's Well-Known URL.

**Important:**

In case you specify an a Discovery URL itsn't necessary to use a Certificate.

Additionally, if you use a Certificate and also specify an a Discovery URL, the certificate has priority over the Discovery URL, but in case the certificate expires the URL will be used.

### [Samples](#Samples)

[HowTo: Authenticate to Google using OpenID Connect with GAM](https://wiki.genexus.com/commwiki/wiki?55185,,)

[HowTo: Authenticate to Azure AD using OpenID Connect with GAM](https://wiki.genexus.com/commwiki/wiki?55121)

### [Considerations](#Considerations)

The identity provider must have the OAuth 2.0 protocol and also implement OpenID Connect. In addition, it must have a service to obtain the authenticated user's data.

If a custom callback URL is to be configured, a procedure must be created to handle the return from the OP for processing. This case is described in the following section.

#### [Custom Callback URL](#Custom+Callback+URL)

A possible implementation for the case where the authentication type has been configured with a custom callback URL is the creation of a procedure containing the following lines to handle the OP's response:

```
&Response = &HTTPRequest.QueryString
GAMRepository.InputExternalAuthentication(&Response)
```

It is also necessary to create an object of URLRewrite type and place the following line:

callback => NombreProcCallback;

This allows you to define a friendly URL to improve the site's usability and accessibility. Thus, the friendly URL for the callback must match the URL provided (for example, if the callback URL placed in the GAM configuration is: https://www.example.com/dirCallback and the procedure that handles the OP's response is named *CallbackIDPCustom*, in the URLRewrite this would be added: dirCallback => CallbackIDPCustom;).

#### [Use of Event Subscriptions for processing user data](#Use+of+Event+Subscriptions+for+processing+user+data)

The developer may define an Event Subscription that provides full control over the user data that will be recorded in the GAM DB. The following is an example with the event "Repository - External Authentication Response." Previously it was necessary to subscribe to this event in the Event Subscription section of GAM and associate it with the procedure that will handle the query when the event is triggered:

In the Rules section of the procedure:

```
Parm(in:&EventName, in:&JsonIIn the Source section of the procedure:N, out:&JsonOUT);
```

In the Source section of the procedure:

```
/*
El JSON de entrada, &JsonIN, tendrá la siguiente forma:
{"GAMToken":"efe29cd2-d45...",
"AuthenticationTypeId":"Oauth20",
"AutenticationTypeName":"google_oidc",
"MethodName":"gettoken"  or  "getuserinfo"  or  "getrefreshtoken" ,
"String":"{\"access_token\":\"27ef...y2\", 
           \"refresh_token\":\"09e5...u6\", 
           \"token_type\":\"bearer\", 
           \"expires_in\":3600, 
           \"id_token\":\"eyJ...8h\"}
         "}
*/

&GAMExternalAuthenticationResponse.FromJsonString(&JsonIN)

If &GAMExternalAuthenticationResponse.AutenticationTypeName = !"google_oidc"  AND
   &GAMExternalAuthenticationResponse.MethodName = !"getuserinfo"
     &JsonString = &GAMExternalAuthenticationResponse.String
     &JsonString.ReplaceRegEx('\"','"') // User must parse the JSON
     &SDT_IDUruguayUser.FromJson(&JsonString)

     &GAMUser.Load(GAMUser.GetId())
     If &GAMUser.Success()
          &GAMUser.FirstName   = Format("%1 %2",&SDT_GoogleUser.first_name.Trim(), &SDT_GoogleUser.middle_name.Trim() )
          &GAMUser.LastName    = Format("%1 %2",&SDT_GoogleUser.last_name.Trim(), &SDT_GoogleUser.second_surname.Trim() )
          &GAMUser.Save()
          If &GAMUser.Success()
               commit
          Endif
     Endif
Endif
```

When a user is registered using **google\_oidc** authentication, this procedure allows the authenticated user to be registered in the GAM DB by entering both first and last names. You can handle the data as you wish, and store the users authenticated via **google\_oidc** in the way that is most convenient to you.


|  |
| --- |
| **Backlinks** |
| [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) | [GAM - OpenID Connect Authentication Type (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57652) |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Authenticate to Azure AD using OpenID Connect with GAM](https://wiki.genexus.com/commwiki/wiki?55121) |

---
