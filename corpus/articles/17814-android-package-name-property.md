---
title: "Android Package Name property"
source_id: 17814
source_url: https://wiki.genexus.com/commwiki/wiki?17814
genexus_version: "18"
---

# Android Package Name property

Specifies the package name of the application, and it serves as a unique identifier for the application, both for the Android device and Google Play.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

Android Package is **required** for all Android apps. It is mostly used for internal purposes in the Android ecosystem and identifies your application (for example, in the Google PlayStore's link: <https://play.google.com/store/apps/details?id=com.genexus.genexusmeeting>).

The rules to name it are similar to those used for a Java package name ([View details](http://developer.android.com/studio/build/application-id.html)). The package name should be unique and may contain uppercase or lowercase letters ('A' through 'Z'), numbers, and underscores ('\_'). However, individual package name parts may only start with letters. For more information: [Android Developers](http://developer.android.com/guide/topics/manifest/manifest-element.html#package) - [Java Package](http://en.wikipedia.org/wiki/Java_package#Package_naming_conventions).

By default, GeneXus sets this property with the following value:  
com.artech.<KB\_name>.<Main\_object\_name>

### [Considerations](#Considerations)

* Once the app is published, you **will never be able to change this property’s value**. The only way to change it is to publish the app again as if it were a different app than before.
* You should change the default value in order to avoid conflicts with other developers, as the package name must be unique. It’s usually the name of an Internet domain you (or your company) own, in reverse, plus the application name (for example, com.example.myapp).
* This value can have repercussions in the apps’ [ASO](https://en.wikipedia.org/wiki/App_store_optimization).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [See Also](#See+Also)

* [HowTo: Publish an application in Google Play](https://wiki.genexus.com/commwiki/wiki?15948)
* [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817)


|  |
| --- |
| **Backlinks** |
| [Android specific properties](https://wiki.genexus.com/commwiki/wiki?31449) | [ClientInformation external object](https://wiki.genexus.com/commwiki/wiki?31271) | [Firebase Analytics Android File property](https://wiki.genexus.com/commwiki/wiki?41573) |
| [GAM - WeChat Authentication type](https://wiki.genexus.com/commwiki/wiki?45037) | [HowTo: Create a Mini App on the Mini App Center](https://wiki.genexus.com/commwiki/wiki?53317) | [HowTo: Get an API Key from Google](https://wiki.genexus.com/commwiki/wiki?19055) | [HowTo: Look for offline database files](https://wiki.genexus.com/commwiki/wiki?23815) |
| [HowTo: Register an application to use JPush services](https://wiki.genexus.com/commwiki/wiki?37021) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) | [Update URL property](https://wiki.genexus.com/commwiki/wiki?37262) |

---
