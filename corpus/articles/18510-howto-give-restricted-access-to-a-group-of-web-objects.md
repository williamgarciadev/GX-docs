---
title: "HowTo: Give Restricted Access to a Group of Web Objects"
source_id: 18510
source_url: https://wiki.genexus.com/commwiki/wiki?18510
genexus_version: "18"
---

# HowTo: Give Restricted Access to a Group of Web Objects

There are some cases in which the required authorization level for a group of users to access a set of an application's web pages is just to allow or deny it.

For instance, if the application is divided into two modules (front-end and back-end), the backend will probably be accessed only by some authorized users (administrator users only).

One way to do this, is to use a Masterpage for the back-end pages, and program the following in the Start Event of the Masterpage:

```
If GAMRepository.CheckPermission("is_authorized_toBackend")
  //OK
Else
  GAMExampleNotAuthorized.Link()
Endif
```

Note that you need to define the "is\_authorized\_toBackend" permission in the WEB [Application](https://wiki.genexus.com/commwiki/wiki?15910), and define [Roles](https://wiki.genexus.com/commwiki/wiki?17569) where this permission is allowed or denied, as desired.

There´s no need to set [Integrated Security Level Property](https://wiki.genexus.com/commwiki/wiki?15214) to "Authorization", just to "Authentication" value.  
[Require Access Permissions](https://wiki.genexus.com/commwiki/wiki?18512) of GAM Application must be set to TRUE.

Recommended reading: [Access restricted to GAM Backend](https://wiki.genexus.com/commwiki/wiki?18495), this paper goes into detail of this topic.

### [See Also](#See+Also)

[GAM Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583)


|  |
| --- |
| **Backlinks** |
| [GAM - Authorization Scenarios](https://wiki.genexus.com/commwiki/wiki?17583) |

---
