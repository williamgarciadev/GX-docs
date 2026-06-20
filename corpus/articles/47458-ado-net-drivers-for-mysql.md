---
title: "ADO.NET drivers for MySQL"
source_id: 47458
source_url: https://wiki.genexus.com/commwiki/wiki?47458
genexus_version: "18"
---

# ADO.NET drivers for MySQL

This article states what drivers can be or are used to connect to MySQL from [.NET](https://wiki.genexus.com/commwiki/wiki?38604) and [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) applications, and the benefits of each option.

## [.NET](#.NET)

Since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46852,,) onwards, when using the [GeneXus .NET Generator](https://wiki.genexus.com/commwiki/wiki?38604), only one driver is available: MySQL Connector.

**Note**: In previous versions, MySQL Data provider was used. However, given its poor performance (2:1 compared to MySQL Connector), it is no longer used.

## [.NET Framework](#.NET+Framework)

Since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46852,,) onwards, when using the [GeneXus .NET Framework Generator](https://wiki.genexus.com/commwiki/wiki?2892), in the [ADO.NET provider property](https://wiki.genexus.com/commwiki/wiki?22755) you can choose between these options:

* MySQLDriverCS
* MySQL Connector

### [MySQLDriverCS vs MySQL Connector](#MySQLDriverCS+vs+MySQL+Connector)

|  | Problems | Benefits |
| --- | --- | --- |
| MySQLDriverCS | * Requires the installation of a MySQL Client, with different DLLs depending on the MySQL Version, 32 or 64 bits, etc. This causes issues or troubleshooting costs in different scenarios for development and deployment. * It does not support UTF8 or Emojis. * It has problems related to memory access. These are difficult to solve since the driver is not fully managed (interop with c++). | * Supports multiple data readers (Less memory consumption loading recordsets from the database (\*)). |
| MySQLConnector | * Higher memory consumption when loading recordsets from the database (\*). | * It is fully managed (It does not require any extra installation). * It is maintained by a broad and active open-source community (Dec 2020). |

(\*) The driver does not support multiple server cursors reading data at the same time. Therefore, when you nest reads, all the data of the outer cursor has to be read first and loaded to memory, and then the nested cursor can start executing. More information at [Performance and memory implications depending Drivers support for multiple data readers](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?47953,,).


|  |
| --- |
| **Backlinks** |
| [ADO.NET provider property](https://wiki.genexus.com/commwiki/wiki?22755) |

---
