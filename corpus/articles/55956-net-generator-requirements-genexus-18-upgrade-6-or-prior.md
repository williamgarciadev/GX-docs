---
title: ".NET Generator Requirements (GeneXus 18 Upgrade 6 or prior)"
source_id: 55956
source_url: https://wiki.genexus.com/commwiki/wiki?55956
genexus_version: "18"
---

# .NET Generator Requirements (GeneXus 18 Upgrade 6 or prior)

This article states the requirements of the .NET Generator requirements for development.

### [.NET SDK](#.NET+SDK)

To build .NET applications, you need to install .NET 6.x SDK, which is available here: [.NET 6 (LTS)](https://dotnet.microsoft.com/download/dotnet/6.0).

### [Optional: Run web applications using IIS](#Optional%3A+Run+web+applications+using+IIS)

By default, the .NET generator runs web applications in the Kestrel web server that is included in the .NET SDK. To run the application with IIS working as a reverse proxy in front of Kestrel,

* Install [ASP.NET Core Runtime 6.x Hosting Bundle](https://dotnet.microsoft.com/download/dotnet/6.0) (e.g. dotnet-hosting-6.0.3-win.exe). It requires a restart of IIS.
* Set the generator's [Web Server property](https://wiki.genexus.com/commwiki/wiki?9017) to "Internet Information Server."

### [DBMS Drivers](#DBMS+Drivers+)

In build time, an internet connection to nuget.org is required in several cases, for example, to get the required version of a DBMS driver.

But in the case of the [SAP HANA Database](https://wiki.genexus.com/commwiki/wiki?31713), the required files are not in a NuGet repository, so you must copy to the bin directory the Sap.Data.Hana.Core.v2.1.dll and libadonetHDB.dll files. These files are part of the [SAP Hana Client for Windows](https://tools.hana.ondemand.com/#hanatools).

### [DBMS configurations](#DBMS+configurations)

To work with Informix, the [DRDA protocol has to be enabled](https://wiki.genexus.com/commwiki/wiki?49253), for this is the one that the driver uses.

## [Troubleshooting](#Troubleshooting)

1) If .NET 6 SDK is not installed (\*), the following error will be displayed:

```
"error: Dotnet.exe doesn't exist. Install .NET 6."
```

or, if a previous version of .NET is available, but .NET 6 is missing:

```
"error: DotNet version >=6 is required. Your dotnet.exe is X.Y.Z. Install .NET SDK"
```

**Note**: After installing the SDK, it is necessary to close GeneXus and open it again..

(\*) If the error still persists after installing dotnet SDK, check your PATH environment variable. It may be including the dotnet folder at Program Files(x86) instead of Program Files (due to a previous installation of any SDK for x86), so it only sees the installed SDKs for x86. In that case, try removing the wrong dotnet path from the environment variable PATH and restart GeneXus.

2) If DRDA is not enabled in Informix, you may get an error like this

```
Internal error: Function call failed (ERROR 08001 IBM SQL30081N A communication error has been detected. Communication protocol being used: "TCP/IP". Communication API being used: "SOCKETS". Location where the error was detected: "172.16.0.205". Communication function detecting the error: "connect". Protocol specific error code(s): "10060", "*", "*". SQLSTATE=08001)
```

The solution is to [enable DRDA](https://wiki.genexus.com/commwiki/wiki?49253) in the DBMS and set the port number configured for DRDA at the [Server TCP/IP Port Property](https://wiki.genexus.com/commwiki/wiki?9382,,).

## [See Also](#See+Also)

* [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900)
