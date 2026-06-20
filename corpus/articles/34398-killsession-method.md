---
title: "KillSession method"
source_id: 34398
source_url: https://wiki.genexus.com/commwiki/wiki?34398
genexus_version: "18"
---

# KillSession method

Identifies the session that is to be killed, returning true or false depending on the success of the execution.

### [Syntax](#Syntax)

**GAMSessionLog.KillSession(**in:GAMSessionToken, out: GAMError Collection**)** : Boolean

### [Description](#Description)

This method receives as a parameter a variable based on GAMSessionToken domain, which identifies the session that is to be killed.

It returns true or false depending on the success of the execution. The errors can be handled using the second parameter of the method, which is based on GAMError collection data type.

The final status of the killed session is Finished.

### [Samples](#Samples)

```
&Isok = GAMSessionLog.KillSession(&GAMSessionToken, &Errors)
if &isOK
  commit
else
//Process errors
EndIf
```

**Notes:**

* In order to use all these methods, setting [Generate Session Statistics GAMRepository property](https://wiki.genexus.com/commwiki/wiki?24375,,) to Minimum or Detail is required.
* When the value is Minimum only the information for non-anonymous users can be retrieved.
* In order to handle the session information for both anonymous and non-anonymous users, you need to set Generate Sessions Statistics GAMRepository property to Detail value.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
