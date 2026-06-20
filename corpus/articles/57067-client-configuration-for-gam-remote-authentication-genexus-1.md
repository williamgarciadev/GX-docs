---
title: "Client Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)"
source_id: 57067
source_url: https://wiki.genexus.com/commwiki/wiki?57067
genexus_version: "18"
---

# Client Configuration for GAM Remote Authentication (GeneXus 18 Upgrade 5 or prior)

In this guide, you will find the Client configuration steps for [GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355).

From the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), add the Authentication Type through the [Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) menu item.

Next, add the information as explained below:

`[imagen omitida: wiki id 51764]`

`[imagen omitida: wiki id 51765]`

Picture #1. Defining GAM Remote Authentication Type. [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) GAMExampleEntryAuthenticationType.

* **Client ID.**                Client ID of the Application  – the same as the one specified in the [Identity Provider](https://wiki.genexus.com/commwiki/wiki?37038).
* **Client Secret.**        Client Secret of the Application – the same as the one specified in the Identity Provider.
* **Local Site URL.**     URL of the client application – the same as the one specified in the Call Back URL in the server.
* **Custom callback URL?.** If checked, GAM doesn't handle the response. The custom callback URL field must be marked in the identity provider.
* **Add gam\_user\_additional\_data scope?**When additional data must be passed (such as [dynamic attributes of GAM User](https://wiki.genexus.com/commwiki/wiki?19634)), you must check this attribute. When this property is set, the "gam\_user\_additional\_data" scope is automatically sent to the server. This corresponds to the property &Application.ClientAllowGetUserAdditionalData that has to be set to TRUE.  
  On the server side, the "Allow Authentication" checkbox under the section Web (Identity Provider, SSO) must be selected.
* **Additional Scope.**The additional scope can be any string. This is to support the [GAM - Events subscription](https://wiki.genexus.com/commwiki/wiki?32698) for Remote Authentication: User\_GetCustomInfo and User\_SaveCustomInfo.  
    
  If no additional scope is added, the following basic information is transferred from the server to the client: Guid, Username, EMail, First\_Name, Last\_name, External\_id, Birthday, Gender, Url\_image, Url\_profile, Phone, Address, City, State, Post\_code, Language, Timezone. To send additional data, check the option "Get user additional data" in the server application.
* **Add gam\_session\_initial\_prop scope?**  
  It is used to ask the Identity Provider to return to the client the initial properties dynamically set at login. The Identity Provider must also be configured to send this information.  
  For more details, see [HowTo: Send and receive properties set at the login](https://wiki.genexus.com/commwiki/wiki?44824).
* **Remote Server URL.** URL of the server application (for example: http://server/TestGAMSSOServer.NetEnvironment). The format is: Http://<Server>:<Port>/<BaseURL>. For Java, don't include "/servlet".
* **Private Encryption Key.** This private encryption key is used to encrypt the communication between client applications and the server application. It must be configured with the same value as the one specified for the GAM application defined in the Identity Provider (the server). If they are different, an error "javax.servlet.ServletException: java.lang.InternalError: invalid key" is thrown.
* **Repository GUID.** Connect to this Repository in the Identity Provider.
* **Validate External Token.**Validate the session expiration using the Token Expiration and Token renovations of the Identity Provider. The property is AutovalidateExternalTokenAndRefresh. For example: &AuthenticationTypeGAMRemote.GAMRemote.AutovalidateExternalTokenAndRefresh = TRUE

### [See Also](#See+Also)

[Identity Provider Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37038)
