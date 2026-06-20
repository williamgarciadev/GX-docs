---
title: "Observability Provider property"
source_id: 53408
source_url: https://wiki.genexus.com/commwiki/wiki?53408
genexus_version: "18"
---

# Observability Provider property

Select an OpenTelemetry provider to be able to instrument, generate, collect, and export telemetry data (metrics, logs, and traces) that will help to analyze the performance and behavior of the software. Instrumentation is solved with OpenTelemetry.

### [Values](#Values)

|  |  |
| --- | --- |
| **AWS Distro for OpenTelemetry** | Uses ADOT (AWS Distro for OpenTelemetry) to provide the AWS service integration for traces and metrics. |
| **Azure Monitor Application Insights** | Exports OpenTelemetry instrumentation for Azure Monitor Application Insights. |
| **None** | Does not provide application observability. |
| **OpenTelemetry** | Exports your telemetry data to an analytics backend using OpenTelemetry SDK. |

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [Description](#Description)

GeneXus uses [OpenTelemetry](https://wiki.genexus.com/commwiki/wiki?53777) as the way to obtain telemetry data (e.g. traces, logs, and metrics) from the application.

The values to select for this property are to use the [OpenTelemetry SDK](https://opentelemetry.io/docs/specs/otel/overview/#sdk) or the distribution of the OpenTelemetry project by other providers, such as [AWS Distro for Opentelemetry](https://aws-otel.github.io/) or [Azure Monitor OpenTelemetry](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=aspnetcore).

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute [Build any object](https://wiki.genexus.com/commwiki/wiki?17719) with the purpose of generating the \*.config files.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).

### [See Also](#See+Also)

[Observability in GeneXus Apps](https://wiki.genexus.com/commwiki/wiki?53773)  
[HowTo: Observability of your GeneXus applications](https://wiki.genexus.com/commwiki/wiki?53767)


|  |
| --- |
| **Backlinks** |
| [Generate Observability span property](https://wiki.genexus.com/commwiki/wiki?55801) | [HowTo: Observability of your GeneXus applications](https://wiki.genexus.com/commwiki/wiki?53767) |
| [HowTo: Observability of your GeneXus applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55863) | [HowTo: Set up the environment to test Observability (using Grafana)](https://wiki.genexus.com/commwiki/wiki?56829) | [HowTo: Setup the environment to test Observability (using AWS CloudWatch)](https://wiki.genexus.com/commwiki/wiki?57258) | [HowTo: Watch .NET logs using OpenTelemetry (with SigNoz)](https://wiki.genexus.com/commwiki/wiki?57281) |
| [Log output property](https://wiki.genexus.com/commwiki/wiki?39568) | [Log output property (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?57249) | [Log settings with environment variables (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?57632) | [Manual Instrumentation: Tracing](https://wiki.genexus.com/commwiki/wiki?57566) |
| [Observability in GeneXus Apps and Environment variables](https://wiki.genexus.com/commwiki/wiki?57151) | [Observability with Azure Monitor Application Insights](https://wiki.genexus.com/commwiki/wiki?54383) | [Observability with Azure Monitor Application Insights (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56153) | [Observability with Lightstep](https://wiki.genexus.com/commwiki/wiki?53776) |
| [Observability with OpenTelemetry](https://wiki.genexus.com/commwiki/wiki?53775) |

---
