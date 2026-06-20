---
title: "Informix Version property"
source_id: 9399
source_url: https://wiki.genexus.com/commwiki/wiki?9399
genexus_version: "18"
---

# Informix Version property

Tells GeneXus which Informix version is installed on the Database Server.

### [Values](#Values)

|  |  |
| --- | --- |
| **11 or higher** | Informix 11 is supported as from GeneXus X. |
| **7.31 to 10.X** |

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** INFORMIX  
**Level:** [Data Store](https://wiki.genexus.com/commwiki/wiki?7117)

### [Description](#Description)

### [[Values](https://wiki.genexus.com/commwiki/wiki?9399)](#https%3A%2F%2Fwiki.genexus.com%2Fcommwiki%2Fservlet%2Fwiki%3F9399%2CInformix%2BVersion%2BProperty%23Values+Values)

**7.31 to 8X**

**Default Value** = 11 or higher

Every new version of the DBMS has new features that are used by GeneXus. This generates different SQL sentences or considers properties that can be applied to the new version.

Informix supports the management of Outer Join with a proprietary syntax (Informix-Extension Outer Joins). And from its 7.x engines, the syntax defined in the SQL-92 standard. The proprietary syntax is called "Informix-Extension Outer Joins", with a significant difference existing between both syntaxes, based on the order in which conditions are assessed.

To make this clear: when you have an Outer Join and want to apply a filter for an attribute in the extended table, Informix proprietary syntax first applies the filters of each table assessing conditions (minimizing the number of records returned), and then applies the JOINS, whereas with the ANSI syntax, the order in which conditions are assessed is well specified on the syntax itself (the Join condition is in one place and the overall conditions go in the associated Where section).

The idea in fact is for conditions assessments to be run post-join; that is: the ANSI syntax allows the specification of post-join filters, while the Informix proprietary syntax (Informix-Extension Outer Joins) returns different results and applies filters prior to joins (pre-join filters).

**DBMS:**  Informix.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691). |

### [See Also](#See+Also)

[SQL server version property](https://wiki.genexus.com/commwiki/wiki?9114)

[Oracle version property](https://wiki.genexus.com/commwiki/wiki?9112)

[Informix Version property](https://wiki.genexus.com/commwiki/wiki?9399)

[MySQL version property](https://wiki.genexus.com/commwiki/wiki?9420)

[DB2 UDB Version property](https://wiki.genexus.com/commwiki/wiki?10479)


|  |
| --- |
| **Backlinks** |
| [DB2 UDB Version property](https://wiki.genexus.com/commwiki/wiki?10479) | [DB2UDB version property](https://wiki.genexus.com/commwiki/wiki?9397) | [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) |
| [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55768) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) | [GXflow Software Requirements](https://wiki.genexus.com/commwiki/wiki?18393) |
| [GXflow Software Requirements (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55579) | [Informix Version property](https://wiki.genexus.com/commwiki/wiki?9399) | [MySQL version property](https://wiki.genexus.com/commwiki/wiki?9420) | [Oracle version property](https://wiki.genexus.com/commwiki/wiki?9112) |
| [SQL server version property](https://wiki.genexus.com/commwiki/wiki?9114) |

---
