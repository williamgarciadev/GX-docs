---
title: "Access technology to set property"
source_id: 9030
source_url: https://wiki.genexus.com/commwiki/wiki?9030
genexus_version: "18"
---

# Access technology to set property

Configures the information required to access the database for all possible technologies.

### [Values](#Values)

|  |  |
| --- | --- |
| **ADO.NET** | Used by the .NET generator defined in the Environment. |
| **iSeries Native** | Used by RPG and Cobol generators defined in the Environment. |
| **Embedded SQL** |
| **JDBC** | Used by the Java generator defined in the Environment. |
| **ODBC** | Used by the Visual FoxPro generator defined in the Environment. |
| **Ruby** | Used by the Ruby generator defined in the Environment (until GeneXus X Evolution 3). |

### [Scope](#Scope)

**Generators:** Cobol, [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604), RPG  
**Level:** [Data Store](https://wiki.genexus.com/commwiki/wiki?7117)

### [Description](#Description)

It is important to point out that when selecting a value in the option ‘Access technology to set’ different options are enabled which are saved separately, and are used by the different generators. For example, you can have one configuration under ADO.NET that is used by all knowledge base objects generated with .NET and under JDBC you have another configuration that is used by the objects generated with Java.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object. |


|  |
| --- |
| **Backlinks** |
| [DataSource property](https://wiki.genexus.com/commwiki/wiki?13604) | [Enable Distributed Transactions property](https://wiki.genexus.com/commwiki/wiki?9243) |
| [Server property](https://wiki.genexus.com/commwiki/wiki?9398) |

---
