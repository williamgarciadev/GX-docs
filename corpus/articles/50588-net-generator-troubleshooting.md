---
title: ".NET Generator Troubleshooting"
source_id: 50588
source_url: https://wiki.genexus.com/commwiki/wiki?50588
genexus_version: "18"
---

# .NET Generator Troubleshooting

In this article, you can find the most common errors related to the use of the [.NET Generator](https://wiki.genexus.com/commwiki/wiki?38604) and solutions to fix them quickly.

### [SQL LocalDB connection failures](#SQL+LocalDB+connection+failures)

SQL LocalDB works over Windows ARM, so you can create your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) by using SQL LocalDB.

When trying to use the public instance MSSQLLocalDB for the generated .NET application hosted at IIS, the following error can appear:

*DBMS Error Code:-1983577832.A network-related or instance-specific error occurred while establishing a connection to SQL Server. The server was not found or was not accessible. Verify that the instance name is correct and that SQL Server is configured to allow remote connections. (provider: SQL Network Interfaces, error: 50 - Local Database Runtime error occurred. Cannot create an automatic instance. See the Windows Application event log for error details.*

This error occurs when a Database is created using the Windows identity user at runtime. The web app connects to the Database with the IIS user (since [Use trusted connection property](https://wiki.genexus.com/commwiki/wiki?9418) =True at Datastore) which does not have access to the database unless the instance is a [shared instance](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/sql-server-express-localdb?view=sql-server-ver15#shared-instances-of-localdb), which is not the case of MSSQLLocalDB.

The error does not happen if the web server = Kestrel since that process executes by default with the same user logged in.

A shared instance can be created with the following commands:

```
SqlLocalDB.exe create LocalTestInstance
SqlLocalDB.exe share "LocalTestInstance"  "LocalSharedInstance"
```

Then set the DataStore properties:

```
Server Name = (localdb)\.\LocalSharedInstance
//Note that \.\ (backslash + dot + backslash) is needed for a shared instance.
Database name = <any name>
```

When using a LocalDB installed on Windows 11 ARM in a Parallels VM on a MacBook the following error can appear:

*Internal error: Function call failed (A network-related or instance-specific error occurred while establishing a connection to SQL Server. The server was not found or was not accessible. Verify that the instance name is correct and that SQL Server is configured to allow remote connections. (provider: SQL Network Interfaces, error: 56 - Unable to load the SQLUserInterface.dll from the location specified in the registry. Verify that the Local Database Runtime feature of SQL Server Express is properly installed. ))*

When that error occurs, try to connect (using Named Pipes) to the instance pipe name. Use the following command to get the instance pipe name:

```
C:\Dev>sqllocaldb info mssqllocaldb
Name:               MSSQLLocalDB
Version:            13.1.4001.0
Shared name:
Auto-create:        Yes
State:              Running
Last start time:    5/27/2022 3:20:50 PM
Instance pipe name: np:\\.\pipe\LOCALDB#AC106136\tsql\query
```

and then change the Data Store's Server name:

`[imagen omitida: wiki id 50943]`

### [Warning when running a Web application in .NET](#Warning+when+running+a+Web+application+in+.NET)

The following **warning**can be printed at Kestrel or Docker container when running a web application in .NET:

Warning in Docker container console:

```
{"EventId":7,"LogLevel":"Warning","Category":"Microsoft.AspNetCore.Session.SessionMiddleware","Message":"Error unprotecting the session cookie.","Exception":"System.Security.Cryptography.CryptographicException: The key {a047273b-f0b0-4f7b-a97c-c1da083a1b05} was not found in the key ring. For more information go to http://aka.ms/dataprotectionwarning at Microsoft.AspNetCore.DataProtection.KeyManagement.KeyRingBasedDataProtector.UnprotectCore(Byte[] protectedData, Boolean allowOperationsOnRevokedKeys, UnprotectStatus\u0026 status) at Microsoft.AspNetCore.DataProtection.KeyManagement.KeyRingBasedDataProtector.Unprotect(Byte[] protectedData) at Microsoft.AspNetCore.Session.CookieProtection.Unprotect(IDataProtector protector, String protectedText, ILogger logger)","State":{"Message":"Error unprotecting the session cookie.","{OriginalFormat}":"Error unprotecting the session cookie."}}
```

Warning in Kestrel console:

```
warn: Microsoft.AspNetCore.Session.SessionMiddleware
Error unprotecting the session cookie.
System.Security.Cryptography.CryptographicException: The key {...} was not found in the key ring. For more information go to http://aka.ms/dataprotectionwarning
```

#### [Steps to reproduce on Docker:](#Steps+to+reproduce+on+Docker%3A)

1. Start a container instance
2. Run the web application
3. Stop the container and start again
4. Refresh the browser and the error is displayed in the container.

#### [Steps to reproduce on Windows when running Kestrel Web Server:](#Steps+to+reproduce+on+Windows+when+running+Kestrel+Web+Server%3A)

1. Run the web application (F5 in GeneXus)
2. Stop and close the Kestrel window
3. Remove \*.xml from %USERPROFILE%\AppData\Local\ASP.NET\DataProtection-Keys
4. Run again from GeneXus
5. Refresh browser; the error is displayed on the Kestrel output.

The error happens because the session cookies are encrypted with a key that changes when running a different container instance or Kestrel process; ASP.NET Core generates different keys to encrypt data in these cases. So when the web page containing a stale cookie (generated with a previous container instance) is refreshed, that cookie cannot be decrypted at the server-side with the new key. The error is printed, and a new one is generated.

#### [How to avoid the error](#How+to+avoid+the+error)

1. Store the session in a distributed storage
2. Delete all existing cookies in the browser for this website before refreshing to access the new container instance or Kestrel process.

More about it at: https://docs.microsoft.com/en-us/aspnet/core/security/data-protection/configuration/overview?view=aspnetcore-6.0#persisting-keys-when-hosting-in-a-docker-container.

### [error MSB4018: The "ResolveAssemblyReference" task failed unexpectedly](#error+MSB4018%3A+The+%22ResolveAssemblyReference%22+task+failed+unexpectedly)

In some projects, in not determined cases, you may get this error in compilation time. The problem stops appearing when you compile again.

```
dotnet build -nologo --force -c Release /v:q /m /p:GxExternalReference=GeneXus.Security.API.Common.dll "d:\Models\MyKB\NetModel\build\LastBuild.sln"
C:\Program Files\dotnet\sdk\6.0.100\Microsoft.Common.CurrentVersion.targets(2304,5): error MSB4018: The "ResolveAssemblyReference" task failed unexpectedly. [d:\Models\MyKB\NetModel\build\raca\raca.csproj]
C:\Program Files\dotnet\sdk\6.0.100\Microsoft.Common.CurrentVersion.targets(2304,5): error MSB4018: System.IO.IOException: The process cannot access the file 'd:\Models\MyKB\NetModel\web\bin\Microsoft.Identity.Client.dll' because it is being used by another process. [d:\Models\MyKB\NetModel\build\raca\raca.csproj]
...
```

This error occurs when GeneXus uses msbuild to [compile multiple projects at the same time](https://docs.microsoft.com/en-us/visualstudio/msbuild/building-multiple-projects-in-parallel-with-msbuild?view=vs-2022). This is the default behavior in .NET projects built with GeneXus. The solution is to not compile in parallel, which will lower the compilation performance and increase build time. To not compile in parallel you can remove the /m modifier from the [MSBuild options property](https://wiki.genexus.com/commwiki/wiki?44168) (or set it to /m:1 and use just one processor).

### [HRESULT: 0x800700C1 An error occurred while loading required library hostpolicy.dll](#HRESULT%3A+0x800700C1+An+error+occurred+while+loading+required+library+hostpolicy.dll)

Compiling any main object the following error appears:

```
========== DeveloperMenu Compilation for Default (.NET) started ==========
dotnet publish -nologo -v q  "C:\KBs\Knowledge Base\NETSQLServer002\web\GxDeps.csproj" -o "C:\KBs\Knowledge Base\NETSQLServer002\web\bin"
Failed to load the dll from [C:\Program Files\dotnet\shared\Microsoft.NETCore.App\6.0.20\hostpolicy.dll], HRESULT: 0x800700C1
An error occurred while loading required library hostpolicy.dll from [C:\Program Files\dotnet\shared\Microsoft.NETCore.App\6.0.20]
Failed: DeveloperMenu Compilation for Default (.NET)
```

This may occur if you installed a x32 version of the .Net SDK on a x64 Windows machine. Review the installation process, use the "*where dotnet.exe*" command to locate the installation folder.


|  |
| --- |
| **Backlinks** |
| [Table of contents:.NET Applications Development](https://wiki.genexus.com/commwiki/wiki?53971) | [How to configure Session State In ASP.NET Core (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54892) | [HowTo: Configure Session State In ASP.NET Core](https://wiki.genexus.com/commwiki/wiki?50626) |

---
