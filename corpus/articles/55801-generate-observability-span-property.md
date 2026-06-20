---
title: "Generate Observability span property"
source_id: 55801
source_url: https://wiki.genexus.com/commwiki/wiki?55801
genexus_version: "18"
---

# Generate Observability span property

Generates a span for the telemetry traces of Procedures, Data Providers, and Business Components.

### [Values](#Values)

|  |  |
| --- | --- |
| **Yes** | Allows the generation of spans in OpenTelemetry traces. |
| **No** | Default value. |

### [Scope](#Scope)

**Objects:** [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [Description](#Description)

The Generate Observability Span property becomes available once the [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) is set to a value other than "None".

By setting the property to "Yes", you enable the generation of [spans](https://opentelemetry.io/docs/concepts/signals/traces/#spans) in OpenTelemetry traces for the main methods of [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270) operations, and [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) methods.

The property has to be enabled at object level. By default, it is disabled for all objects.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at runtime.

### [Samples](#Samples)

#### [Sample #1](#Sample+%231)

Suppose you have defined a Procedure called procedurebc that uses a Business Component to get and update some data.

When you run procedurebc, you will be able to view the Traces. For this you can use AWS X-Ray, for example, which displays the information as shown in the following image, where the spans are highlighted with a red box:

`[imagen omitida: wiki id 56201]`

However, you can use any tool to display the traces, depending on your configuration and your [Observability Provider](https://wiki.genexus.com/commwiki/wiki?53408).

#### [Sample #2](#Sample+%232)

With .NET Generator, the name of the span is the fully qualified name of the object (followed by the method).

For Business Components, the name is Sdt<Transaction Name> followed by the operation (insert, update, delete, etc.).

Below is an Azure Monitor screen of the application generated using .NET.

`[imagen omitida: wiki id 56219]`

In the image above, the spans are the ones highlighted with a red box.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240) | [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241) | [Toc:Observability](https://wiki.genexus.com/commwiki/wiki?53765) |
| [Observability Provider property](https://wiki.genexus.com/commwiki/wiki?53408) |

---
