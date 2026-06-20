---
title: "Storage Endpoint property (Amazon S3)"
source_id: 57446
source_url: https://wiki.genexus.com/commwiki/wiki?57446
genexus_version: "18"
---

# Storage Endpoint property (Amazon S3)

Sets the entry point to the storage service to which all requests are directed.

### [Values](#Values)

|  |  |
| --- | --- |
| **Standard** | Default endpoint |
| **Accelerated** | Endpoint to be used on an bucket with transfer acceleration enabled |
| **Dual-stack accelerated** | Endpoint to be used on an bucket with transfer acceleration enabled over IPv6 |
| **Custom Endpoint** | For using an AWS S3 compatible service |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

This property is available depending on the Storage Provider for Multimedia files used (specified in the [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121)).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,).


|  |
| --- |
| **Backlinks** |
| [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) |

---
