---
title: "Hour format property"
source_id: 39440
source_url: https://wiki.genexus.com/commwiki/wiki?39440
genexus_version: "18"
---

# Hour format property

Sets which divisions of an hour to use (hour, minutes, seconds, milliseconds, or only some of them).

### [Values](#Values)

|  |  |
| --- | --- |
| **Hour and minutes (hh:mm)** | Accepts and displays hours and minutes. |
| **Hour, minutes and seconds (hh:mm:ss)** | Accepts and displays hours, minutes, and seconds. |
| **Hour, minutes, seconds and milliseconds (hh:mm:ss.fff)** | Accepts and displays hours, minutes, seconds, and milliseconds. |
| **Only hour (hh)** | Accepts and displays only hours. |

### [Scope](#Scope)

**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Domain](https://wiki.genexus.com/commwiki/wiki?7221), [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [Description](#Description)

This property is available for attributes and variables based on the [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) to set which divisions of an hour to use.

In addition, depending on the value set in the [Precision property](https://wiki.genexus.com/commwiki/wiki?39306) for the attribute/variable based on the [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370), the **Hour format** property will offer different values.

If the [Precision property](https://wiki.genexus.com/commwiki/wiki?39306) = Seconds, the **Hour format** property will offer the values:

* Only hour (hh)
* Hour and minutes (hh:mm)
* Hour, minutes and seconds (hh:mm:ss)

On the other hand, if the [Precision property](https://wiki.genexus.com/commwiki/wiki?39306) = Milliseconds, the **Hour format** property will offer the value:

* Hour, minutes, seconds and milliseconds (hh:mm:ss:fff)

**Note:** It is possible to handle milliseconds as from [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,). So, this property starts offering the "Hour, minutes, seconds and milliseconds (hh:mm:ss.fff)" value in the same version.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Precision property](https://wiki.genexus.com/commwiki/wiki?39306)


|  |
| --- |
| **Backlinks** |
| [Category:Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802) | [Date data type](https://wiki.genexus.com/commwiki/wiki?7373) | [Date data type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55760) |
| [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) | [Picture Properties Group](https://wiki.genexus.com/commwiki/wiki?6800) | [Precision property](https://wiki.genexus.com/commwiki/wiki?39306) |

---
