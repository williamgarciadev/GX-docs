---
title: "External utilities used by GeneXus generated Android applications"
source_id: 25098
source_url: https://wiki.genexus.com/commwiki/wiki?25098
genexus_version: "18"
---

# External utilities used by GeneXus generated Android applications

In Android, packing just the minimum necessary classes is of great importance for two main reasons:

* The Dalvik Virtual Machine establishes a maximum of 64 thousand Java methods for each indexed file. Since the final application package is composed of a big index of all the classes and resources, each dependency adds to this count.
* The final application size. For very simple applications, it may cause concern for users if they see that the application occupies a lot more space than they expected for no apparent reason.

As explained in the [External utilities used by GeneXus generated Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?25094) document, it is possible to split the dependencies into necessary and optional dependencies.

**Note**: In Android projects, external dependencies could be either AAR libraries, Project libraries, or JAR libraries.

### [Necessary dependencies](#Necessary+dependencies)

#### [AAR libraries](#AAR+libraries)

| Name | License Type | Usage |
| --- | --- | --- |
| AndroidX Libraries | [Apache License 2.0](https://github.com/androidx/androidx/blob/androidx-main/LICENSE.txt) | [Include Android Jetpack libraries](https://developer.android.com/jetpack/androidx) |
| Google Play Services Base | [Android SDK Licence](https://developer.android.com/sdk/terms.html) | Common Google services |
| Gson | Apache License 2.0 | To convert Java Objects into their JSON representation |
| OkHttp | [Apache License 2.0](https://github.com/square/okhttp/blob/master/LICENSE.txt) | Http for modern applications network |

#### [Jar libraries](#Jar+libraries)

| Name | License Type | Usage |
| --- | --- | --- |
| SqlDroid | Eclipse Public License 1.0 | JDBC driver for SQLite databases |
| YouTube Player API | Apache License 2.0 | Incorporate video playback functionality into your Android applications |

### [Optional Dependencies](#Optional+Dependencies)

#### [Project libraries](#Project+libraries)

| Name | License Type | Usage |
| --- | --- | --- |
| MPAndroidChart | [Apache License 2.0](https://github.com/PhilJay/MPAndroidChart/blob/master/LICENSE) | Chart controls |
| Android Billing Library | Apache License 2.0 | In-app purchases |
| ViewPagerIndicator | Apache License 2.0 | Shows current and count of pages for the "SD Paged Grid" control |
| Spinner | Apache License 2.0 | For DateTime pickers and SDWheels |
| Facebook | Apache License 2.0 | "Facebook" External Object |
| Twitter4j | Apache License 2.0 | "Twitter" External Object |
| Baidu Maps |  | Android Maps API for Baidu maps |
| Gaode Maps |  | Android Maps API for AutoNavi maps |
| [SQLCipher](https://wiki.genexus.com/commwiki/wiki?35632,,) | [BSD-style Licence](https://www.zetetic.net/sqlcipher/license/) | [Offline Database encryption](https://wiki.genexus.com/commwiki/wiki?35539) |
| iText 5.x | [Commercial or AGPL License](https://kb.itextpdf.com/home/it5kb/faq/is-itext-java-library-free-of-charge-or-are-there-any-fees-to-be-paid) | [PDF Reports](https://wiki.genexus.com/commwiki/wiki?13531) |
| Google Admob Ads | [Google Developers Site Terms of Service](https://developers.google.com/site-terms) | Advertising |
| Google Analytics | [Android SDK Licence](https://developer.android.com/sdk/terms.html) | Google Analytics |
| Lottie | [MIT License](https://github.com/airbnb/lottie/blob/master/LICENSE) | Animation using Lottie |
| Firebase | [Apache License 2.0](https://github.com/firebase/firebase-android-sdk/blob/master/LICENSE) | Firebase Analytics, Crashlytics, MLKit, Remote Config. |
| FlexBox | [Apache License 2.0](https://github.com/google/flexbox-layout/blob/main/LICENSE) | Flex Layout |
| Google Play Services | [Android SDK Licence](https://developer.android.com/sdk/terms.html) | Google Maps and Location services |
| Huawei HMS | Apache License 2.0 | Huawei generator |
| MapBox | [BSD 2-Clause "Simplified" License](https://github.com/mapbox/mapbox-android/blob/master/LICENSE) | Maps for MapBox |
| OneSignal | [Apache License 2.0](https://github.com/OneSignal/OneSignal-Android-SDK/blob/main/LICENSE) | Notification with OneSignal provider. |
| Jpush | [MIT License](https://github.com/jpush/jpush-docs/blob/master/LICENSE) | Notification with JPush provider. |

### [See also](#See+also)

* [External utilities used by GeneXus generated Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?25094)
* [External utilities used by Genexus generated iOS applications](https://wiki.genexus.com/commwiki/wiki?25150)


|  |
| --- |
| **Backlinks** |
| [Encrypt Offline Database property](https://wiki.genexus.com/commwiki/wiki?35539) | [External utilities used by Genexus generated iOS applications](https://wiki.genexus.com/commwiki/wiki?25150) | [External utilities used by GeneXus generated Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?25094) |
| [Use PDF Reports property](https://wiki.genexus.com/commwiki/wiki?42887) |

---
