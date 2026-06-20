---
title: "Key Store File property"
source_id: 19108
source_url: https://wiki.genexus.com/commwiki/wiki?19108
genexus_version: "18"
---

# Key Store File property

Specifies the key store file that will be used to sign an application that will be published in Google Play.

### [Scope](#Scope)

**Platforms:** Smart Devices(Android)

### [Description](#Description)

When you build in release mode you use your own private key to sign your application. If you don't have a private key, you can use the Keytool utility (JDK *keytool* utility with the *-keystore* parameter) to create one for you; check [here](https://wiki.genexus.com/commwiki/wiki?15948) for a sample. When you compile your application in release mode, the build tools use your private key along with the Jarsigner utility to sign your application's .apk file. Because the Certificate and private key you use are your own, you will have to provide the password for the keystore and [key alias](https://wiki.genexus.com/commwiki/wiki?19112).

#### [About the Android certificate](#About+the+Android+certificate)

* The Android system requires that all installed applications be digitally signed with a certificate whose private key is held by the application's developer.
* The Android system uses the certificate as a means of identifying the author of an application and establishing trust relationships between applications.
* The certificate is not used to control which applications the user can install.
* The certificate does not need to be signed by a certificate authority: it is perfectly allowable, and typical, for Android applications to use self-signed certificates.

### [Samples](#Samples)

```
C:\Users\<UserName>\Documents\AndroidKeyStore\GeneXusLabsKey.keystore
```

`[imagen omitida: wiki id 19111]`

### [See Also](#See+Also)

[Signing Your Applications](http://developer.android.com/tools/publishing/app-signing.html)


|  |
| --- |
| **Backlinks** |
| [Android Application Signing](https://wiki.genexus.com/commwiki/wiki?23328) | [HowTo: Get an API Key from Google](https://wiki.genexus.com/commwiki/wiki?19055) | [HowTo: Publish an application in Google Play](https://wiki.genexus.com/commwiki/wiki?15948) |
| [HowTo: Register a Facebook App](https://wiki.genexus.com/commwiki/wiki?19399) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
