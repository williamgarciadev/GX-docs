---
title: "UseExternalDatasource Property"
source_id: 7746
source_url: https://wiki.genexus.com/commwiki/wiki?7746
genexus_version: "18"
---

# UseExternalDatasource Property

To allow the conection with an external datasource, using the server pool instead of the GeneXus one.

### [Syntax](#Syntax)

**&***DataType***.UseExternalDatasource** = value  
  
**Type Returned:**

Numeric

### [Values:](#Values%3A)

|  |  |
| --- | --- |
| **1** | Connects using a datasource (server pool) |
| **0** | Connects directly with JDBC (GeneXus pool) |

### [Example](#Example)

&dbcon.UseExternalDatasource = 1

### [Scope](#Scope)

**Extended Data Types:** [DBConnection](https://wiki.genexus.com/commwiki/wiki?6923)  
**Interface:** Web

**Languages:** Java

### [See Also](#See+Also)

[DBConnection](https://wiki.genexus.com/commwiki/wiki?6923)

[ExternalDatasourceName Property](https://wiki.genexus.com/commwiki/wiki?7747)


|  |
| --- |
| **Backlinks** |
| [DBConnection Data Type](https://wiki.genexus.com/commwiki/wiki?6923) | [ExternalDatasourceName Property](https://wiki.genexus.com/commwiki/wiki?7747) |

---
