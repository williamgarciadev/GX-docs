---
title: "Reorganize server tables property"
source_id: 8955
source_url: https://wiki.genexus.com/commwiki/wiki?8955
genexus_version: "18"
---

# Reorganize server tables property

Used to state whether the tables of the model are to be reorganized or not by the Client/Server generators.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | The database won't be reorganized. |
| **Yes** | The database will be reorganized. This is the default value. |

### [Description](#Description)

* With multiple generators this property is used only for reorganization generator of the model (the one defined in Model Properties/General/Environment).
* One of the most common uses of the Client/Server generator is to be able to access existing centralized databases which are maintained by either the COBOL or RPG for iSeries generator. In this environment, the Database reorganization is performed by the COBOL or RPG for iSeries generator. The Client/Server must NOT try to reorganize the Database tables. If this occurs, errors will be generated because the Database has been previously reorganized by the other generator.
* It is possible that the database Impact Analysis Report indicates that the tables defined as Client/Server need to be reorganized. This will be ignored by the Client/Server generator ifthe *"**Reorganize Server table"*is set to **NO**.

When you change the value, the next reorganization operation will use the property value change.

### [Scope](#Scope)

**Platforms:** Web(.Net, Java)


|  |
| --- |
| **Backlinks** |
| [Keep GAM database updated property](https://wiki.genexus.com/commwiki/wiki?21453) | [Mark Database as Reorganized Option](https://wiki.genexus.com/commwiki/wiki?12810) |

---
