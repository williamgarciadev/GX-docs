---
title: "Report output property"
source_id: 7943
source_url: https://wiki.genexus.com/commwiki/wiki?7943
genexus_version: "18"
---

# Report output property

Sets the device to be used for a Procedure output.

### [Values](#Values)

|  |  |
| --- | --- |
| **Ask User** | The user will be asked where to send the output at execution time. This value only applies to Windows environments. This is the default value. |
| **Only To File** | The output is sent directly to a file. By default, the generated file has GXRPTn.GXR name (where n is a number starting at 0 and increasing when other open documents exist), except in the case that another name and/or format has been specified using the Output\_File rule. |
| **Only To Printer** | The output is sent directly to the printer (see Output Device Location Property below). |
| **Only To Screen** | The output is sent directly to the screen. |

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, rebuild all the [Procedure objects](https://wiki.genexus.com/commwiki/wiki?6293).

### [See Also](#See+Also)

[Output\_File rule](https://wiki.genexus.com/commwiki/wiki?7965)  
[Output device location property](https://wiki.genexus.com/commwiki/wiki?14110)  
[Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719)


|  |
| --- |
| **Backlinks** |
| [Output device location property](https://wiki.genexus.com/commwiki/wiki?14110) | [Output\_File rule](https://wiki.genexus.com/commwiki/wiki?7965) |
| [PDF Reports](https://wiki.genexus.com/commwiki/wiki?13531) | [PDF Reports (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54937) | [PDF Reports (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55935) | [Printing text reports on the client machine without changing the printer settings](https://wiki.genexus.com/commwiki/wiki?28296) |
| [Show printer dialog on reports property](https://wiki.genexus.com/commwiki/wiki?9004) |
| [Use PDF Reports property](https://wiki.genexus.com/commwiki/wiki?42887) | [Web printing on client printer (without an applet)](https://wiki.genexus.com/commwiki/wiki?33912) |

---
