---
title: "HowTo: Set an exception event in a Span"
source_id: 57609
source_url: https://wiki.genexus.com/commwiki/wiki?57609
genexus_version: "18"
---

# HowTo: Set an exception event in a Span

There is a basic option to set [Span](https://opentelemetry.io/docs/concepts/observability-primer/#spans) status, and the option to fully record the Exception itself to the Span.

The most basic option is to set Span status to Error to indicate that an Exception has occurred.

In the following example, the [Tracer](https://wiki.genexus.com/commwiki/wiki?57593) Object is used to create the Span.  
Then the SetStatus method of [Span](https://wiki.genexus.com/commwiki/wiki?57597), which is overloaded, is used. One method receives the Error description and the other only receives the [SpanStatusCode](https://wiki.genexus.com/commwiki/wiki?57612).

```
&span = Tracer.CreateSpan("TestStatusCode procedure")
//Do something
if &Error
    &spanStatusCode = SpanStatusCode.Error
    &span.SetStatus(&spanStatusCode,"There was an error executing the program.")
endif
&span.End()
```

The previous example showed the most basic reporting of an Exception by leveraging Span status. This approach does not record the Exception itself to do a richer debugging.   
`Span.RecordException()` allows the exception to be stored in the Span as an Event.

```
&span = Tracer.CreateSpan("TestStatusCode procedure")

//Do something
if &Error

        &spanStatusCode = SpanStatusCode.Error
        &span.SetStatus(&spanStatusCode,"There was an error!!! This is a program message")
        &span.RecordException("Exception Message")
Endif
&span.End()
```

This is a view of Grafana showing the span associated with an Exception.

`[imagen omitida: wiki id 57611]`


|  |
| --- |
| **Backlinks** |
| [GeneXusObservability.SpanStatusCode domain](https://wiki.genexus.com/commwiki/wiki?57612) | [Toc:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |

---
