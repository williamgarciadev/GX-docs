---
title: "OpenTelemetry components and configuration"
source_id: 57276
source_url: https://wiki.genexus.com/commwiki/wiki?57276
genexus_version: "18"
---

# OpenTelemetry components and configuration

This is an overview of the main concepts around OpenTelemetry.  
You can take a look at the Opentelemetry documentation to see the [OpenTelemetry Components](https://opentelemetry.io/docs/what-is-opentelemetry/#main-opentelemetry-components).

**Summary**

* [OpenTelemetry Collector](#OpenTelemetry+Collector)

+ [Collector Configuration](#Collector+Configuration)

* [Environment Variable settings](#Environment+Variable+settings)
* [OpenTelemetry Backends](#OpenTelemetry+Backends)

## [OpenTelemetry Collector](#OpenTelemetry+Collector)

The [OpenTelemetry (OTEL) Collector](http://opentelemetry.io/docs/collector/) offers a vendor-agnostic implementation of how to receive, process and export telemetry data.

The Otel Collector can collect data from OpenTelemetry SDKs and other sources (in multiple formats, for example, OTLP, Jaeger, Prometheus, as well as many commercial/proprietary tools), and then export this telemetry to any supported backend, such as Jaeger, Prometheus or Kafka queues. It also supports processing and filtering telemetry data before it gets exported.

Basically, it's a middleware that can run either very close to your workloads (“agent” mode), or on a central location (“collector”, or “service” mode - as a central collector service aggregating across multiple application nodes). For more information on deployment, see [Patterns you can apply to deploy the OpenTelemetry collector](https://opentelemetry.io/docs/collector/deployment/).

### [Collector Configuration](#Collector+Configuration)

By default, the Collector configuration is located in a config.yaml file (see [Location Configuration](https://opentelemetry.io/docs/collector/configuration/#location)).

It is built following a **pipeline principle**, with receivers, processors, and exporters, potentially making use of extensions:

* **[Receivers](https://opentelemetry.io/docs/collector/configuration/#receivers)** are the components responsible for gathering or receiving telemetry data.
* [**Processors**](https://opentelemetry.io/docs/collector/configuration/#processors) can look into the telemetry data and make decisions based on them, such as performing data cleanup, applying sampling decisions, including or removing attributes, and enriching data based on where it’s running, among others.
* [**Exporters**](https://opentelemetry.io/docs/collector/configuration/#exporters) will then send the data out of the process, likely to one or more telemetry backends or another layer of collectors.  
  Therefore, an [exporter](https://github.com/open-telemetry/opentelemetry-collector/tree/main/exporter) defines how data gets sent to different systems/backends. In general, an exporter translates the internal format into another defined format.  
  See OpenTelemetry documentation for Exporters in [Java](https://opentelemetry.io/docs/instrumentation/java/exporters/) and [NET](https://opentelemetry.io/docs/instrumentation/net/exporters/).
* [**Extensions**](https://opentelemetry.io/docs/collector/configuration/#extensions) are not part of the data pipeline but can help other components, for example, by adding extensions for Collector health monitoring.

[**OpenTelemetry Protocol﻿ (OTLP)**](https://opentelemetry.io/docs/specs/otlp/) specifies how OpenTelemetry-related components exchange telemetry data.  
This includes instrumented applications, intermediary services such as the Collector, and backends to which the data is eventually sent.  
OTLP primarily defines message structures, encoding, and endpoints and relies on HTTP or [gRPC](https://grpc.io/) as the underlying transport protocol.

## [Environment Variable settings](#Environment+Variable+settings)

The following are some environment variables generally used to configure the **OTLP Exporter**.

* OTEL\_EXPORTER\_OTLP\_PROTOCOL - The transport protocol (grpc, http/protobuf, http/json).
* OTEL\_EXPORTER\_OTLP\_ENDPOINT - Endpoint (OTLP/HTTP or OTLP/gRPC).

Check [OTLP Exporter configuration](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/).

You can define environment variables for setting one or more **exporters** per signal.

* OTEL\_TRACES\_EXPORTER
* OTEL\_METRICS\_EXPORTER
* OTEL\_LOGS\_EXPORTER

In general, you also define:

* OTEL\_SERVICE\_NAME - Sets the value of the [service.name](https://opentelemetry.io/docs/specs/semconv/resource/#service) resource attribute
* OTEL\_RESOURCE\_ATTRIBUTES - Key-value pairs to be used as [resource](https://opentelemetry.io/docs/concepts/resources/) attributes

Check [General SDK configuration documentation](https://opentelemetry.io/docs/languages/sdk-configuration/general/).

For testing and debugging, see [Debug Exporter](https://github.com/open-telemetry/opentelemetry-collector/blob/main/exporter/debugexporter/README.md).

## [OpenTelemetry Backends](#OpenTelemetry+Backends)

In addition, OpenTelemetry requires a backend system to store, process, analyze, and visualize the telemetry data collected from applications. It does not include a specific built-in backend to process and analyze the data. Instead, it allows to integrate with various backend systems.  
Backend systems receive the exported telemetry data from the instrumented applications or the OpenTelemetry Collector. These systems are responsible for storing, analyzing, and visualizing the telemetry data. For example, Prometheus, AWS Xray, Zipkin, Lightstep, etc.  
  
There are also visualization services for viewing data connected to Backend services. For example, [Grafana](https://grafana.com/docs/grafana/latest/)


|  |
| --- |
| **Backlinks** |
| [Table of contents:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |

---
