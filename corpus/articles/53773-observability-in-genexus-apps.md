---
title: "Observability in GeneXus Apps"
source_id: 53773
source_url: https://wiki.genexus.com/commwiki/wiki?53773
genexus_version: "18"
---

# Observability in GeneXus Apps

GeneXus Observability solution is based on [OpenTelemetry](https://opentelemetry.io/), as the way to obtain telemetry data (traces, logs and metrics) from the application.

This allows to know what exactly is going on in the System, including:

* The time required by Requests.
* Entry points and the most requested programs.
* Execution of SQL sentences. The time required for each Request to be replied to.
* The number of Error 500. The exceptions that occur and which exactly are they.
* Traces of Http calls (micro-services).
* Creation of automatic alerts based on telemetry.

In Java Generator, the instrumentation is [automatic](https://opentelemetry.io/docs/languages/java/automatic/).  
The data instrumented **automatically** (sent to the observability backend by the Apps) are*:*

* Access to the database (Insert, Select, Delete, etc.).
* Calls to API through HttpClient.
* Cache Access (Redis & Memcached).
* Application Server metrics.
* Redis, Memcached, etc.
* Logs are connected to Traces to display GeneXus logs at trace level.

Automatically instrumented libraries in Java are listed [here](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md#libraries--frameworks).

### [Opentelemetry providers](#Opentelemetry+providers)

To have your app instrumented, you may select any of the following SDKs:

* [AWS Distro for OpenTelemetry](https://aws-otel.github.io/) (ADOT)
  + See [Observability with AWS Distro for OpenTelemetry](https://wiki.genexus.com/commwiki/wiki?53774)
* OpenTelemetry SDK
  + See [Observability with OpenTelemetry](https://wiki.genexus.com/commwiki/wiki?53775)
* Azure Monitor Application Insights
  + It's an extension of [Azure Monitor](http://learn.microsoft.com/en-us/azure/azure-monitor/overview) that provides Application Performance Monitoring (APM) features. See [Observability with Azure Monitor Application Insights](https://wiki.genexus.com/commwiki/wiki?54383)

### [See Also](#See+Also)

[HowTo: Observability of your GeneXus applications](https://wiki.genexus.com/commwiki/wiki?53767)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396) | [HowTo: Set up the environment to test Observability (using Grafana)](https://wiki.genexus.com/commwiki/wiki?56829) | [Table of contents:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |
| [Observability in GeneXus Apps (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55862) | [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) |

---
