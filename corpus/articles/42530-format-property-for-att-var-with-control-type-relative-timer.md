---
title: "Format property (for att/var with Control Type=Relative Timer)"
source_id: 42530
source_url: https://wiki.genexus.com/commwiki/wiki?42530
genexus_version: "18"
---

# Format property (for att/var with Control Type=Relative Timer)

Sets the style with which the time interval will be displayed.

### [Values](#Values)

|  |  |
| --- | --- |
| **Abbreviated** | Displays the time interval with numbers next to the initial of each time unit. Example: 59m 59s. |
| **Full** | Displays the time interval with numbers next to the name of each time unit. Example: 59 minutes, 59 seconds. |
| **Positional** | Displays the time interval with numbers separated by ":" (colon). Example: 0:59:59. Default value of the property. |
| **Short** | Displays the time interval with numbers next to the abbreviation of each time unit. Example: 59 min, 59 sec. |
| **Spelled Out** | Displays the time interval next to the name of each time unit. Example: fifty-nine minutes, fifty-nine seconds. |

### [Scope](#Scope)

**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** Attribute/Variable (Control Type: [Relative Timer](https://wiki.genexus.com/commwiki/wiki?42490))

### [Description](#Description)

The Format property offers these values for attributes/variables based on the data types: Date, DateTime, Time, and if their [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) is set to "Relative Timer."

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

`[imagen omitida: wiki id 42503]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Build All.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,).


|  |
| --- |
| **Backlinks** |
| [Relative Timer control](https://wiki.genexus.com/commwiki/wiki?42490) |

---
