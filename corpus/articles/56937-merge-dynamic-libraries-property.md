---
title: "Merge Dynamic Libraries property"
source_id: 56937
source_url: https://wiki.genexus.com/commwiki/wiki?56937
genexus_version: "18"
---

# Merge Dynamic Libraries property

Allows merger of mergeable dynamic libraries to improve application start time.

### [Values](#Values)

|  |
| --- |
| **True** |
| **False** |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

The default value of this property is False. For more information, see [SAC #54016](https://www.genexus.com/en/developers/websac?data=54016;;).

It allows you to combine dynamic mergeable libraries, which is beneficial for improving the time it takes for your application to start.

Instead of loading multiple dynamic libraries separately, merging allows you to combine them into the application binary, which can speed up the application startup process.

**Notes:**

* This feature requires iOS 13.0 as the minimum supported version.
* If you require the use of CocoaPods, this feature should be avoided.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Merge libraries automatically in Xcode](https://developer.apple.com/documentation/xcode/configuring-your-project-to-use-mergeable-libraries#Merge-libraries-automatically-in-Xcode)


|  |
| --- |
| **Backlinks** |
| [Merge Dynamic Libraries property (GeneXus 18 Upgrade 8)](https://wiki.genexus.com/commwiki/wiki?57469) |

---
