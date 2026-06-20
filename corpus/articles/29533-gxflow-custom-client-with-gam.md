---
title: "GXflow Custom Client with GAM"
source_id: 29533
source_url: https://wiki.genexus.com/commwiki/wiki?29533
genexus_version: "18"
---

# GXflow Custom Client with GAM

When using GXflow Custom Client with [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746), you must modify the following object: *WorkflowCheckGAMSession*by removing comments of the source and adding the undefined variables.

The object source code must be as shown below:

```
If GAMSession.IsValid(&GAMSession, &GAMErrors)
  If Not &GAMSession.IsAnonymous
    &userCod = &GAMSession.User.Name.Trim().ToUpper()
    &error = WorkflowGenerateSession(&userCod, '')
    If &error.Code = 0
      &check = True
    Endif
  Endif
Endif
```

Also, the following variables must be created:

* **GAMErrors**: Data type GAMError (Collection)
* **GAMSession**: Data type GAMSession

WorkFlowGenerateSession code is as follows (you can download the code from [file GenerateSession.xpz](https://wiki.genexus.com/commwiki/wiki?29947,,)):

```
Parm(in: &userCod, out: &error);
```

```
&server.Connect(&userCod, '')
Commit

&error = &server.Error

If &server.Error.Code = 0
    &session.Set(WorkflowWebSession.SessionHandle, &server.Session)
    &session.Set(WorkflowWebSession.UserCode, &userCod)
Endif
```

**Note**: At execution time, the standard client application will automatically redirect to the object configured in [Login Object for Web property](https://wiki.genexus.com/commwiki/wiki?15590), and you must link to wfmain object.


|  |
| --- |
| **Backlinks** |
| [Aspects to consider when using GeneXus BPM Suite with GAM](https://wiki.genexus.com/commwiki/wiki?43858) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXflow - GAM Initialization](https://wiki.genexus.com/commwiki/wiki?33095) |
| [GXflow - GAM Integration](https://wiki.genexus.com/commwiki/wiki?18454) |

---
