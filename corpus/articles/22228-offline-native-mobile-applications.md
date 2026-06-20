---
title: "Offline Native Mobile Applications"
source_id: 22228
source_url: https://wiki.genexus.com/commwiki/wiki?22228
genexus_version: "18"
---

# Offline Native Mobile Applications

GeneXus offers the possibility to generate [Offline Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?22237) in addition to Online Apps.

Applications of this type help to deal with common situations like sales, events, or any other scenarios of limited or no Internet connectivity. They allow executing **database****transactions** even if the device has no connectivity.

As a result, GeneXus generates mobile applications that can run online, offline, or in a mixed way.

Generating an offline application involves creating a local database in the device and generating the corresponding programs in native code for each platform (Java for Android, Objective-C for iOS, etc) as stated in [Offline Native Mobile Applications Generation](https://wiki.genexus.com/commwiki/wiki?22262).

### [Getting started](#Getting+started)

Start by [creating your first offline application](https://wiki.genexus.com/commwiki/wiki?20249) now!

To learn more about offline Native Mobile applications, read the document [Offline Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?22237). If you, as a developer, are interested in knowing how GeneXus generates offline Native Mobile applications, read [Offline Native Mobile Applications Generation](https://wiki.genexus.com/commwiki/wiki?22262).

### [Success Stories and Showcases](#Success+Stories+and+Showcases)

* [Conaprole and Hexa - Offline app for Sales activities](http://www.genexus.com/news/read-news/dairy-producer-cooperative-co-na-pro-le-leads-the-way-in-the-use-of-genexus-tilos-offline-features-thanks-to-the-consultancy-firm-hexa?en) (Montevideo, Uruguay)
* [Catarinense Distribuidora gana agilidade nas vendas](http://www.genexus.com/imprensa/leer-noticia/catarinense-distribuidora-ganha-agilidade-nas-vendas-com-aplicativo-movel-criado-em-genexus?pt) (Santa Catarina, Brazil)
* [InfoModulus desenvolve sistema móvel para força de vendas on-line e off-line com GeneXus](http://www.genexus.com/imprensa/leer-noticia/infomodulus?pt ) (Santa Catarina, Brazil)
* [Metro DF 2.0 first iOS Offline App](http://mcrispino.blogspot.com/2013/06/metro-mexico-df-20-primer-aplicacion.html) -  [Metro DF app on Apple Store](https://itunes.apple.com/hk/app/metro-mexico-df/id529815225?mt=8) (Mexico City, Mexico)
* [GX23 Meeting App](https://www.genexus.com/en/meetings/meeting2013/gx23-apps)

#### [Metro DF Offline App in action](#Metro+DF+Offline+App+in+action)


* [Background](https://wiki.genexus.com/commwiki/wiki?22237)
  + [Scenarios](https://wiki.genexus.com/commwiki/wiki?22507)
    - [Point of Sales scenario](https://wiki.genexus.com/commwiki/wiki?23673) (local processing)
    - [Events App scenario](https://wiki.genexus.com/commwiki/wiki?23775) (apps with preloaded data)
    - [Survey](https://wiki.genexus.com/commwiki/wiki?24355,,) (create your own surveys)
  + [Applications architecture](https://wiki.genexus.com/commwiki/wiki?22221)
    - [Advanced concepts](https://wiki.genexus.com/commwiki/wiki?25536)
  + [The Data Synchronization Problem](https://wiki.genexus.com/commwiki/wiki?22240)
    - [Automatically generated identifiers synching conflicts](https://wiki.genexus.com/commwiki/wiki?23543)
* [Applications Generation](https://wiki.genexus.com/commwiki/wiki?22262)
  + [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911)
    - [HowTo: Use the Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?23558)
  + [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509)
    - [Table selection](https://wiki.genexus.com/commwiki/wiki?23561)
    - [Events](https://wiki.genexus.com/commwiki/wiki?23566)
    - [Conditions](https://wiki.genexus.com/commwiki/wiki?23570)
    - [Navigation reports](https://wiki.genexus.com/commwiki/wiki?23568)
    - [Properties](https://wiki.genexus.com/commwiki/wiki?25196)
    - [Reorganizations](https://wiki.genexus.com/commwiki/wiki?27121)
  + [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269)
    - Data Reception
      * [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223)
        + [Automatic Offline Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22267)
      * [Minimum Time Between Receives property](https://wiki.genexus.com/commwiki/wiki?22224)
      * [Data Receive Granularity property](https://wiki.genexus.com/commwiki/wiki?23541)
    - Data Sending
      * [Send Changes property](https://wiki.genexus.com/commwiki/wiki?23392,,)
      * [Synchronization by Chunks](https://wiki.genexus.com/commwiki/wiki?42733)
    - [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602)
      * [Receive method](https://wiki.genexus.com/commwiki/wiki?23603)
      * [ServerStatus method](https://wiki.genexus.com/commwiki/wiki?25839)
      * [Send method](https://wiki.genexus.com/commwiki/wiki?23604)
      * [ResetOfflineDatabase method](https://wiki.genexus.com/commwiki/wiki?29785)
      * [SetSendCheckpoint method](https://wiki.genexus.com/commwiki/wiki?42735)
      * [HowTo: Use the Synchronization API](https://wiki.genexus.com/commwiki/wiki?23605)
      * [Synchronization External Object](https://wiki.genexus.com/commwiki/wiki?43255,,)
    - [Coding your Data Synchronization programs](https://wiki.genexus.com/commwiki/wiki?22266)
      * [Manual Synchronization Code Sample](https://wiki.genexus.com/commwiki/wiki?22543)
      * [Best Practices for Manual Synchronization](https://wiki.genexus.com/commwiki/wiki?22276)
    - [Network API](https://wiki.genexus.com/commwiki/wiki?31310)
    - [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341)
    - [Error handling in Synchronization.Send() operations](https://wiki.genexus.com/commwiki/wiki?25454)
    - [Download content in Offline applications property](https://wiki.genexus.com/commwiki/wiki?40907)
  + [Backup and restore](https://wiki.genexus.com/commwiki/wiki?45171)
  + [HowTo: Create offline mobile applications with a preloaded database](https://wiki.genexus.com/commwiki/wiki?22298)
* [My First Offline App](https://wiki.genexus.com/commwiki/wiki?20249)
* Samples
  + [Sales](https://wiki.genexus.com/commwiki/wiki?23672)
  + [Survey](https://wiki.genexus.com/commwiki/wiki?24355,,)
* [Online into Offline](https://wiki.genexus.com/commwiki/wiki?24591)
  + Security considerations
    - [Offline Native Mobile applications using GAM](https://wiki.genexus.com/commwiki/wiki?23400)
* [Common Issues](https://wiki.genexus.com/commwiki/wiki?20287)
* [Software Requirements](https://wiki.genexus.com/commwiki/wiki?22259)

---
