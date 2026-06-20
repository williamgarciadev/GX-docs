---
title: ".NET Generator Requirements"
source_id: 38605
source_url: https://wiki.genexus.com/commwiki/wiki?38605
genexus_version: "18"
---

# .NET Generator Requirements

This article states the requirements of the [.NET Generator](https://wiki.genexus.com/commwiki/wiki?38604) requirements for development.

### [.NET SDK](#.NET+SDK)

To build .NET applications, you need to install .NET 8.x SDK, which is available here: [.NET 8 (LTS)](https://dotnet.microsoft.com/download/dotnet/8.0).

### [Optional: Run web applications using IIS](#Optional%3A+Run+web+applications+using+IIS)

By default, the .NET generator runs web applications in the Kestrel web server that is included in the .NET SDK. To run the application with IIS working as a reverse proxy in front of Kestrel,

* Install [ASP.NET Core Runtime 8.x Hosting Bundle](https://dotnet.microsoft.com/download/dotnet/8.0) (e.g. dotnet-hosting-8.0.0-rc.1.23421.29-win.exe,  look for the "Hosting Bundle" link on the [download page](https://dotnet.microsoft.com/download/dotnet/8.0) ). It requires a restart of IIS.
* Set the generator's [Web Server property](https://wiki.genexus.com/commwiki/wiki?9017) to "Internet Information Server."

### [DBMS Drivers](#DBMS+Drivers)

In build time, an internet connection to nuget.org is required in several cases, for example, to get the required version of a DBMS driver.

But in the case of the [SAP HANA Database](https://wiki.genexus.com/commwiki/wiki?31713), the required files are not in a NuGet repository, so you must copy to the bin directory the Sap.Data.Hana.Core.v2.1.dll and libadonetHDB.dll files. These files are part of the [SAP Hana Client for Windows](https://tools.hana.ondemand.com/#hanatools).

### [DBMS configurations](#DBMS+configurations)

To work with Informix, the [DRDA protocol has to be enabled](https://wiki.genexus.com/commwiki/wiki?49253), for this is the one that the driver uses.

## [Troubleshooting](#Troubleshooting)

1) If .NET 8 SDK is not installed (\*), the following error will be displayed:

```
"error: Dotnet.exe doesn't exist. Install .NET 8."
```

or, if a previous version of .NET is available, but .NET 8 is missing:

```
"error: DotNet version >=8 is required. Your dotnet.exe is X.Y.Z. Install .NET SDK"
```

**Note**: After installing the SDK, it is necessary to close GeneXus and open it again..

(\*) If the error still persists after installing dotnet SDK, check your PATH environment variable. It may be including the dotnet folder at Program Files(x86) instead of Program Files (due to a previous installation of any SDK for x86), so it only sees the installed SDKs for x86. In that case, try removing the wrong dotnet path from the environment variable PATH and restart GeneXus.

2) If DRDA is not enabled in Informix, you may get an error like this

```
Internal error: Function call failed (ERROR 08001 IBM SQL30081N A communication error has been detected. Communication protocol being used: "TCP/IP". Communication API being used: "SOCKETS". Location where the error was detected: "172.16.0.205". Communication function detecting the error: "connect". Protocol specific error code(s): "10060", "*", "*". SQLSTATE=08001)
```

The solution is to [enable DRDA](https://wiki.genexus.com/commwiki/wiki?49253) in the DBMS and set the port number configured for DRDA at the [Server TCP/IP Port Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?9382,,).

## [See Also](#See+Also)

[GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900)


|  |
| --- |
| **Backlinks** |
| [Table of contents:.NET Applications Development](https://wiki.genexus.com/commwiki/wiki?53971) | [.NET Generator Requirements (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55956) | [KB:FestivalTickets - High Scalability Sample](https://wiki.genexus.com/commwiki/wiki?51266) |
| [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?58946) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55768) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) |
| [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241) | [SAP HANA Database](https://wiki.genexus.com/commwiki/wiki?31713) |

---
