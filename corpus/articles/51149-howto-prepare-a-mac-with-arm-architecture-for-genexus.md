---
title: "HowTo: Prepare a Mac with ARM architecture for GeneXus"
source_id: 51149
source_url: https://wiki.genexus.com/commwiki/wiki?51149
genexus_version: "18"
---

# HowTo: Prepare a Mac with ARM architecture for GeneXus

This document provides the steps to install GeneXus, as well as considerations and existing restrictions regarding Apple's [M1](https://en.wikipedia.org/wiki/Apple_M1) and [M2](https://en.wikipedia.org/wiki/Apple_M2) CPUs.

### Step 1 - Install desktop virtualization software

Since the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272) runs on Windows, you need to install some desktop virtualization software and install a virtual machine. In this case, installing [Parallels](https://www.parallels.com/products/) is suggested and the ongoing steps have been tested on it.

In addition to the [Parallels requirements](https://www.parallels.com/products/desktop/resources/), you need to take into account the [requirements associated with GeneXus](https://wiki.genexus.com/commwiki/wiki?30900).

### [Step 2 - Install Windows ARM](#Step+2+-+Install+Windows+ARM)

The Windows version that must be installed in Parallels is Windows ARM.

If you use the version suggested by Parallels, download the Home version of Windows 11 ARM.

**Notes:**

* To download Windows ARM, you need to log in with a Microsoft account and be a member of the Windows Insider program (free). After downloading, install with Parallels pointing to that image.
* An [Insider version of Windows 11 ARM](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewARM64) can be downloaded.
* Even though GeneXus is an x86 32-bit app, Windows 11 ARM can emulate x86 and x64 apps.

### [Step 3 - Install Microsoft SQL Express LocalDB](#Step+3+-+Install+Microsoft+SQL+Express+LocalDB)

Install [SQL Server Express LocalDB](https://docs.microsoft.com/es-es/sql/database-engine/configure-windows/sql-server-express-localdb?view=sql-server-ver15). It works fine on Windows ARM and is suitable for storing KBs.

You must install LocalDB and not any other edition of SQL Server because none is compatible with Windows ARM.

### [Step 4 - Install GeneXus](#Step+4+-+Install+GeneXus)

Follow the [GeneXus Installation Steps](https://wiki.genexus.com/commwiki/wiki?25842) described in the [GeneXus 18 Installation Manual](https://wiki.genexus.com/commwiki/wiki?31997)

### [Step 5 - Install requirements for Application Prototyping](#Step+5+-+Install+requirements+for+Application+Prototyping)

Since SQL Server is not suitable for Windows ARM, you need to find alternative DBMSes to prototype your applications

For this scenario, the options are:

* GeneXus Prototyping Cloud  
  To use it, [create an environment](https://wiki.genexus.com/commwiki/wiki?24702) and choose 'GeneXus Prototyping Cloud', or select [Deploy to cloud](https://wiki.genexus.com/commwiki/wiki?15041) on an existing environment.  
  This avoids the need to have the DBMS installed locally.
* Docker container with SQL Server  
  To use SQL Server with [GeneXus .NET Generator](https://wiki.genexus.com/commwiki/wiki?38604) locally, you must install the latest [Docker](https://docs.docker.com/desktop/mac/apple-silicon/) version. Then, run a Docker SQL instance, as shown below:

  ```
  docker run -e "ACCEPT_EULA=1" -e "MSSQL_SA_PASSWORD=MyPass@word" -e "MSSQL_PID=Desarrollador" -e "MSSQL_USER=SA" -p 1433:1433 -d --name=sql mcr.microsoft.com/ azure-sql-borde
  ```

  ​​Finally, install [Azure Data Studio](https://hub.docker.com/_/microsoft-azure-sql-edge) and set 127.0.0.1 as the server. Take into account that the Docker container is hosted on port 1433, the default port for SQL. Also, set the user to sa and the password to MyPass@word or whatever values ​​you have chosen.
* Another DBMS that is not SQL Server. For example, MySQL has an ARM version for Mac. You can install MySQL Server on the Mac and then point the [GeneXus data store](https://wiki.genexus.com/commwiki/wiki?7117) to the Mac hostname or IP in the data store properties

Check [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) for other requirements for prototyping applications. On each, take into account that you need a specific setup for Windows ARM.

### [Considerations](#Considerations)

Android applications cannot be compiled on the M1 from GeneXus. You can do it externally from Android Studio on the MAC.

### [See Also](#See+Also)

[HowTo: Prepare a Mac with an Intel processor for GeneXus](https://wiki.genexus.com/commwiki/wiki?51408)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55768) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) | [HowTo: Prepare a Mac with an Intel processor for GeneXus](https://wiki.genexus.com/commwiki/wiki?51408) |

---
