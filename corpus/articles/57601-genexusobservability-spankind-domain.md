---
title: "GeneXusObservability.SpanKind Domain"
source_id: 57601
source_url: https://wiki.genexus.com/commwiki/wiki?57601
genexus_version: "18"
---

# GeneXusObservability.SpanKind Domain

SpanKind is a domain of the [GeneXusObservability module](https://wiki.genexus.com/commwiki/wiki?58681).

It describes the relationship between the Span, its parents, and its children in a Trace. For more information, see [SpanKind](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/trace/api.md#spankind).

|  |  |
| --- | --- |
| **Client** | Indicates that the span describes a request to a remote service. This span is usually the parent of a remote  ``` SERVER ```   span and does not end until the response is received. |
| **Consumer** | Indicates that the span describes a child of an asynchronous  ``` ``` PRODUCER ``` ```   request. |
| **Internal** | Default value. Indicates that the span represents an internal operation within an application, as opposed to an operation with remote parents or children. |
| **Producer** | Indicates that the span describes the initiators of an asynchronous request. This parent span will often end before the corresponding child  ``` CONSUMER ```   span, possibly even before the child span starts. In messaging scenarios with batching, tracing individual messages requires a new  ``` ``` PRODUCER ``` ```   span per message to be created. |
| **Server** | Indicates that the span covers server-side handling of a synchronous RPC or other remote request. This span is often the child of a remote  ``` CLIENT ```   span that was expected to wait for a response. |


|  |
| --- |
| **Backlinks** |
| [Table of contents:Observability](https://wiki.genexus.com/commwiki/wiki?53765) | [Tracer External Object](https://wiki.genexus.com/commwiki/wiki?57593) |

---
