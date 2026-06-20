---
title: "GeneXus FAQ - How to backup a KB?"
source_id: 5735
source_url: https://wiki.genexus.com/commwiki/wiki?5735
genexus_version: "18"
---

# GeneXus FAQ - How to backup a KB?

To back up a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) you just need to back up the associated SQL Server database.

To know which is the associated SQL Server database of a Knowledge Base, explore its directory and open the Knowledgebase.connection file with a text editor.

You will find information like the following:

```
<ConnectionInformation>
	<DBName>GX_KB_Sample</DBName>
	<IntegratedSecurity>True</IntegratedSecurity>
	<ServerInstance>MySQLServer\SQLEXPRESS</ServerInstance>
	<CreateDbInKbFolder>True</CreateDbInKbFolder>
	<Directory>C:\Models\Sample</Directory>
	<DataFile>GX_KB_Sample.mdf</DataFile>
	<LogFile>GX_KB_Sample_log.LDF</LogFile>
	<HostName>MyMachine</HostName>
</ConnectionInformation>
```

The database you have to back up is the one named "GX\_KB\_Sample" in the "MyServer\SQLEXPRESS" SQL Server instance.

You can just use the SQL Server backup option in order to back up the DB or backup the MDF file.

**Be sure that no one is using the KB while you're doing the back up.**

### [See Also](#See+Also)

[HowTo: Create a KB From an .MDF](https://wiki.genexus.com/commwiki/wiki?8276)


|  |
| --- |
| **Backlinks** |
|
| [Steps to build with GeneXus 18 a KB of GeneXus 17 or prior](https://wiki.genexus.com/commwiki/wiki?52345) |

---
