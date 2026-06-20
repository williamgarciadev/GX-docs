---
title: "HowTo: Watching .NET logs at AWS CloudWatch"
source_id: 57287
source_url: https://wiki.genexus.com/commwiki/wiki?57287
genexus_version: "18"
---

# HowTo: Watching .NET logs at AWS CloudWatch

The following is a brief guide of how to get application logs in AWS CloudWatch of a .NET application instrumented using [OpenTelemetry](https://opentelemetry.io/) (OTel).

After following the steps indicated at [HowTo: Setup the environment to test Observability (using AWS CloudWatch)](https://wiki.genexus.com/commwiki/wiki?57258), you need to add some minor modifications to the configuration if you want to see your application logs.

### [1. Add aws.log.group.arns to OTEL\_RESOURCE\_ATTRIBUTES](#1.+Add+aws.log.group.arns+to+OTEL_RESOURCE_ATTRIBUTES)

At docker-compose.yaml (where the application build is defined), add a OTEL resource attribute named *aws.log.group.arns* in order to correlate logs with traces.  
Check the [documentation](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/awsxrayexporter#traces-and-logs-correlation) related to this topic.

```
 # Sample application
  otelsampleapp:
    build:
       context: .
    environment:
    
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://aws-ot-collector:4317
      - OTEL_RESOURCE_ATTRIBUTES=service.namespace=GeneXus,service.name=sampleGX,aws.log.group.arns="arn:aws:logs:us-east-1:11111111111:log-group:metrics/GeneXus/sampleGX:*"
      - AWS_REGION=us-east-1
      - OTEL_METRICS_EXPORTER=otlp
      - OTEL_TRACES_EXPORTER=otlp
      - OTEL_LOGS_EXPORTER=otlp
      - OTEL_PROPAGATORS=xray
      - GX_LOG_LEVEL=debug
      - ASPNETCORE_URLS=http://*:8080
    ports:
      - "9999:8080"
    depends_on:
      - aws-ot-collector
```

You get the Log Group ARN at the Log Group settings.

### [2. Use the [awscloudwatchlogsexporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/awscloudwatchlogsexporter) to export logs to AWS.](#2.+Use+the+https%3A%2F%2Fgithub.com%2Fopen-telemetry%2Fopentelemetry-collector-contrib%2Ftree%2Fmain%2Fexporter%2Fawscloudwatchlogsexporter+awscloudwatchlogsexporter+to+export+logs+to+AWS.)

So in the OTel agent configuration file, add this exporter. Do not forget to add it to the service pipeline also.

```
exporters:
  debug:
    verbosity: detailed
    sampling_initial: 5
    sampling_thereafter: 200
  awsxray:
    region: 'us-east-1'
  awsemf:
    region: 'us-east-1'
  awscloudwatchlogs:
    log_group_name: "metrics/GeneXus/sampleGX"
    log_stream_name: "otel-stream-testgx"
    region: "us-east-1"
    endpoint: "logs.us-east-1.amazonaws.com"

service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [awsxray]
    metrics:
      receivers: [otlp]
      exporters: [awsemf]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [awscloudwatchlogs]
```

You have to replace the settings according to your needs.

### [3. Define roles](#3.+Define+roles+)

There are some permissions that have to be granted to the user (directly through a policy or through IAM Roles), to be able to create [Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html), and add data to that logs.

See [this documentation](https://aws-otel.github.io/docs/setup/permissions). Unless the permissions are set, you won't see any logs at CloudWatch or even the Log Groups and Streams will not be created.  
You can also check [Identity and access management for Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/auth-and-access-control-cwl.html).

After those configuration steps, you can execute the application and see your logs, using Logs Insights.

You can filter by the trace Id, like in the following figure:

`[imagen omitida: wiki id 57288]`

And get all the Logs of that trace:

`[imagen omitida: wiki id 57289]`

### [Availability](#Availability)

Since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242)


|  |
| --- |
| **Backlinks** |
| [HowTo: Observability of your GeneXus applications](https://wiki.genexus.com/commwiki/wiki?53767) | [Toc:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |

---
