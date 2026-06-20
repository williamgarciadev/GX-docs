---
title: "Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 8 or prior)"
source_id: 57694
source_url: https://wiki.genexus.com/commwiki/wiki?57694
genexus_version: "18"
---

# Identity Provider Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 8 or prior)

Below is a guide to configure the GAM Identity Provider for [GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355).

First, define a [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910) on the server for each web application that is going to be a client of the Identity Provider. The credentials of this Application are going to be used for defining the GAM Remote Authentication type in the client's GAM database, as explained in [Client Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37039).

When the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) is used, Applications are added using the Application menu item. Go through "Applications", "Add" button. This calls the Web panel GAMExampleEntryApplication.

In the General tab, enter the name, description, and other basic information of the Application.

In the OAuth Authentication tab, you can enter the Application credentials and other information needed when you are configuring GAM remote.

`[imagen omitida: wiki id 57021]`

By clicking on the "Allow WEB authentication" property, the following fields will become editable.

`[imagen omitida: wiki id 57022]`

In sum, the client application information that must be provided is as follows:

* **Authentication request must include user scopes?.** This property forces the Client Application to request at least one user scope when authenticating.
* **Do not share user IDs.** By setting this property on True, the IDP does not share the user's GUID with the Client Application.
* **Client ID.** Client ID of the Application. It has to be a valid GUID.
* **Client Secret.** Client Secret of the Application. It has to be a valid GUID. By default GAM generates a random string when you save the application, by clicking on "Change" you can change it to your preference.  
  To learn more about how to work through the GAM API with the Client Secret of a GAM Application follow this [SAC](https://www.genexus.com/en/developers/websac?data=53479).

The "**Allow WEB authentication**" check box - under the section **Web (GAMRemote, IDP using SSO)** must be selected to enter the following information (\*):

* **Allowed user scopes.** These scopes are the user data that the Client Application can access.The Client Application may request fewer scopes, but never more than those selected in this configuration. To know more details about them follow this [link](https://wiki.genexus.com/commwiki/wiki?55603).
* **Additional user scopes.** Here you can detail more specifically which user scopes to share with the Client Application. To know more details about them follow this [link](https://wiki.genexus.com/commwiki/wiki?55603).
* **Local Login URL.** URL of the server application login (for example: /TestGAMSSOServer.NetEnvironment/gamremotelogin.aspx). The format is: /<BaseURL>/[<package>.]**gamexampleidplogin**. The **GAMExampleIDPlogin** object is distributed in the [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993).
* **Callback URL.** URL of the client application (for example: http://server:8080/TestGAMRemoteJavaSQLServer). The format is: http://<Server>:<Port>/<BaseURL>. For Java, do not include "/servlet". Since GeneXus 16 Upgrade 7, it is possible to set more than one callback URL. The URLs must be separated by ";". This scenario is useful when many clients have to connect to the same Identity Provider using the same GAM Application. For example, when converting an application and trying to keep both the old and the new version (each one is in a different URL), it is not necessary to define a new GAM Application within the repository in order to specify each Callback URL; it's enough to define both URLs in the Callback URLs property of the same Application.
* **Custom callback URL?.** If selected, GAM will not modify the callback URL. Developers can make their own procedure that handles the response. The custom callback URL field needs to be marked in the GAM Remote authentication type on the client side.
* **State parameter name in response.** The response URL will have the name of the parameter that is placed here. By default, the parameter name is 'state'.
* **Image URL.** URL of the image logo of the client application.
* **Private Encryption Key.** With this private encryption key, the communication between client applications and the server application is encrypted. However, the use of HTTPS is recommended.  
    
  (\*) If "Allow WEB authentication" is not selected, the following error is thrown when the user tries to authenticate to the Identity Provider:  
  Remote authentication is not allowed in this application. Please contact the administrator. (GAM230)

### [See Also](#See+Also)

[Client Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37039)

### [Troubleshooting](#Troubleshooting)

The following error:

Error code 222  
Error message Callback URL doesn't match the one configured in the application (http://<server>/<baseURL>/oauth/gam/callback)

This is due to misconfiguring the callback URL in the Identity Provider. Note that in The Provider, the callback URL is http://<server>/<baseURL>.
