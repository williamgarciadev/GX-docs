---
title: "Units property"
source_id: 42251
source_url: https://wiki.genexus.com/commwiki/wiki?42251
genexus_version: "18"
---

# Units property

Time units used to display the time interval.

### [Description](#Description)

It allows choosing a range of units to display.

|  |  |
| --- | --- |
| Second | s |
| Minute | m |
| Hour | h |
| Day | d |
| Week | w |
| Month | M |
| Year | Y |

For example, if you have an event that happened 1 day, 7 hours, 40 minutes and 15 seconds ago, this value can be shown in the following ways:

|  |  |
| --- | --- |
| **Units property** | **Result displayed on screen** |
| smhd | 1 day, 7 hr, 40 min, 15 sec |
| mh | 31 hr, 40 min |
| md | 1 day, 40 min |

Note that in the case of example 2 the value in seconds is truncated, and even though the hours value is higher than 24 hours (one day), the value continues to increase.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, Build a main object.

### [Scope](#Scope)

**Platforms:** Smart Devices(IOS)  
**Controls:** Attribute/Variable (Control Type: [SD Relative Timer](https://wiki.genexus.com/commwiki/wiki?42490))

### [See Also](#See+Also)

[Relative Timer control](https://wiki.genexus.com/commwiki/wiki?42490)


|  |
| --- |
| **Backlinks** |
| [Relative Timer control](https://wiki.genexus.com/commwiki/wiki?42490) |

---
