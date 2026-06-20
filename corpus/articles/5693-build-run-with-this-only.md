---
title: "Build/Run With This Only"
source_id: 5693
source_url: https://wiki.genexus.com/commwiki/wiki?5693
genexus_version: "18"
---

# Build/Run With This Only

The Build/Run With This Only option is intended to build and run the [Startup Object](https://wiki.genexus.com/commwiki/wiki?5394), ignoring any changes in objects other than the one selected. Say, for example, that the [Startup Object](https://wiki.genexus.com/commwiki/wiki?5393) is set to a [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) named MyMain and changes have been done to programs PgmA, PgmB and PgmC, all belonging to MyMain call tree. Executing Build With This Only on PgmB causes MyMain to be rebuilt with changes to PgmB but ignoring changes to PgmA and PgmC.  
  
Since GeneXus does not check for dependencies, these options are a fast method for testing single object changes. However, they should be used carefully as they may lead you to get confused looking for changes that were not built in the running application.  
  
These options include the following steps:

|  |  |
| --- | --- |
| Steps | Comments |
| Save **any** unsaved objects | The step stops on errors. |
| Reorganize the database if necessary | The step stops on errors. |
| Specify the selected object **only** | Note that if other objects in the Startup Object called tree have changed, they are not specified or generated. The step stops on errors. |
| Generate the selected object only | The step does **not** stop on errors. |
| Compile the Startup Object | The step stops on errors. |
| Deploy | The step stops on errors. |
| Execute the Startup Object (Run) |  |

**Note:** if a 'Build/Run With This Only' task is performed on [SD](https://wiki.genexus.com/commwiki/wiki?20766) objects, such as: [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) or [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), and a [SD](https://wiki.genexus.com/commwiki/wiki?20766) object is set as [Startup Object](https://wiki.genexus.com/commwiki/wiki?5393), then it will be compiled and executed. Otherwise, If there is not any SD object set as Startup Object, the SD developer menu will be compiled/executed ([KBN](https://wiki.genexus.com/commwiki/wiki?18653)).

### [See also](#See+also)

[Build All/Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691)  
[Build/Rebuild/Run](https://wiki.genexus.com/commwiki/wiki?5692)  
[Run Without Building](https://wiki.genexus.com/commwiki/wiki?20689)


|  |
| --- |
| **Backlinks** |
| [Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719) | [Build All/Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691) | [Category:Build Menu](https://wiki.genexus.com/commwiki/wiki?5690) |
| [Build/Rebuild/Run](https://wiki.genexus.com/commwiki/wiki?5692) | [Call tree for build option](https://wiki.genexus.com/commwiki/wiki?18996) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Run Without Building](https://wiki.genexus.com/commwiki/wiki?20689) |

---
