---
title: "Data Receive Granularity property"
source_id: 23541
source_url: https://wiki.genexus.com/commwiki/wiki?23541
genexus_version: "18"
---

# Data Receive Granularity property

Indicates how data is synchronized from the server to the device in Offline Native Mobile applications.

### [Values](#Values)

|  |  |
| --- | --- |
| **By Row** | Default value. Indicates that the synchronization is made row by row. There are two alternatives to this mechanism (refer to the Description section). |
| **By Table** | Indicates that the synchronization is made by table. |

### [Scope](#Scope)

**Objects:** Offline Database  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

Since the addition of Offline Native Mobile Applications in GeneXus, there have been two different algorithms for synchronizing data from the server to the devices: **synchronization by** **table** and **synchronization by row**.

The **synchronization by table** algorithm is straightforward: on the server-side, a hash of the table is computed and compared with the hash sent by the device. If they match, there is nothing to synchronize. If they don’t, the whole table is sent to the device and there, it replaces the previous content.

The **synchronization by row** algorithm requires some further explanation. Without going into much detail, if the table has changed (table hashes don’t match), the changed rows are computed (inserted, updated, and deleted) and sent to the device to be processed. This is the default behavior and we'll refer to it as **synchronization by hash**, but there exists a second variant of the synchronization by row algorithm that uses a timestamp instead of hashes for computing the differences. We'll call this last alternative **synchronization by timestamp** which is defined on a per-table basis by configuring the [Logically Deleted Attribute property](https://wiki.genexus.com/commwiki/wiki?37091) and the [Last Modified Date Time Attribute property](https://wiki.genexus.com/commwiki/wiki?37092).

Further explanation of these alternatives is discussed in [Offline Native Mobile synchronization granularity alternatives](https://wiki.genexus.com/commwiki/wiki?37109) article.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [See Also](#See+Also)

* [Advanced Concepts of Offline Applications architecture](https://wiki.genexus.com/commwiki/wiki?25536)
* [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509)
* [Offline Native Mobile synchronization granularity alternatives](https://wiki.genexus.com/commwiki/wiki?37109)


|  |
| --- |
| **Backlinks** |
| [Advanced Concepts of Offline Applications architecture](https://wiki.genexus.com/commwiki/wiki?25536) | [Automatic Offline Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22267) | [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) |
| [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [Last Modified Date Time Attribute property](https://wiki.genexus.com/commwiki/wiki?37092) | [Minimum Time Between Table Purges property](https://wiki.genexus.com/commwiki/wiki?31160) |
| [Category:Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) | [Offline Database Object properties](https://wiki.genexus.com/commwiki/wiki?25196) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [Offline Native Mobile synchronization granularity alternatives](https://wiki.genexus.com/commwiki/wiki?37109) |

---
