---
title: "Database name property"
source_id: 9080
source_url: https://wiki.genexus.com/commwiki/wiki?9080
genexus_version: "18"
---

# Database name property

Used when the environments need database names. It indicates the name of the database that will contain the application's tables and indexes.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This propertyallows you to indicate the application's database name. In the case of working with DB2 for iSeries, you have to indicate the Library name (the [Library list property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?9401,,) allows indicating more alternative library names separated by blanks).

**Note:** If you complete the Database name propertywithseveral library names separated by blanks, the table will be searched in the first library and if it is not found, it may be searched in the next library, but this is not the recommended way to make the definition.

#### [Technologies to access data:](#Technologies+to+access+data%3A)

JDBC, ADO.NET

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute [Build any object](https://wiki.genexus.com/commwiki/wiki?17719) with the purpose of generating the \*.config files.

### [See Also](#See+Also)

[Database Schema Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?9081,,)  
[Library list property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?9401,,)


|  |
| --- |
| **Backlinks** |
| [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) | [Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041) |
| [Deploy to cloud: Step by Step](https://wiki.genexus.com/commwiki/wiki?18250) | [Deploy to cloud: Step by Step (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58032) | [Deploy to GeneXus Prototyping Cloud - FAQ](https://wiki.genexus.com/commwiki/wiki?18292) | [HowTo: Set up an independent Data Store for Workflow tables](https://wiki.genexus.com/commwiki/wiki?25683) |
| [Use Custom JDBC URL Property](https://wiki.genexus.com/commwiki/wiki?9381) | [User Properties](https://wiki.genexus.com/commwiki/wiki?25111) |

---
