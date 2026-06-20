---
title: "Minimum Time Between Receives property"
source_id: 22224
source_url: https://wiki.genexus.com/commwiki/wiki?22224
genexus_version: "18"
---

# Minimum Time Between Receives property

Determines the time between calls to the synchronization programs.

### [Scope](#Scope)

**Objects:** Offline Database  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

This property applies to Offline Native Mobile applications with Automatic Offline Data Synchronization criteria. It determines the time between calls to the synchronization programs.

The user can set the minimum time interval before the application calls the synchronization's receive services.

The application only performs the Receive operation when the application starts, and only if the time defined by this property has elapsed.

#### [Values](#Values)

|  |  |
| --- | --- |
| **Value (in seconds)** | Minimum time-lapse between calls to the Synchronization.Receive programs by the app. |

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Run the main object.

### [See Also](#See+Also)

[Automatic Offline Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22267)  
[Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269)  
[Offline Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?22237)


|  |
| --- |
| **Backlinks** |
| [Automatic Offline Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22267) | [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223) | [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) |
| [Minimum Time Between Table Purges property](https://wiki.genexus.com/commwiki/wiki?31160) | [Offline Database Object properties](https://wiki.genexus.com/commwiki/wiki?25196) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |

---
