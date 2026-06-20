---
title: "Reorganization"
source_id: 5288
source_url: https://wiki.genexus.com/commwiki/wiki?5288
genexus_version: "18"
---

# Reorganization

Reorganization is part of the [build process](https://wiki.genexus.com/commwiki/wiki?5690). It includes the generation, compilation, and execution of the programs in charge of creating the database (if needed and possible), as well as making changes in the database schema (i.e. creating/changing/dropping Tables, Views, Functions, Indices, and Constraints), and transforming the related data.

### [Features](#Features)

* Executable reorganization programs are generated, compiled, and executed.
* A Reorganization script containing the SQL of the reorganization is generated.
* You can define Pre/Post Reorganization scripts.
* Reorganization programs:
  + Run in multiple threads
  + Can count records to be transformed
  + Verify schema as the first step to avoid failures
  + Verify DBMS version to avoid failures
  + Can resume after failure.

For more information, see [Features of Reorganizations](https://wiki.genexus.com/commwiki/wiki?3154).


|  |
| --- |
| **Sub Categories** |
| [Category:Reorganization Common Issues](https://wiki.genexus.com/commwiki/wiki?11006,Category%3AReorganization+Common+Issues,) |

---

|  |
| --- |
| **Pages** |
| [Database Reorganization cases where a temporary table is created](https://wiki.genexus.com/commwiki/wiki?19529) | [Export Reorganization](https://wiki.genexus.com/commwiki/wiki?34476) | [Features of Reorganizations](https://wiki.genexus.com/commwiki/wiki?3154) |
| [Information in IAR when Reorganize Server Tables Property is set to No](https://wiki.genexus.com/commwiki/wiki?23407,Information+in+IAR+when+Reorganize+Server+Tables+Property+is+set+to+No,) | [Mark Database as Reorganized Option](https://wiki.genexus.com/commwiki/wiki?12810) | [Reorganization Error Codes and Messages](https://wiki.genexus.com/commwiki/wiki?5952) |
| [Reorganization Message rgo0001](https://wiki.genexus.com/commwiki/wiki?5228) | [Reorganization message rgo0002](https://wiki.genexus.com/commwiki/wiki?6272) | [Reorganization message rgo0003](https://wiki.genexus.com/commwiki/wiki?10856) |
| [Reorganization Operation Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?5965) | [Reorganization that converts descriptions attributes in new tables](https://wiki.genexus.com/commwiki/wiki?23411) | [Reorganizations associated to Data Views](https://wiki.genexus.com/commwiki/wiki?43272) |
| [Scenario of backward compatible reorganizations](https://wiki.genexus.com/commwiki/wiki?48715) |

---
