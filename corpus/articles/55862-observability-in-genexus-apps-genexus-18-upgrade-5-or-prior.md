---
title: "Observability in GeneXus Apps (GeneXus 18 Upgrade 5 or prior)"
source_id: 55862
source_url: https://wiki.genexus.com/commwiki/wiki?55862
genexus_version: "18"
---

# Observability in GeneXus Apps (GeneXus 18 Upgrade 5 or prior)

GeneXus accepts OpenTelemetry as the way to obtain telemetry data (traces, logs and metrics) from the application.

This allows to know what exactly is going on in the System, including:

* The time required by Requests.
* Entry points and the most requested programs.
* Execution of SQL sentences. The time required for each Request to be replied to.
* The number of Error 500. The exceptions that occur and which exactly are they.
* Traces of Http calls (micro-services).
* Creation of automatic alerts based on telemetry.

The data instrumented automatically (sent to the observability backend by the Apps) are*:*

### [JAVA](#JAVA)

* Access to the database (Insert, Select, Delete, etc.)
* Calls to API through HttpClient
* Cache Access (Redis & Memcached)
* Application Server metrics
* AWS SDK, Redis, Memcached, etc.

Full List: <https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md#libraries--frameworks>

### [.NET](#.NET)

* Access to the database (Insert, Select, Delete, etc.)
* Calls to API through HttpClient
* Aspnet Core Application Server metrics

### [Opentelemetry providers](#Opentelemetry+providers+)

To achieve this, you may select any of the following SDK:

* AWS Distro for OpenTelemetry (ADOT)
* Lightstep
* SDK OpenTelemetry
* Azure Monitor Application Insights

### [AWS Distro for OpenTelemetry (ADOT)](#AWS+Distro+for+OpenTelemetry+%28ADOT%29)

[ADOT](https://wiki.genexus.com/commwiki/wiki?53774) provides API, libraries and open source agents to compile distributed metrics and traces for app monitoring. It also compiles metadata from its resources and administered services of Amazon Web Services. This makes it possible to correlate the app’s performance data with the data of the underlying infrastructure.

ADOT receives the app’s traces and it is also configured to periodically compile endpoint metrics/app metrics through HTTP.

### [Lightstep](#Lightstep+)

[Lightstep Observability](https://wiki.genexus.com/commwiki/wiki?53776) combines metrics data and trace data to achieve full observability. It provides a series of tools that enable the monitoring of resources and transactions, as well as the classification of incidents and the configuration of alerts, and it defines alert thresholds or critical points, among other things.

### [SDK OpenTelemetry](#SDK+OpenTelemetry+)

[SDK OpenTelemetry](https://wiki.genexus.com/commwiki/wiki?53775) enables the creation of traces and metrics events, in addition to exporting telemetry data to an analysis backend.

### [Azure Monitor Application Insights](#Azure+Monitor+Application+Insights)

[Application Insights](https://wiki.genexus.com/commwiki/wiki?54383) is an extension of [Azure Monitor](http://learn.microsoft.com/en-us/azure/azure-monitor/overview) that provides Application Performance Monitoring (APM) features.

### [Availability](#Availability)

This functionality is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).

### [See Also](#See+Also)

[HowTo: Observability of your GeneXus applications](https://wiki.genexus.com/commwiki/wiki?53767).
