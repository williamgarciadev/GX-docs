---
title: "Observability with Lightstep"
source_id: 53776
source_url: https://wiki.genexus.com/commwiki/wiki?53776
genexus_version: "18"
---

# Observability with Lightstep

GeneXus enables that the telemetry data (traces, logs and metrics) of applications be sent to [Lightstep Observability](https://lightstep.com/).

The steps you must follow are:

1. Accessing Lightstep.
2. Set the [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408).
3. Deploy your application.
4. Configure the Environment Variables.
5. Executing the application’s Docker image.

### [Access Lightstep](#Access+Lightstep)

To start using this platform, the first thing you must do is [create an account](https://app.lightstep.com/signup/developer?signup_source=docs).

Then you must create a [Lightstep access token](https://docs.lightstep.com/docs/create-and-manage-access-tokens#create-an-access-token). Make sure that you save the token generated.

### [Set the Observability Provider property](#Set+the+Observability+Provider+property)

Go to GeneXus and set the [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) to "**OpenTelemetry**" value.

### [Deploy your application](#Deploy+your+application)

Use the deployment engine tool to deploy your app to Docker (builds a Docker image).

### [Configure Environment Variables](#Configure+Environment+Variables)

Configure the following environment variables in the application’s Docker Image:

```
OTEL_EXPORTER_OTLP_TRACES_HEADERS: "lightstep-access-token=<YOUR_ACCESS_TOKEN>"
OTEL_SERVICE_NAME: "<service_name>"
OTEL_EXPORTER_OTLP_PROTOCOL: grpc
OTEL_EXPORTER_OTLP_ENDPOINT: "https://ingest.lightstep.com:443"
OTEL_TRACES_EXPORTER: logging,otlp
OTEL_METRICS_EXPORTER: logging,otlp
```

Where YOUR\_ACCESS\_TOKEN corresponds to the [Lightstep access token](https://docs.lightstep.com/docs/create-and-manage-access-tokens#create-an-access-token) obtained before.

### [Execute Docker image](#Execute+Docker+image)

And to end, execute the application’s Docker image.

When you execute the app and make changes to it, you will be able to, for example, [view the traces](https://docs.lightstep.com/docs/view-traces).

### [Scope](#Scope)

**Generator:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Availability](#Availability)

This functionality is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).


|  |
| --- |
| **Backlinks** |
| [HowTo: Observability of your GeneXus applications](https://wiki.genexus.com/commwiki/wiki?53767) | [HowTo: Observability of your GeneXus applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55863) | [Toc:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |
| [Observability in GeneXus Apps (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55862) |

---
