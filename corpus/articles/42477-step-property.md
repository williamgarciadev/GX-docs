---
title: "Step property"
source_id: 42477
source_url: https://wiki.genexus.com/commwiki/wiki?42477
genexus_version: "18"
---

# Step property

Set 'Step' for discrete control values, defining 'Minimum Value' and 'Maximum Value' properties for the range. A 'Step' of 0 allows any intermediate value.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** Attribute/Variable (Control Type: [Slider](https://wiki.genexus.com/commwiki/wiki?20334))

### [Description](#Description)

Default value: 0.

The Step property should be used when the values of the control can only take some discrete values.

Applies to Attribute/Variable included in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) or [WW](https://wiki.genexus.com/commwiki/wiki?15974) whose [Control Type](https://wiki.genexus.com/commwiki/wiki?9550)=[Slider](https://wiki.genexus.com/commwiki/wiki?20334).

For example, if valid values are {10, 20, 30} set the Minimum Value to 10, the Maximum Value to 30, and the Step to 10. If the Step is 0, then any intermediate value is valid.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [See Also](#See+Also)

[Slider Control](https://wiki.genexus.com/commwiki/wiki?20334)
