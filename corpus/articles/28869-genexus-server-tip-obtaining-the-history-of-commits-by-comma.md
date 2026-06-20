---
title: "GeneXus Server Tip: Obtaining the history of commits by command line"
source_id: 28869
source_url: https://wiki.genexus.com/commwiki/wiki?28869
genexus_version: "18"
---

# GeneXus Server Tip: Obtaining the history of commits by command line

The ability to query the history of commits applied to a given version of a KB in a GXserver is a very convenient and necessary resource. 

Even when this may be simply done in GeneXus with the [Team Development](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18296,,) option of a local version of the KB connected to GXserver, from the [GeneXus Server KB Activity](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?26485,,), in some cases it has become necessary to make the query by command line.

An example would be integrating that information with an external system to manage incidents/tickets/issues.

To do so, a tool command line called TeamDev.exe is under the GeneXus installation path.

When the TeamDev.exe file is executed directly, without parameters, it is possible to view all the options available1. In this case, the invocation should be made with the *history* command.

The output is a plain text list of commits and all the related data. You can use the -x parameter to obtain it formatted as XML.

**Examples**

* Obtaining all commits within a date range:

```
teamdev history /s:http://localhost/GeneXusServer /kb MyKB /u local\admin /p admin123 /from 2013-08-08T10:30:00 /to 2015-08-08T10:35:00
```

* Obtaining all the commits whose comments include a ticket/issue number, such as #TCK00012#:

```
teamdev history /s:http://localhost/GeneXusServer /kb Tests /u local\admin /p admin123 /q:"comment:'#TCK00012#'"
```

* When the -x parameter is added, the output is obtained in XML format. In addition, the following example redirects the output to obtain a Result.xml file.

```
teamdev history /s:http://localhost/GeneXusServer /kb Tests /u local\admin /p admin123 /q:"comment:'#Tck00012#'"  -x  > Result.xml
```

**Notes**

It is advisable to use dates in UTC format (there is a parameter to indicate this).

A temporary restriction exists where the TeamDev.exe will not function against a GXserver lacking security (user / password).

1 TeamDev.exe options:

```
Usage: TeamDev.exe [@argfile] <Command> [/ServerUrl|s:<value>] [/ServerUsername|u:<value>] [/ServerPassword|p:<value>][/ServerKbAlias|kb:<value>] [/ServerKbVersion|v:<value>]    [/FromDate|from:<value>] [/ToDate|to:<value>] [/XmlOutput|x|xml[+|-]] [/UtcTimes|utc[+|-]] [/RevisionId|r:<value>] [/SearchQuery|q:<value>] [/help|?|h] [/version|v]

@argfile                  Read arguments from a file.
Command                   history
/ServerUrl:<value>        GXserver URL (Default is "")
/ServerUsername:<value>   GXserver user name (Default is "")
/ServerPassword:<value>   GXserver user password (Default is "")
/ServerKbAlias:<value>    GXserver KB alias (Default is "")
/ServerKbVersion:<value>  GXserver KB version (Default is "")
/FromDate:<value>         Minimum date
/ToDate:<value>           Maximum date
/XmlOutput[+|-]           Output in XML
/UtcTimes[+|-]            Times in UTC
/RevisionId:<value>       Revision Id (Default is "0")
/SearchQuery:<value>      Search query (Default is "")
/help                     Show usage.
/version                  Show version.
```
