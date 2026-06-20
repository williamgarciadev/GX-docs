---
title: "OpenTelemetry"
source_id: 53777
source_url: https://wiki.genexus.com/commwiki/wiki?53777
genexus_version: "18"
---

# OpenTelemetry

[OpenTelemetry](https://opentelemetry.io) (OTEL) is an open source [observability](https://opentelemetry.io/docs/concepts/observability-primer/#what-is-observability) framework that offers a group of technologies for instrumenting, generating, compiling and exporting telemetry data ([traces](http://opentelemetry.io/docs/concepts/signals/traces/), [metrics](https://opentelemetry.io/docs/concepts/signals/metrics/) and [logs](https://opentelemetry.io/docs/concepts/signals/logs/)).

`[imagen omitida: wiki id 56791]`

## [Traces](#Traces)

Traces give you the big picture of what happens when a request is made to an application. Whether your application is a monolith with a single database or a sophisticated mesh of services, traces are essential to understanding the full “path” a request takes in your application (taken from [here](https://opentelemetry.io/docs/concepts/signals/traces/)).  
  
A trace represents the entire execution path of the request, and each [span](http://opentelemetry.io/docs/concepts/signals/traces/#spans) in the trace represents a single unit of work during that journey, such as an API call or database query.  
Whenever the request enters a service, a top-level child span is created. If the request made multiple commands or queries within the same service, the top-level child span may act as a parent to additional child spans nested beneath it.

### [Distributed Tracing](#Distributed+Tracing)

[Distributed tracing](https://opentelemetry.io/docs/concepts/observability-primer/#distributed-traces) is a method of tracking application requests as they flow from frontend devices to backend services and database.  
[Context Propagation](https://opentelemetry.io/docs/concepts/context-propagation/) is the core concept that enables *Distributed Tracing*. With Context Propagation, Spans can be correlated with each other and assembled into a trace, regardless of where Spans are generated.

## [Metrics](#Metrics)

A [metric](https://opentelemetry.io/docs/concepts/signals/metrics/) is a measurement of a service captured at runtime.

## [Logs](#Logs)

A [log](https://opentelemetry.io/docs/concepts/signals/logs/) is a timestamped text record, either structured (recommended) or unstructured, with metadata.

The purpose of OTEL is to provide a Software Development Kit (SDK), API and standardized tools for consuming, transforming and sending data to an observability backend.  
OpenTelemetry is focused on the generation, collection, management, and export of telemetry.  
A major goal of OpenTelemetry is that you can easily instrument your applications or systems, no matter their language, infrastructure, or runtime environment. The storage and visualization of telemetry is left to other tools (Observability Backends).

## [See also](#See+also)

[Why OpenTelemetry?](https://opentelemetry.io/docs/what-is-opentelemetry/#why-opentelemetry)


|  |
| --- |
| **Backlinks** |
| [Table of contents:Observability](https://wiki.genexus.com/commwiki/wiki?53765) | [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) |

---
