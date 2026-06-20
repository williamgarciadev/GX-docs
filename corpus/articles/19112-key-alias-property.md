---
title: "Key Alias property"
source_id: 19112
source_url: https://wiki.genexus.com/commwiki/wiki?19112
genexus_version: "18"
---

# Key Alias property

The Android system requires that all installed applications be digitally signed with a certificate whose private key is held by the application's developer.

### [Scope](#Scope)

**Platforms:** Smart Devices(Android)

### [Description](#Description)

When you build an [apk](https://wiki.genexus.com/commwiki/wiki?20972) (Android binary file) you use your own private key to sign your application. If you don't have a private key, you can use the Keytool utility (available with the JDK used to compile) to create one for you.

When you compile your application in release mode, the Android build tools use your private key along with the Jarsigner utility to sign your application's .[apk](https://wiki.genexus.com/commwiki/wiki?20972) file. Because the certificate and private key you use are your own, you will have to provide the password for the keystore and key alias.

This alias is needed to get the key of the certificate.

To get the Key Alias from the keystore you can execute this command line, the keytool utility can be found in the jdk\bin folder.

```
keytool -list -keystore your_keystore_name
```

#### [Values](#Values)

A valid KeyStore key entry containing a private key and corresponding public key certificate chain.

`[imagen omitida: wiki id 19111]`

### [See Also](#See+Also)

[Signing your applications](http://developer.android.com/guide/publishing/app-signing.html)  
[HowTo: Publish an application in Google Play](https://wiki.genexus.com/commwiki/wiki?15948)  
[Compile and sign your Android app by command line](https://wiki.genexus.com/commwiki/wiki?16492,,)


|  |
| --- |
| **Backlinks** |
| [Android Application Signing](https://wiki.genexus.com/commwiki/wiki?23328) | [HowTo: Get an API Key from Google](https://wiki.genexus.com/commwiki/wiki?19055) | [Key Store File property](https://wiki.genexus.com/commwiki/wiki?19108) |
| [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
