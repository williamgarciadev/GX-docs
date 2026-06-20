---
title: "Span External Object"
source_id: 57597
source_url: https://wiki.genexus.com/commwiki/wiki?57597
genexus_version: "18"
---

# Span External Object

Manages Observability [spans](https://opentelemetry.io/docs/concepts/observability-primer/#spans).

`[imagen omitida: wiki id 58684]`You can find the Span [External Object](https://wiki.genexus.com/commwiki/wiki?5669) in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) within the [GeneXusObservability module](https://wiki.genexus.com/commwiki/wiki?58681), which in turn is located within the GeneXus module.

## [Properties](#Properties)

### [SpanId](#SpanId)

Gets the Span ID.

### [TraceId](#TraceId)

Gets the [Trace](https://opentelemetry.io/docs/concepts/observability-primer/#distributed-traces) ID.

### [SpanContext](#SpanContext)

Returns the [SpanContext](https://wiki.genexus.com/commwiki/wiki?57603) associated with this Span.

### [IsRecording](#IsRecording)

A Span is recording when the data provided to it via functions like SetAttributes and SetStatus is captured in some way. This flag SHOULD be used to avoid expensive computations of Span attributes or events when a Span is not recorded.

### [Context](#Context)

A [TraceContext](https://wiki.genexus.com/commwiki/wiki?57604) is a propagation mechanism that carries execution-scoped values across API boundaries and between logically associated [execution units](https://opentelemetry.io/docs/specs/otel/glossary/#execution-unit).

## [Methods](#Methods)

### [End](#End)

Marks the end of Span execution. It's important to end the span execution to avoid unpredictable behavior or memory leaks.

| **Return value** | None |
| --- | --- |
| **Parameters** | None |

### [RecordException](#RecordException)

Adds an event containing the information from the specified exception.

| **Return value** | None |
| --- | --- |
| **Parameters** | message:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778) |

### [SetStringAttribute](#SetStringAttribute)

Adds or updates the span [attribute](https://opentelemetry.io/docs/languages/go/instrumentation/#span-attributes) with the given key and value.

| **Return value** | None |
| --- | --- |
| **Parameters** | property:VarChar, value:VarChar |

### [SetLongAttribute](#SetLongAttribute)

Adds or updates the span attribute with the given key and value.

| **Return value** | None |
| --- | --- |
| **Parameters** | property:VarChar, value:[Numeric](https://wiki.genexus.com/commwiki/wiki?6793) |

### [SetDoubleAttribute](#SetDoubleAttribute)

Adds or updates the span attribute with the given key and value.

| **Return value** | None |
| --- | --- |
| **Parameters** | property:VarChar, value:Numeric |

### [SetBooleanAttribute](#SetBooleanAttribute)

Adds or updates the span attribute with the given key and value.

| **Return value** | None |
| --- | --- |
| **Parameters** | name:VarChar, value:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |

### [AddBaggage](#AddBaggage)

Sets the [Baggage](https://opentelemetry.io/docs/concepts/signals/baggage/) with a new key/value pair.

|  |  |
| --- | --- |
| **Return value** | [GeneXusObservability.TraceContext](https://wiki.genexus.com/commwiki/wiki?57604) |
| **Parameters** | property:VarChar, value:VarChar |

Returns TraceContext associated with that Baggage.

### [GetBaggageItem](#GetBaggageItem)

Returns the value of a key-value pair added to the span with AddBaggage.

|  |  |
| --- | --- |
| **Return value** | VarChar |
| **Parameters** | property:VarChar, context:[GeneXusObservability.TraceContext](https://wiki.genexus.com/commwiki/wiki?57604) |

### [SetStatus](#SetStatus)

Sets the status code and description on the span.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | statusCode:[SpanStatusCode](https://wiki.genexus.com/commwiki/wiki?57612), message:VarChar |

### [SetStatus](#SetStatus)

Sets the status code on the span.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | statusCode:[SpanStatusCode](https://wiki.genexus.com/commwiki/wiki?57612) |

## [Samples](#Samples)

* [HowTo: Create new Spans manually](https://wiki.genexus.com/commwiki/wiki?57598)
* [HowTo: Add items to the Baggage](https://wiki.genexus.com/commwiki/wiki?57605)

## [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

## [Availability](#Availability)

Since [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243).


|  |
| --- |
| **Backlinks** |
| [GeneXusObservability module](https://wiki.genexus.com/commwiki/wiki?58681) | [HowTo: Add items to the Baggage](https://wiki.genexus.com/commwiki/wiki?57605) | [HowTo: Set an exception event in a Span](https://wiki.genexus.com/commwiki/wiki?57609) |
| [Table of contents:Observability](https://wiki.genexus.com/commwiki/wiki?53765) | [Tracer External Object](https://wiki.genexus.com/commwiki/wiki?57593) |

---
