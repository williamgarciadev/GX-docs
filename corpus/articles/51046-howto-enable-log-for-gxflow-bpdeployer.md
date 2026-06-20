---
title: "HowTo: Enable Log for GXflow BPDeployer"
source_id: 51046
source_url: https://wiki.genexus.com/commwiki/wiki?51046
genexus_version: "18"
---

# HowTo: Enable Log for GXflow BPDeployer

This document explains how to enable logging for the [Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?11607).

To do so, run the Business Process Deployer from the command line as shown below, depending on whether you are generating in [.NET](https://wiki.genexus.com/commwiki/wiki?38604) or [Java](https://wiki.genexus.com/commwiki/wiki?12258):

### [In .NET](#In+.NET)

**Example:**

```
GXBPDeployer -netlogfile "C:\logs\deploy.log" -netloglevel 6
```

**Where:**  
*netlogfile*  
Defines the path to the log file. In the above example, all errors will be logged in the *C:*\logs\*deploy.log* file.

*netloglevel*Defines the level of errors that will be logged. Possible values are:

0 - OFF  
1 - FATAL  
2 - ERROR  
3 - WARN  
4 - INFO  
5 - DEBUG  
6 - ALL

### [In Java](#In+Java)

**Example:**

```
GXBPDEployer -jdbclogfile "C:\logs\deploy.log" -jdbclogdetail 2
```

**Where:**  
*jdblogfile* Defines the path to the JDBC log file. In the example above, all errors will be logged in the *C:*\logs\*deploy.log* file.

*jdbclogdetail*Defines the level of errors that will be logged. Possible values are:

0 - HIGH  
1 - MEDIUM  
2 - LOW

### [See Also](#See+Also)

[Business Process Deployer Command line](https://wiki.genexus.com/commwiki/wiki?27496)  
[HowTo: Enable Log for GXflow runtime](https://wiki.genexus.com/commwiki/wiki?24568)  
[HowTo Generate log for GXflow license manager](https://wiki.genexus.com/commwiki/wiki?37207)


|  |
| --- |
| **Backlinks** |
| [Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?11607) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [HowTo: Enable Log for GXflow runtime](https://wiki.genexus.com/commwiki/wiki?24568) |
| [HowTo: Impact the production database in GXflow with the Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?52734) |

---
