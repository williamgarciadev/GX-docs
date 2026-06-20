---
title: "ADO.NET drivers for PostgreSQL"
source_id: 47954
source_url: https://wiki.genexus.com/commwiki/wiki?47954
genexus_version: "18"
---

# ADO.NET drivers for PostgreSQL

GeneXus supports connecting to PostgreSQL using the .NET Framework and .NET Generators. Below is a list of which drivers can be or are used, including the benefits of each option.

## [Npgsql 1.0.0](#Npgsql+1.0.0)

To use Npgsql 1.0.0 in the .NET Framework Generator, download and copy the following to your GeneXus installation folder:

* npgsql.dll version 1.0.0.0
* Mono.Security.dll version 1.0.0.0

## [Npgsql 3.2.7](#Npgsql+3.2.7)

The .NET and .NET Framework Generators use npgsql.dll 3.2.7 by default.

## [Comparing versions](#Comparing+versions)

|  | Problems | Benefits |
| --- | --- | --- |
| Npgsql 1.0 | * Does not support PostgreSQL 13 | * Supports multiple data readers (less memory consumption when loading recordsets from the database (\*)) |
| Npgsql 3.x or higher | * Higher memory consumption when loading recordsets from the database (\*) | * Supports PostgreSQL 11 or higher (including PostgreSQL 13) * Supports **Auto-prepare** to improve performance |

(\*) The driver does not support multiple server cursors reading data at the same time. Therefore, when you nest reads, all the data of the outer cursor has to be read first and loaded to memory, and then the nested cursor can start running. More information at [Performance and memory implications depending on Drivers support for multiple data readers](https://wiki.genexus.com/commwiki/wiki?47953,,).

### [Auto-Prepare: Higher Performance](#Auto-Prepare%3A+Higher+Performance)

**Version 3.2.7** or higher supports auto-prepare (<https://www.npgsql.org/doc/prepare.html>).

To enable this feature, add '**Max Auto Prepare**=N' to the [Additional connection string attributes property](https://wiki.genexus.com/commwiki/wiki?9037), where N is an integer number > 0.

#### [Max Auto Prepare](#Max+Auto+Prepare)

Defines the maximum limit of SQL statements that can be automatically prepared at any given time. When this limit is reached, the least used statement is recycled.

To enable it, you must add 'Max Auto Prepare=N', where zero is the default value, meaning that the function is disabled. For example, with Max Auto Prepare=50, Npgsql will prepare up to 50 SQL commands automatically.

This setting is crucial in applications with limited SQL command repetition, thus reducing the load on the server when compiling and caching statements, improving performance, and reducing latency, especially in high-traffic environments.

The optimal value for Max Auto Prepare depends on the specific application and the frequency with which statements are repeated. Keeping a larger number of prepared statements in memory can speed up the execution of previously used statements, although this also means higher memory usage.

### [See Also](#See+Also)

<https://www.npgsql.org/doc/connection-string-parameters.html>


|  |
| --- |
| **Backlinks** |
| [PostgreSQL version property](https://wiki.genexus.com/commwiki/wiki?9419) |

---
