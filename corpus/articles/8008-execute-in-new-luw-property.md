---
title: "Execute in new LUW property"
source_id: 8008
source_url: https://wiki.genexus.com/commwiki/wiki?8008
genexus_version: "18"
---

# Execute in new LUW property

This property indicates whether the procedure will be run in a new LUW or not.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Description](#Description)

Default value: False.

As a result, the called procedure and everything called by it will be executed in an LUW that is independent from the caller object's LUW. Also, when a Commit or Rollback of this LUW is performed, there will be no Commit or Rollback of the caller object's LUW.

### [Scope](#Scope)

**Objects:** Procedure  
**Platforms:** Web(.Net, Java)

### [See Also](#See+Also)

[Commit on Exit property](https://wiki.genexus.com/commwiki/wiki?7942,,)  
[LUW](https://wiki.genexus.com/commwiki/wiki?2424)


|  |
| --- |
| **Backlinks** |
| [Before connect property](https://wiki.genexus.com/commwiki/wiki?8997) | [GAM - Events subscription](https://wiki.genexus.com/commwiki/wiki?32698) |

---
