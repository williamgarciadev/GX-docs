---
title: "HowTo: Configuring SAML 2.0 GAM Authentication type using SAP"
source_id: 41235
source_url: https://wiki.genexus.com/commwiki/wiki?41235
genexus_version: "18"
---

# HowTo: Configuring SAML 2.0 GAM Authentication type using SAP

**Warning**: This sample shows how to configure the SAML 2.0 GAM Authentication type using SAP Cloud Platform Identity Authentication. GeneXus does not support the configuration of these external systems. Samples, screenshots, parameters, and/or locations may change over time.

This document explains the steps to be followed in SAP Cloud Platform in order to configure [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) to authenticate using [SAML 2.0 Authentication type](https://wiki.genexus.com/commwiki/wiki?41212) using SAP.

### [SAP Cloud Platform Identity Authentication configuration](#SAP+Cloud+Platform+Identity+Authentication+configuration)

1. Contract the service [SAP Cloud Platform Identity Authentication](https://www.sap.com/products/technology-platform.html).
2. Create the certificates necessary to connect to SAP as an SAML 2.0 Identity Provider.  
   Get the Response certificates from the SAP Cloud Platform Identity Authentication console. Go through Applications > Resources >Tenant Settings > SAML 2.0 Configuration, and click "download metadata".  
     
   `[imagen omitida: wiki id 41236]`  
   Generate a Response certificate for SAP (keystore). It's used to complete the **Response Credentials** section,in the SAML 2.0 Authentication type configuration. For detailed information on the subject, see [HowTo: Generate certificates for authentication using SAML 2.0 GAM Authentication](https://wiki.genexus.com/commwiki/wiki?41243).
3. Create an application in SAP Cloud Platform Identity Authentication. Go through Applications & Resources > Applications, and click "Add".  
   `[imagen omitida: wiki id 41237]`
4. Assign a name to the application just created and save.  
   `[imagen omitida: wiki id 41238]`
5. To configure the application, go through the Trust option, and configure the Authentication type (by default, it will be SAML 2.0).  
   `[imagen omitida: wiki id 41239]`
6. Select SAML 2.0 Configuration:  
   `[imagen omitida: wiki id 41240]`  
     
   Then configure:
   1. **Name**: the external identifier that will be assigned to the application (the same to be configured at the **Service Provider Entity ID** in the SAML 2.0 Authentication type Login General tab configuration).
   2. **Assertion Consumer Service Endpoint**: the URL of the [Service Provider](https://en.wikipedia.org/wiki/Service_provider_(SAML)) (the GeneXus application) that receives responses from the [Identity Provider](https://en.wikipedia.org/wiki/Identity_provider_(SAML)) (e.g.: https://gxexample/KBExample/saml/gam/signin).

      **Important**: The format of the URL must be https://<domain>/<url\_base>/saml/gam/signin
   3. **Single Logout Endpoint**: the URL of the single logout endpoint of the Service Provider (e.g.: https://gxexample/KBExample/saml/gam/signout)

      **Important**: The format of the URL must be https://<domain>/<url\_base>/saml/gam/signout
   4. **Signing Certificate**: public key used by the Service Provider to sign the requests to the Identity Provider (the certificate.pem created previously).
   5. **Algorithm**: the algorithm for signing the response messages.

In the GAM backend, you'll have a screen like the one below:

`[imagen omitida: wiki id 52308]`

**Authentication Context**: Leave it empty for SAP.

The **Identity Provider Entity ID**is the Identity Provider used. (e.g.: https://aenbqmdqv.accounts.ondemand.com)

The **Saml Endpoint Location** to beconfigured in the GAM backend should be taken from the SAP configuration (Single Sign On Endpoint). Likewise, the **Single Logout Endpoint** value to be configured in the backend should be taken from the Single Logout Endpoint in SAP.

**`[imagen omitida: wiki id 41564]`**

### [Getting user information](#Getting+user+information+)

By default, SAP returns the following information: first name, last name, and email; all of which will be added to the assertion. It should be mapped in the SAML 2.0 Authentication type configuration under the User Information tab, as follows:

* User First Name tag: first\_name
* User Last Name tag: last\_name
* User E-mail tag: mail

If desired, further information may be added. First go through the "Assertion Attributes" -> Add option in the SAP Cloud Platform and select the attribute you wish to add. Then specify the tag in the User Information tab configuration of the SAML 2.0 Authentication type.

`[imagen omitida: wiki id 52307]`

### [See Also](#See+Also)

[HowTo: Generate certificates for authentication using SAML 2.0 GAM Authentication](https://wiki.genexus.com/commwiki/wiki?41243)


|  |
| --- |
| **Backlinks** |
| [GAM - SAML 2.0 Authentication type](https://wiki.genexus.com/commwiki/wiki?41212) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Setup Single Sign On between GeneXus and SAP Cloud Platform Fiori Application using SAML](https://wiki.genexus.com/commwiki/wiki?43404) |

---
