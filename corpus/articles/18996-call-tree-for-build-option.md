---
title: "Call tree for build option"
source_id: 18996
source_url: https://wiki.genexus.com/commwiki/wiki?18996
genexus_version: "18"
---

# Call tree for build option

The default [Build/Rebuild/Run](https://wiki.genexus.com/commwiki/wiki?5692) process (specify|generate|compile) in GeneXus takes a given [Main Object](https://wiki.genexus.com/commwiki/wiki?5770), usually the [Startup Object](https://wiki.genexus.com/commwiki/wiki?5393), analyzes each object in its call tree for changes and specify and regenerates those that were modified.

In the compilation phase, the call tree search stops (also known as "cuts"), by default, on every other main object found. That is, if main object A calls B and this one calls C that is a main object too, the default call tree for A is comprised of A and B only. C is *not* included so only A and B are compiled and C is not.

Notice that the [Build/Run With This Only](https://wiki.genexus.com/commwiki/wiki?5693) operation on C object will not compile it, because the object is not in the startup object call tree (A object).

The [Call tree for build option](https://wiki.genexus.com/commwiki/wiki?24030) lets you change this behaviour.

### [Values](#Values)

|  |  |
| --- | --- |
| **Stop on main objects** | The call tree search is cut on every other main object. |
| **Full** | The call tree search does not stop on every other main object. This value must be used for applications having a specific entry point object (usually a login form) whose call tree includes many other main objects. Using this value is not recommended as it may significantly increase the Build/Rebuild/Run times as more objects (usually not changed) have to be analyzed.  This is the default option since GeneXus Xev3 |

### 

### [See also](#See+also)

[Build/Rebuild/Run](https://wiki.genexus.com/commwiki/wiki?5692)  
[Startup Object](https://wiki.genexus.com/commwiki/wiki?5393)


|  |
| --- |
| **Backlinks** |
| [Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719) | [Build/Rebuild/Run](https://wiki.genexus.com/commwiki/wiki?5692) |

---
