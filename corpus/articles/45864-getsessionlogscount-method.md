---
title: "GetSessionLogsCount method"
source_id: 45864
source_url: https://wiki.genexus.com/commwiki/wiki?45864
genexus_version: "18"
---

# GetSessionLogsCount method

Returns the number of sessions that comply with the filters.

### [Syntax](#Syntax)

**GAMRepository.GetSessionLogsCount(**in:GAMSessionLogsCountFilter**)**: int

### [Description](#Description)

The GetAliveSessionCount method is available for the [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568) as well as for GAM external objects. It receives as parameter a variable based on the GAMSessionLogFilter external object, which allows setting the filters for the search (date range, Authentication Type, isAlive, etc). This method returns the number of sessions that comply with the filters.

The only way to execute this method is by connecting to the [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617).

**Note**: This method was called GetSessionsCount until [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
