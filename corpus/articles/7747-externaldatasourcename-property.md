---
title: "ExternalDatasourceName Property"
source_id: 7747
source_url: https://wiki.genexus.com/commwiki/wiki?7747
genexus_version: "18"
---

# ExternalDatasourceName Property

To allow the conection with an external datasource, using the server pool instead of the GeneXus one.

When the connection is through an external datasource (UseExternalDatasource = 1), the name of the datasource must be set in this property.

### [Syntax](#Syntax)

**&***DataType***.UseExternalDatasource** = value  
  
**Type Returned:**

Character

### [Example](#Example)

&dbcon.ExternalDatasourceName = "jdbc/orabarba1"

### [Scope](#Scope)

**Extended Data Types:** [DBConnection](https://wiki.genexus.com/commwiki/wiki?6923)  
**Interface:** Web

**Languages:** Java

### [See Also](#See+Also)

[DBConnection](https://wiki.genexus.com/commwiki/wiki?6923)

[UseExternalDatasource Property](https://wiki.genexus.com/commwiki/wiki?7746)


|  |
| --- |
| **Backlinks** |
| [DBConnection Data Type](https://wiki.genexus.com/commwiki/wiki?6923) | [UseExternalDatasource Property](https://wiki.genexus.com/commwiki/wiki?7746) |

---
