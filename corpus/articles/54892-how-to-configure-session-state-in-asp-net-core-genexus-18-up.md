---
title: "How to configure Session State In ASP.NET Core (GeneXus 18 Upgrade 3)"
source_id: 54892
source_url: https://wiki.genexus.com/commwiki/wiki?54892
genexus_version: "18"
---

# How to configure Session State In ASP.NET Core (GeneXus 18 Upgrade 3)

In this article, you can find the steps to configure a Session State in ASP.NET Core.

Sessions in ASP.NET Core are of two types:

1) InProc (or In-memory)

If your session is in-memory and your application is hosted on Web-Farm environment, you need to use sticky sessions to tie each session to a specific server.

2) OutProc (distributed session)

OutProc session does not require sticky sessions; they are the most preferred way to use session in your application.

Below you will find the necessary steps to configure OutProc sessions.

### [How to configure OutProc - SQL Server Session state in ASP.NET Core](#How+to+configure+OutProc+-+SQL+Server+Session+state+in+ASP.NET+Core)

In SQL Server Session state, the previous version of ASP.NET requires a number of tables and stored Procedures to manage session storage in SQL server. ASP.NET Core requires only one table. This can be generated with "Microsoft.Extensions.Caching.SqlConfig.Tools" tool:

1. Install the tool with:

```
dotnet tool install --global dotnet-sql-cache
```

2. Generate the required table:

```
dotnet sql-cache create <connection string>  <schema>  <table name>
```

For example:

```
dotnet sql-cache create "Data Source=.\sqlexpress2019,1433;Initial Catalog=SessionDatabase;User=test;Password=test;" dbo SessionData

dotnet sql-cache create "Data Source=.\sqlexpress2019;Initial Catalog=SessionDatabase;Integrated Security=True;" dbo SessionData
```

3. Configure connection string in CloudServices.**dev**.config (in web directory, this file is not overwritten by GeneXus on build as the CloudServices.config is) adding the following section:

```
 <Services>
  ...
  <Service>
    <Name>DATABASE</Name>
    <Type>Session</Type>
    <ClassName></ClassName>
    <Properties>
      <Property>
        <Name>SESSION_PROVIDER_ADDRESS</Name>
        <Value>Data Source=.\sqlexpress2019,1433;Initial Catalog=SessionDatabase;User=test</Value>
      </Property>
      <Property>
         <Name>SESSION_PROVIDER_SESSION_TIMEOUT</Name>
         <Value>30</Value>
     </Property>
      <Property>
        <Name>SESSION_PROVIDER_PASSWORD</Name>
        <Value>L3KpX01Y+7yriRShRiH2vS==</Value>
      </Property>
      <Property>
        <Name>SESSION_PROVIDER_SCHEMA</Name>
        <Value>dbo</Value>
      </Property>
      <Property>
        <Name>SESSION_PROVIDER_TABLE_NAME</Name>
        <Value>SessionData</Value> 
      </Property>
    </Properties>
  </Service>
</Services>
```

The password value must be encrypted in the same way Database password is encrypted in appsettings.json. Also, you can use [GxEncryptCMD](https://wiki.genexus.com/commwiki/wiki?45615).

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

2. To use Redis as session state in ASP.NET Core, you need to add the following section to CloudServices.**dev**.config (in web directory, this file is not overwritten by GeneXus on build as the CloudServices.config is):

```
<Services> 
  <Service>
    <Name>REDIS</Name>
    <Type>Session</Type>
    <ClassName></ClassName>
    <Properties>
      <Property>
        <Name>SESSION_PROVIDER_ADDRESS</Name>
        <Value>localhost:6379</Value>
      </Property>
    </Properties>
 </Service> 
</Services>
```

If it is a password configured for Redis at the redis.conf, add it as a property and with the value encrypted in the same way as the Database password is encrypted in appsettings.json. Also, you can use [GxEncryptCMD](https://wiki.genexus.com/commwiki/wiki?45615).

For example:

```
<Services> 
...
  <Service>
    <Name>REDIS</Name>
    <Type>Session</Type>
    <ClassName></ClassName>
    <Properties>
      <Property>
        <Name>SESSION_PROVIDER_ADDRESS</Name>
        <Value>localhost:6379</Value>
      </Property>
      <Property>
        <Name>SESSION_PROVIDER_PASSWORD</Name>
        <Value>L3KpX01Y+7yriRShRiH2vS==</Value>
      </Property>
    </Properties>
 </Service> 
</Services>
```

### [See also](#See+also)

[.NET Generator Troubleshooting](https://wiki.genexus.com/commwiki/wiki?50588)
