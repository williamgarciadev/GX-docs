---
title: "Observability with OpenTelemetry"
source_id: 53775
source_url: https://wiki.genexus.com/commwiki/wiki?53775
genexus_version: "18"
---

# Observability with OpenTelemetry

GeneXus collects telemetry data (traces, logs, and metrics) of its applications with [OpenTelemetry](https://opentelemetry.io/).

`[imagen omitida: wiki id 53778]`

The steps you must follow to use it are:

1. Set the [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408).
2. Execute the OpenTelemetry collector.
3. Configure the Environment Variables. See [General purpose configuration](https://opentelemetry.io/docs/concepts/sdk-configuration/general-sdk-configuration/) and [OTLP Exporter configuration](https://opentelemetry.io/docs/concepts/sdk-configuration/otlp-exporter-configuration/).
4. Configure the Collector with an Observability Backend.
5. Execute.

### [Set the Observability Provider Property](#Set+the+Observability+Provider+Property)

Select the value Opentelemetry in the [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408).

### [Execute the OpenTelemetry collector](#Execute+the+OpenTelemetry+collector)

Follow the document [Getting Started](https://opentelemetry.io/docs/collector/getting-started/) to execute the collector.

### [Configure Environment Variables](#Configure+Environment+Variables)

Configure the following environment variables in the application’s Docker Image.

* [OTEL\_EXPORTER\_OTLP\_ENDPOINT](https://opentelemetry.io/docs/concepts/sdk-configuration/otlp-exporter-configuration/)
* [OTEL\_RESOURCE\_ATTRIBUTES](https://opentelemetry.io/docs/concepts/sdk-configuration/otlp-exporter-configuration/)

For more information, refer to: [SDK Configuration](https://opentelemetry.io/docs/concepts/sdk-configuration/).

#### [Sample](#Sample)

```
OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317
OTEL_METRICS_EXPORTER=otlp 
OTEL_RESOURCE_ATTRIBUTES=service.namespace=GeneXus,service.name=sample-app,service.version=1.0.1
```

### [Configure the Collector with a Backend](#Configure+the+Collector+with+a+Backend)

Refer to the [Configure](https://opentelemetry.io/docs/collector/configuration/) document.

#### [Sample](#Sample)

If the application runs in Docker, it is possible to execute OpenTelemetry through [Docker Compose](https://docs.docker.com/engine/reference/commandline/compose/).

You may execute the following compose.yaml that has the configured collector connected to the GeneXus application to be deployed.

otel-collector-confing.yaml sample can be seen here: <https://opentelemetry.io/docs/collector/configuration/>

**compose.yaml:**

```
version: "2"
services:
   # Collector
  otel-collector:
    image: otel/opentelemetry-collector-dev:latest
    command: ["--config=/etc/otel-collector-config.yaml", ""]
    volumes:
      - ./otel-collector-config.yaml:/etc/otel-collector-config.yaml          

    ports:
      - "4317:4317"   # OTLP gRPC receiver
      - "4318:4318"   # OTLP Http receiver
         
  smaplegenexusapp:
    build:
      context: .    
    environment:
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317
      - OTEL_RESOURCE_ATTRIBUTES=service.namespace=GeneXus,service.name=sample-app,service.version=1.0.1
      - OTEL_METRICS_EXPORTER=otlp    
      - GX_LOG_LEVEL=info
      - GX_LOG_LEVEL_USER=debug
      - GX_LOG_OUTPUT=ConsoleAppender

    ports:
      - "80:80"
```

### [Scope](#Scope)

**Generator:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [Availability](#Availability)

This functionality is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).

### [See Also](#See+Also)

[Log settings with environment variables](https://wiki.genexus.com/commwiki/wiki?53361)


|  |
| --- |
| **Backlinks** |
| [HowTo: Observability of your GeneXus applications](https://wiki.genexus.com/commwiki/wiki?53767) | [HowTo: Observability of your GeneXus applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55863) | [Toc:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |
| [Observability in GeneXus Apps](https://wiki.genexus.com/commwiki/wiki?53773) | [Observability in GeneXus Apps (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55862) |

---
