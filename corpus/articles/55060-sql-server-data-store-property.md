---
title: "SQL Server Data Store property"
source_id: 55060
source_url: https://wiki.genexus.com/commwiki/wiki?55060
genexus_version: "18"
---

# SQL Server Data Store property

Specifies the SQL Server Data Store to save session data when the "Database" value is chosen as the Session State Provider.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604)  
**Level:** Generator

### [Description](#Description)

This property is part of the configuration to handle session state in a web application when using "Database" as the [Session State Provider](https://wiki.genexus.com/commwiki/wiki?54782).

This property is configured together with the [Database Table Name property](https://wiki.genexus.com/commwiki/wiki?54777).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

To create the necessary database and table, you can use the dotnet sql-cache command. However, you must make sure that you have previously installed the dotnet-sql-cache tool globally. Otherwise, you can do it using the command:

dotnet tool install --global dotnet-sql-cache

Then you can create the database using the following command as an example:

dotnet sql-cache create "Data Source=.\sqlexpress2019,1433;Initial Catalog=SessionDatabase;User=myuser;Password=mypassword;" dbo SessionData

Where the Data Source=.\sqlexpress2019,1433 part of the connection string corresponds to the database server name, with sqlexpress2019 as the hostname and 1433 as the port number.

This information is needed to establish the connection to the database server.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).

### [See Also](#See+Also)

[HowTo: Configure Session State In ASP.NET Core](https://wiki.genexus.com/commwiki/wiki?50626)


|  |
| --- |
| **Backlinks** |
| [Database Table Name property](https://wiki.genexus.com/commwiki/wiki?54777) | [HowTo: Configure Session State In ASP.NET Core](https://wiki.genexus.com/commwiki/wiki?50626) |

---
