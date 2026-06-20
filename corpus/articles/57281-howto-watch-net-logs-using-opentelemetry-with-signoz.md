---
title: "HowTo: Watch .NET logs using OpenTelemetry (with SigNoz)"
source_id: 57281
source_url: https://wiki.genexus.com/commwiki/wiki?57281
genexus_version: "18"
---

# HowTo: Watch .NET logs using OpenTelemetry (with SigNoz)

The following is a sample scenario using the [SigNoz](https://signoz.io/) Observability back end.  
In this case, [containers](https://www.docker.com/resources/what-container/) are used to easily test a .NET application using [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/) (OTel).  
This is just one possible scenario you can set up to test [Observability](https://wiki.genexus.com/commwiki/wiki?53773) in .NET.

According to the [documentation](https://signoz.io/docs/instrumentation/dotnet/), there are two ways to send data to SigNoz Cloud:

* Send traces directly to SigNoz Cloud
* Send traces via OTel Collector (recommended)

In this document, the second option is used.

**Summary**

* [Prerequisite](#Prerequisite)
* [GeneXus application setup](#GeneXus+application+setup)
* [Environment setup](#Environment+setup)
* [Build the application](#Build+the+application)
* [Run the application](#Run+the+application)
* [Additional useful tips](#Additional+useful+tips)
* [Availability](#Availability)

## [Prerequisite](#Prerequisite)

You only need the following requirements on your local machine:

* [Get Docker](https://docs.docker.com/get-docker/)
* [SigNoz account](https://signoz.io/teams/)

## [GeneXus application setup](#GeneXus+application+setup)

The GeneXus web application is generated using [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243).

First, configure the [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) with the "OpenTelemetry" value and do a Build with this only of any object.  
From GeneXus' side, that's all you need to do.

## [Environment setup](#Environment+setup)

Below is a step-by-step guide to set up the local environment:

1. [Deploy your application to Docker](https://wiki.genexus.com/commwiki/wiki?36951).  
This packages your application and builds a Docker image, leaving it ready to be run when needed.  
The context folder of your deployment folder has this structure. Note that it has the dockerfile and a temp folder with your binaries and all the resources needed to run your app.

* context
  + temp
  + dockerfile

2. Copy the following files to the context folder (where the dockerfile is located).

* **docker-compose.yaml**

```
version: "3"
services:
      
  # OTEL Collector to receive logs, metrics and traces from the application
  otel-collector:
    image: otel/opentelemetry-collector:latest
    command: [ "--config=/etc/otel-collector.yaml" ]
    volumes:
      - ./otel-collector.yaml:/etc/otel-collector.yaml
    ports:
      - "4317:4317"
      - "4318:4318"
      - "9201:9201"

# Sample application
  otelsampleapp:
    build:
      context: .     
    environment:
      - OTEL_EXPORTER_OTLP_PROTOCOL=grpc
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317
      - OTEL_RESOURCE_ATTRIBUTES=service.namespace=GeneXus,service.name=sample-app,service.version=1.0.1
      - OTEL_METRICS_EXPORTER=otlp
      - OTEL_TRACES_EXPORTER=otlp
      - OTEL_LOGS_EXPORTER=otlp,logging
      - GX_LOG_LEVEL=debug
      - ASPNETCORE_URLS=http://*:8080

    ports:
      - "9999:8080"
```

Note that this file has an entry called otelsampleapp.  
This is the definition of your web application, which has its dockerfile located in the context directory.  
There you define the necessary environment variables.

* **otel-collector.yaml**

The file has the following contents:

```
receivers:
  otlp:
    protocols:
      grpc:
      http:

processors:
  batch:

exporters:
  debug:
    verbosity: detailed
  otlp:
    endpoint: "ingest.{your_region}.signoz.cloud:443"
    tls:
      insecure: false
    headers:
      "signoz-access-token": <your_access_token>

service:
  pipelines:

    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]
```

The access token can be found in the Settings pane of SigNoz UI.

For more information on the configuration of the OTel Collector, see [here](https://signoz.io/docs/tutorial/opentelemetry-binary-usage-in-virtual-machine/).

## [Build the application](#Build+the+application)

First, run the [docker-compose command](https://docs.docker.com/engine/reference/commandline/compose_up/) to create and start the container.  
Open a terminal in the context folder and run:

- docker-compose up -d  
  
You can see the created container using [Docker desktop](https://www.docker.com/products/docker-desktop/).

## [Run the application](#Run+the+application)

Run the application to generate some traffic.

In the SigNoz account, open the Services tab. Click on the Refresh button on the top right corner, and your application should appear in the list of Applications.  
You might have to wait for a few seconds before the data appears on SigNoz UI.

You can see the [Traces](https://wiki.genexus.com/commwiki/wiki?53777) of your application at the Traces pane:

`[imagen omitida: wiki id 57282]`

The following are the details of a selected Trace:

`[imagen omitida: wiki id 57283]`

The log correlation with other telemetry signals such as Traces is an important feature of OpenTelemetry.  
You can click on "Related Logs" and see the logs of the application (.NET standard classes logs and logs using the [Log external object](https://wiki.genexus.com/commwiki/wiki?37872)), filtered by the Trace\_Id.

`[imagen omitida: wiki id 57284]`

## [Additional useful tips](#Additional+useful+tips)

If you configure the [debug exporter](https://github.com/open-telemetry/opentelemetry-collector/blob/main/exporter/debugexporter/README.md) like this:

```
debug:

  verbosity: detailed
```

There is debug information for the execution and to detect any misconfigurations or errors.

`[imagen omitida: wiki id 57286]`

Besides, by configuring the logging exporter for LOGS, you have the logging telemetry data at the std output.

```
OTEL_LOGS_EXPORTER=otlp,logging
```

## [Availability](#Availability)

Since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242)


|  |
| --- |
| **Backlinks** |
| [HowTo: Observability of your GeneXus applications](https://wiki.genexus.com/commwiki/wiki?53767) | [Toc:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |

---
