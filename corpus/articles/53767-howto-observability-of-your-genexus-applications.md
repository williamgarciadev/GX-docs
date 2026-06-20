---
title: "HowTo: Observability of your GeneXus applications"
source_id: 53767
source_url: https://wiki.genexus.com/commwiki/wiki?53767
genexus_version: "18"
---

# HowTo: Observability of your GeneXus applications

GeneXus collects telemetry data (traces, logs, and metrics) of its applications with [OpenTelemetry](https://opentelemetry.io/).

This article explains the necessary steps to allow OpenTelemetry for your applications’ observability.

First, you have to configure your infrastructure to support observability, according to the Opentelemetry provider you will be using, and the Observability backend of your choice.

Next, follow the steps below.

## [Steps](#Steps)

**1.** Activate Observability in GeneXus.  
In [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408), select the service provider.

* [Observability with OpenTelemetry](https://wiki.genexus.com/commwiki/wiki?53775)
  + [Observability with Lightstep](https://wiki.genexus.com/commwiki/wiki?53776)
* [Observability with AWS Distro for OpenTelemetry](https://wiki.genexus.com/commwiki/wiki?53774)
* [Observability with Azure Monitor Application Insights](https://wiki.genexus.com/commwiki/wiki?54383)

**3.** Build any object.  
**4.** Deploy/Run.

**Note**: In the case of Java applications, the deployment to Docker automatically packages all the requirements and sets the environment settings to start the Docker image and have the application observable without the need for any extra configuration.  
If you are not using Docker containers, follow the instructions of [OpenTelemetry Java Automatic instrumentation](https://opentelemetry.io/docs/languages/java/automatic/). That is, download the [Java Agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases) and add -javaagent:path/to/opentelemetry-javaagent.jar and other config to your JVM startup arguments.

## [Logs and traces correlation](#Logs+and+traces+correlation)

Standardizing log correlation with traces and metrics increases the value of observability.

This is OpenTelemetry’s collection of logs, traces, and metrics:

`[imagen omitida: wiki id 57199]`

The connection between Logs and Traces is achieved by registering the trace\_id in the Logs.  
  
To achieve this with [GeneXus Java Generator](https://wiki.genexus.com/commwiki/wiki?12258), you only need to set the [Log Format property](https://wiki.genexus.com/commwiki/wiki?53005) = JSON, and the Observability Provider property must take a value other than None.

### [Java Sample](#Java+Sample)

Suppose you are working in a Java [environment](https://wiki.genexus.com/commwiki/wiki?7115) and you have configured the following properties:

[Log Format property](https://wiki.genexus.com/commwiki/wiki?53005) = JSON  
Observability Provider property = Observability with AWS Distro for OpenTelemetry.

Then a Log showing this connection will look like this:

```
{
    "@timestamp": "2023-09-25T05:02:11.812Z",
    "ecs.version": "1.2.0",
    "log.level": "DEBUG",
    "message": "Hello, world!",
    "process.thread.name": "http-nio-8080-exec-165",
    "log.logger": "GeneXusUserLog.GBrain.Middleware.Utils.ResponseExtractText",
    "AWS-XRAY-TRACE-ID": "1-65111441-4939baba8728c6453e80769f@a6ad1d8bfe037e4f",
    "span_id": "a6ad1d8bfe037e4f",
    "trace_flags": "01",
    "trace_id": "651114414939baba8728c6453e80769f"
}
```

### [.NET Sample](#.NET+Sample)

**Azure Monitor Sample**

* [Getting Opentelemetry logs in Application Insights](https://wiki.genexus.com/commwiki/wiki?54383).

**Opentelemetry Sample**

* [HowTo: Watch .NET logs using OpenTelemetry (with SigNoz)](https://wiki.genexus.com/commwiki/wiki?57281)

**AWS Distro sample**

* [HowTo: Watching .NET logs at AWS CloudWatch](https://wiki.genexus.com/commwiki/wiki?57287)


|  |
| --- |
| **Backlinks** |
| [HowTo: Observability of your GeneXus applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55863) | [Manual Instrumentation: Tracing](https://wiki.genexus.com/commwiki/wiki?57566) | [Table of contents:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |
| [Observability in GeneXus Apps](https://wiki.genexus.com/commwiki/wiki?53773) | [Observability in GeneXus Apps (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55862) | [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) |

---
