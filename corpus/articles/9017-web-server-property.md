---
title: "Web Server property"
source_id: 9017
source_url: https://wiki.genexus.com/commwiki/wiki?9017
genexus_version: "18"
---

# Web Server property

Indicates the Web Server that will be used at runtime.

### [Values](#Values)

|  |
| --- |
| **Internet Information Server** |
| **Kestrel HTTP Server** |
| **ASP.NET Development Web Server** |
| **WebDev.WebServer2** |

### [Scope](#Scope)

**Platforms:** Web (.Net, .Net Core)  
**Level:** Generator

### [Description](#Description)

This property is available if the [Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041) is set to No.

The default value depends on the Web Server installed. If IIS or ASP.NET are installed, they are the default value, respectively. Otherwise, if no Web Server is installed, the default value is WEDdev.WebServer2, which is installed with GeneXus.

Visual Studio WebDev and WebDev2 may be useful in certain scenarios where a Visual Studio environment is installed and you don't want to install IIS (for example, to minimize security issues in Windows Vista).

It can be useful in reduced operating systems where IIS can't be installed.

Visual Studio WebDev comes installed with:

- Visual Studio 2005 or  
- VWD (Visual Web Developer)  
- .NET Framework 2.0 SDK (not the redistributable package)

It is not provided with Microsoft .NET Framework 2.0 or Windows Vista (it is included in the redistributable Microsoft .NET Framework 3.0).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.


|  |
| --- |
| **Backlinks** |
| [.NET Generator Requirements](https://wiki.genexus.com/commwiki/wiki?38605) | [.NET Generator Requirements (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55956) | [Comparing the .NET generator with the .NET Framework generator](https://wiki.genexus.com/commwiki/wiki?45778) |
| [Troubleshooting 'Execution failed' message when running a Web app](https://wiki.genexus.com/commwiki/wiki?49557) | [User Properties](https://wiki.genexus.com/commwiki/wiki?25111) |

---
