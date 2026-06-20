---
title: "GAM - Google Authentication Type"
source_id: 29013
source_url: https://wiki.genexus.com/commwiki/wiki?29013
genexus_version: "18"
---

# GAM - Google Authentication Type

Using [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) you can authenticate in Google site, just by following these steps.

### [Setup](#Setup)

#### [Create a Google app](#Create+a+Google+app)

1. You need to create a "Google client application" in the Google site and obtain Client Id and Client Secret for that application.

For that, go to the following link: <https://code.google.com/apis/console>

2. There go to API´s & Services section. First, click on the Credentials section, and select "OAuth client ID":

`[imagen omitida: wiki id 53574]`

Select "Application type" = Web application

`[imagen omitida: wiki id 53575]`

And the following will be displayed:

`[imagen omitida: wiki id 53576]`

You need to change the Redirect URIs. There you may specify the complete URI of your application, including the /oauth/gam/signin, as the figure shows:

`[imagen omitida: wiki id 53577]`

Click on the "CREATE" button and the Client ID and Client Secret information is displayed:

`[imagen omitida: wiki id 53578]`

**Important note**

In all cases —[Java](https://wiki.genexus.com/commwiki/wiki?12258) and [.NET](https://wiki.genexus.com/commwiki/wiki?38604)— you need to specify the complete URI of the application including the virtual directory followed by /oauth/gam/signin

### [Configuration to be done in the GAM Backend](#Configuration+to+be+done+in+the+GAM+Backend)

* Define a new Authentication Type = Google using the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935).
* Enter Client Id and Client Secret obtained in Google site.

`[imagen omitida: wiki id 52344]`

**Important note**

About the Local Site URL configuration in GAM backend. You just need to enter the domain of the server running the application.  
It isn't necessary to enter the complete site URL, but in case you enter it, do not include the "/servlet" in java.

### [Google Login](#Google+Login)

#### [How to login using Google account in Web applications](#How+to+login+using+Google+account+in+Web+applications)

See the [GAMExampleLogin object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?39427,,) for details about how the login is executed.

#### [How to login using Google account in Native Mobile applications](#How+to+login+using+Google+account+in+Native+Mobile+applications)

In the case of Native Mobile applications, you need to add an event in the login object to authenticate using Google.  
The logic inside the event associated will include a call to a method of [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350), named "LoginExternal".

The first parameter is based on the GAMAuthenticationTypes domain, and its value should be "Google".  
The &User and &password parameters are ignored in this case.  
The &LoginExternalAdditionalParameters has an "AuthenticationTypeName" property where you can set the name of the Authentication Type. This is due to the fact that more than one Google Authentication Type can be defined in the Repository.

```
Event 'Google'
    Composite
        &LoginExternalAdditionalParameters.AuthenticationTypeName    = !"Googleb"
      GeneXus.SD.Actions.LoginExternal(GAMAuthenticationTypes.Google, &User, &Password, &LoginExternalAdditionalParameters)
      Return
    EndComposite
EndEvent
```

Another way to program the Google login, when you only have one Google Authentication Type in the repository, is the following (without passing the &LoginExternalAdditionalParameters):

```
Event 'Google'
    Composite
        GeneXus.SD.Actions.LoginExternal(GAMAuthenticationTypes.Google, &User, &Password)
        Return
    EndComposite
EndEvent
```

See [GAM Login Method](https://wiki.genexus.com/commwiki/wiki?19269) for details.

### [See Also](#See+Also)

[GAM - Facebook Authentication Type](https://wiki.genexus.com/commwiki/wiki?29007)  
[GAM - Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208)  
[Additional Scope Property for GAM Google / Facebook Authentication Types](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?21584,,)


|  |
| --- |
| **Backlinks** |
| [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) | [GAM - Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) |
| [GAM - Facebook Authentication Type](https://wiki.genexus.com/commwiki/wiki?29007) | [GAM - OAuth 2.0 Authentication Type](https://wiki.genexus.com/commwiki/wiki?39484) | [GAM - Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208) | [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) |
| [GAM Google Authentication Type (X Evolution 3 upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?20020) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
