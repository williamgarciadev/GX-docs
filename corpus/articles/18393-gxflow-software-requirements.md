---
title: "GXflow Software Requirements"
source_id: 18393
source_url: https://wiki.genexus.com/commwiki/wiki?18393
genexus_version: "18"
---

# GXflow Software Requirements

This document lists software requirements that GXflow components require at runtime. For developer requirements please check [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900)

### [Server-side requirements](#Server-side+requirements)

GXflow is a multi-platform Software solution, so its server-side requirements vary depending on the selected language (Java, .NET) and DBMS.

|  |  |
| --- | --- |
| **Language** | **Requirements** |
| **.NET Framework** | \* Microsoft .NET Framework 4.6.2 or higher  \* ADO .NET provider associated with the selected DBMS  \* IIS 6.0 or higher(1)  \* [URL Rewrite](https://wiki.genexus.com/commwiki/wiki?14958) |
| **.NET** | \* ASP.NET Core Runtime 6  \* .NET Runtime 6  More information at <https://dotnet.microsoft.com/download/dotnet/6.0> |
| **Java** | \* Oracle JRE or Open JRE 1.8 or higher  \* J2EE Server or Servlet Server(2)  \* DBMS JDBC Driver (3) |

(1) - Internet Information Server 7 or higher when using [Azure](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?15052,,).  
(2) - When using Apache Tomcat, use version 7.0.67 or higher.  
(3) - Redistributable JDBC Drivers are automatically packaged with the application (ref.: [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092)).

#### [Supported DBMSs](#Supported+DBMSs)

|  |  |
| --- | --- |
| **DBMS** | **Version** |
| \* DB2 Universal Database   \* DB2 UDB for iSeries  \* MySQL  \* Oracle  \* PostgreSQL  \* SQL Server  \* SAP Hana | \* [8.0 or higher](https://wiki.genexus.com/commwiki/wiki?10479)  \* V5R2 or higher  \* [5.7.0 or higher](https://wiki.genexus.com/commwiki/wiki?9420)  \* [12.0 or higher](https://wiki.genexus.com/commwiki/wiki?9112)  \* [8.3 or higher](https://wiki.genexus.com/commwiki/wiki?9419)  \* [2012 or higher](https://wiki.genexus.com/commwiki/wiki?9114)  \* [1.0 or higher](https://wiki.genexus.com/commwiki/wiki?47895) |

**Important notes**:

* In the case of MySQL 8.0 you must set the charset and collation in this way

```
ALTER DATABASE  '<schema-name>' DEFAULT CHARACTER SET utf8mb4 COLLATE
utf8mb4_unicode_ci
```

### [Client-side requirements](#Client-side+requirements)

These are the client-side requirements for the built-in components; custom clients may have others.

[GXflow Inbox](https://wiki.genexus.com/commwiki/wiki?7465) runs in web browsers; the [GXflow client for Native Mobile](https://wiki.genexus.com/commwiki/wiki?29037) runs on iOS and Android.

#### [Supported Internet Browsers](#Supported+Internet+Browsers)

|  |  |  |
| --- | --- | --- |
| **Browser** | **Minimum Version with Restrictions** | **Recommended Version** |
| **Mozilla Firefox** | 97 | Current, ESR(1) |
| **Google Chrome** | 99 | Current |
| **Safari** | 15.4 | Current |
| **Microsoft Edge(2)** | 99 | Current |

(1) - Refer to <https://www.mozilla.org/en-US/firefox/enterprise/> for ESR meaning.  
(2) - Note that current versions of Edge are based on Chromium and older ones (like version 20) are now are referred to as 'legacy' in Microsoft's documentation (ref.: <https://support.microsoft.com/en-us/help/4026494/microsoft-edge-difference-between-legacy>).

Supported Native OS

|  |  |  |
| --- | --- | --- |
| **OS** | **Minimum Version** | **Recommended Version** |
| **iOS** | 9.0 | Latest available |
| **Android** | 5 (Lollipop) | Latest available |

Android and iOS applications store local data for caching purposes or offline scenarios using SQLite databases. The SQLite DBMS is part of Android and iOS Operating Systems and its version is defined by Android and iOS Requirements.

Check [Apple Requirements](https://wiki.genexus.com/commwiki/wiki?19478) and [Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449) for more information.

### [Additional Requirements](#Additional+Requirements)

There may be additional requirements that depend on the application interoperates with GXflow and whether the security is based on [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746).

For those cases, check the Application execution requirements section at [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900).


|  |
| --- |
| **Backlinks** |
|
| [Table of contents:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXflow Software Requirements (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60055) |

---
