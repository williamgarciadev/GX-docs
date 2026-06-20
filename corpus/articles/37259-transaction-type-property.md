---
title: "Transaction Type property"
source_id: 37259
source_url: https://wiki.genexus.com/commwiki/wiki?37259
genexus_version: "18"
---

# Transaction Type property

When an EJB is called from a web panel, a new LUW is created. This property determines how the LUW is managed.

### [Values](#Values)

|  |  |
| --- | --- |
| **Object** | The bean behaves as usual, meaning that the object's programmer defines the size of the LUW using the commit and/or rollback commands, as well as the Commit on Exit property. |
| **Container** | The LUW will be managed by the EJB Container. |

### [See Also](#See+Also)

* [Transactional Integrity and Enterprise Java Beans](https://wiki.genexus.com/commwiki/wiki?8012)
