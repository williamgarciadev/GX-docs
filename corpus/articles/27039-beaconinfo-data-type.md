---
title: "BeaconInfo Data Type"
source_id: 27039
source_url: https://wiki.genexus.com/commwiki/wiki?27039
genexus_version: "18"
---

# BeaconInfo Data Type

Each [Beacon](https://wiki.genexus.com/commwiki/wiki?27025) has several data that identifies it. In general they have a UUID for the Beacon and numeric values (major and minor) that can be set to the hardware by some specific software of the Beacon vendor.  
So, when you have several beacons each one should have a unique UUID and optionally you can set the values for the numeric values in order to give further information about the semantic position of the Beacon in the world.

This SDT is defined in order to identify a Beacon.

### [Fields](#Fields)

|  |  |  |
| --- | --- | --- |
| **Name** | **Type** | **Description** |
| UUID | GUID | The proximity ID of the beacon. |
| GroupId | Numeric(5,0) | Group Identifier (Major Id). |
| Id | Numeric(5,0) | Identifier within the GroupId (Minor Id). |


|  |
| --- |
| **Backlinks** |
| [Beacons external object](https://wiki.genexus.com/commwiki/wiki?27025) |
| [HowTo: Using Beacons](https://wiki.genexus.com/commwiki/wiki?27070) | [StartAsBeacon method](https://wiki.genexus.com/commwiki/wiki?27063) |

---
