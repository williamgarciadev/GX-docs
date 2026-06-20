---
title: "How to configure In-App Purchases in an iOS application"
source_id: 20043
source_url: https://wiki.genexus.com/commwiki/wiki?20043
genexus_version: "18"
---

# How to configure In-App Purchases in an iOS application

GeneXus-generated Smart Device applications allow including the [In-App Purchase](https://wiki.genexus.com/commwiki/wiki?20003,,) functionality through the [Store API](https://wiki.genexus.com/commwiki/wiki?20004,,). However, some specific platform configurations need to be performed beforehand, in order to make the functionality work.

Below is a list of configuration requirements when working with iOS applications.

1. Enable In-App Purchases for the App ID

In the [iOS Provisioning Portal](https://developer.apple.com/ios/manage/overview/index.action) inside the [iOS Dev Center](https://developer.apple.com/devcenter/ios/index.action), check that In-App Purchases are enabled for the application App ID.

`[imagen omitida: wiki id 20047]`

2. Create your application in the [iTunes Connect](https://itunesconnect.apple.com) portal. The Bundle ID configured for the application must have In-App Purchase enabled, as mentioned in the previous step; this value should be configured in the [iOS Bundle Identifier](https://wiki.genexus.com/commwiki/wiki?17380) property in the Smart Device application main object in GeneXus. Next, select the option labeled Manage In-App Purchases.

`[imagen omitida: wiki id 20048]`

3. Indicate all the In-App Purchases products that will be available for the application. You can add as many as you want using the "Create New" button. [iOS Store Kit Framework](https://developer.apple.com/reference/storekit) allows selecting five different kinds of products. In GeneXus applications, only Consumable and Non-Consumable products are supported for the moment (GeneXus X Evolution 2 Upgrade #2). Check the [iOS In-App Purchases documentation](https://developer.apple.com/reference/storekit) and iTunes Connect documentation for details on each product type and how to define them.

`[imagen omitida: wiki id 20049]`

4. The last step is to Submit the In-App Purchases products with the application binaries for review. In the main page of the application in [iTunes Connect](http://itunesconnect.apple.com), go to the Current Version section, which should be set to **Prepare for Upload** status, and select "View Details". In the page displayed you will find an In-App Purchases section.

`[imagen omitida: wiki id 20050]`

Selecting the "Edit" option will display a list of all In-App Purchases products, for you to choose those that will be submitted for review with the application version.

`[imagen omitida: wiki id 20051]`  
  
`[imagen omitida: wiki id 20052]`


|  |
| --- |
| **Backlinks** |
| [In-App Purchase Sample - Classified Ads](https://wiki.genexus.com/commwiki/wiki?20010) | [In-App Purchase Sample - My Kitchen](https://wiki.genexus.com/commwiki/wiki?20021) |

---
