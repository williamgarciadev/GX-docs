---
title: "Default KB language and Database Collation"
source_id: 42336
source_url: https://wiki.genexus.com/commwiki/wiki?42336
genexus_version: "18"
---

# Default KB language and Database Collation

GeneXus Knowledge Bases can have many languages but only one will be the default. It is specified in the Knowledge Base [Kb Language property](https://wiki.genexus.com/commwiki/wiki?7671).

Every text inserted in the Knowledge Base objects (objects descriptions, attributes descriptions, string inserted in events and rules codes, etc.) will be considered to be in this language. If the [Kb Language](https://wiki.genexus.com/commwiki/wiki?7671) value is *Spanish* and you have this line TextBlock.Caption = "日本語" (Japanese language) in an object events code, the "日本語" literal will be taken as a Spanish literal.

GeneXus Knowledge Bases are stored in a SQL Server database and saves the default language literals in this database tables, so we need to consider setting the appropriate collation in the KB database in order to support the default language characters.

The collation to a new Knowledge Base database can be set when [creating it](https://wiki.genexus.com/commwiki/wiki?9596). This is very important because the database collation cannot be changed after the database is created.

### [Examples](#Examples)

Some known collations are:

|  |  |
| --- | --- |
| English (US) | SQL\_Latin1\_General\_CP1\_CI\_AS |
| Japanese | Japanese\_CI\_AS |
| Chinese (PRC) | Chinese\_PRC\_CI\_AS |
| Arabic | Arabic\_CI\_AS |
| Spanish | Modern\_Spanish\_CI\_AS |
| English (non US)  Portuguese  Italian | Latin1\_General\_CI\_AS |

**Warning**: Always use CI (Case Insensitive) and AS (Accent Sensitive) when selecting your Collation..

For more detail check [SQL Server Collation Settings](https://docs.microsoft.com/es-es/previous-versions/sql/sql-server-2008-r2/ms143508(v=sql.105)).

## [Application Database](#Application+Database)

The same issue happens if you use SQLServer for prototyping your application, make sure to use the correct collation configuration. You can manually create the database with the desired collation as follows:

```
CREATE DATABASE [DatabaseName]
COLLATE <InsertCorrectCollationHere>
GO
```

Then, use [Create Database](https://wiki.genexus.com/commwiki/wiki?7877) command to create the tables.

## [Troubleshooting](#Troubleshooting)

### [Question Marks ??????? or funny characters is displayed on the generated application](#Question+Marks+%3F%3F%3F%3F%3F%3F%3F+or+funny+characters+is+displayed+on+the+generated+application)

An application is executed and question marks are displayed instead of the correct characters. It could be on the application labels or database values.

`[imagen omitida: wiki id 42337]`

This is a hint there is a problem with the KB Database collation or the Application database collation or UTF encoding. Review the case based on this article; once the correct collation is configured characters are correctly seen:

`[imagen omitida: wiki id 42338]`

### [The SQL Server instance 'Localhost\SQLEXPRESS' chosen for the Knowledge Base storage does not support the collation 'Latin1\_General\_100\_CI\_AS\_SC\_UTF8' required to create the Knowledge Base. (Details)](#The+SQL+Server+instance+%27Localhost%5CSQLEXPRESS%27+chosen+for+the+Knowledge+Base+storage+does+not+support+the+collation+%27Latin1_General_100_CI_AS_SC_UTF8%27+required+to+create+the+Knowledge+Base.+%28Details%29)

The following error appears when creating a KB from gxserver.

```
error: The SQL Server instance 'Localhost\SQLEXPRESS' chosen for the Knowledge Base storage does not support the collation 'Latin1_General_100_CI_AS_SC_UTF8' required to create the Knowledge Base. (Details)
Failed: Create Knowledge Base
```

The default database collation is *Latin1\_General\_100\_CI\_AS\_SC\_UTF8* when using SQLServer 2019/LocalDB 15 or higher since [GeneXus 17 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?49616,,). You need to install an equivalent version locally to download the KB ([SAC#50653](https://www.genexus.com/developers/websac?en,,,50653)).

## [See Also](#See+Also)

[Working with Collations](https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms187582(v=sql.105))  
[Collation and International Terminology](https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143726(v=sql.105))  
[International Considerations for Databases and Database Engine Applications](https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms190245(v=sql.105))


|  |
| --- |
| **Backlinks** |
| [Default KB language and Database Collation (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?53433) | [HowTo: Add RTL styles](https://wiki.genexus.com/commwiki/wiki?42319) | [HowTo: Add RTL styles (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54443) |
| [Workstation Settings](https://wiki.genexus.com/commwiki/wiki?42339) |

---
