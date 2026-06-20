---
title: "HowTo: Use the Synchronization API"
source_id: 23605
source_url: https://wiki.genexus.com/commwiki/wiki?23605
genexus_version: "18"
---

# HowTo: Use the Synchronization API

The [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602) is a very useful tool that makes synchronization between the Device and the Server extremely easy. You do **not** have to worry about how to apply changes on the server, or how to receive data changes from the server and apply them on the device.  
The [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602) has two methods: [Receive](https://wiki.genexus.com/commwiki/wiki?23603) and [Send](https://wiki.genexus.com/commwiki/wiki?23604), that makes that hard work **automatically**.

It is very important to note that the [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602) can be called **at any time**, even if the developer has set any value for the [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223) or [Send Changes property](https://wiki.genexus.com/commwiki/wiki?23392,,), both methods Receive and Send are still going to work.

This document explains how to create a simple offline application calling the synchronization programs **manually**, using the [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602) to synchronize the device with the server.

**Note**: If you are interested on calling the synchronization programs automatically, then you should check out the [Automatic Offline Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22267) document.

### [How it works](#How+it+works)

Take the "Simple Version Manual" version of the [Sales](https://wiki.genexus.com/commwiki/wiki?23672) sample as an example. In this application's version, the application needs to be synchronized whenever the user wants to.

The first step to do that is to configure the [Offline Database Object properties](https://wiki.genexus.com/commwiki/wiki?25196). As in this sample application it is necessary to manage the synchronization manually, it is needed to set the [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223)  and the [Send Changes property](https://wiki.genexus.com/commwiki/wiki?23392,,) to "Manual" as shown in the following image:

`[imagen omitida: wiki id 54107]`

The second step is to create a new [Panel](https://wiki.genexus.com/commwiki/wiki?24829). In this example it is called “SynchPanel”, and adds 2 buttons in the layout like shown in the image below:

`[imagen omitida: wiki id 54108]`

Finally, each button is going to have an event where the Synchronization API is called:

```
Event 'Receive'
    Synchronization.Receive()
Endevent

Event 'Send'
    Synchronization.Send()
Endevent
```

By doing just that, it is possible to synchronize data whenever the user wants to. When tapping the "Receive" button, the data from the server is going to be synchronized into the device, and when tapping the Send button, all local changes are submitted to the server in order to apply changes.

### [Limitations](#Limitations)

The [Synchronization.Send method](https://wiki.genexus.com/commwiki/wiki?23604) sends data to the server in a single request, that may be a problem if connectivity is very unstable and the amount of data to send is big. In that case, consider executing it when a stable connection is available or [Coding your Data Synchronization programs](https://wiki.genexus.com/commwiki/wiki?22266).

### [See Also](#See+Also)

[Sales](https://wiki.genexus.com/commwiki/wiki?23672) sample  
[Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602)  
[Synchronization.Receive method](https://wiki.genexus.com/commwiki/wiki?23603)  
[Synchronization.Send method](https://wiki.genexus.com/commwiki/wiki?23604)  
[Synchronization.ResetOfflineDatabase method](https://wiki.genexus.com/commwiki/wiki?29785)  
[Coding your Data Synchronization programs](https://wiki.genexus.com/commwiki/wiki?22266)


|  |
| --- |
| **Backlinks** |
| [Coding your Data Synchronization programs](https://wiki.genexus.com/commwiki/wiki?22266) | [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223) | [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) |
| [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602) | [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) |

---
