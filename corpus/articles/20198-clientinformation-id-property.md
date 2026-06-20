---
title: "ClientInformation.Id property"
source_id: 20198
source_url: https://wiki.genexus.com/commwiki/wiki?20198
genexus_version: "18"
---

# ClientInformation.Id property

The Id property of the [ClientInformation external object](https://wiki.genexus.com/commwiki/wiki?31271) returns an acceptable client identifier in both Web and Native Mobile platforms.

## [Native Mobile apps](#Native+Mobile+apps)

In some Native Mobile apps, it is important to identify the device being used. Some examples of this are as follows:

* For security
  + Transactions on a certain Bank account may only be made from a certain device.
  + Certain Users may only use certain devices during predetermined hours.
* For promotions
  + When installing two or more applications of a certain Company on a certain device, you may get a discount.
* For calculating use statistics.

It would be best to know the equivalent of the device’s serial number or MAC Address, a feature that uniquely identifies it, but it’s not so easy.

Even though all devices include some kind of unique identification that is accessed through software, for privacy reasons it will not be available for use, and access to it might even be forbidden (Apple).

The ClientInformation.Id property provided in the [ClientInformation external object](https://wiki.genexus.com/commwiki/wiki?31271) counteracts this situation with acceptable device identification mechanisms whose implementations have a common base and variations for the different platforms.

The value of the ClientInformation.Id is:

* Universally unique.

The same criteria of a GUID (UUID) applies.

Two devices may return the same value of ClientInformation.Id in any of the following situations:

* In Apple, when a device contains the restored data of another device.
* In Android, rooted devices may change the value returned, losing the guarantee of unicity.

* Stable (on all platforms) throughout the life of an application (from the moment it is installed until it is uninstalled).
* Each device has a unique value of ClientInformation.Id.

In Android, any GeneXus application installed on a device will return the same value (see exception in Annex below).  
In Apple, the same device can return different values of ClientInformation.Id depending on the application (see Annex below).

In sum:

* Identifying a device (hardware) univocally is not among the best practices, and sometimes it is impossible.
* GeneXus provides an acceptable mechanism to identify devices that have platform variations.

## [Web Applications](#Web+Applications)

In the case of Web applications, the ClientInformation.Id property returns a user identifier that persists in all sessions unless the end user deletes the browser cookies. The ClientInformation.Id remains unchanged for the same application and browser because it's saved on a cookie with the maximum expiration date. It identifies the browser where the user accesses the application.

One use case is the following, where the user is identified using the ClientInformation.Id called in the Start Event of a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916). Then, the obtained ClientInformation.Id is stored in the database:

```
Event Start
    &clientId = ClientInformation.Id
    SaveClient(&clientId)              //SaveClient is a Procedure object defined in the KB.
Endevent
```

The SaveClient [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) is defined as follows:

```
Rules
Parm(&clientId);

Source
For each Clients
    delete
Endfor
New
  ClientId = &clientId
Endnew
```

After that, another Web Panel object uses the stored ClientId to send a [web notification](https://wiki.genexus.com/commwiki/wiki?22442) for that particular user.

In the Web Panel object that sends the notification, you get the ClientId saved in the database.

```
Event 'Notify'
  for each Clients
      &ClientId = ClientId
  endfor 
  &NotificationInfo.Id= &ClientId         //&NotificationInfo is based on the Server.Socket external object
  &NotificationInfo.Message= &MyMessage
  &NotificationInfo.NotifyClient(&ClientId, &NotificationInfo)  //The NotifyClient method is sending the message only to the involved client/user.
Endevent
```

Download [ClientInformation.Id Sample](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?33475,,).

## [Annexes](#Annexes)

### [Android](#Android)

The value of ClientInformation.Id is a GUID generated from the [device’s internal identifier](http://developer.android.com/reference/android/provider/Settings.Secure.html#ANDROID_ID). This guarantees, at least, that its value will be the same between two applications installed on the same device during the life of the device.

The known exceptions are:

* In the case of a factory reset, the ID may change.
* On a rooted device, it is possible to change the ID.

Since you stored the GUID generated, the applications installed before the rooting will return an ID value while those installed after the rooting will probably return a different one. However, the value returned by the same application will not change.

* The devices from certain manufacturers have an error in Android 2.2 that makes them all return the same ANDROID\_ID.

This number is known; in this case, you generate a random GUID (per application).

See this response in Stack Overflow for a detailed explanation. The proposed solution is practically the same as the one you are using, except that you do not consider the IMEI for generating the GUID (because to do that you would need special permits).

### [Apple](#Apple)

The value of ClientInformation.Id is a GUID calculated at the time of installing the first GX application on the device. The value is stored in what is known as Keychain and maintained even when the application that created it is uninstalled and installed again.

In Apple, every application has its own Keychain, although it is possible to share the same one among several applications. As for ClientInformation.Id, a shared Keychain means that all applications with the same Keychain will return the same value of ClientInformation.Id for a given device. Without a shared Keychain, each application installed on a device will return a different value of ClientInformation.Id.

The value of ClientInformation.Id may change when a factory reset is done or when the firmware is restored (reinstalls the Operating System), and if NO security copy is restored. An example is when the device is passed on to a different person (when sold, for example).

Several devices can have the same ClientInformation.Id value when a security copy is restored on several devices. This case may occur when a device is replaced with a newer model and a security copy of the old device is restored in the new one.

#### [**How to obtain the same value of ClientInformation.Id for several applications from the same provider**](#How+to+obtain+the+same+value+of+ClientInformation.Id+for+several+applications+from+the+same+provider)

To achieve this, you need to make an implementation change. In addition, the GX user must be aware that it is possible to control this behavior. Which applications are shared and which are not will be up to the user.

The unique identifier in an Apple application (Application ID) consists of two parts: <Bundle Seed ID>.<Bundle Identifier>. The Bundle Seed ID is a chain with 10 unique characters; it is unique in the entire App Store and generated by Apple. The Bundle Identifier is a chain of characters that must be unique among the same provider’s applications, and in GX it is configured with a property with the same name in the Main.

For two (or more) applications from the same provider to return the same value of ClientInformation.Id on the same device, they must have the same Bundle Seed ID value.

Because the Bundle Seed Id may not be changed after an application has been published, it is VERY IMPORTANT to be aware of how this works. Fortunately, when a new App ID is created on the Apple site (developer.apple.com) by default the Bundle Seed ID is shared by all apps (see combo at "Use Team ID"):

`[imagen omitida: wiki id 20200]`


|  |
| --- |
| **Backlinks** |
| [ClientInformation external object](https://wiki.genexus.com/commwiki/wiki?31271) | [HowTo: Receiving and processing a notification message from an external app](https://wiki.genexus.com/commwiki/wiki?33633) | [KB:PlantCare - ECommerce Sample](https://wiki.genexus.com/commwiki/wiki?50476) |
| [KB:PlantCare and SweetWorld - ECommerce Sample (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?56139) | [Server.Socket external object](https://wiki.genexus.com/commwiki/wiki?22442) |

---
