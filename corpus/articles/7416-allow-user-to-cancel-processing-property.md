---
title: "Allow user to cancel processing property"
source_id: 7416
source_url: https://wiki.genexus.com/commwiki/wiki?7416
genexus_version: "18"
---

# Allow user to cancel processing property

Indicates whether the program can be cancelled by pressing Esc.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | It is not possible to cancel the program. |
| **Yes** | It is possible to cancel the program. This is the default value. |

### [Description](#Description)

In a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) that prints an invoice which is called from a [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) it is very useful to set this property to "No", to make sure that the invoice is always printed.

### [Scope](#Scope)

**Objects:** Procedure  
**Platforms:** Web(.Net, Java)
