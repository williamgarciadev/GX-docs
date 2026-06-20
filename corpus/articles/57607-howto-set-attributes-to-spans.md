---
title: "HowTo: Set attributes to Spans"
source_id: 57607
source_url: https://wiki.genexus.com/commwiki/wiki?57607
genexus_version: "18"
---

# HowTo: Set attributes to Spans

[Attributes](https://opentelemetry.io/docs/languages/go/instrumentation/#span-attributes) are keys and values that are applied as metadata to your [spans](https://opentelemetry.io/docs/concepts/observability-primer/#spans) and are useful for aggregating, filtering, and grouping traces.

The following example uses the [CreateSpan](https://wiki.genexus.com/commwiki/wiki?57593) method of the [Tracer](https://wiki.genexus.com/commwiki/wiki?57593) Object to create a Span.  
Then, different attributes are set to the span using the methods for that purpose.

```
&span = Tracer.CreateSpan("TestSetAtts procedure")

&span.SetBooleanAttribute("MyBooleanAtt",true)
&span.SetDoubleAttribute("MyDoubleAtt",1256.69)
&span.SetLongAttribute("MyLongAtt",8965)
&span.SetStringAttribute("MyStringAtt","This is the Value of Attribute")

&span.End()
```

The following is a view of Grafana showing the created span and its attributes.

`[imagen omitida: wiki id 57608]`


|  |
| --- |
| **Backlinks** |
| [Toc:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |

---
