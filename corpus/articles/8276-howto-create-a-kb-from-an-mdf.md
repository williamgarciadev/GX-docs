---
title: "HowTo: Create a KB From an .MDF"
source_id: 8276
source_url: https://wiki.genexus.com/commwiki/wiki?8276
genexus_version: "18"
---

# HowTo: Create a KB From an .MDF

All [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) information is stored in an SQL Server database. So, with that database, you can create the [KB](https://wiki.genexus.com/commwiki/wiki?2428) and build all again. You can also copy or duplicate a Knowledge Base in a new folder.

All that you need to do for creating a KB from an MDF, is just to select the .mdf file in the ["Open KB" dialog](https://wiki.genexus.com/commwiki/wiki?9599):

`[imagen omitida: wiki id 10439]`

### [Steps to manually restore the KB or duplicate it in another folder](#Steps+to+manually+restore+the+KB+or+duplicate+it+in+another+folder)

Suppose you have the GX\_KB\_TEST.mdf and GX\_KB\_TEST.LDF files, and you want to open them as a KB with GeneXus. Follow these steps:

**1.** Copy GX\_KB\_TEST.mdf and GX\_KB\_TEST.LDF files to a directory, like, for example, c:\Models\Test.

**2.** Create an empty file called Test.gxw in C:\Models\Test.

**3.** Create a text file named 'knowledgebase.connection'. Open it with notepad, and add the following text:

```
<ConnectionInformation>
    <DBName>GX_KB_Test</DBName>
    <IntegratedSecurity>True</IntegratedSecurity>
    <ServerInstance>SERVERNAME\SQLEXPRESS</ServerInstance>
    <CreateDbInKbFolder>False</CreateDbInKbFolder>
</ConnectionInformation>
```

Make sure to change connection parameters according to your local environment.

**1.** Go to the SQL Server Management Studio, log in to SERVERNAME\SQLEXPRESS with integrated security (trusted connection) and [Attach](http://technet.microsoft.com/en-us/library/ms190209.aspx) the MDF.

**2.** In GeneXus, click on **File > Open > Knowledge Base** and select the C:\Models\Test\Test.gxw file.

Enjoy!

If you find any troubles, check [Basic tips about Managing KBs using SQL Server](https://wiki.genexus.com/commwiki/wiki?6543,,).

### [Copying an mdf from another PC](#Copying+an+mdf+from+another+PC)

There is an easier way to create a Knowledge Base from an .mdf file, that only works when the .mdf file is brought from another PC. The following steps are not supposed to be used in order to duplicate a local KB to another folder in the same PC.

**1.** Copy the GX\_KB\_TEST.mdf file to a directory,  for example, c:\Models\Test.

**2.** In GeneXus click on **File > Open > Knowledge Base** and select the C:\Models\Test\GX\_KB\_TEST.mdf.

Enjoy!


|  |
| --- |
| **Backlinks** |
| [GeneXus FAQ - How to backup a KB?](https://wiki.genexus.com/commwiki/wiki?5735) | [Open - Knowledge Base](https://wiki.genexus.com/commwiki/wiki?9599) |

---
