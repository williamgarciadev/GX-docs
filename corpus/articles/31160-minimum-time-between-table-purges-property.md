---
title: "Minimum Time Between Table Purges property"
source_id: 31160
source_url: https://wiki.genexus.com/commwiki/wiki?31160
genexus_version: "18"
---

# Minimum Time Between Table Purges property

For [Offline Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?22237) using GeneXus generated synchronization programs, this property determinates the time between calls to the internal maintenance programs to purge the synchronization tables ( 'GXPARAMETERS', 'GXDEVICERESULT' and 'GXRESULTROW').

### [Values](#Values)

|  |  |
| --- | --- |
| **Value (in seconds)** | Minimum time lapse the app waits between calls for the Maintenance programs - by default 3600 seconds |

### [Description](#Description)

The user can set the minimum time interval that needs to pass before the maintenance programs should be called in order to avoid that the Synchronization Tables increment its size. For example, if the value is 1 hour (3.600 seconds), then the Synchronization Tables will be "cleaned" in each hour. And if the [Minimum Time Between Receives property](https://wiki.genexus.com/commwiki/wiki?22224) is greater than 1 hour, then this process will be triggered each time the synchronization process is done.

This property is available when the [Data Receive Granularity](https://wiki.genexus.com/commwiki/wiki?23541) property has "By Row" value.

### [How To Apply Changes](#How+To+Apply+Changes)

Run of the Main Object for Smart Devices is enough to apply this changes.

### [Availability](#Availability)

As from [GeneXus Salto Beta 3](https://wiki.genexus.com/commwiki/wiki?30609,,)

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) |
| **Platforms** | Android, Apple iOS |
| **Generators** | .Net, Java |

### [See Also](#See+Also)

* [Automatic Offline Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22267)
* [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269)


|  |
| --- |
| **Backlinks** |
| [Advanced Concepts of Offline Applications architecture](https://wiki.genexus.com/commwiki/wiki?25536) | [Offline Data backup and restore](https://wiki.genexus.com/commwiki/wiki?45171) |

---
