---
title: "Display Value property"
source_id: 42203
source_url: https://wiki.genexus.com/commwiki/wiki?42203
genexus_version: "18"
---

# Display Value property

Indicates whether the control should display a bubble with the current value upon interaction.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** Attribute/Variable (Control Type: [Slider](https://wiki.genexus.com/commwiki/wiki?20334))

### [Description](#Description)

Default value: False.

Applies to Attribute/Variable included in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) or [WW](https://wiki.genexus.com/commwiki/wiki?15974) whose [Control Type](https://wiki.genexus.com/commwiki/wiki?9550)=[Slider](https://wiki.genexus.com/commwiki/wiki?20334).

Indicates whether the control should display the value. This value is shown as a floating bubble above the slider.

If the control is on the upper screen, it could lack the space required to display the value; in that case, it will not be shown. To avoid this undesired behavior, leaving a separate space between the control and the application bar is advisable.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [See Also](#See+Also)

[Slider Control](https://wiki.genexus.com/commwiki/wiki?20334)
