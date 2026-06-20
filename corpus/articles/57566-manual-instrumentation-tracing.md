---
title: "Manual Instrumentation: Tracing"
source_id: 57566
source_url: https://wiki.genexus.com/commwiki/wiki?57566
genexus_version: "18"
---

# Manual Instrumentation: Tracing

Instrumentation is the act of adding observability code to an app.

The objects that compose the [GeneXusObservability module](https://wiki.genexus.com/commwiki/wiki?58681) allow adding distributed [tracing](https://opentelemetry.io/docs/concepts/signals/traces/) instrumentation manually. That is, add new custom distributed tracing instrumentation besides the one already included in GeneXus applications when Opentelemetry is activated. For more information, see [HowTo: Observability of your GeneXus applications](https://wiki.genexus.com/commwiki/wiki?53767).

Manually instrumenting your applications with OpenTelemetry gives you greater control over what to track and monitor. Nevertheless, note that adding custom Spans to Traces involves an advanced tool, and in many cases the basic instrumentation would be enough, without the need to add additional spans.

**Note**: It is recommended to use [automatic instrumentation](https://opentelemetry.io/docs/languages/java/automatic/) to get started and then enrich your code with manual instrumentation as needed.  
If you cannot modify the source code of your app, you can skip manual instrumentation and only use automatic instrumentation.

OpenTelemetry is a powerful tool, and proper instrumentation requires careful consideration of what metrics, traces, and logs are essential for your specific use case.

## [Scenarios of use](#Scenarios+of+use)

Manual instrumentation can be used to instrument any part of the application code.  
Some of the scenarios where you could use this functionality are the following:

* Detect the cause of slowness or malfunction in a program.
* Mark a section of the program that is working slowly or poorly; for example, the login. In this case, Opentelemetry will give information about what is happening, and how long the request takes. You can even add information such as the User Id as an Attribute within the OpenTelemetry SPAN.
* Throw a recordException given any exception in the scope of the span.

## [Availability](#Availability)

Since [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243) | [Table of contents:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |

---
