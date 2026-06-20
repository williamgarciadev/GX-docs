---
title: "HowTo: Configure Push Notifications in Apple Applications (GeneXus 18 Upgrade 2 or prior)"
source_id: 54517
source_url: https://wiki.genexus.com/commwiki/wiki?54517
genexus_version: "18"
---

# HowTo: Configure Push Notifications in Apple Applications (GeneXus 18 Upgrade 2 or prior)

**Warning**: As Apple deprecated (November, 2020) and removed (March 31, 2021) the legacy binary protocol of the Push Notification Service, Notification Provider is the only method available to integrate Push Notifications in a GeneXus-generated Apple application.

This is a step by step guide to set up push notifications for an Apple Application. If you need general information on how to use push notifications please see [Push Notifications in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19945).

### [Requirements](#Requirements)

Push Notifications in GeneXus applications are only available in compiled applications. This means that in the Mobile generator preferences, you have to set the [Execution Type property](https://wiki.genexus.com/commwiki/wiki?18658)  (in the Apple Specific group) with a value different from "*Knowledge Base Navigator (Device)*" and insert the connection information of the MAC OS computer where the application will be built.

Also, some actions are required when developing an Apple application that uses the [Apple Push Notifications Service](https://wiki.genexus.com/commwiki/wiki?35452,,).

You need to:

1. [Create](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/establishing_a_certificate-based_connection_to_apns)[a SSL](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/establishing_a_certificate-based_connection_to_apns) [Certificate](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/establishing_a_certificate-based_connection_to_apns) to be able to use the service.
2. [Export it](https://support.apple.com/en-is/guide/keychain-access/import-and-export-keychain-items-kyca35961/mac) from the Keychain Access in the MAC.
3. [Create an appropriate Provisioning Profile](https://wiki.genexus.com/commwiki/wiki?17442) for the application.

### [Sender configuration](#Sender+configuration)

Notifications can be enabled for [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829) and [Work With](https://wiki.genexus.com/commwiki/wiki?15974) objects with the [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) set to True. This can be done by setting the [Enable Notifications property](https://wiki.genexus.com/commwiki/wiki?49799) to True, in the Main object properties group. When doing this, a new group of properties is available called Notifications with the following properties:

* #### [**iOS PKCS12 Certificate and iOS PKCS12 Password**](#iOS+PKCS12+Certificate+and+iOS+PKCS12+Password)

In these properties, you have to indicate the file name and password of the SSL Certificate that was previously generated and exported in order to work with the Apple Push Notifications Service. **This file has to be located in the private directory under the Web directory of the environment folder.**

The best way to do this is by selecting the p12 file from the property's file selector (...). In this way, the file will be imported into the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and will automatically deploy to the private directory in the next build process.

If a [Notification Provider](https://wiki.genexus.com/commwiki/wiki?33670) is used, there is no need to set these two properties.

* #### [**iOS use Sandbox Server**](#iOS+use+Sandbox+Server)

Apple Push Notification Service has two different working environments, which require a different SSL Certificate for each of them, Sandbox environment (or development, using for testing purposes) and Production environment (or distribution). In this property, you have to indicate which environment we are going to work with in the Apple Push Notifications Service.

If a [Notification Provider](https://wiki.genexus.com/commwiki/wiki?33670) is used, there is no need to set this property either.

* #### [**iOS Silent Notifications allowed**](#iOS+Silent+Notifications+allowed)
* #### [**iOS Device Registration Mode**](#iOS+Device+Registration+Mode)

Finally, you need to consider the *iOS Bundle Identifier* property value, which is very important here. The default value will be *com.artech.<MainObjectName>*, but you need to change it (if necessary) for the Bundle Identifier configured in the App ID associated with the SSL Certificate used.

Since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,) this configuration can be done at runtime using the [NotificationsConfiguration external object](https://wiki.genexus.com/commwiki/wiki?39411,,).

### [Ports](#Ports)

Check if the ports indicated in this document are open: <https://support.apple.com/en-is/HT203609>

### [Intermediate Step](#Intermediate+Step)

From now on, every time you execute a GeneXus application which has Push Notifications enabled in a Mobile Device, the [Devices Registration Service](https://wiki.genexus.com/commwiki/wiki?18149) is executed in order to register and store the device information to be used in the future to send messages (Push Notifications) to the device.

### [How are notifications sent?](#How+are+notifications+sent%3F)

Notifications are sent as shown in this Sample: [Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687)

### [Application execution](#Application+execution)

Like any iOS applications which use the Apple Push Notifications Service, the first time you execute the GeneXus-generated iOS application, a message is shown asking if you want to enable the notifications. Regardless of the option that you select in this message, the application notifications will be available to be configured later in the iOS Notifications Center.

**Note**: Notifications don't work if the client application does not give permission.
