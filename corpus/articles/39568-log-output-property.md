---
title: "Log output property"
source_id: 39568
source_url: https://wiki.genexus.com/commwiki/wiki?39568
genexus_version: "18"
---

# Log output property

Indicates the Log provider to use.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

### [Values](#Values)

|  |  |
| --- | --- |
| **ASP.NET trace** | The log is displayed in ASP.NET Trace, run the trace.axd object to access it.  It's available on .NET Framework, for .NET refer notes bellow. |
| **Console** | The log is displayed on the Console Appender. |
| **Event viewer** | The log is displayed on the Event viewer (.NET Framework only). |
| **File** | Default value. The log is generated as a file. |
| **Azure Application Insights** | The log is displayed in Azure Application Insights (.NET only). See [HowTo: Logging to Azure Application Insights](https://wiki.genexus.com/commwiki/wiki?58044). |

The Log Output can also be set using an environment variable, as explained in [Log settings with environment variables](https://wiki.genexus.com/commwiki/wiki?53361).

In the case of selecting [Azure Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview), log4NET is not used, but Azure Application Insights is used as a Log provider.  
Consider the following:

* The Log Level must be set using the [GX\_LOG\_LEVEL](https://wiki.genexus.com/commwiki/wiki?53361) environment variable.
* The APPLICATIONINSIGHTS\_CONNECTION\_STRING environment variable has to be defined and indicates the Connection String of the Application Insights resource.  
  In Azure cloud, the environment variables are defined as [App Settings](https://learn.microsoft.com/en-us/azure/app-service/reference-app-settings?tabs=kudu%2Cdotnet).

`[imagen omitida: wiki id 56150]`

**Notes:**

1. In .NET [environment](https://wiki.genexus.com/commwiki/wiki?7115), when the [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) is set to Azure Monitor Application Insights / AWS Distro for OpenTelemetry, or OpenTelemetry values, the Log output property is ignored, and the corresponding Log provider is used: Azure Monitor, AWS Distro or OpenTelemetry, respectively.

2. Avoid setting the 'ASP.NET trace' and 'Event viewer' values when using the .NET Generator. Instead, it is recommended to use the 'Console' value to view the logs in /url/trace.axd

3.  As of GeneXus 18 Upgrade 13, and as a security improvement, access to trace logs via trace.axd is only allowed in "Development" environments, following recommended best practices. An environment is considered Development when the ASPNETCORE\_ENVIRONMENT environment variable is set to "Development".  
This can also be explicitly defined in the web.config file, as shown below (this section is included but commented out by default):

<aspNetCore ...>  
    <environmentVariables>  
        <environmentVariable name="ASPNETCORE\_ENVIRONMENT" value="Development" />  
    </environmentVariables>  
</aspNetCore>

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [See Also](#See+Also)

[Log level property](https://wiki.genexus.com/commwiki/wiki?36304)  
[HowTo: See trace information in applications hosted on .NET Cloud](https://wiki.genexus.com/commwiki/wiki?20541)  
[Log settings with environment variables](https://wiki.genexus.com/commwiki/wiki?53361)  
[HowTo: Logging to Azure Application Insights](https://wiki.genexus.com/commwiki/wiki?58044)


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [Chatbot Generator - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?41260) |
| [HowTo: Configure GAM to use Security Token Service](https://wiki.genexus.com/commwiki/wiki?43206) | [HowTo: Enable Log for GXflow runtime](https://wiki.genexus.com/commwiki/wiki?24568) |
| [HowTo: Logging to Azure Application Insights](https://wiki.genexus.com/commwiki/wiki?58044) | [HowTo: Monitor Azure Functions](https://wiki.genexus.com/commwiki/wiki?49260) | [HowTo: Monitor Azure Functions (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?58050) | [HowTo: See trace information in applications hosted on .NET Cloud](https://wiki.genexus.com/commwiki/wiki?20541) |
| [Log external object](https://wiki.genexus.com/commwiki/wiki?37872) | [Log file property](https://wiki.genexus.com/commwiki/wiki?39601) | [Log level property](https://wiki.genexus.com/commwiki/wiki?36304) | [Log level property (GeneXus 18 upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56151) |
| [Log output property (GeneXus 18 Upgrade 0 or prior)](https://wiki.genexus.com/commwiki/wiki?53419) | [Log output property (GeneXus 18 upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56148) | [Log output property (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?57249) | [Log settings with environment variables](https://wiki.genexus.com/commwiki/wiki?53361) |
| [Log settings with environment variables (GeneXus 18 upgrade 1)](https://wiki.genexus.com/commwiki/wiki?53615) | [Log settings with environment variables (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56152) | [Log settings with environment variables (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?57632) | [Observability with Azure Monitor Application Insights](https://wiki.genexus.com/commwiki/wiki?54383) |

---
