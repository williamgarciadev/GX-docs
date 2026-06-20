---
title: "Counting Type property"
source_id: 42253
source_url: https://wiki.genexus.com/commwiki/wiki?42253
genexus_version: "18"
---

# Counting Type property

Sets whether the Relative Timer control will operate as a countdown timer, an elapsed time counter, or a combination of both.

### [Values](#Values)

|  |  |
| --- | --- |
| **Auto** | If the event hasn't started yet, it works as a countdown (Down), decrementing from the specified time. Once the event starts, it seamlessly transitions to counting up (Up), capturing the elapsed time until the event concludes. |
| **Down** | Configures the control to operate exclusively as a countdown timer. |
| **Up** | Sets the control to work only as an elapsed time counter. |

### [Scope](#Scope)

**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** Attribute/Variable (Control Type: [Relative Timer](https://wiki.genexus.com/commwiki/wiki?42490))

### [Description](#Description)

This property is only visible for [Panel](https://wiki.genexus.com/commwiki/wiki?24829) Attributes/Variables whose Data Type is [DateTime](https://wiki.genexus.com/commwiki/wiki?7370) and [Control Type](https://wiki.genexus.com/commwiki/wiki?9550)=[Relative Timer](https://wiki.genexus.com/commwiki/wiki?42490).

Allows specifying whether the control will work as a countdown, count the elapsed time, or perform both actions based on whether the event has occurred.

For example, you may want the control to count down only (Counting Type = Down), and once the count reaches zero, the count ends. In this case, suppose the event will happen within 15 minutes. The control will begin to count and decrease the time until reaching zero; then it will stop.

Also, you may want the counter to start only after the event begins (Counting Type = Up). In this case, time will start to be added after the event's start time; when the event starts, the control will start counting from zero up to the time the event ends.

When the variable value is set to Auto and the event hasn't started, the control behaves as if the property value is set to Down. Once the event begins, it switches to behave as if the property value is set to Up.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [See Also](#See+Also)

[Relative Timer control](https://wiki.genexus.com/commwiki/wiki?42490)


|  |
| --- |
| **Backlinks** |
| [Relative Timer control](https://wiki.genexus.com/commwiki/wiki?42490) |

---
