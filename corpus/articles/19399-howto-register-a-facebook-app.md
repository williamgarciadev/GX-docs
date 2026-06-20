---
title: "HowTo: Register a Facebook App"
source_id: 19399
source_url: https://wiki.genexus.com/commwiki/wiki?19399
genexus_version: "18"
---

# HowTo: Register a Facebook App

You must register the Facebook application to use the Facebook features offered by GeneXus in the [Native Mobile Generator](https://wiki.genexus.com/commwiki/wiki?14451).  
This document will show how to do this in a few steps.

### [Step 1: Registration and Validation](#Step+1%3A+Registration+and+Validation)

In the main screen of the Facebook Home Page go to the Developers Center.

`[imagen omitida: wiki id 19401]`

You will be requested to sign in with a valid Facebook Account.

In some cases, you may have to validate your account. The following link can be very helpful to complete this step: http://developers.facebook.com/blog/post/386/

### [Step 2: Create your application](#Step+2%3A+Create+your+application)

Once you have logged in to your Facebook developers home page with a valid Facebook developer account, click on the Apps button and then choose Create a New App.

`[imagen omitida: wiki id 19405]`

Complete the information requested about the App.

**Note**: Only providing a valid app Name is mandatory; any other information is optional.

`[imagen omitida: wiki id 19407]`

### [Step 3: Connect your Facebook app with your Native Mobile Application in GeneXus](#Step+3%3A+Connect+your+Facebook+app+with+your+Native+Mobile+Application+in+GeneXus)

The last step is to connect your Native Mobile application with the Facebook one. This has to be done in two places.

a- **In GeneXus:**

Copy the Facebook AppID value (in Facebook web site) to the Facebook App Id property of the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770), as shown in the figure.

`[imagen omitida: wiki id 23637]` `[imagen omitida: wiki id 19409]`

b- **In Facebook:**

Open your application and click on the Settings option. Now on the basics settings, add the platforms that you need by clicking the Add Platform button.

In case it is for
[Apple](https://wiki.genexus.com/commwiki/wiki?14917), you need to:

Enter, in the iOS **Bundle ID,** the value of the iOS Bundle Identifier property of your GeneXus' main object.

`[imagen omitida: wiki id 23638]`

`[imagen omitida: wiki id 19408]`

And in case it is for
[Android](https://wiki.genexus.com/commwiki/wiki?14453) you need:

The **package name** is on the Android Package Name property on the Android Group of the Main object.

`[imagen omitida: wiki id 23639]`

And the **key hash**.

**Note**: If you are signing the application with the default [keystore](https://wiki.genexus.com/commwiki/wiki?19108), the key hash is **qzImOU1ch6oucyE6hr8s9GbTgys=**

To get the key hash (if you are not using the default) you need to know:

* Where the keystore file is (in this example is "C:\my-release.keystore")
* The alias in keystore (in this case is "alias\_name")
* The path to keytool (in this case is "C:\OpenSSL-Win32\bin\keytool.exe")
* The path to openssl (in this case is "C:\OpenSSL-Win32\bin\openssl")
* The password to keystore (In this case is "artech")

With this, run this code in CMD:

```
"C:\Program Files\Java\jdk1.6.0_25\bin\keytool.exe" -exportcert -alias alias_name -keystore C:\my-release.keystore | C:\OpenSSL-Win32\bin\openssl sha1 -binary | C:\OpenSSL-Win32\bin\openssl base64>keyhash.txt
```

This will leave the key in a file called keyhash.txt.

`[imagen omitida: wiki id 21684]`

If you need to add "class name", this value is in the *AndroidManifest.xml*, it must be the class that contains the main action:

`[imagen omitida: wiki id 48589]`

#### [**Important**](#Important)

For testing purporses, you have to add Developer Roles to make tests on your application.

`[imagen omitida: wiki id 56215]`


|  |
| --- |
| **Backlinks** |
| [Facebook Button control](https://wiki.genexus.com/commwiki/wiki?31841) | [Facebook external object](https://wiki.genexus.com/commwiki/wiki?38432) | [GAM - Facebook Authentication Type](https://wiki.genexus.com/commwiki/wiki?29007) |
| [HowTo: Request data from Facebook using Graph API and Access Token](https://wiki.genexus.com/commwiki/wiki?38437) | [HowTo: Use Share Action for the Image Gallery](https://wiki.genexus.com/commwiki/wiki?19507) |

---
