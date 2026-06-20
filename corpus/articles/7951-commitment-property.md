---
title: "Commitment property"
source_id: 7951
source_url: https://wiki.genexus.com/commwiki/wiki?7951
genexus_version: "18"
---

# Commitment property

Enables and disables the transactional integrity controls in the generated programs.

### [Values](#Values)

|  |  |
| --- | --- |
| **Disabled** | The program is generated with no transactional integrity controls. |
| **Enabled** | The program is generated with the transactional integrity controls. This is the default value. |

### [Description](#Description)

#### [Notes](#Notes)

* This option is ignored for Client Server (DB/2 and Oracle Generators) because these DBMSs do not allow to deactivate the Transactional Integrity facility.
* **iSeries environment:** This property is only valid:
  + When working in a centralized environment.
  + When working in a client/server environment the object is called via RPC. For example, if we are working in a C/S environment and the object where we want to disable the commitment is a visual program (e.g.: Visual Basic, Visual FoxPro), the property is not valid. In this case, what we can do is create a Cobol or RPG program (disabling the commitment control so that the commit is performed) and call it via RPC.

### [Scope](#Scope)

**Objects:** Procedure, Transaction  
**Platforms:** Web(.Net, Java)

### [See Also](#See+Also)

[Commit on Exit property](https://wiki.genexus.com/commwiki/wiki?7942,,)


|  |
| --- |
| **Backlinks** |
| [Commit command](https://wiki.genexus.com/commwiki/wiki?7964) | [Confirm Transactions property](https://wiki.genexus.com/commwiki/wiki?7999) |
| [Rollback command](https://wiki.genexus.com/commwiki/wiki?7998) |

---
