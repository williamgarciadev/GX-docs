---
title: "Time Only Compatibility property"
source_id: 44960
source_url: https://wiki.genexus.com/commwiki/wiki?44960
genexus_version: "18"
---

# Time Only Compatibility property

For mobile applications, set it to True if you want to store times always with UTC applicated.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Level:** Version

### [Description](#Description)

By setting this property to True, the Time and DateTime data types fields will vary on the devices depending on the TimeZone they have set. On the other hand, if this property is set to False, the time is stored and shown always with the original value.

**Note:** This property is not visible by default. To make it visible it is necessary to create a file named "TimeOnlyCompatibility.flag" in the GeneXus installation path, as the following image shows:

`[imagen omitida: wiki id 45264]`

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Rebuild All.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,).
