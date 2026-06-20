---
title: "GetSessionLogsOrderBy method"
source_id: 34396
source_url: https://wiki.genexus.com/commwiki/wiki?34396
genexus_version: "18"
---

# GetSessionLogsOrderBy method

Returns all the sessions defined in the repository where the application is connected to, but it sets an order for the search.

### [Syntax](#Syntax)

**GAMRepository.GetSessionLogsOrderBy(**in:GAMSessionLogFilter, in:GAMSessionLogListOrder, out:GAMError Collection**): GAMSessionLog Collection**

### Description

Its purpose is the same as that of [GetSessionLog method](https://wiki.genexus.com/commwiki/wiki?34395), but it receives an additional parameter which allows setting an order for the search. The parameter is based on domain.

### [Samples](#Samples)

```
For &GAMSessionLog in GAMRepository.GetSessionLogsOrderBy(&GAMSessionLogFilter, GAMSessionLogListOrder.Date_Desc, &Errors)
       &GAMSessionToken  = &GAMSessionLog.Token
       &GAMUserlogin   = &GAMSessionLog.AuthenticatedLogin
       &GAMSessionStatus  = &GAMSessionLog.Status
       &LoginDate    = &GAMSessionLog.LoginDate
EndFor
```

**Notes:**

1. Both GetSessionLogsOrderBy and GetSessionLogs allow getting the results by pages, using the GAMSessionLogFilter parameter of the methods (download the example below).
2. You should not use static methods over an instance variable (&GAMSessionLog). So, the following is not correct:

```
&GAMSessionLog.User.GetId()
```

Instead, you should use:

```
&GAMSessionLog.User.GUID
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
