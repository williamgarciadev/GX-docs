---
title: "Synchronization.Receive method"
source_id: 23603
source_url: https://wiki.genexus.com/commwiki/wiki?23603
genexus_version: "18"
---

# Synchronization.Receive method

### [Syntax](#Syntax)

&SynchResult = Synchronization**.Receive**()

**Where:**

&SynchResult is a Numeric variable.

### [Description](#Description)

This method receives in the device all the changes made in the server since last synchronization. When this method is executed the first time it tries to get all data from the server. Note that all received data is previously filtered in the server by appliyng the [Offline Database Object conditions](https://wiki.genexus.com/commwiki/wiki?23570).

**Note**: If this method is executed inside a [Composite](https://wiki.genexus.com/commwiki/wiki?17389) block and for some reason the data reception fails, the Composite block execution stops, which means all actions declarated after this method call are not being executed.

### [Type returned](#Type+returned)

Returns one of the following values, which in GeneXus are defined in the SynchronizationReceiveResult domain:

| Receive message code | Receive message | Receive message causes |
| --- | --- | --- |
| 0 | Receive OK. | Receive was successfully made. |
| 1 | Receive is not needed. | All data is already synchronized. |
| 2 | Application is not offline. | The application is trying to call the Synchronization programs from an Online panel. |
| 3 | Has pending events. | Can not perform a Receive if there are already pending events to send. Check the [Synchronization.Send method](https://wiki.genexus.com/commwiki/wiki?23604) for further learning. |
| 8 | Already Running. | A receive process is already running in the application. |
| 51 | Metadata error code received. Code: 1 | The device is sending an invalid or old version of the OfflineDatabase for the synchronization by row. |
| 52 | Metadata error code received. Code: 2 | The hashes sent to the server are invalid, so the server can not calculate the differences between the client tables and the server tables. |
| 53 | Metadata error code received. Code: 3 | The device is sending an invalid or old version of the OfflineDatabase. |
| 99 | Unknown error. | Unknown error. |

**Note**: Errors 51, 52, and 53 occur only in the server side, unlike the others which occur in the device.

### [Example](#Example)

An example of calling the Receive method when pressing a button:

```
Event "MyAction"
    &SynchResult = Synchronization.Receive()
EndEvent
```

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087) |
| **Platforms** | Android, Apple iOS |

### [Considerations](#Considerations)

For versions of GeneXus prior to [GeneXus X Evolution 3 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?26959,,), values returned by this method are defined like in the following table:

| Receive message code | Receive message |
| --- | --- |
| 0 | Receive OK. |
| 1 | Receive is not needed. |
| 2 | Application is not offline. |
| 3 | Has pending events. |
| 4 | Unknown error. |
| 5 | Metadata error code received. Code: 1 |
| 6 | Metadata error code received. Code: 2 |
| 7 | Metadata error code received. Code: 3 |

### [Availability](#Availability)

As from [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,)

### [See also](#See+also)

* [Synchronization.Send method](https://wiki.genexus.com/commwiki/wiki?23604)
* [Synchronization.ServerStatus method](https://wiki.genexus.com/commwiki/wiki?25839)
* [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602)


|  |
| --- |
| **Backlinks** |
| [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223) | [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) |
| [HowTo: Use the Synchronization API](https://wiki.genexus.com/commwiki/wiki?23605) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [Offline Native Mobile applications using GAM](https://wiki.genexus.com/commwiki/wiki?23400) | [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602) |
| [Synchronization.ResetOfflineDatabase method](https://wiki.genexus.com/commwiki/wiki?29785) | [Synchronization.Send method](https://wiki.genexus.com/commwiki/wiki?23604) | [Synchronization.ServerStatus method](https://wiki.genexus.com/commwiki/wiki?25839) |

---
