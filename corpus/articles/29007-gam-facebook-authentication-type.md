---
title: "GAM - Facebook Authentication Type"
source_id: 29007
source_url: https://wiki.genexus.com/commwiki/wiki?29007
genexus_version: "18"
---

# GAM - Facebook Authentication Type

[GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) provides a way to authenticate using Facebook.

### [Steps to follow](#Steps+to+follow)

#### [1. Create a "Facebook client application"](#1.+Create+a+%22Facebook+client+application%22)

Create a "Facebook client application" in the Facebook site and obtain App Id and App Secret for that application.

Go to Facebook for developers (http://developers.facebook.com/) > My apps > Add a new app, as shown in the following figures:

`[imagen omitida: wiki id 37857]`

`[imagen omitida: wiki id 37858]`

`[imagen omitida: wiki id 37859]`

Enter the Site URL = http://<domain> (eg.: apps5.genexus.com).

`[imagen omitida: wiki id 37860]`

Go through Settings > Basic, to get the App Id and App Secret of the application.

`[imagen omitida: wiki id 37861]`

The following step is not necessary if your application runs on *localhost:*

Go through Products > Facebook Login > Settings. There, enter a valid value for "Valid OAuth redirect URIs" field.  
A valid format is : https://<server>/<base url>/oauth/gam/callback  
You can enter as many URIs as you want in that field. For example, if [the REST Web Services of the mobile application](https://wiki.genexus.com/commwiki/wiki?21146) are separated from the Web application, you need to add the URL as well, following the format :

https://<server>/<Services base url >/oauth/gam/callback

Note also that "Web OAuth Login" must always be set to YES.

**Note**: Remember to make the FB application public.

#### [2. Define "Facebook Authentication Type"](#2.+Define+%22Facebook+Authentication+Type%22)

Define "Facebook Authentication Type" using the [GAM backend](https://wiki.genexus.com/commwiki/wiki?15935) or the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535). Go through [Authentication Types link](https://wiki.genexus.com/commwiki/wiki?16508).

`[imagen omitida: wiki id 52329]`

Important note:

The Local Site URL specified is only the domain where the application runs. You don't need to enter the complete site URL. For example https://apps6.genexus.com.  
If you enter the complete Site URL is also right, but never include the "/servlet" in Java.

Facebook Authentication Type can be used in Web Applications and Native Mobile applications also.

### [Web Applications](#Web+Applications)

See the [GAMExampleLogin object](https://wiki.genexus.com/commwiki/wiki?39427,,) for details about how the login is executed.

Considerations: The LoginFacebook function doesn't work as expected in popup windows (the same happens to LoginTwitter). This is a limitation of those sites, who don't support a redirect from an HTML iframe. For a workaround, see [SAC 34259](https://www.genexus.com/developers/websac?en,,,34259;;)

### [Native Mobile Applications](#Native+Mobile+Applications)

In the case of Native Mobile applications, you need to add an event in the login object to authenticate using Facebook.  
The logic inside the event associated will include a call to a method of [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350), named "LoginExternal".

The first parameter is based on the GAMAuthenticationTypes domain, and its value should be "Facebook".  
The &User and &password parameters are ignored in this case.  
The &LoginExternalAdditionalParameters has an "AuthenticationTypeName" property where you can set the name of the Authentication Type. This is due to the fact that more than one Facebook Authentication Type can be defined in the Repository.

```
Event 'Facebook'
    Composite
        &LoginExternalAdditionalParameters.AuthenticationTypeName    = !"facebook1"  
      GeneXus.SD.Actions.LoginExternal(GAMAuthenticationTypes.Facebook, &User, &Password, &LoginExternalAdditionalParameters)
      Return
    EndComposite
EndEvent
```

Another way to program the Facebook login, when you only have one Facebook Authentication Type in the repository, is the following (without passing the &LoginExternalAdditionalParameters):

```
Event 'Facebook'
    Composite
        GeneXus.SD.Actions.LoginExternal(GAMAuthenticationTypes.Facebook, &User, &Password)
        Return
    EndComposite
EndEvent
```

#### [**Important**](#Important)

For testing purporses, you have to add Developer Roles to make tests on your application.

`[imagen omitida: wiki id 56215]`

See [GAM Login Method](https://wiki.genexus.com/commwiki/wiki?19269) for details.

### [Software Requirements](#Software+Requirements)

* Java: JDK 1.7 or upper is required to be installed on the application server. Otherwise, the Facebook certificate has to be installed in the key store of the JVM.
* Csharp: The certificate of Facebook has to be installed on the Windows server.

Notes:

1. Facebook Authentication is solved using OAuth.  
2. In case you want to "work with friends", or do any particular action after the user has logged in, you need to communicate with the Facebook API. In that case, you'll probably need to get the ExternalToken method of GAMSession EO. The result of invoking this method should be passed to the Facebook API.

### [See Also](#See+Also)

[HowTo: Register a Facebook App](https://wiki.genexus.com/commwiki/wiki?19399)  
[GAM - Facebook Interaction Sample](https://wiki.genexus.com/commwiki/wiki?16569)  
[GAM - Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208)  
[GAM - Google Authentication Type](https://wiki.genexus.com/commwiki/wiki?29013)  
[Additional Scope Property for GAM Google / Facebook Authentication Types](https://wiki.genexus.com/commwiki/wiki?21584,,)  
[iOS 6.0 Facebook Integration](https://wiki.genexus.com/commwiki/wiki?27798,,)  
[Windows Phone Facebook Integration](https://wiki.genexus.com/commwiki/wiki?27935,,)


|  |
| --- |
| **Backlinks** |
| [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) | [Facebook external object](https://wiki.genexus.com/commwiki/wiki?38432) |
| [GAM - Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) | [GAM - Google Authentication Type](https://wiki.genexus.com/commwiki/wiki?29013) | [GAM - Impersonation](https://wiki.genexus.com/commwiki/wiki?24241) | [GAM - OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484) |
| [GAM - Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208) | [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) | [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Get the email address of a Facebook user](https://wiki.genexus.com/commwiki/wiki?25087) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Prototyping applications with Facebook or Twitter Authentication locally](https://wiki.genexus.com/commwiki/wiki?17141) |
|

---
