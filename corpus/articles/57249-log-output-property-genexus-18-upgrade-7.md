---
title: "Log output property (GeneXus 18 Upgrade 7)"
source_id: 57249
source_url: https://wiki.genexus.com/commwiki/wiki?57249
genexus_version: "18"
---

# Log output property (GeneXus 18 Upgrade 7)

Indicates the Log provider to use.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

### [Values](#Values)

|  |  |
| --- | --- |
| **ASP.NET trace** | The log is displayed on the ASP .NET trace (.NET Framework only).  Execute the *trace.axd* object to check the log. |
| **Console** | The log is displayed on the Console Appender. |
| **Event viewer** | The log is displayed on the Event viewer (.NET Framework only). |
| **File** | Default value. The log is generated as a file. |
| **Azure Application Insights** | The log is displayed in Azure Application Insights (.NET only). |

The Log Output can also be set using an environment variable, as explained in [Log settings with environment variables](https://wiki.genexus.com/commwiki/wiki?53361).

In the case of selecting [Azure Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview) as a Log provider, consider the following:

* The Log Level must be set using the [GX\_LOG\_LEVEL](https://wiki.genexus.com/commwiki/wiki?53361) environment variable.
* The APPLICATIONINSIGHTS\_CONNECTION\_STRING environment variable has to be defined and indicates the Connection String of the Application Insights resource.  
  In Azure cloud, the environment variables are defined as [App Settings](https://learn.microsoft.com/en-us/azure/app-service/reference-app-settings?tabs=kudu%2Cdotnet).

`[imagen omitida: wiki id 56150]`

**Notes:**

1. When the [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) is set to Azure Monitor Application Insights, the Log output property is ignored and the Log provider used is Azure Monitor.

2. Avoid setting the 'ASP.NET trace' and 'Event viewer' values when using the .NET Generator. Instead, it is recommended to use the 'Console' value to view the logs in /url/trace.axd

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [See Also](#See+Also)

[Log level property](https://wiki.genexus.com/commwiki/wiki?36304)  
[HowTo: See trace information in applications hosted on .NET Cloud](https://wiki.genexus.com/commwiki/wiki?20541)
