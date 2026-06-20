---
title: "How to configure In-App Billing in an Android application"
source_id: 21330
source_url: https://wiki.genexus.com/commwiki/wiki?21330
genexus_version: "18"
---

# How to configure In-App Billing in an Android application

GeneXus-generated [Native Mobile Generator](https://wiki.genexus.com/commwiki/wiki?14451) applications allow including the [In-App Purchase](https://wiki.genexus.com/commwiki/wiki?20003,,) functionality through the [StoreManager external object](https://wiki.genexus.com/commwiki/wiki?31320). However, some specific platform configurations need to be performed beforehand, in order to make the functionality work.

Below is a list of configuration requirements when working with Android applications. Follow these steps.

### [1. In the Google Play web site](#1.+In+the+Google+Play+web+site)

#### [Create the In-App Products for your application](#Create+the+In-App+Products+for+your+application)

Go to the [Google Play Developer Console](https://play.google.com/apps/publish/), search for your application and click to see the details. In the new page select the option *In-App Product*and then click *Add new product.*

`[imagen omitida: wiki id 21333]`

Select the type of the new In-App Product/Suscription and an identifier for it. This ID will be used later in GeneXus to work with the new product in the application.

`[imagen omitida: wiki id 21334]`

Then, you can edit more information for the recently created In-App Product, such as title and description in several languages, and pricing details. Finally, you need to *activate* the new product in order to be available for purchase in the application. To be able to activate the product is necessary to enter title and description in at least one language and at least one default price.

`[imagen omitida: wiki id 21335]`

The new In-App Product will not be available inmediately, it needs some time to be processed.

`[imagen omitida: wiki id 21336]`

### 

### [2. In GeneXus](#2.+In+GeneXus)

#### [Set generator properties](#Set+generator+properties)

In the Smart Devices generator properties, you will find the *In App Public Key property* in the "In Application Billing" group inside the "Android Specific" group.

`[imagen omitida: wiki id 33833]`

The value for "In App Public Key" property can be found in the [Google Play Developer Console](https://play.google.com/apps/publish/), in the *Services & APIs* section for your application.

`[imagen omitida: wiki id 21338]`

### [Notes](#Notes)

Google requires a Google Play Developer Console account and a Google Payments Merchant account. Use this [link](https://support.google.com/googleplay/android-developer/table/3539140?hl=en) as a reference when registering an application to view the locations supported.


|  |
| --- |
| **Backlinks** |
| [In-App Purchase Sample - Classified Ads](https://wiki.genexus.com/commwiki/wiki?20010) | [In-App Purchase Sample - My Kitchen](https://wiki.genexus.com/commwiki/wiki?20021) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |
| [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) | [StoreManager external object](https://wiki.genexus.com/commwiki/wiki?31320) | [Use Huawei In App Billing property](https://wiki.genexus.com/commwiki/wiki?47543) |

---
