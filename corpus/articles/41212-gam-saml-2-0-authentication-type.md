---
title: "GAM - SAML 2.0 Authentication type"
source_id: 41212
source_url: https://wiki.genexus.com/commwiki/wiki?41212
genexus_version: "18"
---

# GAM - SAML 2.0 Authentication type

[GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) allows you to authenticate using any [SAML](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=security#overview) 2.0 provider.

Some example Providers are:

* [AGESIC](https://wiki.genexus.com/commwiki/wiki?41266)
* [SAP](https://wiki.genexus.com/commwiki/wiki?41235)
* [Okta](https://wiki.genexus.com/commwiki/wiki?49660)

SAML is a secure XML-based communication mechanism for communicating identities between organizations. It's the acronym for Security Assertion Markup Language. The main use case that SAML solves is [SSO](http://en.wikipedia.org/wiki/Single_sign-on), so it avoids the need to maintain multiple credentials in multiple locations, and it increases security while decreasing administration timing tasks.  
Another benefit of using SAML is the possibility of a federated identity for users. Users often have local user identities within the domains of each application. Identity federation provides a means for these applications to agree on a shared name identifier for referring to the user.

### [How does it work?](#How+does+it+work%3F)

SAML is an XML-based framework for authentication and authorization between two entities: a [Service Provider](https://en.wikipedia.org/wiki/Service_provider_(SAML)) (SP) and an [Identity Provider](https://en.wikipedia.org/wiki/Identity_provider_(SAML)) (IdP). The Service Provider agrees to trust the Identity Provider for authenticating users. For authenticating, the IdP may request some information from the user - such as user name and password (though it could be any authentication method). Then, the IdP generates an authentication assertion (i.e. a statement used by service providers to make access-control decisions), to indicate that a user has been authenticated.

For more information, see [SAML v2.0 Technical overview](https://www.oasis-open.org/committees/download.php/27819/sstc-saml-tech-overview-2.0-cd-02.pdf).

In sum, the behavior implies that, when there is no valid session, the user is redirected to the IdP login page. After logging in, the user is redirected to the application again. Within the same browser, when another Service Provider tries to login using the same IdP, if there is a valid session already, then the user will not be required to login again.

\*This authentication type it's available for Java up to Tomcat 9 and .Net Framework generators.

### [How to configure SAML 2.0 Authentication Type using GAM](#How+to+configure+SAML+2.0+Authentication+Type+using+GAM)

First, define a new GAM Authentication Type SAML 2.0. It requires a detailed configuration of the protocol, following the documentation of the Identity Provider to which you wish to be connected.

`[imagen omitida: wiki id 51840]`

#### [Tab General](#Tab+General)

Basic identification information of the application in SAML 2.0. All this information should be completed following a service agreement with the SAML Provider.

`[imagen omitida: wiki id 51842]`

* **Local Site URL**:Configure the URL used to register your application (Service Provider) in the IdP. The URL has to be of the format: protocol://domain:port/<virtual directory> (e.g.: http://testgamagesic.com:8080/gamlogin).

Tip: Using tomcat, you may edit the server.xml file under the conf directory, and add the following Context tag (inside the Host tag), so that the real URL may be changed to what you have configured in the IDP. In this example, the TestGamAgesicJavaEnvironment servlet directory is changed to /gamlogin:  
<Context reloadable="true" privileged="true" path="/gamlogin" docBase="TestGamAgesicJavaEnvironment" />

* Configure the **[Service Provider](https://en.wikipedia.org/wiki/Service_provider_(SAML)) Entity ID**, which is an identifier of your application in the Identity Provider. It is configured in this field, as well as in the Identity Provider itself.

*How to check the Service Provider Entity ID in the Provider's configuration?*This is the <Issuer> of the SAML request.

* In the **Identity Provider Entity Id** field, complete the Entity Id given by the Provider's (IDP). The completion of this field is necessary only for .NET Framework applications.

*How to get the Identity Provider Entity Id in my SAML Provider?* This is the <Issuer> of the SAML response.

* **Execute SAML Requests using GET**  
    
  *How to get this information in the SAML Provider?* Itcorresponds to the ProtocolBinding attribute of the requests. Furthermore, this property is directly associated with the HTTP method with which the request is made to the IDP.

The General tab has two specific sections:

#### [Login](#Login)

* There is the **SAML Endpoint Location** field, where the location of the Identity Provider's endpoint must be configured in order to login.

*How to know the SAML Endpoint Location of my SAML Provider?* Take a look at the Provider's documentation, and look for the "Destination". The Destination concept is explained in this [link](http://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf).

* **Name ID Policy format**  
    
  Some identity providers restrict the format of the NameID policy. Here select the correct value according to the requirements of the IDP.
* **Force Authentication** = TRUE means that every time that a login is required on a different Service Provider, the IdP will request the user to enter credentials again (SSO will not be used). It's supported by some identity providers only.

*How to know the Force Authentication of my SAML Provider?* Look at [this](http://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf) link where the Force Authn attribute is explained. Then you can go for that information at your SAML Identity Provider.

* **Authentication Context**: Some possible values are SMARTCARD\_PKI\_AUTHN\_CTX and PPT\_AUTHN\_CTX. The first value corresponds to SmartcardPKI, and the second to PasswordProtectedTransport. Check the provider's documentation to know the value to be configured in this property.

*How to know the Authentication Context of my SAML Provider?* Look at [this](http://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf) link where the AuthnContext attribute is explained.

#### [Logout](#Logout)

* **Disable Single Logout**  
  If this property is checked, Single logout (SLO) is not executed, which means that the logout is done in the SP exclusively (not at the IdP).
* The **Single Logout Endpoint** is configured in this section. It works just like the SAML Endpoint Location, except that, in this case, indicating the location to logout.

*How to know the Single Logout Endpoint of my SAML Provider?*It's the Destination of the logout request. The Destination concept is explained in this [link](http://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf).

Note: All this information is agreed upon in the contract with the IdP.

#### [Credentials Tab](#Credentials+Tab)

Using SAML authentication requires signature certificates. There are two Sections in this Tab:

* Request Credentials: these are the credentials to access the Keystore that contains the signature certificates to make the request.
* Response Credentials: just as you have keys to sign the request, the Identity Provider provides you with the keys to also validate its signatures.  
  In the case of Java applications, these keys must be added in a TrustStore. The credentials to access the TrustStore have to be configured in this section in that case.

Java generated application example:

In the case of Java applications, the Response credentials have to be in a TrustStore so you have to open the "Advanced configuration" to set the TrustStore information.

`[imagen omitida: wiki id 51843]`

.Net Framework generated application example:

In the case of .NET Framework apps, the Response credentials have to be a .cer file (without using a TrustStore).

`[imagen omitida: wiki id 51844]`

See [HowTo: Generate certificates for authentication using SAML 2.0 GAM Authentication](https://wiki.genexus.com/commwiki/wiki?41243) for information on how to generate the certificates and what should be completed in each field.

#### [User Information tab](#User+Information+tab)

Once duly authenticated, the Identity Provider returns an [assertion](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language#Assertions) containing the user's data. Each provider returns the data according to varied criteria. In this tab, you must enter the mapping from the assertion data to the GAM data.

For additional user information returned in the IdP assertion - which is not listed under the User Information tab -, you may add it by using the grid below the "Custom User Attributes" section. That information will be stored as [extended properties](https://wiki.genexus.com/commwiki/wiki?19634) for the GAM User.

Click on the "Add" button to add the Attribute Name that will be stored in the GAM database, in addition to the Attribute tag included in the assertion.

`[imagen omitida: wiki id 51856]`

### [Configuration in the Identity Provider](#Configuration+in+the+Identity+Provider)

Basically, you need to configure:

**Assertion Consumer Service Endpoint / Assertion Consumer Service Location / Single Sign On Service Endpoint** (different names which can be used by the Provider)

* Java:  https://<domain>/<base\_url>/saml/gam/signin
* Net Framework: https://<domain>/<base\_url>/Saml2/Acs

**Single Logout Location**

* Java or Net Framework:https://<domain>/<base\_url>/saml/gam/signout

### [Having an SSO behavior](#Having+an+SSO+behavior)

See [HowTo: Have an SSO behavior by using SAML Authentication](https://wiki.genexus.com/commwiki/wiki?44887)

### [Availability](#Availability)

As of [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?40782,,) for Java only.

Since [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?42129,,) it's available for .NET Framework applications also. SAC [42156](https://www.genexus.com/developers/websac?en,,,45156)

### [Considerations](#Considerations)

By default, the Artech.Security.Saml.jar connector does not generate tracing information. In order to have tracing info, create a file called "simplelogger.properties" under your servlet's server installation, at \WEB-INF\classes directory, with the following lines:

```
# It has to be one of these ("trace", "debug", "info", "warn", "error" or "off"). The default value is "info".
org.slf4j.simpleLogger.defaultLogLevel = debug

# The output can be writen to any file or to the standard output (the default is the standard output).
# org.slf4j.simpleLogger.logFile

org.slf4j.simpleLogger.showDateTime = true

# The date and time format to be used in the output messages. The pattern describing the date and time format is defined by SimpleDateFormat.
org.slf4j.simpleLogger.dateTimeFormat = dd-MM-yyyy hh:mm:ss
```

Up to GeneXus 18 Upgrade 13, the SAML project has the following JARS as dependencies:  
  
*- commons-collections-3.2.1.jar  
- commons-httpclient-3.1.jar  
- esapi-2.0.1.jar  
- not-yet-commons-ssl-0.3.9.jar  
- velocity-1.7.jar*

In case you **do not** **use SAML** in your project you can remove the above mentioned JARs from your deploy.

### [See Also](#See+Also)

[HowTo: Generate certificates for authentication using SAML 2.0 GAM Authentication](https://wiki.genexus.com/commwiki/wiki?41243)  
[HowTo: Configuring SAML 2.0 GAM Authentication type using SAP](https://wiki.genexus.com/commwiki/wiki?41235)  
[HowTo: Configuring SAML 2.0 GAM Authentication type using Agesic](https://wiki.genexus.com/commwiki/wiki?41266)  
[HowTo: Configure SAML 2.0 GAM Authentication type using Okta](https://wiki.genexus.com/commwiki/wiki?49660)  
Useful tool to inspect the SAML assertions: [SAML Chrome panel](https://chrome.google.com/webstore/detail/saml-chrome-panel/paijfdbeoenhembfhkhllainmocckace?hl=en)


|  |
| --- |
| **Backlinks** |
|
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Configure SAML 2.0 GAM Authentication type using Azure](https://wiki.genexus.com/commwiki/wiki?54751) | [HowTo: Configure SAML 2.0 GAM Authentication type using Okta](https://wiki.genexus.com/commwiki/wiki?49660) | [HowTo: Configuring SAML 2.0 GAM Authentication type using Agesic](https://wiki.genexus.com/commwiki/wiki?41266) |
| [HowTo: Configuring SAML 2.0 GAM Authentication type using SAP](https://wiki.genexus.com/commwiki/wiki?41235) | [HowTo: Generate certificates for authentication using SAML 2.0 GAM Authentication](https://wiki.genexus.com/commwiki/wiki?41243) | [HowTo: Have an SSO behavior by using SAML Authentication](https://wiki.genexus.com/commwiki/wiki?44887) |

---
