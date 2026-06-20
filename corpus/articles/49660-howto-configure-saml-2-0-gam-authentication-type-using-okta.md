---
title: "HowTo: Configure SAML 2.0 GAM Authentication type using Okta"
source_id: 49660
source_url: https://wiki.genexus.com/commwiki/wiki?49660
genexus_version: "18"
---

# HowTo: Configure SAML 2.0 GAM Authentication type using Okta

**Warning**: This sample shows how to configure the SAML 2.0 GAM Authentication type using Okta. GeneXus does not support the configuration of these external systems. Samples, screenshots, parameters, and/or locations may change over time.

This document explains the steps to follow in [Okta](https://www.okta.com) and GAM to configure authentication with Okta as IDP for [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) using [SAML 2.0 Authentication type](https://wiki.genexus.com/commwiki/wiki?41212).

## [Okta Configuration](#Okta+Configuration)

1. Go to the website of [Okta](https://www.okta.com)
2. Once logged in, click on the profile icon, and click on the **Your apps** menu option as shown in the image below:

`[imagen omitida: wiki id 49661]`

        3. Follow the steps below to create an application with SAML authentication:

`[imagen omitida: wiki id 49662]`  
`[imagen omitida: wiki id 49663]`

        4. Configuration:

`[imagen omitida: wiki id 50131]`

**Single sign-on URL**: URL of the application’s local site, following this format:

* Java: https://<domain>/<base\_url>/saml/gam/signin
* Net: https://<domain>/<base\_url>/Saml2/Acs

**Audience URL (SP Entity ID)**: It can contain any value, but here you must enter the same value as in the **Service Provider Entity ID** GAM back-end field.  
  
`[imagen omitida: wiki id 49665]`

The defined field names will be used in the GAM back end in the **User Information** tab to obtain data about the users.  
  
The rest of the application settings in Okta can be used by default.

         5. Once the application is created, go to the **Sign On** tab and then to the **View Setup Instruction** button:

`[imagen omitida: wiki id 49666]`  
  
You will be redirected to a site containing what you need to configure GAM.

`[imagen omitida: wiki id 49671]`

## [GAM Configuration](#GAM+Configuration)

Read about the GAM back end configuration for this authentication in [GAM - SAML 2.0 Authentication type](https://wiki.genexus.com/commwiki/wiki?41212).

### [Distinctive aspects of this configuration:](#Distinctive+aspects+of+this+configuration%3A)

### [General Tab](#General+Tab)

`[imagen omitida: wiki id 51859]`

The highlighted fields depend on the Okta configuration:

1. As seen in step 4, the value here must be the same as in the **Audience URL** field in Okta.
2. It is the **Identity Provider Issuer** value from step 5.
3. It must contain the value of**the Identity Provider Single Sign-On URL** also obtained in step 5 of the Okta configuration.

### [Credentials Tab](#Credentials+Tab)

`[imagen omitida: wiki id 51860]`

**Important:** It is a standard configuration, taking into account that in the last step of the Okta configuration you obtained the certificate for your application there. This certificate must be converted to a keyresponse.jks and then used in the response part. For more information, read: [HowTo: Generate certificates for authentication using SAML 2.0 GAM Authentication](https://wiki.genexus.com/commwiki/wiki?41243).

### [User Information Tab](#User+Information+Tab)

`[imagen omitida: wiki id 51861]`

The names defined in Okta must be used for the user attributes.

## [See Also](#See+Also)

[GAM - SAML 2.0 Authentication type](https://wiki.genexus.com/commwiki/wiki?41212)  
[HowTo: Generate certificates for authentication using SAML 2.0 GAM Authentication](https://wiki.genexus.com/commwiki/wiki?41243)


|  |
| --- |
| **Backlinks** |
| [GAM - SAML 2.0 Authentication type](https://wiki.genexus.com/commwiki/wiki?41212) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
