---
title: "HowTo: Configure SAML 2.0 GAM Authentication type using Azure"
source_id: 54751
source_url: https://wiki.genexus.com/commwiki/wiki?54751
genexus_version: "18"
---

# HowTo: Configure SAML 2.0 GAM Authentication type using Azure

**Warning**: This sample shows how to configure the SAML 2.0 GAM Authentication type using Azure. GeneXus does not support the configuration of these external systems. Samples, screenshots, parameters, and/or locations may change over time.

This document explains the steps to follow in  [Azure](https://portal.azure.com/#home) and GAM to configure authentication with Azure as IDP for [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) using [SAML 2.0 Authentication type](https://wiki.genexus.com/commwiki/wiki?41212).

## [Azure Configuration](#Azure+Configuration)

1. Go to the [Azure website](https://portal.azure.com/#home).

2. Once logged in, go to Enterprise applications and select "+ New application".

`[imagen omitida: wiki id 54752]`

3. Next, click on "Create your own application"*.*

4. After entering a name for your application, a screen like this will appear:

`[imagen omitida: wiki id 54753]`

5. Save your **Application ID** and **Object ID.** Click on "Set up single sign on"and select **SAML**.

6. Here you must fill in all the required fields. To do so, select "Edit".

`[imagen omitida: wiki id 54754]`

Next, you will see the following screen:

`[imagen omitida: wiki id 54755]`

The required information depends on the generator you are using:

* Java: https://<domain>/<base\_url>/saml/gam/signin
* Net: https://<domain>/<base\_url>/Saml2/Acs

7. "Attributes & Claims" should look as follows:

`[imagen omitida: wiki id 54756]`

8. In the "SAML Certificates" section, download **Certificate (Base 64)**.

9. The "Set up test" section shows endpoints that will be useful in the GAM Backoffice configuration.

`[imagen omitida: wiki id 54758]`

10. Finally, select "Users and Groups" in the left panel (under "Manage") and add some users or your own user.

## [GAM Configuration](#GAM+Configuration)

Distinctive aspects of this configuration:

### [General Tab](#General+Tab)

`[imagen omitida: wiki id 54759]`

In the case of Java, you must fill the property "Authentication context" with the value "urn:oasis:names:tc:SAML:2.0:ac:classes:Password".

### [Credentials Tab](#Credentials+Tab)

`[imagen omitida: wiki id 54760]`

**Note**: To learn more about how to generate the request credentials, read [HowTo: Generate certificates for authentication using SAML 2.0 GAM Authentication](https://wiki.genexus.com/commwiki/wiki?41243).

### [User Information Tab](#User+Information+Tab)

`[imagen omitida: wiki id 54761]`

Here you use your Attributes & Claims recently configured.

**Note**: This is a default configuration; the information retrieved always depends on the IDP configuration (Azure).

## [Important](#Important)

If you are getting an error like this:

*Received message contains unexpected InResponseTo "id9ab431ed1e434dba80c0562d2e2b48a8". No cookie preserving state from the request was found so the message was not expected to have an InResponseTo attribute. This error typically occurs if the cookie set when doing SP-initiated sign on have been lost.*

Please read [**here**](https://www.genexus.com/es/developers/websac?data=50188;;) how to solve it.

#### [Workaround](#Workaround)

Configure the Environment properties

#### [HTTP:](#HTTP%3A)

SameSite cookie attribute = Do not Specify

Parameter Style = Positional.

#### [HTTPS:](#HTTPS%3A)

SameSite cookie attribute = None

Parameter Style = Positional

## [See Also](#See+Also)

[GAM - SAML 2.0 Authentication type](https://wiki.genexus.com/commwiki/wiki?41212)  
[HowTo: Generate certificates for authentication using SAML 2.0 GAM Authentication](https://wiki.genexus.com/commwiki/wiki?41243)


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
