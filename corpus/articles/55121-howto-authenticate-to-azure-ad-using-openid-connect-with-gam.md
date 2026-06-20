---
title: "HowTo: Authenticate to Azure AD using OpenID Connect with GAM"
source_id: 55121
source_url: https://wiki.genexus.com/commwiki/wiki?55121
genexus_version: "18"
---

# HowTo: Authenticate to Azure AD using OpenID Connect with GAM

**Warning**: This sample shows how to use GAM with Azure AD as an external OpenID Connect provider. GeneXus does not support the configuration of this external system. Samples, screenshots, parameters, and/or locations may change over time.

**Note**: As of July 2023, Microsoft has changed the name of its Azure Active Directory product to Microsoft Entra ID.

This tutorial explains how to authenticate your users using the OpenID Connect protocol with [Azure Active Directory](https://azure.microsoft.com/en-us/products/active-directory/) and GAM.

You need to use [OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484) and do some settings on the Azure Active Directory (Azure AD) Admin Center and the GAM's backend.

### [Configuration in the Azure AD Admin Center](#Configuration+in+the+Azure+AD+Admin+Center)

**1.**Define and register an application. See [this guide](https://docs.microsoft.com/en-us/graph/auth-register-app-v2) from Microsoft.

**2.**Get the app's Application Id, since you'll need it later on:

`[imagen omitida: wiki id 48910]`

**3.**Configure a Redirect URI. Go through the Authentication menu option (Panel on the left) and create a new Web platform. Then add a Redirect URI of the form:

`[imagen omitida: wiki id 48911]`

http://<server>:<port>/<BackendBaseURL>/oauth/gam/callback

**4.**Go through the Certificates & secrets option, and create a NewSecret. You should copy the **value** of the secret, as it will be needed later.

`[imagen omitida: wiki id 48912]`

**5.** In the API permissions tab, verify that you have added the following:

`[imagen omitida: wiki id 55124]`

The following steps will help you to obtain the certificate that you will later use in the GAM backend configuration.

**6.** Configure certificates using Discovery URL

You don't need to manually obtain or configure certificates from Azure AD. GAM automatically uses the [Discovery URL](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc) to get all the provider’s configuration and active signing certificates. This includes the necessary endpoints for authentication and the certificates required to validate tokens.

GAM also automatically handles key rotation, so token validation always uses the correct signing certificate without requiring manual updates.

**7.** Go to  [Format Certificate Web Tool](https://www.samltool.com/format_x509cert.php ) and paste the certificate you choose in the last step.

`[imagen omitida: wiki id 55129]`

**8.** Create a .crt file in a folder (For example: *C:/YourKB/NetSql/web/Certs*), and paste the resulting certificate from the Certificate Web Tool.

**9.** Finally, upload this .crt certificate in the Upload certificate option:

`[imagen omitida: wiki id 55123]`

### [Configuration in the GAM Backend](#Configuration+in+the+GAM+Backend)

In the GAM Backend go to "Settings" and "Authentication Types" and create an [OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484).

Go to the General tab and configure the following:

`[imagen omitida: wiki id 55130]`

**1.**The Client Id value from the second step of the Azure AD portal configuration.

**2.** The Client Secret value from the fourth step of the Azure AD portal configuration.

Go to the Authorization Tab and configure the following:

`[imagen omitida: wiki id 55131]`

**Note:** The {tenant} value must be obtained from the application's Overview Panel.

`[imagen omitida: wiki id 55132]`

**Important:**For the OpenID connect authentication type to work correctly, make sure that you have checked "Enable OpenID Connect Protocol?" and "Validate ID Token".

**Issuer URL**: The value for this field must be obtained from the request to this URL: *https://login.microsoftonline.com/organizations/v2.0/.well-known/openid-configuration* in the browser or Postman.

**Tip:** To find the value in the request result, use Ctrl + F and type "issuer".

Go to Token Tab and configure the following:

`[imagen omitida: wiki id 55135]`

`[imagen omitida: wiki id 55137]`

#### [Configuration in the User Information Tab](#Configuration+in+the+User+Information+Tab)

For the OpenID Connect authentication type, you do not have to configure anything in the user information tab.

### [See Also](#See+Also)

[GAM - OpenID Connect Authentication Type](https://wiki.genexus.com/commwiki/wiki?49183)


|  |
| --- |
| **Backlinks** |
| [GAM - OpenID Connect Authentication Type](https://wiki.genexus.com/commwiki/wiki?49183) | [GAM - OpenID Connect Authentication Type (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57652) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |
| [HowTo: Authenticate to Azure AD using OpenID Connect with GAM (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?60566) |

---
