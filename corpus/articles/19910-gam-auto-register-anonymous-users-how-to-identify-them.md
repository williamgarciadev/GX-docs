---
title: "GAM - Auto-register anonymous users - How to identify them"
source_id: 19910
source_url: https://wiki.genexus.com/commwiki/wiki?19910
genexus_version: "18"
---

# GAM - Auto-register anonymous users - How to identify them

This article describes how to inform if there is no session in the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) or if the session that exists is anonymous.  
  
It is valid both for [auto registered anonymous users](https://wiki.genexus.com/commwiki/wiki?19395) and for [knowing if the session is anonymous in web applications](https://wiki.genexus.com/commwiki/wiki?16414).

```
&GAMSession=GAMSession.Get(&GAMErrors) //&GAMErrors: GAMError collection data type / &GAMSession: GAMSession data type

If &GAMSession.IsAnonymous
       //Anonymous user
Else
       //Registered user
Endif
```

This is how you can find out if the Native Mobile application has an auto-registered user:

```
If &GAMUser.IsAutoRegisteredUser
       //Anonymous user
Else
       //Registered user
Endif
```

### [See Also](#See+Also)

[GAM - Auto-register anonymous user - Panel usage example](https://wiki.genexus.com/commwiki/wiki?19911)


|  |
| --- |
| **Backlinks** |
| [GAM - Auto-register anonymous users](https://wiki.genexus.com/commwiki/wiki?19395) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
