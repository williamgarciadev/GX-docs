---
title: "Show Application Bars property"
source_id: 23305
source_url: https://wiki.genexus.com/commwiki/wiki?23305
genexus_version: "18"
---

# Show Application Bars property

Sets whether to display the Application Bar in the device.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974)  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

Useful when you need more space to display texts, images, etc, depending on the device. For example, if you are designing an application for iPad and iPhone, you could need more space in the iPhone; then, set this property to False in the iPhone layout.

You can dynamically show or hide the application bar by writing a user event with the following code:

```
Event 'ShowHideApplicationBars'
     ApplicationBar.Visible = not ApplicationBar.Visible
EndEvent
```

Where *ApplicationBars* is its Control Name.

### [Notes](#Notes)

* When this property is set to True, [Application Bars Class property](https://wiki.genexus.com/commwiki/wiki?37518) is available.
* Runtime change of this property is not available for the Menu object.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Visible property](https://wiki.genexus.com/commwiki/wiki?8849)


|  |
| --- |
| **Backlinks** |
| [Application Bar control in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19486) | [Getting Started with tvOS](https://wiki.genexus.com/commwiki/wiki?40787) |

---
