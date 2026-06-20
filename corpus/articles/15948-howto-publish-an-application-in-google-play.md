---
title: "HowTo: Publish an application in Google Play"
source_id: 15948
source_url: https://wiki.genexus.com/commwiki/wiki?15948
genexus_version: "18"
---

# HowTo: Publish an application in Google Play

This document is intended to guide you in the process of publishing (for the first time or update) your Android applications on Google Play.

### [Prerequisites](#Prerequisites)

* Get (if not already have one) a Google Play Developer account. See [Google Play Developer site](https://play.google.com/apps/publish/) for details.
* **Alert**:  Google Play requires that new apps target at least Android 11 (API level 30) from August 2021, and that app updates target Android 11 from November 2021. This implies that you must use [GeneXus 17 upgrade 2](https://wiki.genexus.com/commwiki/wiki?47418,,) or higher to be able to deploy to Google Play. More information in [Play Console Help](https://support.google.com/googleplay/android-developer/answer/9859152#zippy=%2Ctarget-api-level-requirements-for-play-console) site*.*

### [Step 1. Signing the Application](#Step+1.+Signing+the+Application)

Every application that will be published in Google Play must be signed, and after being uploaded it will only be updated if it is signed with the same signature. Refer to [How to obtain a signature](https://wiki.genexus.com/commwiki/wiki?15948) section of this document.

**Warning**: GeneXus signs the application with a **debug signature** for testing purposes, that will not be accepted by Google if the application isn't signed with this key: See Notes section.

### [Step 2. Test your application thoroughly](#Step+2.+Test+your+application+thoroughly)

It's highly important to test the application before uploading it to the store. The validation process of Google takes a while, if you need a second emergency update, consider that the end users do not have the application fixed instantaneously.

### [Step 3. Choose the icon and images that you will use for the publication](#Step+3.+Choose+the+icon+and+images+that+you+will+use+for+the+publication)

You will need (not counting optional)

**Screenshots**:  
**- Format**: PNG or JPEG (no alpha) of 24 bits.  
**- Resolutions**: 320 x 480, 480 x 800, 480 x 854, 1280 x 720 or 1280 x 800 pixels  
**- Considerations**: Full screen, no borders.

**Application icon**:  
**- Format**: PNG of 32 bits or JPEG image  
**- Resolutions**: 512 x 512 pixels  
**- Size**: 1024 KB

### [Step 4. Publish](#Step+4.+Publish)

At this point, you are ready to upload the application to Google Play.

Login to [Google Play Developer site](https://play.google.com/apps/publish/). Once you are there:

* If you are **creating a new application:**  
  Click *Create Application* button to access a wizard to create a new application.  
  See [here](https://support.google.com/googleplay/android-developer/answer/113469?hl=en) for detailed information.  
    
  `[imagen omitida: wiki id 37604]`
* If you are **updating an existing application:**  
  Click on your application title, and the detail information will be displayed (e.g. our Sales Order app).  
  On the left-side menu, go to *Release management > App releases > Manage production*.  
  Once there, click on *Create release* button.  
    
  `[imagen omitida: wiki id 37605]`  
    
  Finally, upload the new APK file by clicking on *Browse Files* button. You should note that:
  + The **Version Code** or **Version Name** property must have a higher value than the previous version.
  + The keystore used to sign the application has to be the same as the previous version.

### [How to obtain a signature](#How+to+obtain+a+signature)

**1.** Create an account in [Google Play](https://play.google.com/apps/publish/signup/) (reference price at June/2011: registration fee $25.00).

**2.** Create a "Key Store file" for signature the application's packets with the following command. It is distributed with the JDK on the */bin* directory.  
> keytool -genkey -v -keystore **my\_release.keystore** -alias **my\_alias\_name** **-****keyalg** **RSA** -keysize 2048 -validity 10000

|  |  |  |
| --- | --- | --- |
| **Where:** |  |  |
|  | **-genkey** | Generate a key pair (public and private keys). |
|  | **-v** | Enable verbose output. |
|  | **-keystore** | The name for the keystore containing the private key. |
|  | **-alias** | An alias for the key. Only the first eight characters of the alias are used. |
|  | **-keyalg** | The encryption algorithm to use when generating the key. Must be RSA for GeneXus applications. |
|  | **-keysize** | The size of each generated key (bits). If not supplied, Keytool uses a default key size of 1024 bits. In general, it is recommended to use a key size of 2048 bits or higher. |
|  | **-validity** | The validity period for the key, in days. A value of 10000 or greater is recommended. |

**Note**: if you sign your application using your keystore, and it uses SD Map control, you have to follow the steps mentioned in: [HowTo: Get an API Key from Google](https://wiki.genexus.com/commwiki/wiki?19055).

**3.** Complete all information requested. You **must save the password** for the next step.

**4.** At [Main object level](https://wiki.genexus.com/commwiki/wiki?17817) set the [Compilation Mode property](https://wiki.genexus.com/commwiki/wiki?35447) in "Distribution" and complete the [Application Signing properties](https://wiki.genexus.com/commwiki/wiki?23328) in the generator properties:

* **[Key Store File](https://wiki.genexus.com/commwiki/wiki?19108):** The filepath to "**my\_release.keystore**" file in the keytool command.
* **Store Password**: That's the one you set (you are asked for it ) while you run the keytool command.
* **Key Password**: That's the one you set (you are asked for it ) while you run the keytool command.

See the image below:  
  
`[imagen omitida: wiki id 33132]`

### [Notes](#Notes)

* There isn't any relation between the signature and the developer registered in the Google Play. Any developer can publish any APK; the signature is not important.
* Once the APK was published with a user, only this user can upload new versions of the same application. However, this user may assign the application to another, then, this one can upload new versions.
* GeneXus 15 (since U2) signs the APKs file automatically with the Android's default debug-signature. On every build, the IDE alerts of this state with a warning message until the developer signs it with an own signature.  
    
  ========== Android Compilation started ==========  
  The generated application will be signed using a default key. Note that you  
  should change this key (in SmartDevices > Android Specific > Application Signing) before releasing it.  
    
  This mechanism forces the developers to sign their applications when they publish it (on production) but allowing an easy prototyping of it.  
  **If the application is not signed with a custom certificate, Google Play does not publish it in the store**.
* For those developers who already have applications in production with the previous default settings (i.e. the \*.apk file signed with Artech credentials) must set its properties manually with legacy values.

  |  |  |  |
  | --- | --- | --- |
  | **Property** | **Default** | **Legacy (as of GeneXus 15 Upgrade 3)** |
  | **Key Store File** | *C:\path\_to\_GeneXus\_installation\Android\debug.keystore* | *C:\path\_to\_GeneXus\_installation\Android\legacy.keystore* |
  | **Key Alias** | androiddebugkey | *alias\_name* |
  | **Store Password** | android | *artech* |
  | **Key Password** | android | *artech* |

### [See Also](#See+Also)

[Android Developer - Icon Design Guidelines](https://developer.android.com/guide/practices/ui_guidelines/icon_design)[Google Support - Graphic Assets for your Application](https://support.google.com/googleplay/android-developer/answer/1078870)  
[Google Support - Upload an app](https://support.google.com/googleplay/android-developer/answer/113469?hl=en)  
[Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Prototyping features and Deployment of applications for Smart Devices](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/prototyping-features-and-deployment-of-applications-for-smart-devices?p=3694)


|  |
| --- |
| **Backlinks** |
| [Android Application Signing](https://wiki.genexus.com/commwiki/wiki?23328) | [Android Package Name property](https://wiki.genexus.com/commwiki/wiki?17814) | [Category:Android platform](https://wiki.genexus.com/commwiki/wiki?14453) |
| [Android specific properties](https://wiki.genexus.com/commwiki/wiki?31449) | [HowTo: Get an API Key from Google](https://wiki.genexus.com/commwiki/wiki?19055) | [HowTo: Publish an application in Google Play](https://wiki.genexus.com/commwiki/wiki?15948) | [HowTo: Version Your Native Mobile Application](https://wiki.genexus.com/commwiki/wiki?17223) |
| [Key Alias property](https://wiki.genexus.com/commwiki/wiki?19112) | [Key Store File property](https://wiki.genexus.com/commwiki/wiki?19108) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
