---
title: "Log output property (GeneXus 18 Upgrade 0 or prior)"
source_id: 53419
source_url: https://wiki.genexus.com/commwiki/wiki?53419
genexus_version: "18"
---

# Log output property (GeneXus 18 Upgrade 0 or prior)

Indicates the Log provider to be used.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

## [Values](#Values)

|  |  |
| --- | --- |
| **ASP.NET trace** | The log is displayed on the ASP .NET trace (.NET and .NET Framework only).  Execute the *trace.axd* object to check the log. |
| **Console Appender** | The log is displayed on the Console Appender (Java only). |
| **Event viewer** | The log is displayed on the Event viewer (.NET and .NET Framework only). |
| **File** | The log is generated as a file. |

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [See Also](#See+Also)

[Log level property](https://wiki.genexus.com/commwiki/wiki?36304)  
[HowTo: See trace information in applications hosted on .NET Cloud](https://wiki.genexus.com/commwiki/wiki?20541)
