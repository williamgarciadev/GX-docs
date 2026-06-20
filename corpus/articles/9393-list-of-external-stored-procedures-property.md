---
title: "List of external stored procedures property"
source_id: 9393
source_url: https://wiki.genexus.com/commwiki/wiki?9393
genexus_version: "18"
---

# List of external stored procedures property

To allow specification of a list of programs stored in the database (stored procedures). The program names must be separated by spaces.

### [Description](#Description)

#### [Note:](#Note%3A)

* This property is kept only for compatibility reasons.
* When the generator finds a call to a program included in the list, it makes a call via JDBC (Java), Ado.Net (.Net) or ODBC (VFP) instead of making a regular call.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [Scope](#Scope)

**Platforms:** Web(.Net, Java)


|  |
| --- |
| **Backlinks** |
| [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) |

---
