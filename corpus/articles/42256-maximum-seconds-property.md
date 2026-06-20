---
title: "Maximum Seconds property"
source_id: 42256
source_url: https://wiki.genexus.com/commwiki/wiki?42256
genexus_version: "18"
---

# Maximum Seconds property

Sets a number of seconds such that when the counter becomes equal to or greater than that value, the text set in the Maximum Text property is displayed.

### [Scope](#Scope)

**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** Attribute/Variable (Control Type: [Relative Timer](https://wiki.genexus.com/commwiki/wiki?42490))

### [Description](#Description)

This property is only visible for [Panel](https://wiki.genexus.com/commwiki/wiki?24829) Attributes or Variables whose data type is [DateTime](https://wiki.genexus.com/commwiki/wiki?7370).

By setting a specific duration, this property triggers an event: when a counter achieves or surpasses this predefined time frame, the content specified in the [Maximum Text property](https://wiki.genexus.com/commwiki/wiki?42257) is displayed.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Suppose that the Maximum Seconds property = 30. When the counter becomes greater than or equal to 30 seconds, the value entered in the Maximum Text property appears.

`[imagen omitida: wiki id 42524]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [See Also](#See+Also)

[Relative Timer control](https://wiki.genexus.com/commwiki/wiki?42490)  
[Minimum Seconds property](https://wiki.genexus.com/commwiki/wiki?42258)  
[Maximum Text property](https://wiki.genexus.com/commwiki/wiki?42257)


|  |
| --- |
| **Backlinks** |
| [Maximum Text property](https://wiki.genexus.com/commwiki/wiki?42257) | [Minimum Seconds property](https://wiki.genexus.com/commwiki/wiki?42258) | [Relative Timer control](https://wiki.genexus.com/commwiki/wiki?42490) |

---
