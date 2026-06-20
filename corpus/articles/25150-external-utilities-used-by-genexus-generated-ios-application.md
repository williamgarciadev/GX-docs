---
title: "External utilities used by Genexus generated iOS applications"
source_id: 25150
source_url: https://wiki.genexus.com/commwiki/wiki?25150
genexus_version: "18"
---

# External utilities used by Genexus generated iOS applications

As explained in the [External utilities used by GeneXus generated Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?25094) document, it is possible to split the dependencies into necessary and optional dependencies. However, unlike other platforms, the iOS flexible client framework packs all external utilities compiled in the binary file, so this documents lists all dependecies as "necessary".

### [Necessary dependencies](#Necessary+dependencies)

| **Name** | Licence | **Usage** |
| --- | --- | --- |
| AQGridView | [Licence terms](https://github.com/AlanQuatermain/AQGridView/blob/master/LICENSE) | Dashboard objects with property Control=Table |
| SDWebImage | [MIT](https://raw.github.com/rs/SDWebImage/master/LICENSE) | Image downloading throughout the flexible client |
| YAJL | [Licence terms](https://github.com/gabriel/yajl-objc/blob/master/LICENSE) | JSON parsing throughout the flexible client |
| SDNetworkActivityIndicator | [Licence terms](https://github.com/rs/SDNetworkActivityIndicator/blob/master/LICENSE) | Showing/hiding network activity indicator |
| Core Plot | [Licence terms](https://github.com/core-plot/core-plot/blob/master/License.txt) | SD Charts user control |
| PListCompiler | [BSD License](http://sourceforge.net/directory/license:bsd/) |  |
| KTPhotoBrowser | [MIT](https://github.com/kirbyt/KTPhotoBrowser/blob/master/LICENSE) | SD Image Gallery user control |
| DLStarRating | [Eclipse Public Licence](https://github.com/dlinsin/DLStarRating/blob/master/LICENSE.txt) | SD Star Rating user control |
| UIImageExtensions | [Licence terms](http://vocaro.com/trevor/blog/2009/10/12/resize-a-uiimage-the-right-way/) (at the bottom of the article) | Image resizing |
| ZipArchive | [MIT](https://github.com/ZipArchive/ZipArchive/blob/master/LICENSE.txt) | Handling of Zip files throughout the flexible client |
| AudioStreamer | No licence information | Audio streaming (AudioAPI external object) |
| ValueTrackingSlider | No licence information | SD Slider user control |
| FacebookSDK | [Apache Licence 2.0](https://github.com/facebook/facebook-ios-sdk/blob/master/LICENSE) | Facebook integration |
| Google Analytics | [Apache Licence 2.0](http://www.apache.org/licenses/LICENSE-2.0) | Google Analytics |
| [Twofish](http://en.wikipedia.org/wiki/Twofish) reference C implementation | No licence information | Encrypt64/Decrypt64 implementation |
| ios-deploy | [Licence terms](https://github.com/phonegap/ios-deploy/blob/master/LICENSE) | Execution on Device |
| [QBImagePicker](https://github.com/questbeat/QBImagePicker) | [MIT](https://github.com/questbeat/QBImagePicker/blob/master/LICENSE) | PhototLibraryAPI external object |
| fmdb | [MIT](https://github.com/mcrispino/fmdb/blob/master/LICENSE.txt) | SQLite wrapper for Objective-C, used to access the Offline database. |
| WKTParser | [MIT](https://github.com/alejandrofcarrera/WKTParser/blob/master/LICENSE) | WKT Parser for Geography data type handling. |
| OneSignal SDK | [Apache Licence 2.0](http://www.apache.org/licenses/LICENSE-2.0) | One Signal Notifications Provider |
| [OpenSSL](https://wiki.genexus.com/commwiki/wiki?35453,,) | [Apache Licence 2.0](http://www.apache.org/licenses/LICENSE-2.0) | In-App Purchases (StoreManager external object) |
| [SQLCipher](https://wiki.genexus.com/commwiki/wiki?35632,,) | [BSD-style Licence](https://www.zetetic.net/sqlcipher/license/) | [Offline Database encryption](https://wiki.genexus.com/commwiki/wiki?35539) |
| [Twitter Kit for iOS](https://wiki.genexus.com/commwiki/wiki?36780,,) | No licence information | [Twitter](https://wiki.genexus.com/commwiki/wiki?31335,,) and [Share](https://wiki.genexus.com/commwiki/wiki?29800) Exteral Objects (iOS 11 and above) |
| [Card.io](https://github.com/card-io/card.io-iOS-SDK) | [MIT](https://github.com/card-io/card.io-iOS-SDK/blob/master/LICENSE.md) | Scanning credit cards |
| WechatOpenSDK ([pod](https://cocoapods.org/pods/WechatOpenSDK)) | [Custom](https://mp.weixin.qq.com/) (as linked from CocoaPods) | Integration of WeChat services |
| YogaKit ([pod](https://cocoapods.org/pods/YogaKit)) | [MIT](https://github.com/facebook/yoga/blob/main/LICENSE) | Flex Grid & Flex Table |
| lottie-ios ([pod](https://cocoapods.org/pods/lottie-ios)) | [Apache 2.0](https://api.github.com/licenses/apache-2.0) | AnimationView user control |
| GoogleMaps ([pod](https://cocoapods.org/pods/GoogleMaps)) | Custom, see in CocoaPods | Google Maps |
| Google-Maps-iOS-Utils (pod) | [Apache 2.0](https://api.github.com/licenses/apache-2.0) | Google Maps |
| TrustKit ([pod](https://cocoapods.org/pods/TrustKit)) | [MIT](https://api.github.com/licenses/mit) | SSL Pinning |
| Google-Mobile-Ads-SDK ([pod](https://cocoapods.org/pods/Google-Mobile-Ads-SDK)) | [Custom](https://developers.google.com/ad-manager/mobile-ads-sdk) (as linked from CocoaPods) | Ads |
| Firebase/Analytics ([pod](https://cocoapods.org/pods/FirebaseAnalytics)) | [Custom](https://firebase.google.com/features/analytics/) (as linked from CocoaPods) | Firebase Analytics |
| Firebase/Crashlytics ([pod](https://cocoapods.org)) | [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0) | Firebase Crashlytics |
| Firebase/RemoteConfig ([pod](https://cocoapods.org/pods/FirebaseRemoteConfig)) | [Apache 2.0](https://api.github.com/licenses/apache-2.0) | Firebase RemoteConfig |
| JPush ([pod](https://cocoapods.org/pods/jpush)) | [Custom](http://www.jpush.cn/) (as linked from CocoaPods) | Notifications |
| MercadoPagoServicesV4 ([pod](https://cocoapods.org/pods/MercadoPagoServicesV4)) | [MIT](https://github.com/mercadopago/px-ios_services/blob/master/LICENSE) | Integration of Mercado Pago services |
| Smart-Display-SDK ([pod](https://cocoapods.org/pods/Smart-Display-SDK)) | No licence information | Ads |

### [See also](#See+also)

* [External utilities used by GeneXus generated Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?25094)
* [External utilities used by GeneXus generated Android applications](https://wiki.genexus.com/commwiki/wiki?25098)


|  |
| --- |
| **Backlinks** |
| [Encrypt Offline Database property](https://wiki.genexus.com/commwiki/wiki?35539) | [External utilities used by GeneXus generated Android applications](https://wiki.genexus.com/commwiki/wiki?25098) | [External utilities used by GeneXus generated Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?25094) |

---
