---
title: "LoginRetries and LoginRetryCount properties"
source_id: 34399
source_url: https://wiki.genexus.com/commwiki/wiki?34399
genexus_version: "18"
---

# LoginRetries and LoginRetryCount properties

It's possible to get information about all the GAM Sessions that had at least one failed login (login retries).

**LoginRetryCount** and **LoginRetries** are properties of the *GAMSessionLog* object. The former gets the number of login retries for that GAM Session, and the latter gives information about it. The information is a collection of *GAMSessionLogLoginRetry*.

`[imagen omitida: wiki id 34424]`

### [Example](#Example)

In this example, we scan all the sessions of a repository; for each of them, if there was more than one login retry, we process the information of the login retries which have been made.

In order to get the GAM Sessions that have Login Retries (using the GAMRepository.GetSessionLogs method), we use the following filters (properties of *GAMSessionLogFilter* object)

* **LoadLoginRetries** (GAMBoolean data type: True, False). Generate the query to the GAM Sessions including the LoginRetries information. This property is useful for performance reasons.
* **IncludeLoginRetriesLog** (GAMBooleanFilter data type: All, True, False). Select to get the GAM Sessions that have any LoginRetry information, those that don't have any or all of them.

`[imagen omitida: wiki id 34425]`

```
Event GridWW.Load

    &GAMSessionLogFilter.LoadLoginRetries        = &LoadLoginRetries
    &GAMSessionLogFilter.IncludeLoginRetriesLog = &IncludeLoginRetries
    &GAMSessionLogFilter.Start = (&CurrentPage-1) * &GAMSessionLogFilter.Limit + 1
    
    For &GAMSessionLog in GAMRepository.GetSessionLogsOrderBy(&GAMSessionLogFilter, GAMSessionLogListOrder.Date_Desc, &Errors)
      
        &LoginRetriesChar.SetEmpty()
        If &GAMSessionLog.LoginRetryCount > 0
            For &GAMSessionLogLoginRetry in &GAMSessionLog.LoginRetries
                &LoginRetriesChar = &GAMSessionLogLoginRetry.UserLogin + ".-."+ &GAMSessionLogLoginRetry.Number.ToString() 
                
            EndFor
        Endif

        GridWW.Load()
    Endfor

EndEvent
```

Download the sample from [GAM session handling sample](https://wiki.genexus.com/commwiki/wiki?34420,,).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
