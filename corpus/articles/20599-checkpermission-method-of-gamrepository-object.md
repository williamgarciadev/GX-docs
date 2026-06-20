---
title: "Checkpermission method of GAMRepository Object"
source_id: 20599
source_url: https://wiki.genexus.com/commwiki/wiki?20599
genexus_version: "18"
---

# Checkpermission method of GAMRepository Object

Verifies whether the [GAM User](https://wiki.genexus.com/commwiki/wiki?22082) currently logged in has a given permission or not.

### [Syntax](#Syntax)

**GAMRepository*.*CheckPermission(***PermissionName​​​​***)**

**Where:**

*GAMRepository* Is a fixed part of the syntax. Read more at [GAM - Repository](https://wiki.genexus.com/commwiki/wiki?17568).  
   
*PermissionName*  Input parameter corresponding to the permission name. This parameter must be of [Character data type](https://wiki.genexus.com/commwiki/wiki?6777) based on GAMDescriptionLong.

**Type Returned:**  
GAMBoolean

### [Samples](#Samples)

```
Event Start
  If GAMRepository.CheckPermission("is_gam_administrator")
      //OK
    Else
      GAMExampleNotAuthorized.Link()
  Endif
EndEvent
```

### [See Also](#See+Also)

[GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912)


|  |
| --- |
| **Backlinks** |
| [GAM - Permissions](https://wiki.genexus.com/commwiki/wiki?15912) |

---
