---
title: "HowTo: Set up the environment to test Observability (using Grafana)"
source_id: 56829
source_url: https://wiki.genexus.com/commwiki/wiki?56829
genexus_version: "18"
---

# HowTo: Set up the environment to test Observability (using Grafana)

This is just one possible scenario you can set up to test [Observability](https://wiki.genexus.com/commwiki/wiki?53773) in .NET.

In this case, [containers](https://www.docker.com/resources/what-container/) are used to easily test a .NET application using [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/) (OTEL).

[Prometheus](https://prometheus.io/) will be used to analyze Metrics and [Tempo](https://grafana.com/oss/tempo/) (distributed tracing backend) to watch Traces, all in [Grafana](https://grafana.com/) running in a Docker container.

**Summary**

* [Prerequisite](#Prerequisite)
* [GeneXus application setup](#GeneXus+application+setup)
* [Environment setup](#Environment+setup)
* [How to run the application](#How+to+run+the+application)
* [Using Grafana](#Using+Grafana)

### [Prerequisite](#Prerequisite)

You only need the following requirement on your local machine:

* [Get Docker](https://docs.docker.com/get-docker/)

### [GeneXus application setup](#GeneXus+application+setup)

The GeneXus web application is generated using [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) (which uses .NET 8).

First, configure the [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) with the "OpenTelemetry" value and do a Build with this only of any object. This generates the CloudServices.config file with the following contents to have the generated application use the Opentelemetry SDK.

```
 <Service>
    <Name>OPENTELEMETRY</Name>
    <Type>Observability</Type>
    <ClassName>GeneXus.OpenTelemetry.OpenTelemetry.OpenTelemetryProvider, GeneXus.OpenTelemetry, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null</ClassName>
    <Properties />
  </Service>
```

From GeneXus' side, that's all you need to do.

### [Environment setup](#Environment+setup)

Below is a step-by-step guide to set up the local environment

1. [Deploy your application to Docker](https://wiki.genexus.com/commwiki/wiki?36951).  
This packages your application and builds a Docker image, leaving it ready to be run when needed.  
The *context* folder of your deployment folder has this structure. Note that it has the *dockerfile* and a *temp* folder with your binaries and all the resources needed to run your app.

* context
  + temp
  + dockerfile

2. Copy the following files to the *context* folder (where the dockerfile is located).

* *docker-compose.yaml*  
  [Compose](https://docs.docker.com/compose/) a file that loads the services: otel-collector, tempo, prometheus, grafana, and your application service. You can download the file [here](https://wiki.genexus.com/commwiki/wiki?56838,,).  
    
  Note that this file has an entry like the following.  
  This is the definition of your web application, which has its dockerfile located in the context directory.  
  Here you can define the environment variables.

```
# Sample application
  otelsampleapp:
    build:
      context: .     
    environment:
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317
      - OTEL_RESOURCE_ATTRIBUTES=service.namespace=GeneXus,service.name=sample-app,service.version=1.0.1
      - OTEL_METRICS_EXPORTER=otlp
      - OTEL_TRACES_EXPORTER=otlp
      - OTEL_LOGS_EXPORTER=otlp,logging
      - GX_LOG_OUTPUT=ConsoleAppender
      - ASPNETCORE_URLS=http://*:8080
    ports:
      - "9999:8080"
```

The [ASPNETCORE\_URLS](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/web-host?view=aspnetcore-8.0#server-urls) environment variable is necessary for .NET 8 applications. In this case, the default port where the application will be running at the container is 8080.

"ports" indicates the port mapping. Your app can be accessed locally at port 9999.  
  
For more information on OTEL environment variables, click [here](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/).

* *grafana-datasources.yaml*  
  The file has the following contents:

```
apiVersion: 1

datasources:
- name: Prometheus
  type: prometheus
  uid: prometheus
  access: proxy
  orgId: 1
  url: http://prometheus:9090
  basicAuth: false
  isDefault: true
  version: 1
  editable: false
  jsonData:
    httpMethod: GET
    exemplarTraceIdDestinations:
    - name: trace_id
      datasourceUid: Tempo
- name: Tempo
  type: tempo
  access: proxy
  orgId: 1
  url: http://tempo:3200
  basicAuth: false
  isDefault: false
  version: 1
  editable: false
  apiVersion: 1
  uid: tempo
  jsonData:
    httpMethod: GET
    serviceMap:
      datasourceUid: prometheus
```

* *otel-collector.yaml*  
  Here we [configure the OpenTelemetry collector](https://opentelemetry.io/docs/collector/configuration/). The file has the [following contents](https://wiki.genexus.com/commwiki/wiki?56882,,).
* *prometheus.yaml*  
  This is the configuration of Prometheus. Download it from [here](https://wiki.genexus.com/commwiki/wiki?56883,,).
* tempo.yaml  
  This is the configuration of Tempo.

  ```
  server:
    http_listen_port: 3200

  distributor:
    receivers:
      otlp:
        protocols:
          http:
          grpc:

  storage:
    trace:
      backend: local
      wal:
        path: /tmp/tempo/wal
      local:
        path: /tmp/tempo/blocks
  ```

### [How to run the application](#How+to+run+the+application)

First, run the [docker-compose command](https://docs.docker.com/engine/reference/commandline/compose_up/) to create and start the container.  
Open a terminal in the context folder and run:

- docker-compose up -d

`[imagen omitida: wiki id 56830]`

This pulls all the required images and creates a container with all of them.

You can see the created container using [Docker desktop](https://www.docker.com/products/docker-desktop/).

`[imagen omitida: wiki id 56839]`

In this case, the sample app runs on the local port 9999.

Since in this example your main object is wwtestdata2, you can access the application at: http://localhost:9999/wwtestdata2.aspx

`[imagen omitida: wiki id 56833]`

You may use the following Powershell script to generate a load to the application.

```
while($true)
{
    Invoke-WebRequest http://localhost:9999/wwtestdata2.aspx
    Start-Sleep -Milliseconds 500
}
```

### [Using Grafana](#Using+Grafana)

The application sends metrics and traces to the OTel Collector, which exports metrics and traces to Prometheus and Tempo, respectively.

Wait for 2 minutes while running tests before analyzing the data, so that enough data is generated and exported.

Open Grafana (http://localhost:3000), select Explore and select Prometheus as the source.

There you have a "Metric" combo box with all the available metrics to view.

`[imagen omitida: wiki id 56836]`

`[imagen omitida: wiki id 56835]`

Using Tempo datasource you can view the traces generated by OpenTelemetry.

`[imagen omitida: wiki id 56837]`

**Tip:** The following command line is useful for troubleshooting when a container fails to start:

docker logs <container\_id> -f


|  |
| --- |
| **Backlinks** |
| [HowTo: Watch application logs using Loki](https://wiki.genexus.com/commwiki/wiki?57290) | [Toc:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |

---
