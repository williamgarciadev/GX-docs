---
title: "UpdateExpiredSessionLog method"
source_id: 44915
source_url: https://wiki.genexus.com/commwiki/wiki?44915
genexus_version: "18"
---

# UpdateExpiredSessionLog method

Updates session status to Expired, optimizing the use of the GAMRepository.[GetSessionLog](https://wiki.genexus.com/commwiki/wiki?34395)() method accurately.

### [Syntax](#Syntax)

**GeneXusSecurity.GAM.UpdateExpiredSessionLog(**&GAMProcessSessionLogFilter, &Errors**)**: Boolean

### [Description](#Description)

If a session hasn't been used again since its expiration, its status may stay active, despite being expired after the session timeout.

In such case, the use of the GAMRepository.[GetSessionLog](https://wiki.genexus.com/commwiki/wiki?34395)() will return more active (or expired) sessions than the actual number.

The UpdateExpiredSessionLog method updates session status to "Expired" for those active, when in fact they should be expired. It receives a variable as parameter that is based on the GAMProcessSessionLogFilter external object. It returns True if the change was made correctly, or False if it wasn't.

**Note**: a Commit must be done

When the method's execution indicates error, it can be handled by the method's second parameter, which is based on collection data type. This optimizes the use of the GAMRepository.[GetSessionLog](https://wiki.genexus.com/commwiki/wiki?34395)() method, with more accurate results.

### [Samples](#Samples)

```
// Set expired sessions from yesterday
&GAMProcessSessionLogFilter = new()
&GAMProcessSessionLogFilter.CleanUpToDate = &Today.AddDays(-1)
&isOK = GeneXusSecurity.GAM.UpdateExpiredSessionLog(&GAMProcessSessionLogFilter, &Errors)
If &isOK
  Commit
Endif
```

### [Availability](#Availability)

This method is available since [GeneXus 16 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?44454,,).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
