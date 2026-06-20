---
title: "Center property"
source_id: 42220
source_url: https://wiki.genexus.com/commwiki/wiki?42220
genexus_version: "18"
---

# Center property

Indicates the criteria to center the map at startup.

### [Values](#Values)

|  |  |
| --- | --- |
| **Custom** | A specific location (coordinate) is used to center the map. |
| **Default** | The map center is determined by the points loaded in it. |
| **My location** | The map is centered in the current device location. |

### [Description](#Description)

Allows indicating how the map is centered at startup.

* When *My Location* is chosen, the map is centered in the current location of the device.
* If *Custom* is chosen, an [Attribute/Variable](https://wiki.genexus.com/commwiki/wiki?6911) of [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644) or [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) must be selected where the center location is stored. The [Custom Center Attribute property](https://wiki.genexus.com/commwiki/wiki?42221) or [Custom Center Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42222) are used for this purpose.
* When *Default* is chosen, the map center is determined by the points loaded in the map and the value in [Initial Zoom property](https://wiki.genexus.com/commwiki/wiki?42217).
  + If Initial Zoom is set to Nearest point visible, the point in the middle of the region determined by the device location and the nearest point is used to center the map.
  + If Initial Zoom is set to Show All Points, the point in the middle of the region determined by all the points is used to center the map.
  + In other cases, the center of the map is not determined.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [Scope](#Scope)

**Objects:** Panel for Smart Devices, Work With for Smart Devices  
**Platforms:** Smart Devices(Android, IOS)  
**Controls:** Grid (Control Type: [SD Maps](https://wiki.genexus.com/commwiki/wiki?15309))

### [See Also](#See+Also)

[Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309)  
[Initial Zoom property](https://wiki.genexus.com/commwiki/wiki?42217)


|  |
| --- |
| **Backlinks** |
| [Animations Layer property](https://wiki.genexus.com/commwiki/wiki?43487) | [Custom Center Attribute property](https://wiki.genexus.com/commwiki/wiki?42221) | [Custom Center Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42222) |
| [Initial Zoom Radius Attribute property](https://wiki.genexus.com/commwiki/wiki?42218) | [Initial Zoom Radius Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42219) | [Maps Control Type Properties](https://wiki.genexus.com/commwiki/wiki?54092) |

---
