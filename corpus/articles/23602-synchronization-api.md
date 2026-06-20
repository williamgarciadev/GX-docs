---
title: "Synchronization API"
source_id: 23602
source_url: https://wiki.genexus.com/commwiki/wiki?23602
genexus_version: "18"
---

# Synchronization API

The synchronization API makes it easier to call the generated synchronization programs for Offline applications in order to make the synchronization between the device and the web server whenever the developer wants to.

### [Methods](#Methods)

|  |  |
| --- | --- |
| [ServerStatus](https://wiki.genexus.com/commwiki/wiki?25839) | Determines the server status. |
| [Receive](https://wiki.genexus.com/commwiki/wiki?23603) | Receives in the device all the changes made in the server. |
| [Send](https://wiki.genexus.com/commwiki/wiki?23604) | Sends the pending modifications to the application server in order to submit the changes. |
| [ResetOfflineDatabase](https://wiki.genexus.com/commwiki/wiki?29785) | It returns the local database (offline) content to its initial state. That means:   * restoring the [preloaded database](https://wiki.genexus.com/commwiki/wiki?22298) if it exists, or * executing a Create Database to empty database tables. |
| [SetSendCheckpoint](https://wiki.genexus.com/commwiki/wiki?42735) | Set checkpoints in the pending events in order to allow [batch synchronization](https://wiki.genexus.com/commwiki/wiki?42733) |

### [Samples](#Samples)

```
Event ‘Do Receive’
    Synchronization.Receive()
EndEvent
```

### [Considerations](#Considerations)

If using the Synchronization API make sure not to set the [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223) to the "Never" value, it could generate strange errors when using the API.

The UI could display the following error:

```
Synchronization.Send Error 3
```

Internally the error could be

```
{"error":{"code":"0","message":"Invalid Synchronizer SDOfflineDatabase"}}{"EventResults":[]}"}}
```

where *SDOfflineDatabase* refers to the associated [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509).

### [Availability](#Availability)

SetSendCheckpoint method is available as from [GeneXus 16 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,).

### [See Also](#See+Also)

[HowTo: Use the Synchronization API](https://wiki.genexus.com/commwiki/wiki?23605)


|  |
| --- |
| **Backlinks** |
| [Coding your Data Synchronization programs](https://wiki.genexus.com/commwiki/wiki?22266) | [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223) | [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) |
| [HowTo: Use the Synchronization API](https://wiki.genexus.com/commwiki/wiki?23605) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [OfflineEventReplicator procedure](https://wiki.genexus.com/commwiki/wiki?26218) | [Synchronization by Chunks](https://wiki.genexus.com/commwiki/wiki?42733) |
| [Synchronization.Receive method](https://wiki.genexus.com/commwiki/wiki?23603) | [Synchronization.ResetOfflineDatabase method](https://wiki.genexus.com/commwiki/wiki?29785) | [Synchronization.Send method](https://wiki.genexus.com/commwiki/wiki?23604) | [Synchronization.ServerStatus method](https://wiki.genexus.com/commwiki/wiki?25839) |
| [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) |

---
