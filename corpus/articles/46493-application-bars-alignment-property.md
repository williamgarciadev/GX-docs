---
title: "Application Bars Alignment property"
source_id: 46493
source_url: https://wiki.genexus.com/commwiki/wiki?46493
genexus_version: "18"
---

# Application Bars Alignment property

Controls the alignment of the Application Bar title.

### [Values](#Values)

|  |  |
| --- | --- |
| **Center Screen** | Centers the title of the application bar according to the full width of the image. |
| **Center Space** | Centers the title of the application bar according to its free space. |
| **Left** | Aligns the title of the application bar to the left. |
| **Platform Default** | The default value for Android generator is Left. |
| **Right** | Aligns the title of the application bar to the right. |

### [Scope](#Scope)

**Objects:** [Theme](https://wiki.genexus.com/commwiki/wiki?17876,,)  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

|  |
| --- |
| Center Screen |
|  |

|  |
| --- |
| Center Space |
|  |

|  |
| --- |
| Left |
|  |

**Note:**The generated application always saves space on the left for its back button. In order to fully fit the left space, the call stack must be empty, or you can disable the back button by programming the Back Event as empty. In this last case, the back function defined by the OS will also be disabled, so use it at your own risk.

|  |
| --- |
| Right |
|  |

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [See Also](#See+Also)

[Theme object](https://wiki.genexus.com/commwiki/wiki?16595)
