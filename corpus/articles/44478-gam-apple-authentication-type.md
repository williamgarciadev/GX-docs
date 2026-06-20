---
title: "GAM - Apple Authentication type"
source_id: 44478
source_url: https://wiki.genexus.com/commwiki/wiki?44478
genexus_version: "18"
---

# GAM - Apple Authentication type

[GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) provides a way to authenticate using Apple.

The Apple Authentication type is supported for all platforms - Web and Mobile (Apple and Android).

In this article, they are explained the steps needed to follow in order to configure your application to login using Apple.

To do that, you need a Native mobile application generated for Apple, having these properties in the Main object:

* [Development Team ID property](https://wiki.genexus.com/commwiki/wiki?30100)
* [Enable Sign in with Apple property](https://wiki.genexus.com/commwiki/wiki?44467)

Then, verify the [Apple Bundle Identifier property](https://wiki.genexus.com/commwiki/wiki?37617), which in this example is "com.genexus.testAppleSignIn."

### [Apple backend: Application Registration](#Apple+backend%3A+Application+Registration)

On the [Apple developer site](https://developer.apple.com/) (to follow these steps, you need to be admin or account holder):

1. Access **Certificate Identifiers & Profiles** through the menu.  
   Then go to **All** **Identifiers** and search for the application by filtering through your Apple Bundle Identifier.  
   Verify that your app is marked as "Enable as a primary App ID".  
   `[imagen omitida: wiki id 44480]``[imagen omitida: wiki id 44481]`
2. Create a new identifier of type "Services IDs"  
     
   `[imagen omitida: wiki id 44482]`  
   `[imagen omitida: wiki id 44495]`
3. Enter an identifier name that is similar to the "Apple Bundle Identifier" (for easy identification) and a description. Check "Sign In with Apple" and click on the "Configure" button.  
     
   `[imagen omitida: wiki id 44496]`
4. In the "Primary App ID" combo select your app (check that the Apple "Bundle Identifier" matches yours).  
     
   `[imagen omitida: wiki id 44497]`  
     
   In Domains section enter the domain of the application. If the domain was not previously verified for the Apple Development Team, it is necessary to verify it. The instructions to do so are on the same screen (via apple-developer-domain-association.txt file). For more information, see the [Apple documentation](https://help.apple.com/developer-account/#/dev1c0e25352) on this topic.
5. `[imagen omitida: wiki id 44498]`  
     
   In callback URL configure the following:  
     
   **<URLbase>/<web app>/oauth/gam/callback**  
     
   Next, press Continue button. In the screen "Register a Services ID" that is displayed, press the "Register" button.  
     
   `[imagen omitida: wiki id 44499]`  
     
   To verify the process, you can go to the Identifiers option again, filtering by service's ID.
6. Create and download an Apple private key.  
   For the menu, go to the item Keys.  
     
   `[imagen omitida: wiki id 44500]`  
     
   Give the key a name.  
     
   `[imagen omitida: wiki id 44501]`  
     
   Check Sign In with Apple and click the "Configure" button. In the Configure Key screen, you must select the "Primary App ID" created previously. Click on Save and then Continue.  
     
   `[imagen omitida: wiki id 44502]`  
     
   Click on Register. That leaves the private key available for a one-time download.  
   Save the "Key ID" of the created key:  
     
   `[imagen omitida: wiki id 44494]`
7. Generate client secrets for the web application (and Android) and the Apple native application using the [client\_secret.rb](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44503,,) program. It is a prerequisite of this step to have the gem "jwt" installed.  
   To install it, execute the following: **gem install jwt.**  
     
   Complete the fields in the "client\_secret.rb" program:  
     
   key\_file : the path to the private key file that was downloaded from the Apple website. It is recommended to have it in the same directory as the program.  
   key\_id : "Key ID" of the created key. It is obtained from the Apple website (step 5 of this document) or also from the original name of the downloaded private key file.  
   team\_id : ID of the development team (same value as in [Development Team ID property](https://wiki.genexus.com/commwiki/wiki?30100))  
   app\_client\_id : Apple application bundle identifier ([Apple Bundle Identifier property](https://wiki.genexus.com/commwiki/wiki?37617))  
   server\_client\_id: bundle identifier of the services ID type created previously (step 3 of this document).

```
     Example:

     key_file     = 'AuthKey_LAXKCWQ5D7.p8'
     key_id         = 'LAXKCWQ5D7'
     team_id     = 'xxxxxxxx'
     app_client_id         = 'com.genexus.testAppleSignIn'
     server_client_id     = 'com.genexus.TestAppleSignIn-server'
```

          Execute the program:

**ruby client\_secret.rb**

          The output of this step (Apple native token and Web token) will be the client secrets for the authentication types to be used in the GAM backend configuration.

### [GAM backend](#GAM+backend)

Depending on your app, native Apple or other (web or Android), the configuration of the Apple ID Authentication Type should be different.

#### [Authentication for Apple](#Authentication+for+Apple)

This type of authentication has to be used from the Apple app.

**Warning**: Sign In With Apple is available as of Apple 13 and above. For prior to Apple versions, you have to use it as if it was authenticating in Web or Android.

Configure the following:

Client Id: the value found at the [Apple Bundle Identifier property](https://wiki.genexus.com/commwiki/wiki?37617) of the Apple application.  
Client Secret: the one generated in the last step (6) with the name of "iOS native token."

`[imagen omitida: wiki id 44508]`

The code in GeneXus should be as follows:

```
Event 'Login Apple'
 composite
    &LoginExternalAdditionalParameters = new()
    &LoginExternalAdditionalParameters.AuthenticationTypeName = !"apple id sd"  //here the name of the Authentication Type you've defined.
    Actions.LoginExternal(GAMAuthenticationTypes.Apple, !"",!"",&LoginExternalAdditionalParameters)
    return
 Endcomposite
Endevent
```

#### [Authentication Type for Web and Android apps](#Authentication+Type+for+Web+and+Android+apps)

This type of authentication is the one that should be used from an Android app or from Web. It should also be used in Apple for versions older than Apple 13.  
  
Client Id: the bundle identifier of type Services ID created in step 3 above.  
Client Secret: The one generated in step 6 above with the name of "Web token."

`[imagen omitida: wiki id 44509]`

The login in Android apps is web:

`[imagen omitida: wiki id 52604]`

### [Availability](#Availability)

Since [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?43978,,)

### [Notes](#Notes)

* It is possible to get the full name and email from a user. Users can select the option to use a forwarder, instead of their real email.
* If you want the users to be impersonated to the GAM local users, configure [GAM Impersonation](https://wiki.genexus.com/commwiki/wiki?24241) to local in the GAM Apple Authentication type.
* The information of the user is sent only once for the application and the device. If you are testing and need the information to be sent again, you can go to this [link](https://appleid.apple.com/account/manage), then to "security," "manage," and in the popup window select your application to stop using Apple ID.  
  The next time the user logs in will be as the first one.


|  |
| --- |
| **Backlinks** |
| [Enable Sign in with Apple property](https://wiki.genexus.com/commwiki/wiki?44467) |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
