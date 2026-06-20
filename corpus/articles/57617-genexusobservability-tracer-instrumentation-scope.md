---
title: "GeneXusObservability.Tracer: Instrumentation scope"
source_id: 57617
source_url: https://wiki.genexus.com/commwiki/wiki?57617
genexus_version: "18"
---

# GeneXusObservability.Tracer: Instrumentation scope

The [GeneXusObservability.Tracer External Object](https://wiki.genexus.com/commwiki/wiki?57593) uses an *instrumentation scope name* and *instrumentation scope version* to obtain a tracer to instrument the code and collect telemetry information for observability in your program.

*The instrumentation scope name* and *instrumentation scope version*are used to initialize the Tracer when you first call a method (i.e. [CreateSpan](https://wiki.genexus.com/commwiki/wiki?57593)).

The information is passed through environment variables and the logic is as follows:

### [Java Generator](#Java+Generator)

Reads JAVA\_INSTRUMENTATION\_SCOPE\_NAME and JAVA\_INSTRUMENTATION\_SCOPE\_VERSION environment variables.

If any of the above is empty, it does the same as the .NET generator.

### [.NET Generator](#.NET+Generator)

The following is processed to get the *instrumentation-scope-name.*

Reads the **OTEL\_SERVICE\_NAME** environment variable to be used as the *instrumentation-scope-name*.  
If it's empty, it reads the **OTEL\_RESOURCE\_ATTRIBUTES** environment variable to get the service.name key/value pair.   
If it's empty, it uses *instrumentation-scope-name= "GeneXus.Tracing".*

The following is done to get the *instrumentation-scope-version*.

Reads the **OTEL\_SERVICE\_VERSION** environment variable to be used as the *instrumentation-scope-version*.  
If it's empty, it reads the **OTEL\_RESOURCE\_ATTRIBUTES** environment variable to get the service.version key/value pair.   
If it's empty, *instrumentation-scope-version* is left empty.

###


|  |
| --- |
| **Backlinks** |
| [GeneXusObservability.Tracer External Object](https://wiki.genexus.com/commwiki/wiki?57593) |

---
