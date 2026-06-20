---
title: "GetSessionLog method"
source_id: 34395
source_url: https://wiki.genexus.com/commwiki/wiki?34395
genexus_version: "18"
---

# GetSessionLog method

Returns all the sessions defined in the repository where the application is connected to.

### [Syntax](#Syntax)

**GAMRepository.GetSessionLogs(**in:GAMSessionLogFilter,out:GAMError Collection**): GAMSessionLog Collection**

### Description

This method returns a collection of the GAMSessionLog object which contains all the information on the session.   
It receives as a parameter a variable based on GAMSessionLogFilter external object which allows setting the filters for the search (date range, Initial IP Address, Status, UserGUID, isAlive, etc).  
If any error is thrown by its execution, it can be handled by the second parameter of the method which is based on GAMError collection data type.

### [Samples](#Samples)

#### [Example 1](#Example+1)

```
&GAMSessionLogFilter.DateFrom  = &DateFrom
&GAMSessionLogFilter.DateTo  = &DateTo
&GAMSessionLogFilter.EndedFrom  = &EndedFrom
&GAMSessionLogFilter.EndedTo  = &EndedTo
&GAMSessionLogFilter.Limit   = &SessionsXPage
&GAMSessionLogFilter.Start = (&CurrentPage-1) * &GAMSessionLogFilter.Limit + 1

For &GAMSessionLog in GAMRepository.GetSessionLogs(&GAMSessionLogFilter, &Errors)
      &GAMSessionToken  = &GAMSessionLog.Token
      &GAMuserGUID   = &GAMSessionLog.User.GUID
      &name     = &GAMSessionLog.User.Name
Endfor
```

#### [Example 2](#Example+2)

The following example will return the list of the active sessions. Note that the status of the session has to be active and the isAlive property must be true.

```
&GAMSessionLogFilter.Status   = GAMSessionStatus.Active
&GAMSessionLogFilter.isAlive   = True

For &GAMSessionLog in GAMRepository.GetSessionLogs(&GAMSessionLogFilter, &Errors)
      &GAMSessionToken  = &GAMSessionLog.Token
      &GAMuserGUID   = &GAMSessionLog.User.GUID
      &name     = &GAMSessionLog.User.Name
Endfor
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [GetSessionLogsOrderBy method](https://wiki.genexus.com/commwiki/wiki?34396) | [UpdateExpiredSessionLog method](https://wiki.genexus.com/commwiki/wiki?44915) |

---
