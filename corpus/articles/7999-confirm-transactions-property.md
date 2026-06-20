---
title: "Confirm Transactions property"
source_id: 7999
source_url: https://wiki.genexus.com/commwiki/wiki?7999
genexus_version: "18"
---

# Confirm Transactions property

Forces a confirmation prompt for a Transaction object allowing a COMMIT or a ROLLBACK.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | No confirmation of the LUW is asked and the Commit command is automatically executed. This is the default value. |
| **Yes** | Forces a confirmation prompt at the LUW level or Transaction. This allows the user to confirm (COMMIT) or not (ROLLBACK) the changes made to the database during the LUW. |

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

It is valid only in Transactions with the [Commit on Exit property](https://wiki.genexus.com/commwiki/wiki?7942,,) = Yes and [Commitment property](https://wiki.genexus.com/commwiki/wiki?7951) = Enabled. Otherwise, the property Confirm Transactions = Yes will be ignored.

### [See Also](#See+Also)

[Confirmation property](https://wiki.genexus.com/commwiki/wiki?7422)  
[Commit on Exit property](https://wiki.genexus.com/commwiki/wiki?7942,,)  
[Commitment property](https://wiki.genexus.com/commwiki/wiki?7951)


|  |
| --- |
| **Backlinks** |
| [Commit command](https://wiki.genexus.com/commwiki/wiki?7964) | [Rollback command](https://wiki.genexus.com/commwiki/wiki?7998) |

---
