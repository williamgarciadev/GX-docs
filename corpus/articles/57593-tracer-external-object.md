---
title: "Tracer External Object"
source_id: 57593
source_url: https://wiki.genexus.com/commwiki/wiki?57593
genexus_version: "18"
---

# Tracer External Object

Creates [span](https://opentelemetry.io/docs/concepts/signals/traces/#spans) instances, which represent a single operation within a trace.

`[imagen omitida: wiki id 58682]`

You can find the Tracer [External Object](https://wiki.genexus.com/commwiki/wiki?5669) in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) within the [GeneXusObservability module](https://wiki.genexus.com/commwiki/wiki?58681), which in turn is located within the GeneXus module.

## [Methods](#Methods)

All the methods of this External Object are static.

### [CurrentSpan](#CurrentSpan)

Gets the current span.

|  |  |
| --- | --- |
| **Return value** | [GeneXusObservability.Span](https://wiki.genexus.com/commwiki/wiki?57597) |
| **Parameters** | None |

### [CreateSpan](#CreateSpan)

Creates and starts a new span, using the specified name.

|  |  |
| --- | --- |
| **Return value** | GeneXusObservability.Span |
|
| **Parameters** | name:[VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) |

### [CreateSpan](#CreateSpan)

Creates and starts a new span, using the specified name and kind.

|  |  |
| --- | --- |
| **Return value** | GeneXusObservability.Span |
| **Parameters** | name:VarChar data type, kind:[SpanKind](https://wiki.genexus.com/commwiki/wiki?57601) |

### [CreateSpan](#CreateSpan)

Creates and starts a new span, using the specified name, kind, and context. The context is used to set the parent of the newly created Span.

|  |  |
| --- | --- |
| **Return value** | GeneXusObservability.Span |
| **Parameters** | name:VarChar data type, context:[TraceContext](https://wiki.genexus.com/commwiki/wiki?57604), kind:SpanKind |

## [Considerations](#Considerations)

### [Tracer Initialization](#Tracer+Initialization)

See [GeneXusObservability.Tracer: Instrumentation scope](https://wiki.genexus.com/commwiki/wiki?57617)

### [Spans creation](#Spans+creation+)

#### [**.NET**](#.NET)

The creation of the new span does the following:

* Sets [Parent](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.activity.parent?view=net-8.0#system-diagnostics-activity-parent) to hold [Current](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.activity.current?view=net-8.0#system-diagnostics-activity-current).
* Sets [Current](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.activity.current?view=net-8.0#system-diagnostics-activity-current) to this [Span](http://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.activity?view=net-8.0).
* If StartTime is not passed, it defaults to [DateTime.UtcNow](https://learn.microsoft.com/en-us/dotnet/api/system.datetime.utcnow?view=net-8.0#system-datetime-utcnow).
* Generates a unique [Id](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.activity.id?view=net-8.0#system-diagnostics-activity-id) for this span.

#### [**JAVA**](#JAVA)

The new span is not associated automatically with the current context. The Context has to be passed as explained in [HowTo: Create new Spans manually](https://wiki.genexus.com/commwiki/wiki?57598)

## [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

## [Availability](#Availability)

Since [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243).


|  |
| --- |
| **Backlinks** |
| [GeneXusObservability module](https://wiki.genexus.com/commwiki/wiki?58681) | [GeneXusObservability.Tracer: Instrumentation scope](https://wiki.genexus.com/commwiki/wiki?57617) | [HowTo: Add items to the Baggage](https://wiki.genexus.com/commwiki/wiki?57605) |
| [HowTo: Create new Spans manually](https://wiki.genexus.com/commwiki/wiki?57598) | [HowTo: Set an exception event in a Span](https://wiki.genexus.com/commwiki/wiki?57609) | [HowTo: Set attributes to Spans](https://wiki.genexus.com/commwiki/wiki?57607) | [Table of contents:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |

---
