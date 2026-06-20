---
title: "HowTo: Create new Spans manually"
source_id: 57598
source_url: https://wiki.genexus.com/commwiki/wiki?57598
genexus_version: "18"
---

# HowTo: Create new Spans manually

To create a Span, use the [CreateSpan](https://wiki.genexus.com/commwiki/wiki?57593) method of the [Tracer External Object](https://wiki.genexus.com/commwiki/wiki?57593).

The CreateSpan method is overloaded, and the simplest method receives the name of the Span to be created.

```
TestBasic3 procedure:

//Some code here
&span = Tracer.CreateSpan("Calculating Debt")
```

Suppose that you need to create a new span in an object "TestBasic4" (invoked by "TestBasic3"), and want to create a new span inside the invoked object (which should be a sibling of the parent span).

In the [.NET Generator](https://wiki.genexus.com/commwiki/wiki?38604), you just create the span inside the invoked procedure and the span will be automatically created as a sibling Span.

```
TestBasic3 procedure:

//Some code here
&span = Tracer.CreateSpan("Calculating Debt")
//Do more things

TestBasic4.Call()
&span.End()
```

```
TestBasic4 procedure:

&span = Tracer.CreateSpan("Processing User Debt")
// Do something else
&span.End()
```

The following is a view of the spans, using Grafana:

`[imagen omitida: wiki id 57600]`

In the [Java Generator](https://wiki.genexus.com/commwiki/wiki?12258), to get the same result it is necessary to pass to the called program the [TraceContext](https://wiki.genexus.com/commwiki/wiki?57604) obtained while creating the parent span.

The context variable in the example is represented as a TraceContext object.

```
TestBasic3 procedure:

&span = Tracer.CreateSpan("Calculating Debt")
&Context = &span.Context // Get the Trace Context. &Context is of type TraceContext External Object.

//Do more things
TestBasic4.Call(&Context)
&span.End()
```

The TraceContext is going to be used to set the parent of the newly created Span.

```
TestBasic4 procedure:

parm(&Context)

&span = Tracer.CreateSpan("Processing User Debt",&Context) //Pass the Context while creating the sibling span.
// Do something else
&span.End()
```

**Note**: Passing the context is compatible with both generators, Java and .NET.


|  |
| --- |
| **Backlinks** |
| [Table of contents:Observability](https://wiki.genexus.com/commwiki/wiki?53765) | [Span External Object](https://wiki.genexus.com/commwiki/wiki?57597) | [TraceContext External Object](https://wiki.genexus.com/commwiki/wiki?57604) |
| [Tracer External Object](https://wiki.genexus.com/commwiki/wiki?57593) |

---
