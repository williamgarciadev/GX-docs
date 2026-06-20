---
title: "HowTo: Setup the environment to test Observability (using AWS CloudWatch)"
source_id: 57258
source_url: https://wiki.genexus.com/commwiki/wiki?57258
genexus_version: "18"
---

# HowTo: Setup the environment to test Observability (using AWS CloudWatch)

This is one possible scenario you can set up to test Observability (Traces and Metrics) using [AWS X-Ray](https://aws.amazon.com/xray/?nc1=h_ls) and [AWS CloudWatch](https://aws.amazon.com/es/cloudwatch/) for a .NET application.

In this case, the [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) is set to AWS Distro for Opentelemetry (ADOT).  
  
Start by noting that, by setting this property, GeneXus generates your .NET application to be instrumented using OpenTelemetry SDK enabled for use with X-Ray.  
  
You only need to setup the [AWS OpenTelemetry (ADOT) Collector](https://github.com/aws-observability/aws-otel-collector) to have the whole system working.

In this sample case, containers are used to easily test the application, using AWS credentials for connecting to AWS services.  
If you haven't set up your AWS Credential profile yet, please follow the [instructions](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) for setting up your AWS credentials. They are required to connect to Amazon services.

For detailed information on other scenarios (such as using [AWS ECS](https://aws-otel.github.io/docs/setup/ecs), [AWS EC2](https://aws-otel.github.io/docs/setup/ecs), [EKS](https://aws-otel.github.io/docs/getting-started/adot-eks-add-on), [AWS AppRunner](https://docs.aws.amazon.com/apprunner/latest/dg/monitor-xray.html), [on-premises](https://aws-otel.github.io/docs/setup/on-premises)), please refer to the AWS corresponding documentation.

**Summary**

* [Prerequisite](#Prerequisite)
* [GeneXus application setup](#GeneXus+application+setup)
* [Environment setup](#Environment+setup)
* [How to run the application](#How+to+run+the+application)
* [Viewing the telemetry data at AWS X-Ray](#Viewing+the+telemetry+data+at+AWS+X-Ray)
* [See Also](#See+Also)

## [Prerequisite](#Prerequisite)

You only need the following requirement on your local machine:

* [Get Docker](https://wiki.genexus.com/commwiki/wiki?39548,,)

## [GeneXus application setup](#GeneXus+application+setup)

The GeneXus web application is generated using [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) (which uses .NET 8).

First, configure the Observability Provider property with the "AWS Distro for Opentelemetry" value and do a Build with this only for any object. This generates the CloudServices.config file with the following contents. To have the generated application use the Opentelemetry SDK.

```
 <Service>
    <Name>AWSOTEL</Name>
    <Type>Observability</Type>
    <ClassName>GeneXus.OpenTelemetry.AWS.AWSOtelProvider, GeneXus.OpenTelemetry.AWS.AspNet, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null</ClassName>
    <Properties />
  </Service>
```

From GeneXus' side, that's all you need to do.

## [Environment setup](#Environment+setup)

Below is a step-by-step guide to set up the local environment:

1. [Deploy you application to Docker](https://wiki.genexus.com/commwiki/wiki?36951)  
  
This packages your application and builds a Docker image, leaving it ready to be run when needed.  
The context folder of your deployment folder has this structure. Note that it has the dockerfile and a temp folder with your binaries and all the resources needed to run your app.

* context
  + temp
  + dockerfile

2. Copy the following files to the context folder (where the dockerfile is located).

* docker-compose.yaml

[Compose](https://docs.docker.com/compose/) a file that loads the services: ADOT Collector, and your application service. You can download the file [here](https://wiki.genexus.com/commwiki/wiki?57263,,).

Note that this file has an entry like the following:  
This is the definition of your web application, which has its dockerfile located in the context directory.  
Here, you can define the environment variables.

```
otelsampleapp:
    build:
      context: .
    environment:
    
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://aws-ot-collector:4317
      - OTEL_RESOURCE_ATTRIBUTES=service.namespace=GeneXus,service.name=sampleGX
      - AWS_REGION=us-east-1
      - OTEL_METRICS_EXPORTER=otlp
      - OTEL_TRACES_EXPORTER=otlp
      - OTEL_LOGS_EXPORTER=otlp
      - GX_LOG_LEVEL=debug
      - ASPNETCORE_URLS=http://*:8080
    ports:
      - "9999:8080"
    depends_on:
      - aws-ot-collector
```

The [ASPNETCORE\_URLS](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/web-host?view=aspnetcore-8.0#server-urls) environment variable is necessary for .NET 8 applications. In this case, the default port where the application will be running at the container is 8080.  
"ports" indicates the port mapping. Your app can be accessed locally at port 9999.  
For more information on OTEL environment variables, click [here](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/).

The ADOT collector has to be added to the docker-compose file as shown.  
Note that you should add your AWS credentials, or otherwise, your AWS\_PROFILE.  
The AWS Region should also be modified as required.

```
 # ADOT Collector
  aws-ot-collector:
    image: public.ecr.aws/aws-observability/aws-otel-collector:latest
    command: ["--config=/etc/otel-agent-config.yaml"]
    environment:
      - AWS_REGION=us-east-1
      - AWS_ACCESS_KEY_ID=<Here your Access Key>
      - AWS_SECRET_ACCESS_KEY=<Here your Secret Access Key>
    volumes:
      - ./config-test.yaml:/etc/otel-agent-config.yaml
      - /.aws:/home/aoc/.aws
    ports:
      - "1777:1777"   # pprof extension
      - "55680:55680" # zpages extension
      - "13133"       # health_check
```

* config-test.yaml  
  It defines the receivers, and exporters (awsxray for traces, [awsemf](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/exporter/awsemfexporter/README.md) for metrics). Download it [here](https://wiki.genexus.com/commwiki/wiki?57264,,).

## [How to run the application](#How+to+run+the+application)

First, run the docker-compose command to create and start the container.  
Open a terminal in the context folder and run:

```
- docker-compose up -d
```

This pulls all the required images and creates a container with all of them.  
You can see the created container using [Docker desktop](https://www.docker.com/products/docker-desktop/).

In this case, the sample app runs on the local port 9999.

Since, in this example, your main object is wwtestdata2, you can access the application at: http://localhost:9999/wwtestdata2.aspx

## [Viewing the telemetry data at AWS X-Ray](#Viewing+the+telemetry+data+at+AWS+X-Ray)

After executing the application, you can go to the AWS console and see the telemetry data emitted by your application.

You will see that a Logging Group is created using the service.name that you established for your service (in this example: "sampleGX").

The following is the Trace Map under X-Ray Traces menu option.

`[imagen omitida: wiki id 57265]`

This is a view of a Trace and its Spans:

`[imagen omitida: wiki id 57266]`

The following is a view of some Metrics:

`[imagen omitida: wiki id 57267]`

## [See Also](#See+Also)

[Observability with AWS Distro for OpenTelemetry](https://wiki.genexus.com/commwiki/wiki?53774)  
[CloudWatch EMF Exporter (awsemf)](https://aws-otel.github.io/docs/getting-started/cloudwatch-metrics#cloudwatch-emf-exporter-awsemf)  
[Configuring permissions](https://aws-otel.github.io/docs/setup/permissions)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243) | [HowTo: Watching .NET logs at AWS CloudWatch](https://wiki.genexus.com/commwiki/wiki?57287) | [Toc:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |
| [Observability with AWS Distro for OpenTelemetry](https://wiki.genexus.com/commwiki/wiki?53774) |

---
