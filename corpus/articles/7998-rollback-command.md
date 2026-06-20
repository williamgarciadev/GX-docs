---
title: "Rollback command"
source_id: 7998
source_url: https://wiki.genexus.com/commwiki/wiki?7998
genexus_version: "18"
---

# Rollback command

Forces a program to rollback.

### [Syntax](#Syntax)

**Rollback**

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

The Rollback command invalidates the set of database updates in a [Logical Unit of Work (LUW)](https://wiki.genexus.com/commwiki/wiki?7963).

It may be used in [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) or [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916), but not in [Transactions](https://wiki.genexus.com/commwiki/wiki?1908).

**Note**: The Rollback command is ignored by [Environments](https://wiki.genexus.com/commwiki/wiki?7115) that do not use [Transactional Integrity](https://wiki.genexus.com/commwiki/wiki?45612).

### [See Also](#See+Also)

[Commit command](https://wiki.genexus.com/commwiki/wiki?7964)  
[Commitment property](https://wiki.genexus.com/commwiki/wiki?7951)  
[Commit on Exit property](https://wiki.genexus.com/commwiki/wiki?7942,,)  
[Confirm Transactions property](https://wiki.genexus.com/commwiki/wiki?7999)


|  |
| --- |
| **Backlinks** |
| [Before Commit, After Commit, Before Rollback and After Rollback Generator properties](https://wiki.genexus.com/commwiki/wiki?8996) | [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Commit command](https://wiki.genexus.com/commwiki/wiki?7964) |
| [Logical Unit of Work (LUW)](https://wiki.genexus.com/commwiki/wiki?7963) |

---
