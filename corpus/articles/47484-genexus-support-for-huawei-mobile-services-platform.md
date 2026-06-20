---
title: "GeneXus support for Huawei Mobile Services Platform"
source_id: 47484
source_url: https://wiki.genexus.com/commwiki/wiki?47484
genexus_version: "18"
---

# GeneXus support for Huawei Mobile Services Platform

This article explains how to generate for the [Huawei Platform](https://wiki.genexus.com/commwiki/wiki?47546,,) (HMS for short). That is, how to generate for Huawei devices that do not support [Google Play Services](https://developer.android.com/distribute/play-services).

## [How to enable generation for HMS](#How+to+enable+generation+for+HMS)

Applications generated for HMS are Android applications, so the first step to enable HMS generation is to enable the [Generate Android property](https://wiki.genexus.com/commwiki/wiki?18654).

Next, you need to enable the [Generate Huawei property](https://wiki.genexus.com/commwiki/wiki?47485).

When you set this, GeneXus is going to generate two editions of the Android application, one classic Android application under the *mobile\Android* folder and an additional one under the *mobile\Huawei* folder.

`[imagen omitida: wiki id 47550]`

## [How to test an application generated for Huawei](#How+to+test+an+application+generated+for+Huawei)

When the [Generate Huawei property](https://wiki.genexus.com/commwiki/wiki?47485) is set to *True*, you can select *Huawei* as the main prototyping platform by setting [Main Platform property](https://wiki.genexus.com/commwiki/wiki?18657) = Huawei.

In this way, you can switch between Android or Huawei prototypes.

`[imagen omitida: wiki id 47551]`

## [How to enable different services for a Huawei application](#How+to+enable+different+services+for+a+Huawei+application)

First, you need to register at [Huawei Developers](https://developer.huawei.com/consumer/en/doc/start/introduction-0000001053446472) to get a [HuaweiID](https://id1.huawei.com/AMW/portal/homepage.html). Once validated, you can access all the services provided for developing, testing, distributing, and monetizing your app. Depending on your organization's size, you can consider creating a [Team account](https://developer.huawei.com/consumer/en/Team-account/).

Then, register and create your [app](https://developer.huawei.com/consumer/en/doc/distribution/app/agc-create_app) with [AppGallery Connect](https://developer.huawei.com/consumer/en/agconnect), enable the desired services, and follow the configuration steps. In general, the selected APIs can be checked in the *My projects* > *Project settings* > *Manage APIs* section.

Finally, there is a new set of properties in each main object to give information to the generator about which services are going to be used in the generated Huawei application.

* [Use Huawei Analytics property](https://wiki.genexus.com/commwiki/wiki?47541)(1)
* [Use Huawei Notifications property](https://wiki.genexus.com/commwiki/wiki?47542)(1)
* [Huawei Services File property](https://wiki.genexus.com/commwiki/wiki?47545)(1)
* [Use Huawei In App Billing property](https://wiki.genexus.com/commwiki/wiki?47543)(1)
* [Use Huawei Maps property](https://wiki.genexus.com/commwiki/wiki?48086)(2)

Thoroughly test your application and when ready go back to [AppGallery Connect](https://developer.huawei.com/consumer/en/agconnect) to upload the APK and release your application on the [AppGallery](https://appgallery.huawei.com/#/Featured).

(1) - Available since [GeneXus 17 upgrade 2](https://wiki.genexus.com/commwiki/wiki?47418,,)  
(2) - Available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,)

## [References](#References)

[Liga BBVA MX App Oficial](https://appgallery.huawei.com/#/app/C100975729) uses this feature and is already available at Huawei's AppGallery.
