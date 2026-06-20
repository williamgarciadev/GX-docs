---
title: "Buffer Response property"
source_id: 55195
source_url: https://wiki.genexus.com/commwiki/wiki?55195
genexus_version: "18"
---

# Buffer Response property

Avoids buffering the response so that the client server can act on partial responses as quickly as possible.

### [Values](#Values)

|  |  |
| --- | --- |
| **Disabled** | Avoids buffering. The response is gradually sent in chunks to the client server as they become available. |
| **Platform Default** | Default value. The response is buffered or not depending on the target platform. |

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)

### [Description](#Description)

The underlying platforms typically manage buffers. In general, they are the best to do so. For example, the .NET platform does not buffer, while the .NET Framework and Java platforms buffer by default.

In certain scenarios, however, you may need to force quick partial responses so that the client can act on them. For example, when you write text on the server to the output and want to allow the client to show it and give feedback to the end user while you are still processing and writing more text to the output.

In those scenarios, and in the case that it is not already the default behavior of the platform, you can disable buffering with this property.

To send fragments, called chunks, you can use the [HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934) with the [AddString(string) method](https://wiki.genexus.com/commwiki/wiki?7063). This way, the response is sent gradually as you add these chunks. That is, you can be sure that after each &httpresponse.AddString() the buffer is flushed.

Note that when buffering is disabled, once you write a string to the response (&httpresponse.AddString()), any sent header (&httpresponse.AddHeader()) afterward will be ignored.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241).

### [See Also](#See+Also)

[Reading and writing chunked responses](https://wiki.genexus.com/commwiki/wiki?55630)


|  |
| --- |
| **Backlinks** |
| [Reading and writing chunked responses](https://wiki.genexus.com/commwiki/wiki?55630) |

---
