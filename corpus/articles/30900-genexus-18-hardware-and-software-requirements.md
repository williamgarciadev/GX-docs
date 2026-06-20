---
title: "GeneXus 18 hardware and software requirements"
source_id: 30900
source_url: https://wiki.genexus.com/commwiki/wiki?30900
genexus_version: "18"
---

# GeneXus 18 hardware and software requirements

The following is a list of the requirements to run [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).

[GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272) runs on the [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows) Operating System.

|  |  |
| --- | --- |
| **Hardware Requirements** | \* Processor: minimum of 1 GHz (multi-core recommended)  \* Memory: minimum of 4 GB of RAM (8 GB recommended; 16 GB recommended to generate Android applications)  \* Hard disk: minimum of 1.2 GB of disk space for the installation. To generate applications, you will need additional space or a shared disk unit to create the knowledge bases and generate the code |
| **Software Requirements** | \* Microsoft .NET Framework 4.7.1, 4.7.2, or 4.8 (Check its requirements, specifically the supported Windows Versions [here](https://docs.microsoft.com/en-us/dotnet/framework/get-started/system-requirements)(1))  \* Microsoft SQL Server 2012 or higher (Express, Standard or any other Edition) or [LocalDB](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/sql-server-express-localdb?redirectedfrom=MSDN&view=sql-server-ver15)(4)  \* Microsoft Internet Explorer when using Windows 10 or prior. Minimum Version: 6.0 SP1 (11 or higher recommended)(2)  \* [Apache Maven 3.6.1 or higher](http://maven.apache.org/download.cgi)(3)  \* [.NET SDK 8](https://dotnet.microsoft.com/en-us/download/dotnet/8.0)(5) |

(1) - For [Live Editing](https://wiki.genexus.com/commwiki/wiki?27805), Windows 8.1 or higher is required.  
(2) - Internet Explorer base libraries (MSHTML) are used for the [HTML Editor](https://wiki.genexus.com/commwiki/wiki?7673) at design time. These base libraries are installed in Windows 10 or prior versions as part of the Internet Explorer feature and are part of Windows 11 [ref.](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/internet-explorer-11-desktop-app-retirement-faq/ba-p/2366549)  
(3) - For [installing](Manage Module References) or [distributing](https://wiki.genexus.com/commwiki/wiki?31376) modules.  
(4) - LocalDB is only supported to create a Knowledge Base, not for use by the generated applications.  
(5) - As long as your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) has a [Query object](https://wiki.genexus.com/commwiki/wiki?9026) or a [Dashboard object](https://wiki.genexus.com/commwiki/wiki?36769).

In addition, the user running GeneXus IDE must have administrator rights.

### [Generation requirements:](#Generation+requirements%3A)

|  |  |
| --- | --- |
| **Generator** | **Requirements** |
| **.NET Framework** | \* ADO .NET provider associated with the selected DBMS |
| **.NET** | \* [.NET SDK 8](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) |
| **Java** (1) | \* Oracle JDK or Open JDK 1.8 to Open JDK 21(2) |
| **Native Mobile** | \* [Apple Requirements](https://wiki.genexus.com/commwiki/wiki?19478)  \* [Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449) |
| **Angular** | \* [Angular requirements](https://wiki.genexus.com/commwiki/wiki?42541) |

(1) - For local prototyping, you can only use:

* Apache Tomcat (in versions ranging from 7.0.67 to 11.0.x).
* Spring Boot (make sure you have a version between JDK 17 and JDK 21 installed).

Any other web server will not work automatically.

(2) - JDK 11 to JDK 21 is recommended to improve compilation performance.

### [Execution requirements:](#Execution+requirements%3A)

|  |  |
| --- | --- |
| **Generator** | **Requirements** |
| **.NET Framework** | \* Microsoft .NET Framework 4.6.2 (1) or higher  \* Internet Information 6.0 or higher (2)  \* ADO .NET provider associated with the selected DBMS  \* [URL Rewrite](https://wiki.genexus.com/commwiki/wiki?14958) for REST Services and [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |
| **.NET** | \* Windows: [ASP.NET Core Runtime 8.x Hosting Bundle](https://dotnet.microsoft.com/en-us/download/dotnet/8.0)(5)  \* Linux: [Details...](https://wiki.genexus.com/commwiki/wiki?37908) |
| **Java** | \* Oracle JRE or Open JRE 1.8 to Open JRE 21  \* JAVA EE or JAKARTA EE Server with a Servlet specification ranging from 3.0 to 6.0(3)  \* DBMS JDBC Driver (4) |
| **Native Mobile** | \* [Apple Requirements](https://wiki.genexus.com/commwiki/wiki?19478)  \* [Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449) |
| **Angular** | \* [Angular requirements](https://wiki.genexus.com/commwiki/wiki?42541) |

(1) - Framework 4.7.2 when [SameSite cookie attribute property](https://wiki.genexus.com/commwiki/wiki?47685) is set to a value other than 'Do not specify'.  
(2) - Internet Information Server 8 when using [Server.Socket external object](https://wiki.genexus.com/commwiki/wiki?22442). Make sure to install the Windows feature 'WebSocket Protocol' module in the IIS 8 section.  
- Internet Information Server 7 or higher when using [Azure](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?15052,,).  
(3) - When using Apache Tomcat, use a version between 7.0.67 and 10.1.x.  
(4) - They are obtained at build time. See more information in [DBMS Drivers](https://wiki.genexus.com/commwiki/wiki?54302).  
(5) - The .NET Core Windows Server Hosting Bundle is for running the application on IIS. More information at [.NET Generator Requirements](https://wiki.genexus.com/commwiki/wiki?38605).

#### [**Notes**](#Notes)

* To enable the 'WebSocket Protocol' module on Windows, follow these steps: "Turn Windows features on or off" > Internet Information Services > World Wide Web Services > Application Development Features > WebSocket Protocol. It requires restarting the machine.
* To verify that .NET Framework 4.6 is installed, go to "Turn Windows features on or off" and check .Net Framework 4.6 Advanced Services.
* [Solutions for the case when a 404 or 500.19 error occurs](https://wiki.genexus.com/commwiki/wiki?18398).

### [Supported DBMSs](#Supported+DBMSs)

When generating applications that use databases, the supported DBMSs are as follows:

|  |  |  |
| --- | --- | --- |
| **Generator** | **DBMS** | **DBMS Version** |
| **.NET Framework, .NET, and Java** | \* DB2 Universal Database  \* DB2 UDB for iSeries(1)  \* Informix(2)  \* MySQL(3)  \* Oracle(4)  \* PostgreSQL  \* SQL Server(5,7)  \* SAP Hana DB | \* [7.1 or higher](https://wiki.genexus.com/commwiki/wiki?10479)  \* V5R1 or higher  \* [7.31 or higher](https://wiki.genexus.com/commwiki/wiki?9399)  \* [4.x or higher](https://wiki.genexus.com/commwiki/wiki?9420)  \* [8.1.5 or higher](https://wiki.genexus.com/commwiki/wiki?9112)  \* [7.x or higher](https://wiki.genexus.com/commwiki/wiki?9419)  \* [2000 or higher](https://wiki.genexus.com/commwiki/wiki?9114)  \* [1.0 or higher](https://wiki.genexus.com/commwiki/wiki?47895) |
| **Android and iOS** | \* SQLite(6) |  |

(1) - For Query and Dashboard objects:

* When generating with [.NET](https://wiki.genexus.com/commwiki/wiki?38604): The DB2 Connect provider is required (https://www.ibm.com/support/pages/ibm-i-net-data-provider-and-net-core) and therefore a license provided by IBM is required. The db2\*.lic file must be copied to the "<Environment>\web\bin\clidriver\license" directory.  If you have already been generating for .NET and DB2 UDB for iSeries, you sure have a license (read more at [SAC #50548](https://www.genexus.com/en/developers/websac?data=50548;;)). Otherwise, you have to consider it.
* When generating with [Java](https://wiki.genexus.com/commwiki/wiki?12258) or [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892): Read [SAC #60159](https://www.genexus.com/es/developers/websac?data=60159;;).

(2) - .NET specific: DRDA protocol must be enabled and therefore the minimum Informix version is 11.x. More information at [.NET Generator Requirements](https://wiki.genexus.com/commwiki/wiki?38605) and [Enabling DRDA on Informix](https://wiki.genexus.com/commwiki/wiki?49253).  
(3) - When using [GAM](https://wiki.genexus.com/commwiki/wiki?24746) or [GXflow](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?4179,,), the supported version for MySQL is 5.0.3 or higher.  
(4) - When using [GXflow](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?4179,,), the supported version is Oracle 9 or higher.  
(5) - When using [GXflow](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?4179,,), the supported version is SQL Server 2012 or higher. When using GAM, the supported version is 2008 or higher. Any Edition of SQL Server is supported.  
(6) - SQLite is part of Android and iOS Operating Systems and its version is defined by Android and iOS Requirements.  
(7) LocalDB is not supported.

See also [Cloud Database](https://wiki.genexus.com/commwiki/wiki?31685) for more options.

### [Supported Internet Browsers](#Supported+Internet+Browsers)

#### [For a front end created with Java, .NET, or .NET Framework generators:](#For+a+front+end+created+with+Java%2C+.NET%2C+or+.NET+Framework+generators%3A)

|  |  |  |  |
| --- | --- | --- | --- |
| **Browser** | **Minimum Version with Restrictions(1)** | **Minimum Version(2)** | **Recommended Version(3)** |
| **Mozilla Firefox** | 97 | Current - 1, ESR(4) | Current, ESR(4) |
| **Google Chrome** | 99 | Current - 1 | Current |
| **Safari** | 15.4 | Current - 1 | Current |
| **Microsoft Edge** | 99 | Current - 1 | Current |
| **Others** | Check footnotes (1)(2)(3)(4) | | |

(1) - Web applications require Browsers with [CSS Cascade Layers](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer) support. Also, native mobile apps that load those web applications using [Component domain](https://wiki.genexus.com/commwiki/wiki?16186) (Webview) require devices with the corresponding browser version or an up-to-date base software.  
The following is a detailed list of browsers that support this feature: <https://caniuse.com/css-cascade-layers>. Note that on Apple devices, iOS 15.4 or higher is required. Furthermore, Android devices require an updated [Android System Webview](https://play.google.com/store/apps/details?id=com.google.android.webview&hl=en&gl=US) as stated in <https://caniuse.com/css-cascade-layers>.  
Note: Although as of November 2022, 89% of the browsers support CSS Cascade Layers (*source: <https://caniuse.com/css-cascade-layers>)*, [GeneXus 18 Upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081) will remove this requirement for applications that use [Theme object](https://wiki.genexus.com/commwiki/wiki?16595) to improve compatibility.  
(2) - If [Server.Socket external object](https://wiki.genexus.com/commwiki/wiki?22442), [ProgressIndicator external object](https://wiki.genexus.com/commwiki/wiki?31275), [Responsive Web Design (RWD)](https://wiki.genexus.com/commwiki/wiki?25161) features are used these are the minimum supported versions.  
Since many functionalities of the generated web front end are based on jQuery 3.5.1, Browser support is mainly tied to <https://jquery.com/browser-support/>  
(3) - In all cases, the latest available browser version is recommended, primarily because of improvements related to performance and security.  
(4) - Refer to <https://www.mozilla.org/en-US/firefox/enterprise/> for ESR meaning.

#### [For a front end created with Java, .NET, or .NET Framework or Angular generator:](#For+a+front+end+created+with+Java%2C+.NET%2C+or+.NET+Framework+or+Angular+generator%3A)

Browsers must support the es6-module. The following is a detailed list of browsers that support this feature: <https://caniuse.com/es6-module>.

More information: [Angular Generator Browser Support](https://wiki.genexus.com/commwiki/wiki?42541).

### [GeneXus IDE on Mac or Linux](#GeneXus+IDE+on+Mac+or+Linux)

Since GeneXus IDE runs on Windows, you must run it on Virtual Machines with that Operating System and the associated requirements mentioned above when your base OS is Mac OS or Linux.  
Read [HowTo: Prepare a Mac with ARM architecture for GeneXus](https://wiki.genexus.com/commwiki/wiki?51149).

[GeneXus Next](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?57864,,) will be an alternative to this in the future.


|  |
| --- |
| **Backlinks** |
| [.NET Generator Requirements](https://wiki.genexus.com/commwiki/wiki?38605) | [.NET Generator Requirements (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55956) | [Comparison between Theme and Design System objects](https://wiki.genexus.com/commwiki/wiki?48985) |
| [Category:GeneXus .NET Framework Generator](https://wiki.genexus.com/commwiki/wiki?2892) |
|
| [GeneXus 18 Compatibility Section](https://wiki.genexus.com/commwiki/wiki?51080) | [GeneXus 18 Compatibility Section (GeneXus 18)](https://wiki.genexus.com/commwiki/wiki?53520) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?58946) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55768) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) | [Category:GeneXus 18 Installation Manual](https://wiki.genexus.com/commwiki/wiki?31997) | [GeneXus for SAP Systems - Hardware and Software Requirements](https://wiki.genexus.com/commwiki/wiki?33981) | [GeneXus Installation Steps](https://wiki.genexus.com/commwiki/wiki?25842) |
| [Category:GeneXus Java Generator](https://wiki.genexus.com/commwiki/wiki?12258) | [GXflow Software Requirements](https://wiki.genexus.com/commwiki/wiki?18393) |
| [GXflow Software Requirements (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55579) | [Table of contents:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [HowTo: My first GeneXus Java Application](https://wiki.genexus.com/commwiki/wiki?45875) | [HowTo: My first GeneXus Java Application (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55769) |
| [HowTo: Prepare a Mac with an Intel processor for GeneXus](https://wiki.genexus.com/commwiki/wiki?51408) | [HowTo: Prepare a Mac with ARM architecture for GeneXus](https://wiki.genexus.com/commwiki/wiki?51149) | [Java Generator Requirements](https://wiki.genexus.com/commwiki/wiki?54302) | [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |
| [Offline Native Mobile Applications Requirements](https://wiki.genexus.com/commwiki/wiki?22259) | [Packaged Module Management Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?46761) | [Packaged Modules Management messages (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55022) | [Welcome to Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?18321) |

---
