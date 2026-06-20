---
title: "HowTo: Configure Session State In ASP.NET Core"
source_id: 50626
source_url: https://wiki.genexus.com/commwiki/wiki?50626
genexus_version: "18"
---

# HowTo: Configure Session State In ASP.NET Core

In this article, you can find the steps to configure a session state in ASP.NET Core using the OutProc approach.

Sessions in ASP.NET Core are of two types:

1. InProc (or In-memory)  
     
   If your session is in-memory and your application is hosted on a Web-Farm environment, you need to use sticky sessions to tie each session to a specific server.
2. OutProc (distributed session)  
     
   OutProc session does not require sticky sessions; they are the most preferred way to use session in your application.

Below you will find the necessary steps to configure OutProc sessions using SQL server and  Redis.

### [How to configure OutProc - SQL Server Session state in ASP.NET Core](#How+to+configure+OutProc+-+SQL+Server+Session+state+in+ASP.NET+Core)

In the previous version of ASP.NET, to manage session storage in SQL Server, a set of tables and stored procedures were required. However, in ASP.NET Core, only one table is required. This table can be easily generated using the "Microsoft.Extensions.Caching.SqlConfig.Tools" tool, as shown below:

1. Install the tool with the following code:

```
dotnet tool install --global dotnet-sql-cache
```

2. Then, generate the required table:

```
dotnet sql-cache create <connection string>  <schema>  <table name>
```

For example:

```
dotnet sql-cache create "Data Source=.\sqlexpress2019,1433;Initial Catalog=SessionDatabase;User=test;Password=test;" dbo SessionData

dotnet sql-cache create "Data Source=.\sqlexpress2019;Initial Catalog=SessionDatabase;Integrated Security=True;" dbo SessionData
```

3. Finally, go to Preferences > Back end, select the Generator, and configure the following:

* [Session Timeout property](https://wiki.genexus.com/commwiki/wiki?54781)
* [Session State Provider property](https://wiki.genexus.com/commwiki/wiki?54782) = Database
* [SQL Server Data Store property](https://wiki.genexus.com/commwiki/wiki?55060)
* [Database Table Name property](https://wiki.genexus.com/commwiki/wiki?54777)

### [Note](#Note)

When using Web Server = Internet Information Server ensure that the user configured in the app pool has enough permissions to access the registry. For example by default Local System user has access. This is required to persist Data Protections Keys. If it does not have access you can see warnings like these at web\logs\\*.log files after accessing the website hosted in iis:

```
warn: Microsoft.AspNetCore.DataProtection.Repositories.EphemeralXmlRepository[50]
      Using an in-memory repository. Keys will not be persisted to storage.
warn: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[59]
      Neither user profile nor HKLM registry available. Using an ephemeral key repository. Protected data will be unavailable when application exits.
warn: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[35]
      No XML encryptor configured. Key {b2577f9d-c6bc-4920-b1ca-84804c9ff0c4} may be persisted to storage in unencrypted form.
```

When it works properly a message like this will appear in web\logs\\*.log file after accesing for the first page the web application:

```
info: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[63]
      User profile is available. Using 'C:\Windows\system32\config\systemprofile\AppData\Local\ASP.NET\DataProtection-Keys' as key repository and Windows DPAPI to encrypt keys at rest.
```

To test if it works, set a session variable:

```
 &WebSession.Set('mykey','myvalue')
```

and get the same session value after recycling the aspnet process:

```
if (&WebSession.Get('mykey') = 'myvalue')
 msg("Session persisted")
endif
```

It should return the same value setted before.

### [Configure OutProc - Redis Session state in ASP.NET Core](#Configure+OutProc+-+Redis+Session+state+in+ASP.NET+Core)

[Redis](https://redis.io/docs/) [documentation](https://redis.io/) is an open-source and in-memory data store that is used as a distributed cache. You can install it locally and configure it. Also, you can configure an Azure Redis Cache.

One way to have Redis on Windows is by installing [Redis Server](https://github.com/microsoftarchive/redis/releases/tag/win-3.2.100) from https://github.com/microsoftarchive/redis/releases:

1. Once Redis Server is installed, start Redis Server:

redis-server.exe

2. To use Redis as a session state in ASP.NET Core, you must go to Preferences > Back end, select the Generator, and configure the following:

* [Session Timeout property](https://wiki.genexus.com/commwiki/wiki?54781)
* [Session State Provider property](https://wiki.genexus.com/commwiki/wiki?54782) = Redis
* [Location property at Back end Generator level](https://wiki.genexus.com/commwiki/wiki?54883)
* [Instance Name property](https://wiki.genexus.com/commwiki/wiki?54780)
* [Password property at Back end Generator level](https://wiki.genexus.com/commwiki/wiki?54884)

### [See Also](#See+Also)

[.NET Generator Troubleshooting](https://wiki.genexus.com/commwiki/wiki?50588)


|  |
| --- |
| **Backlinks** |
| [Toc:.NET Applications Development](https://wiki.genexus.com/commwiki/wiki?53971) | [Database Table Name property](https://wiki.genexus.com/commwiki/wiki?54777) | [How to configure Session State In ASP.NET Core (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54892) |
| [Instance Name property](https://wiki.genexus.com/commwiki/wiki?54780) | [Password property at Back end Generator level](https://wiki.genexus.com/commwiki/wiki?54884) | [Session State Provider property](https://wiki.genexus.com/commwiki/wiki?54782) | [Session Timeout property](https://wiki.genexus.com/commwiki/wiki?54781) |
| [SQL Server Data Store property](https://wiki.genexus.com/commwiki/wiki?55060) |

---
