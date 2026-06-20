---
title: "Observability with AWS Distro for OpenTelemetry"
source_id: 53774
source_url: https://wiki.genexus.com/commwiki/wiki?53774
genexus_version: "18"
---

# Observability with AWS Distro for OpenTelemetry

GeneXus integrates with [AWS Distro for OpenTelemetry](https://aws-otel.github.io/) to compile metrics and traces of applications, offering a comprehensive approach to application observability. This guide outlines the steps to configure and utilize AWS Distro for OpenTelemetry with your GeneXus applications.

Follow these steps for a successful integration:

1. **Set the Observability Provider Property:** Choose 'AWS Distro for OpenTelemetry' as your observability provider.
2. **Execute the AWS OpenTelemetry Collector:** Install and run the AWS Otel collector based on the official guide.
3. **Configure the Environment Variables:** Set necessary environment variables in your app’s Docker image.
4. **Configure AWS Credentials:** Ensure your collector has the appropriate AWS credentials with minimal required permissions.
5. **Execute the App’s Docker Image:** Run your application’s Docker image with the configured settings.

### [Set the Observability Provider Property](#Set+the+Observability+Provider+Property)

Select **AWS Distro for OpenTelemetry** in the [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) to integrate AWS telemetry services with your application.

### [Execute the AWS OpenTelemetry Collector](#Execute+the+AWS+OpenTelemetry+Collector)

Refer to [this guide](https://github.com/aws-observability/aws-otel-collector) to install and run the AWS OpenTelemetry collector, which is essential for telemetry data collection.

### [Configure the Environment Variables](#Configure+the+Environment+Variables)

Set the following environment variables in your application's Docker image for proper telemetry data export:

* [OTEL\_EXPORTER\_OTLP\_ENDPOINT](https://opentelemetry.io/docs/concepts/sdk-configuration/otlp-exporter-configuration/)
* [OTEL\_RESOURCE\_ATTRIBUTES](https://opentelemetry.io/docs/concepts/sdk-configuration/otlp-exporter-configuration/)

#### [Sample Configuration:](#Sample+Configuration%3A)

```
OTEL_EXPORTER_OTLP_ENDPOINT=http://aws-ot-collector:4317
OTEL_METRICS_EXPORTER=otlp
OTEL_RESOURCE_ATTRIBUTES=service.namespace=GeneXus,service.name=sample-app,service.version=1.0.1
```

For detailed information on SDK configuration, visit: [SDK Configuration](https://opentelemetry.io/docs/concepts/sdk-configuration/).

### [Configure the AWS Credentials](#Configure+the+AWS+Credentials)

Assign the necessary [AWS Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console) to the collector. These credentials should adhere to the minimal IAM Policy requirements for security and efficiency.

### [Execute Docker Image](#Execute+Docker+Image)

Finally, execute your application's Docker image with the configured settings.

#### [Sample](#Sample)

It is possible to execute OpenTelemetry through [Docker Compose](https://docs.docker.com/engine/reference/commandline/compose/).

You may execute the following compose.yaml that has the configured collector connected to the GeneXus application to be deployed.

**compose.yaml:**

```
version: "2"
services:
  # ADOT Collector
  aws-ot-collector:
    image: public.ecr.aws/aws-observability/aws-otel-collector:latest
    environment:
      - AWS_REGION=us-east-1
      - AWS_ACCESS_KEY_ID=XXXXX
      - AWS_SECRET_ACCESS_KEY=XXXXXXXXXX

    ports:
      - "4317:4317"

  smaplegenexusapp:
    build:
      context: .    
    environment:
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://aws-ot-collector:4317
      - OTEL_RESOURCE_ATTRIBUTES=service.namespace=GeneXus,service.name=sample-app,service.version=1.0.1
      - OTEL_METRICS_EXPORTER=otlp    
      - GX_LOG_LEVEL=info
      - GX_LOG_LEVEL_USER=debug
      - GX_LOG_OUTPUT=ConsoleAppender

    ports:
      - "80:80"
```

### 

### [**\*\* IAM minimal Policy: AWSDistroOpenTelemetryPolicy**](#**+IAM+minimal+Policy%3A+AWSDistroOpenTelemetryPolicy)

<https://aws-otel.github.io/docs/setup/permissions>

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:PutLogEvents",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:DescribeLogStreams",
                "logs:DescribeLogGroups",
                "logs:PutRetentionPolicy",
                "xray:PutTraceSegments",
                "xray:PutTelemetryRecords",
                "xray:GetSamplingRules",
                "xray:GetSamplingTargets",
                "xray:GetSamplingStatisticSummaries",
                "ssm:GetParameters"
            ],
            "Resource": "*"
        }
    ]
}
```

### [Scope](#Scope)

**Generator:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [Availability](#Availability)

This functionality is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).

### [See Also](#See+Also)

* [HowTo: Setup the environment to test Observability (using AWS CloudWatch)](https://wiki.genexus.com/commwiki/wiki?57258)
* [Log settings with environment variables](https://wiki.genexus.com/commwiki/wiki?53361)


|  |
| --- |
| **Backlinks** |
| [HowTo: Observability of your GeneXus applications](https://wiki.genexus.com/commwiki/wiki?53767) | [HowTo: Observability of your GeneXus applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55863) | [HowTo: Setup the environment to test Observability (using AWS CloudWatch)](https://wiki.genexus.com/commwiki/wiki?57258) |
| [Toc:Observability](https://wiki.genexus.com/commwiki/wiki?53765) | [Observability in GeneXus Apps](https://wiki.genexus.com/commwiki/wiki?53773) | [Observability in GeneXus Apps (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55862) |

---
