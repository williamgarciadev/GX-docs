---
title: "Client Configuration for GAM Remote Authentication"
source_id: 37039
source_url: https://wiki.genexus.com/commwiki/wiki?37039
genexus_version: "18"
---

# Client Configuration for GAM Remote Authentication

In this guide, you will find the Client configuration steps for [GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355).

From the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), add the Authentication Type through the [Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) menu item.

Next, add the information as explained below:

`[imagen omitida: wiki id 57049]`

`[imagen omitida: wiki id 60958]`

Picture #1. Defining GAM Remote Authentication Type. [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) GAMExampleEntryAuthenticationType.

* **Client ID.** Client ID of the Application – the same as the one specified in the [Identity Provider](https://wiki.genexus.com/commwiki/wiki?37038).
* **Client Secret.** Client Secret of the Application – the same as the one specified in the Identity Provider.
* **Local Site URL.** URL of the client application – the same as the one specified in the Callback URL in the server.
* **Custom callback URL?.** If checked, GAM doesn't handle the response. The custom callback URL field must be marked in the identity provider.
* **Request these scopes.** These scopes will be the user data requested to the IDP, if more scopes are requested than those shared by the IDP it will not be possible to authenticate.To know more details about them follow this [link](https://wiki.genexus.com/commwiki/wiki?55603).
* **Additional scopes.** Here you can detail more specifically which user scopes to request to the IDP. To know more details about them follow this [link](https://wiki.genexus.com/commwiki/wiki?55603).
* **Enable PKCE?:**This property allows you to specify whether the authentication flow against the Identity Provider will use [PKCE](https://www.oauth.com/oauth2-servers/pkce/) over OAuth 2.0.

  + **Method:**Possible values are PLAIN or S256.
  + **Challenge length:**This property defines the length of the code\_verifier. A longer value increases entropy and security.
* **Enable SLO?:**This property allows you to specify whether you want the GAMRemote client to notify the IDP that it has logged out and also trigger the logout in the Identity Provider when it logs out.
* **Remote Server URL.** URL of the server application (for example: http://server/TestGAMSSOServer.NetEnvironment). The format is: Http://<Server>:<Port>/<BaseURL>. For Java, don't include "/servlet".
* **Private Encryption Key.** This private encryption key is used to encrypt the communication between client applications and the server application. It must be configured with the same value as the one specified for the GAM application defined in the Identity Provider (the server). If they are different, an error "javax.servlet.ServletException: java.lang.InternalError: invalid key" is thrown.
* **Repository GUID.** Connect to this Repository in the Identity Provider.
* **Validate External Token.** Validate the session expiration using the Token Expiration and Token renovations of the Identity Provider. The property is AutovalidateExternalTokenAndRefresh. For example: &AuthenticationTypeGAMRemote.GAMRemote.AutovalidateExternalTokenAndRefresh = TRUE.

### [See Also](#See+Also)

[Identity Provider Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37038)


|  |
| --- |
| **Backlinks** |
| [Client Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57067) | [GAM - GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |
| [HowTo: Send and receive properties set at the login](https://wiki.genexus.com/commwiki/wiki?44824) | [Identity Provider Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37038) | [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60954) | [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57020) |
| [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57694) | [TimeoutToFinishOAuthAuthenticationUsingIDP property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?58086) |

---
