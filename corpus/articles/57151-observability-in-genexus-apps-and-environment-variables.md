---
title: "Observability in GeneXus Apps and Environment variables"
source_id: 57151
source_url: https://wiki.genexus.com/commwiki/wiki?57151
genexus_version: "18"
---

# Observability in GeneXus Apps and Environment variables

In the case of [GeneXus .NET Generator](https://wiki.genexus.com/commwiki/wiki?38604), the following system environment variables influence the behavior of your app with active Observability (i.e. [Observability Provider](https://wiki.genexus.com/commwiki/wiki?53408) = OpenTelemetry / Azure Monitor Application Insights / AWS Distro for OpenTelemetry).

|  |  |  |
| --- | --- | --- |
| **Environment Variable** | **none** | **console** |
| **OTEL\_METRICS\_EXPORTER** | If it's not defined, or if its value is other than "none", metrics will be instrumented.  Therefore, to avoid the instrumentation of metrics, set this system environment variable to "none". | When you set `OTEL_METRICS_EXPORTER=console`, it configures OpenTelemetry to export metrics to the console (stdout).  This is useful for development and debugging purposes, as you can see the metric data in your console output. |
| **OTEL\_TRACES\_EXPORTER** | If it's not defined, or if its value is other than "none", traces will be instrumented.  Therefore, to avoid the instrumentation of traces, set this system environment variable to "none". | When you set `OTEL_TRACES_EXPORTER=console`, it configures OpenTelemetry to export traces to the console (stdout).  This is useful for development and debugging purposes. |
| **OTEL\_LOGS\_EXPORTER** | If it's not defined, or if its value is other than "none", logs will be instrumented.  Therefore, to avoid the instrumentation of logs, set this system environment variable to "none". | When you set `OTEL_LOGS_EXPORTER=console(logging)`, it configures OpenTelemetry to export logs to the console (stdout).  This is useful for development and debugging purposes. |

## 

|  |  |
| --- | --- |
| **Environment Variable** |  |
| **GX\_LOG\_LEVEL** | The LogLevel specifies the minimum level to log.  LogLevel indicates the severity of the log and ranges from 0 to 6:  Trace = 0, Debug = 1, Information = 2, Warning = 3, Error = 4, Critical = 5, and None = 6. Also, the following equivalent values that are valid as well (all in lowercase):  * debug * all (equals to Trace) * info * warn * error * fatal (equals to Critical)   For the standard levels, there are ALL(Trace) < DEBUG < INFO < WARN < ERROR < FATAL (critical) < OFF(None). |

## [Availability](#Availability)

Since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) | [Toc:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |

---
