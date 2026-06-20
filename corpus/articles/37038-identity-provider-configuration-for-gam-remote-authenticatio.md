---
title: "Identity Provider Configuration for GAM Remote Authentication"
source_id: 37038
source_url: https://wiki.genexus.com/commwiki/wiki?37038
genexus_version: "18"
---

# Identity Provider Configuration for GAM Remote Authentication

Below is a guide to configure the GAM Identity Provider for [GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355).

### [Prerequisites](#Prerequisites)

First, define a [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910) on the server for each web application that is going to be a client of the Identity Provider. The credentials of this Application are going to be used for defining the GAM Remote Authentication type in the client's GAM database, as explained in [Client Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37039).

### [Configuration steps](#Configuration+steps)

#### [Adding Applications Using the GAM Backoffice](#Adding+Applications+Using+the+GAM+Backoffice)

When the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) is used, Applications are added using the Application menu item. Go through **Applications** > **Add** button. This calls the Web Panel GAMExampleEntryApplication.

In the **General** tab, enter the name, description, and other basic information of the Application.

In the **OAuth Authentication** tab, you can enter the Application credentials and other information needed when you are configuring GAM remote.

`[imagen omitida: wiki id 60957]`

By clicking on the **Allow OAuth 2.0 (authorization code flow in /oauth/gam)?** property, the following fields will become editable.

`[imagen omitida: wiki id 60956]`

In sum, the client application information that must be provided is as follows:

* **Authentication request must include user scopes?:**This property forces the Client Application to request at least one user scope when authenticating.
* **Do not share user IDs:** By setting this property on True, the IDP does not share the user's GUID with the Client Application.
* **Client ID:** Client ID of the Application. It has to be a valid GUID.
* **Client Secret:** Client Secret of the Application. It has to be a valid GUID. By default GAM generates a random string when you save the application, by clicking on **Change** you can change it to your preference.  
  To learn more about how to work through the GAM API with the Client Secret of a GAM Application, follow this [SAC 53479](https://www.genexus.com/en/developers/websac?data=53479).

The **Allow OAuth 2.0 (authorization code flow in /oauth/gam)?** check box that is under the section **WEB (IDP using SSO, authorization code flow)** must be selected to enter the following information (\*):

* **OAuth 2.0 option:** The possible values are Basic, [PKCE](https://www.oauth.com/oauth2-servers/pkce/), and Basic and PKCE. Setting this option to PKCE or Basic and PKCE allows the current application to function as a GAMRemote PKCE Identity Provider.  
  If this property is set to Basic, the application will act as a standard OAuth 2.0 Identity Provider.  
  If it is set to PKCE, it will only support clients that authenticate using OAuth 2.0 PKCE.  
  Finally, if it is set to Basic and PKCE, the application will operate as both a standard OAuth 2.0 and an OAuth 2.0 PKCE Identity Provider simultaneously.
* **Allowed PKCE Method:**The possible values are PLAIN or S256.
* **Allowed user scopes:**These scopes are the user data that the Client Application can access. The Client Application may request fewer scopes, but never more than those selected in this configuration. To know more details about them, follow this [GAM - OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603).
* **Additional user scopes:**Here you can detail more specifically which user scopes to share with the Client Application. To know more details about them, follow this [GAM - OAuth User Scopes](https://wiki.genexus.com/commwiki/wiki?55603).
* **Image URL:** URL of the image logo of the client application.
* **Local Login URL:** URL of the server application login (for example: /TestGAMSSOServer.NetEnvironment/gamremotelogin.aspx). The format is: /<BaseURL>/[<package>.]**gamexampleidplogin**. The **GAMExampleIDPlogin** object is distributed in the [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993).

  It is possible to configure an authentication type instead of a Login object. This allows the client application that authenticates against this application to be automatically redirected to the GAM IDP or an OAuth 2.0 IDP.

  The authentication types **currently supported** by this configuration are **OAuth 2.0 and GAMRemote**.

  It is possible to configure more than one authentication type in this property by separating them with “;”. For example, using GAM API:

  ```
   &GAMApplication.ClientLocalLoginURL                        = !"auth:oauth20-google;gamremote"
  ```
* **Callback URLs:** URL of the client application (for example: http://server:8080/TestGAMRemoteJavaSQLServer). The format is: http://<Server>:<Port>/<BaseURL>. For Java, do not include **/servlet**. Since GeneXus 16 Upgrade 7, it is possible to set more than one callback URL. The URLs must be separated by ";". This scenario is useful when many clients have to connect to the same Identity Provider using the same GAM Application. For example, when converting an application and trying to keep both the old and the new version (each one is in a different URL), it is not necessary to define a new GAM Application within the repository in order to specify each Callback URL. It's enough to define both URLs in the Callback URLs property of the same Application.
* **Custom callback URL?:**If selected, GAM will not modify the callback URL. You can make your own Procedure that handles the response. The custom callback URL field needs to be marked in the GAM Remote authentication type on the client side.
* **State parameter name in response:** The response URL will have the name of the parameter that is placed here. By default, the parameter name is 'state'.
* **Private Encryption Key:** With this private encryption key, the communication between client applications and the server application is encrypted. However, the use of HTTPS is recommended.
* **Disable Single Logout (SLO)?:**If this property is checked, when the Single Logout is done, this application is not called to notify it that it can kill its token. When this property is set to True (&GAMApplication.ClientSingleLogoutDisableSLO=True) the **Custom Single Logout URLs** property will be ignored.
* **Custom Single Logout URLs:**Allows you to customize the SLO URL of the application, you can configure a list of URLs separated by ";".  
  If this property is empty, and **Custom Callback URL** (&GAMApplication.ClientCallbackURLisCustom = False), the SLO URL is the same as the Callback URL, but the /oauth/gam/signout service is called.  
  If this property is empty and **Custom Callback URL** (&GAMApplication.ClientCallbackURLisCustom = True), the SLO URL is the same as the Callback URL.  
  If you specify a URL at **Custom Single Logout URLs** (&GAMApplication.ClientSingleLogoutCustomURLsSLO) property select one of them, automatically will be selected the URL from which client application logged in.  
    
  The Custom SLO URL specified will receive these parameters:  
    
  **client\_id:** Client ID of the application.  
  **redirect\_uri:** Callback URL (it must match the one configured in the application)  
  **state:** Random string that stores the status before the request, required.  
    
  For example: https://<your\_server>/<virtual\_directory>**/slo?client\_id=**<Client\_ID>**state=**<random\_alphanumeric>**&redirect\_uri=**https://<your\_server>/<virtual\_directory>/callback  
    
  When finished it should redirect to the received redirect\_uri sending the received state.  
    
  For example: https://<your\_server>/<virtual\_directory>**/callback?state=**<random\_alphanumeric>
* **Valid URLs after Single Logout:**This allows you to configure a list of possible URLs to redirect to after the SLO is finished, if none is entered all the URLs received are valid.

(\*) If **Allow OAuth 2.0 (authorization code flow in /oauth/gam)?** is not selected, the following error is thrown when the user tries to authenticate to the Identity Provider:  
Remote authentication is not allowed in this application. Please contact the administrator. (GAM230).

### [See Also](#See+Also)

[Client Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37039)

### [Troubleshooting](#Troubleshooting)

The following error:

```
Error code 222
Error message Callback URL doesn't match the one configured in the application (http://<server>/<baseURL>/oauth/gam/callback)
```

This is due to misconfiguring the callback URL in the Identity Provider. Note that in The Provider, the callback URL is http://<server>/<baseURL>.


|  |
| --- |
| **Backlinks** |
| [Client Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37039) | [Client Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57067) | [GAM - GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355) |
| [GAM - Impersonation](https://wiki.genexus.com/commwiki/wiki?24241) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Get user's additional information from the GAM Identity Provider](https://wiki.genexus.com/commwiki/wiki?37703) |
| [HowTo: Send and receive properties set at the login](https://wiki.genexus.com/commwiki/wiki?44824) | [HowTo: Signout from a SSO applications not using GAM (GeneXus 18 Upgrade 12)](https://wiki.genexus.com/commwiki/wiki?60831) | [HowTo: Single Logout from a SSO applications not using GAM (SLO)](https://wiki.genexus.com/commwiki/wiki?36239) |
| [HowTo: Use GAM as an OAuth 2.0 provider](https://wiki.genexus.com/commwiki/wiki?45493) | [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60954) | [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?57020) | [Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57694) |
| [TimeoutToFinishOAuthAuthenticationUsingIDP property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?58086) |

---
