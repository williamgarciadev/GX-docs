---
title: "New Events Color property"
source_id: 54523
source_url: https://wiki.genexus.com/commwiki/wiki?54523
genexus_version: "18"
---

# New Events Color property

Sets the background color for new events.

### [Scope](#Scope)

**Controls:** [Scheduler](https://wiki.genexus.com/commwiki/wiki?11583)

### [Description](#Description)

This property will determine the background color of newly inserted events.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at runtime and at design time.

### [Samples](#Samples)

The property can also be set in runtime in the Start event.

```
Event Start
      //Sets the background color of the newly inserted events as Green.
      GXScheduler1.NewEventsColor = rgb(0,225,0)
EndEvent
```

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [See Also](#See+Also)

[GXScheduler User Control](https://wiki.genexus.com/commwiki/wiki?11583)
