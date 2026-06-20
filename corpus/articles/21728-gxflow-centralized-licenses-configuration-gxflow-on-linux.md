---
title: "GXflow centralized licenses configuration (GXflow on Linux)"
source_id: 21728
source_url: https://wiki.genexus.com/commwiki/wiki?21728
genexus_version: "18"
---

# GXflow centralized licenses configuration (GXflow on Linux)

This document helps you to set up a GXflow Application (that runs on Linux) to use licenses from a GeneXus Protection Server (that runs on Windows). As stated in [this document](https://wiki.genexus.com/commwiki/wiki?37204), this protection method is used primarily for prototyping purposes; for production purposes a Native protection method is the most (or only) suitable.

**Warning**: If you are in [GeneXus 15 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?36355,,) or lower, read [How to configure GXflow running in Linux using licenses from a Windows server](https://wiki.genexus.com/commwiki/wiki?37734,,).

So to configure a GXflow Application that runs in Linux to use the protection system from a Windows server, follow these steps:

### [Step 1 – Install GeneXus Protection Server](#Step+1+%E2%80%93+Install+GeneXus+Protection+Server)

Install the latest [GeneXus Protection Server](https://wiki.genexus.com/commwiki/wiki?18887,,) version on a Windows Server. This server will centralize GeneXus licenses products.

### [Step 2 – Configure the GeneXus License Manager](#Step+2+%E2%80%93+Configure+the+GeneXus+License+Manager)

Download the files from [here](https://www.genexus.com/es/developers/downloadcenter?data=4141;;).  
On the Linux server where the application is running install the GeneXus License Manager. You need to unzip the LinuxCSProt.zip file (located in Packages\Gxpm\Protection\Linux under GeneXus installation folder) into a directory, for example, gxprot. The License Manager must be configured via command line options; check Annex I for further detail on License Manager Options. The location for the Protection server is stored in a file called protect.properties (same as Protect.ini in Windows environments); which is used by the Web application and License Manager to locate the Protection Server.

To set the Protection Server location, execute the following:

```
java -Dgxprotect.dir=/gxprot/license –jar licmgr.jar -s server.host=localhost user.domain=localhost user.id=test user.pwd=test123
```

where:

* *-Dgxprotect.dir*: System Property to set the path where the protect.properties file will be generated.
* *server.host*: IP or hostname where the GeneXus Protection server is executing.
* *user.domain*: Windows domain to be used to authenticate with.
* *user.id*: User to be used to authenticate with.
* *user.pwd*: Password to be used to authenticate with.

You don't need to set all properties at once; you can execute the same command several times with different parameters. The specified user to access the server must have security permissions to access the server via DCOM.

### [Step 3 – Configure the application to use the Windows Protection Server](#Step+3+%E2%80%93+Configure+the+application+to+use+the+Windows+Protection+Server)

Open [GXflow license manager](https://wiki.genexus.com/commwiki/wiki?37207) and configure the Remote location settings.

### [Annex I – License Manager Options](#Annex+I+%E2%80%93+License+Manager+Options)

Whenever you run the License Manager you must reference a System Property as a parameter, for example:

java –Dgxprotect.dir=”gxprot” –jar licmgr.jar

It is recommended to explicitly set the directory that will be used to save the properties file. When using the license manager it is advisable to use a system property "gxprotect.dir". License Manager available options are:

`[imagen omitida: wiki id 15075]`


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |
| [HowTo: Deploy a Workflow-based Application](https://wiki.genexus.com/commwiki/wiki?19848) |

---
