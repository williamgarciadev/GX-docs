---
title: "HowTo: Configuring SAML 2.0 GAM Authentication type using Agesic"
source_id: 41266
source_url: https://wiki.genexus.com/commwiki/wiki?41266
genexus_version: "18"
---

# HowTo: Configuring SAML 2.0 GAM Authentication type using Agesic

**Warning**: This sample shows how to configure the SAML 2.0 GAM Authentication type using Agesic. GeneXus does not support the configuration of these external systems. Samples, screenshots, parameters, and/or locations may change over time.

This document explains the steps to be followed in order to configure [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) to authenticate using [SAML 2.0 Authentication type](https://wiki.genexus.com/commwiki/wiki?41212) using [Agesic](https://www.agesic.gub.uy/).

As indicated in [Agesic: Integración con el servicio de Autenticación](https://centroderecursos.agesic.gub.uy/web/seguridad/wiki/-/wiki/Main/Integraci%C3%B3n+con+servicio+de+autenticaci%C3%B3n), in section "Solicitud de alta en el servicio", you should send an email requesting a form to complete all data necessary to generate the partnership between the Service Provider (your application) and the Identity Provider (Agesic in this specific case).

In the second section of the form that you receive from Agesic ("Información técnica del solicitante" section), you are required to complete, among other fields, the following information:

* **Entity ID**: it is the Service Provider id that must be used to complete the field Service Provider Entity ID in the SAML 2.0 Authentication type Login General tab configuration.
* **Assertion Consumer Service Location**: it is the URL that will receive the SAML responses from the Identity Provider  
    
  Java apps:  
    
  If the application is generated using Java,

Note: The format of the URL must be https://<domain>/<url\_base>/saml/gam/signin

(e.g.:https://testgamagesic.com:8080/gamlogin**/saml/gam/signin**)  
  
.Net apps:

If the application is generated using .Net,

Note: The format of the URL must be https://<domain>/<url\_base>/Saml2/Acs

e.g.: https://gamtestnet.com/kbaux.NetEnvironment/Saml2/Acs

* **Single Logout Location**: it is the URL that will receive the SAML requests from the Identity Provider to execute a local logout (e.g.:https://testgamagesic.com:8080/gamlogin**/saml/gam/signout**)

Note: Important: The format of the URL must be https://<domain>/<url\_base>/saml/gam/signout

In sum, in GAM, you will have configured the following fields:

`[imagen omitida: wiki id 52214]`

**Force Authentication** = TRUE means that every time that a login is needed in a different Service Provider, the IdP will request the user to enter credentials again (SSO will not be used). It's supported by Agesic only. For further details on this item, take a look at the [Agesic](https://centroderecursos.agesic.gub.uy/web/seguridad/wiki/-/wiki/Main/Integraci%C3%B3n+con+servicio+de+autenticaci%C3%B3n) documentation, and search for ***ForceAuth***.

**Authentication Context**: for Agesic, use "Both". For further details on this item, take a look at the [Agesic](https://centroderecursos.agesic.gub.uy/web/seguridad/wiki/-/wiki/Main/Integraci%C3%B3n+con+servicio+de+autenticaci%C3%B3n) documentation, and search for ***RequestedAuthnContext***.

**Local Site URL**:configure the URL used to register your application (Service Provider) in Agesic (e.g.: http://testgamagesic.com:8080/gamlogin).

In the third section of the form provided by Agesic you will find the information necessary to configure the **SAML Endpoint Location** and the **Single Logout Endpoint** in SAML 2.0 Authentication type General tab.

* **SAML Endpoint Location in GAM Backend**

For Java apps, copy the contents of Http-redirect endpoint to that field. For .Net apps, copy the contents of Http-Post endpoint.

* **Single Logout Endpoint in GAM Backend**

Copy the contents of Single logout endpoint to that field.

### [Important Note](#Important+Note)

For Agesic, you have to configure the following, because the HTTP requests must be done using the GET HTTP method. As this property (isRedirectBinding) isn't available in the form to entry the SAML Authentication Type of the GAM backend, you have to do it programmatically.

```
&AuthenticationTypeSaml20.Load(&Name)
&AuthenticationTypeSaml20.Saml20.isRedirectBinding  = true
&AuthenticationTypeSaml20.Save()
If &AuthenticationTypeSaml20.Success() 
        Commit
    Else
        &Errors = &AuthenticationTypeSaml20.GetErrors()
        For &Error in &Errors
            Msg(Format(!"%1 (GAM%2)", &Error.Message, &Error.Code))
        EndFor
    EndIf
```

For the credentials section of the GAM configuration, see [HowTo: Generate certificates for authentication using SAML 2.0 GAM Authentication](https://wiki.genexus.com/commwiki/wiki?41243).

### [User Information](#User+Information)

`[imagen omitida: wiki id 56624]`


|  |
| --- |
| **Backlinks** |
| [GAM - SAML 2.0 Authentication type](https://wiki.genexus.com/commwiki/wiki?41212) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
