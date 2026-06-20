---
title: "Use Application Server Datasource property"
source_id: 44032
source_url: https://wiki.genexus.com/commwiki/wiki?44032
genexus_version: "18"
---

# Use Application Server Datasource property

Indicates whether the deployed application will define the JDBC Datasource in the web.xml configuration file, or an already defined JDBC Datasource in the application server shall be used.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Description](#Description)

This property will be visible only if a Java Environment is being deployed, and if the [Use Datasource for Web Based Applications Property](https://wiki.genexus.com/commwiki/wiki?9384,,) is set to true.

You might already have a Datasource defined in your Application Server configuration file; in this case, the deployed application must use that Datasource, and therefore this property should be set to true.

If, on the other hand, you do not have a Datasource already defined, set this property to false to include the Datasource information in the deployed application's configuration file.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,).

### [See Also](#See+Also)

[Use Datasource for Web Based Applications Property](https://wiki.genexus.com/commwiki/wiki?9384,,)


|  |
| --- |
| **Backlinks** |
| [Deploying a Java application on a JBoss server](https://wiki.genexus.com/commwiki/wiki?46032) |

---
