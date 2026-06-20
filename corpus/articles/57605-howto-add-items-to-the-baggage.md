---
title: "HowTo: Add items to the Baggage"
source_id: 57605
source_url: https://wiki.genexus.com/commwiki/wiki?57605
genexus_version: "18"
---

# HowTo: Add items to the Baggage

In OpenTelemetry, [Baggage](https://opentelemetry.io/docs/concepts/signals/baggage/) is contextual information that is passed between spans.  
It’s a key-value store that resides alongside span context in a trace, making values available to any span created within that trace.

As stated in the [Opentelemetry documentation](https://opentelemetry.io/docs/concepts/signals/baggage/#what-should-otel-baggage-be-used-for), common use cases of the Baggage include information that’s only accessible further up a stack, such as account Identification, User IDs, Product IDs, and origin IPs, etc. Passing these down your stack allows you to add them to your Spans in downstream services to make it easier to filter when searching in your Observability backend.

### [Example](#Example)

Use the [CreateSpan](https://wiki.genexus.com/commwiki/wiki?57593) method of [Tracer](https://wiki.genexus.com/commwiki/wiki?57593) to create the parent Span.  
The AddBaggage method should be invoked using the [Span](https://wiki.genexus.com/commwiki/wiki?57597) object previously obtained. It returns a [TraceContext](https://wiki.genexus.com/commwiki/wiki?57604) that should be used to propagate the information.

```
Parent procedure:

&span = Tracer.CreateSpan("TestBaggageParent procedure")
&context =  &span.AddBaggage("PropertyToBaggage","ValueToBaggage") //&Context is of TraceContext External Object
//Do something else
testbaggageChild(&context)
&span.End()
```

```
TestBaggageChild procedure:

parm(&Context)

&span = Tracer.CreateSpan("TestBaggageChild procedure",&context,SpanKind.Client) //Create Span passing &Context
//Do something else
&value = &span.GetBaggageItem("PropertyToBaggage")

&span.End()
```


|  |
| --- |
| **Backlinks** |
| [GeneXusObservability.Span External Object](https://wiki.genexus.com/commwiki/wiki?57597) | [Toc:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |

---
