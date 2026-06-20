---
title: "GAM - Twitter Authentication Type"
source_id: 17208
source_url: https://wiki.genexus.com/commwiki/wiki?17208
genexus_version: "18"
---

# GAM - Twitter Authentication Type

To authenticate to Twitter using [GAM](https://wiki.genexus.com/commwiki/wiki?14960), follow the steps below:

### [Setup](#Setup)

#### [Step 1. Create a Twitter application.](#Step+1.+Create+a+Twitter+application.)

You need to create a "Twitter application" on the Twitter website and get a Consumer Key and Consumer Secret for that application.

Go to the Application Management page of Twitter for Developers (https://apps.twitter.com/) and create a new application, considering the following settings:

##### Figure 1. Configuring Twitter Application: Settings

**Important**: Set Callback URL = http://<domain>/oauth/gam/callback

and WEB SITE to your domain (eg.: apps5.genexus.com).

##### Figure 2. Configuring Twitter Application: Keys and Access Tokens

From here you will obtain a "Consumer Key" and "Consumer Secret".

#### [Step 2. Define Twitter authentication type](#Step+2.+Define+Twitter+authentication+type)

Define the "Twitter authentication type" using the [GAM](https://wiki.genexus.com/commwiki/wiki?14960) backend ([Authentication Types link](https://wiki.genexus.com/commwiki/wiki?16508)).

Enter the Consumer Key and Consumer Secret obtained on Twitter's developer website.

`[imagen omitida: wiki id 52342]`

##### [Figure 3. Configuring Twitter Authentication in GAM backend.](#Figure+3.+Configuring+Twitter+Authentication+in+GAM+backend.)

**Important note**

About the CallBack URL configuration in GAM Backend: you only need to enter the domain of the server running the application.  
It isn't necessary to enter the complete website URL. However, if you enter it, do not include the "/servlet" in Java.

\*This authentication type it's not allowed in Angular Generator.

### [Twitter Login](#Twitter+Login)

Twitter authentication type can be used in Web Applications and in Native Mobile applications.

### [Web Applications](#Web+Applications)

See the [GAMExampleLogin object](https://wiki.genexus.com/commwiki/wiki?39427,,) for details about how login is executed.

### [Native Mobile Applications](#Native+Mobile+Applications)

In the case of Native Mobile applications, you need to add an event in the login object to authenticate using Twitter.  
The logic inside the associated event will include a call to a method of the [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) named "LoginExternal".

The first parameter is based on the GAMAuthenticationTypes domain, and its value should be "Twitter".  
The &User and &password parameters are ignored in this case.  
The &LoginExternalAdditionalParameters parameter has an "AuthenticationTypeName" property where you can set the name of the Authentication Type. This is because more than one Twitter authentication type can be defined in the Repository.

```
Event 'Twitter'
    Composite
        &LoginExternalAdditionalParameters.AuthenticationTypeName    = !"Twitterb"  
      GeneXus.SD.Actions.LoginExternal(GAMAuthenticationTypes.Twitter, &User, &Password, &LoginExternalAdditionalParameters)
      Return
    EndComposite
EndEvent
```

Below is another way to program the Twitter login when you only have one Twitter authentication type in the repository (without passing the &LoginExternalAdditionalParameters):

```
Event 'Twitter'
    Composite
        GeneXus.SD.Actions.LoginExternal(GAMAuthenticationTypes.Twitter, &User, &Password)
        Return
    EndComposite
EndEvent
```

See [GAM Login Method](https://wiki.genexus.com/commwiki/wiki?19269) for details.

#### [Important considerations for Apple apps](#Important+considerations+for+Apple+apps)

It is necessary to configure the Twitter Consumer Key and Twitter Consumer Secret properties. See [Twitter Consumer Key and Twitter Consumer Secret property using GAM](https://wiki.genexus.com/commwiki/wiki?26947) for additional information.

#### [Notes:](#Notes%3A)

1. The Twitter API needs the SITE URL to be public and without any port; therefore, if your application is hosted under port 8080, for example, you need to use any kind of proxy or similar (like Apache web server) in order to use port 80. For more details, see the additional information at the bottom of this page.   
2. The first time users log in to Twitter, they will probably need to complete a form where they have to enter their email.  
3. **Important:** If you don't set a callback URL = http://<domain>/oauth/gam/**callback**you may get the following errors:

#### [.NET:](#.NET%3A)

`[imagen omitida: wiki id 55114]`

#### [Java:](#Java%3A)

`[imagen omitida: wiki id 55113]`

### [See Also](#See+Also)

[Twitter Consumer Key and Twitter Consumer Secret property using GAM](https://wiki.genexus.com/commwiki/wiki?26947)  
[Facebook Authentication Type](https://wiki.genexus.com/commwiki/wiki?29007)  
[Google Authentication Type](https://wiki.genexus.com/commwiki/wiki?29013)


|  |
| --- |
| **Backlinks** |
| [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) | [GAM - Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) |
| [GAM - Facebook Authentication Type](https://wiki.genexus.com/commwiki/wiki?29007) | [GAM - Google Authentication Type](https://wiki.genexus.com/commwiki/wiki?29013) | [GAM - Impersonation](https://wiki.genexus.com/commwiki/wiki?24241) | [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) |
| [GAM Google Authentication Type (X Evolution 3 upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?20020) | [GAM: "User Missing Required Data" Form](https://wiki.genexus.com/commwiki/wiki?18920) | [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Prototyping applications with Facebook or Twitter Authentication locally](https://wiki.genexus.com/commwiki/wiki?17141) |
| [Testing Facebook / Twitter authentication for SD applications using Android Emulator](https://wiki.genexus.com/commwiki/wiki?17191) | [Testing Facebook / Twitter authentication for WEB - NET applications](https://wiki.genexus.com/commwiki/wiki?17148) | [Twitter Consumer Key and Twitter Consumer Secret property using GAM](https://wiki.genexus.com/commwiki/wiki?26947) |

---
