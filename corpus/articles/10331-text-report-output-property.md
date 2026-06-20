---
title: "Text report output property"
source_id: 10331
source_url: https://wiki.genexus.com/commwiki/wiki?10331
genexus_version: "18"
---

# Text report output property

To select the way that the output report will be shown or printed. It's valid for Reports in text mode.

### [Values](#Values)

|  |  |
| --- | --- |
| **Report Viewer** | the output text will be generated using the Report Viewer utility (the rbuilder.dll and gxdib32.dll are used). The resulting report is a .gxr file. In case of Java generator, the JVM for 32 bits is required on the machine where the report runs (further information: sac 20155). |
| **Text** | the output text will be generated using a native implementation depending on the platform.The resulting report is a .txt file. Default value. |

### [Description](#Description)

The "text" value is supported for Windows platforms as of Upgrade 3 of the Java generator of GeneXus X Evolution 1. In previous versions, it only works for Linux platform.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Re-Build All.

### [Scope](#Scope)

**Objects:** Procedure  
**Platforms:** Web(.Net, Java)

### [See Also](#See+Also)

[Show printer dialog on reports property](https://wiki.genexus.com/commwiki/wiki?9004)  
[Graphic report output property](https://wiki.genexus.com/commwiki/wiki?9245)  
In case of .NET WEB, see [http://www2.gxtechnical.com/portal/hgxpp001.aspx?15,4,61,O,S,0,,28690;S;0;A;0;0;;;;;;;;;;;;;;;;;A;%20%20/%20%20/%20%20;;0;9;;28690;;99;;0;1;%200;N;N;S;B;B


|  |
| --- |
| **Backlinks** |
| [Graphic report output property](https://wiki.genexus.com/commwiki/wiki?9245) |
| [Show printer dialog on reports property](https://wiki.genexus.com/commwiki/wiki?9004) |

---
