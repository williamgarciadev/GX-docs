---
title: "GeneXus Protection troubleshooting"
source_id: 53402
source_url: https://wiki.genexus.com/commwiki/wiki?53402
genexus_version: "18"
---

# GeneXus Protection troubleshooting

### [Access Denied when connecting to remote licenses.](#Access+Denied+when+connecting+to+remote+licenses.)

The solution in almost all cases is related to some DCOM permissions in the client PC and [here](https://wiki.genexus.com/commwiki/wiki?12481,,) are listed the step to get the solution.  
In addition, other causes can be the source of the problem and they are listed [here](https://wiki.genexus.com/commwiki/wiki?12482,,) and in [SAC # 22835](https://www.genexus.com/en/developers/websac?data=22835;;).

### [Protection Server 6.7 or later is required](#Protection+Server+6.7+or+later+is+required)

The following error appears when running GeneXus:

```
Authorization Required
Protection Server 6.7 or later is required, you have version UNKNOWN on "machinename"
```

Install the latest [GeneXus Protection Server](https://wiki.genexus.com/commwiki/wiki?18887,,) and retry, if the problem still occurs please enable the Protection Server logging or change manually the configuration as follows:

```
HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\ARTech\GeneXus Authorizer\Programs
GxAuth_LogFile="c:\temp\protauth.log"
```

Reproduce the problem again, the error will be detailed on the log file.


|  |
| --- |
| **Backlinks** |
| [GeneXus Protection Manual](https://wiki.genexus.com/commwiki/wiki?7353) |

---
