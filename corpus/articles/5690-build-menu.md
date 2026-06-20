---
title: "Build Menu"
source_id: 5690
source_url: https://wiki.genexus.com/commwiki/wiki?5690
genexus_version: "18"
---

# Build Menu

Build is the process of doing all the tasks required to get everything ready for the next execution of your entire application or part of it. Building involves checking for database changes and [reorganizing](https://wiki.genexus.com/commwiki/wiki?5288) the database if needed, as well as specifying, generating, and compiling (not running). The Build process can be applied to all the objects in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), the Developer Menu, or a [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). This is a very important process, as it is executed many, many times while developing. That's why it must be fast and accurate.  
  
GeneXus keeps track of every "item" that every single object depends on; for example, if a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) accesses a database table, calls another object, etc. In this way, GeneXus can detect what objects must be rebuilt when anything changes in your application, and do it fast.

The Build options available are as follows:

* [Build All/Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691)
* [Build/Rebuild/Run](https://wiki.genexus.com/commwiki/wiki?5692)
* [Build/Run With This Only](https://wiki.genexus.com/commwiki/wiki?5693)

The entire build process can be done in batches using [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908).

Note: The "View Navigation" option is not a Build Option in that all it does is show the object's navigation –it doesn't perform any impact analysis, etc.


|  |
| --- |
| **Sub Categories** |
| [Category:Reorganization](https://wiki.genexus.com/commwiki/wiki?5288) |

---

|  |
| --- |
| **Pages** |
| [Build All/Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691) | [Build/Rebuild/Run](https://wiki.genexus.com/commwiki/wiki?5692) | [Build/Run With This Only](https://wiki.genexus.com/commwiki/wiki?5693) |
| [Create Database Tables](https://wiki.genexus.com/commwiki/wiki?7158) | [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908) | [MSBuild Tasks (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53867) |
| [MSBuild Tasks (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54112) | [Run Without Building](https://wiki.genexus.com/commwiki/wiki?20689) | [Startup Object](https://wiki.genexus.com/commwiki/wiki?5393) |

---
