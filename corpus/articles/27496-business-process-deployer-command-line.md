---
title: "Business Process Deployer Command line"
source_id: 27496
source_url: https://wiki.genexus.com/commwiki/wiki?27496
genexus_version: "18"
---

# Business Process Deployer Command line

The [Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?11607) utility can be executed command line; just use the -help for further detail.

Net

```
C:\GXFolderInstallation\Packages\Gxpm\Tools\BPDeployer\Net\GXBPDeployer -help
```

Java

```
java -jar C:\GXFolderInstallation\Packages\Gxpm\Tools\BPDeployer\Java\GXBPDeployer.jar -help
```

Usage: GXBPDeployer [-options] <deploy file path>

|  |  |
| --- | --- |
| -help | Print this help page. |
| -nonewversion | Do not create new versions of business processes. |
| -nogui | Do not display GUI. |
| -forcecreatedb | Forces creation of workflow tables before deploy. |
| -currentversion <version> | Specifies that the current workflow tables in the database corresponds to version <version> of the workflow runtime. |
| -noask | Do not ask for confirmation before executing database reorganizations. |
| -serverhost <host> | DNS name or IP of the database server host. |
| -serverport <port> | TCP port where the database server is listening for TCP connections. |
| -dbname <name> | Database name. |
| -userid <user id> | User ID for database connection. |
| -userpwd <user password> | User password for database connection. |
| -addconnattrs <attributes> | .NET only: additional database connection string attributes. |
| -jdbcdriver <driver> | Java only: JDBC driver name. ie: for mysql: com.mysql.jdbc.Driver |
| -jdbcurl <url> | Java only: JDBC URL. |
| -ifxserver <server instance> | Informix server instance |
| -classpath <classpath> | Java only: additional classpath. |
| -interpreter <path> | Java only: optional path of the interpreter to be used when executing the deploy process. |
| -netlogdetail <level> | .NET only: log level, 0 = Off, 1 = Fatal, 2 = Error,  3 = Warn, 4 = Info, 5 = Debug, 6 = All. |
| -netlogfile <path> | .NET only: log file path |
| -jdbclogdetail <level> | Java only: JDBC log level. 0 = High, 1 = Medium, 2 = Low. |
| -jdbclogfile <path> | Java only: log file path |

### [Notes](#Notes)

* By default, any needed database reorganization will be performed automatically before executing the actual deploy. Use the options -forcecreatedb or -currentversion to change this behaviour.
* In Java, if you are using one of the predefined JDBC drivers, the option -jdbcurl can be ignored. Just provide the host, TCP port and database name.

NET

Example:

```
# Net with SQLServer
GXBPDeployer -nogui -jdbcdriver com.microsoft.sqlserver.jdbc.SQLServerDriver -serverhost SERVER_IP -dbname DB_NAME ".\SQLServer.bpd"
```

JAVA

Example:

```
# Java with SQLServer
java -jar GXBPDeployer.jar -nogui -jdbcdriver net.sourceforge.jtds.jdbc.Driver -jdbclogdetail 1 -classpath "C:\Temp\drivers\jtds-1.2.jar" -forcecreatedb -serverhost SERVER_IP -serverport 1433 -dbname DB_NAME -userid USER -userpwd password ".\SQLServer.bpd"
```

### [See Also](#See+Also)

[HowTo: Deploy a Workflow-based Application](https://wiki.genexus.com/commwiki/wiki?19848)  
[Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?11607)


|  |
| --- |
| **Backlinks** |
| [Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?11607) | [Table of contents:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [HowTo: Enable Log for GXflow BPDeployer](https://wiki.genexus.com/commwiki/wiki?51046) |
| [HowTo: Impact the production database in GXflow with the Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?52734) |

---
