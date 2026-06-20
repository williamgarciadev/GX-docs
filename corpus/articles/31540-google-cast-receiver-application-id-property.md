---
title: "Google Cast Receiver Application Id property"
source_id: 31540
source_url: https://wiki.genexus.com/commwiki/wiki?31540
genexus_version: "18"
---

# Google Cast Receiver Application Id property

Enables media casting by using Google services.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

This property allows you to enable Google Cast support for media playback (audio in background, images, or videos), whose value must be the application identifier that runs on the [Google Cast receiver](https://developers.google.com/cast/docs/receiver_apps) device when casting from the application that has the property set.

### [How does it work?](#How+does+it+work%3F)

When you set this property, the app is considered as a *sender*, showing the cast icon in the top right corner when a cast device is detected, and the end user can share media content with a *receiver* (e.g. Chromecast device connected to a TV).

`[imagen omitida: wiki id 31541]`

`[imagen omitida: wiki id 31561]`

### [What is the Receiver Application Identifier?](#What+is+the+Receiver+Application+Identifier%3F)

The *cast architecture* has two main components:

* **Sender application** - The application that shares its content with the cast device.
* **Receiver application**- The application hosted on the cast device that receives content from the sender application.

`[imagen omitida: wiki id 31542]`

The receiver is a particular web application executed in the cast device. Unlike a typical web application, the receiver is not identified by a URL. It uses a unique identifier provided by Android through its [developer console](https://console.developers.google.com/apis?project=one-proyect) when the application is registered.

There are three kinds of receivers:

* [Default Media Receiver](https://developers.google.com/cast/docs/receiver_apps#default) - Provided by Google. It does not allow customizing its aspect and is used for testing purposes. Its identifier is CC1AD845.
* [Styled Media Receiver](https://developers.google.com/cast/docs/receiver_apps#Styled) - It is a flexible version of the previous one, but only allows customizing the UI through CSS.
* [Custom Receiver](https://developers.google.com/cast/docs/receiver_apps#Custom) - It allows customizing every aspect of the receiver using HTML, JavaScript, and CSS, and even allows you to create your protocol to communicate with the cast device.

For the last two receivers, you must get the identifier once you have [registered](http://developers.google.com/cast/docs/registration#publish) it in the developer console.  
Then you can enter this AppID in the GeneXusproperty, and your application is available to communicate with it.

### [Notes](#Notes)

* For *testing purposes*, you can use the default media receiver application ID: '**CC1AD845**'.
* Styled Media and Custom receivers must be developed using the tools mentioned above. [See examples](https://github.com/googlecast) and [How to register it](https://developers.google.com/cast/docs/registration#RegisterApp).
* It can be helpful to follow [this diagram](https://developers.google.com/cast/docs/receiver_apps#choose-a-receiver) to choose which receiver is more convenient for your application.
* At the moment, it is only available for [Android platform](https://wiki.genexus.com/commwiki/wiki?14453) and [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) (including the [Audio Player](https://wiki.genexus.com/commwiki/wiki?31046)). It is highly recommended to set the *ContentType*and *StreamType*fields of the MediaItem SDT for the adequate management of resources by the receiver app and the cast device.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Availability](#Availability)

This property is available since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?27605,,).

### [See Also](#See+Also)

* [Google Developer - Sender Applications](https://developers.google.com/cast/docs/sender_apps)
* [Google Developer - Receiver Applications](https://developers.google.com/cast/docs/receiver_apps)
* [Google Cast Github - Receiver Applications examples](https://github.com/googlecast)


|  |
| --- |
| **Backlinks** |
| [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
