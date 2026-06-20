---
title: "Run Without Building"
source_id: 20689
source_url: https://wiki.genexus.com/commwiki/wiki?20689
genexus_version: "18"
---

# Run Without Building

The Run Without Building option is intended to quickly run the selected [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) or [Startup Object](https://wiki.genexus.com/commwiki/wiki?5394) (Ctrl-F5). There is no build, reorganization, or compilation; objects are only run. The idea is to run the selected object as it was when it was last built or run, ignoring any changes in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).  
  
This option performs the following steps:

|  |  |
| --- | --- |
| Steps | Comments |
| Saves any unsaved objects in the workspace | This step stops on errors |
| Does \_NOT\_ reorganize the database even if it is necessary |  |
| Does \_NOT\_ specify any object |  |
| Does \_NOT\_ generate |  |
| Does \_NOT\_ compile anything |  |
| Executes the selected (explicit or implied) main object |  |

### **Note**

If the selected (explicit or implied) object was never run/built before, the execution will fail.

### [Availability](#Availability)

This option is available as of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

### [See also](#See+also)

[Build All/Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691)  
[Build/Rebuild/Run](https://wiki.genexus.com/commwiki/wiki?5692)  
[Build/Run With This Only](https://wiki.genexus.com/commwiki/wiki?5693)


|  |
| --- |
| **Backlinks** |
| [Build All/Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691) | [Build/Rebuild/Run](https://wiki.genexus.com/commwiki/wiki?5692) | [Build/Run With This Only](https://wiki.genexus.com/commwiki/wiki?5693) |
| [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |

---
