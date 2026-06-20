---
title: "Storage Custom Endpoint property (Storage Provider)"
source_id: 48409
source_url: https://wiki.genexus.com/commwiki/wiki?48409
genexus_version: "18"
---

# Storage Custom Endpoint property (Storage Provider)

Provides a custom entry point for working with services compatible with AWS S3 SDK.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

You must set a value for this property only if the [Storage Endpoint property](https://wiki.genexus.com/commwiki/wiki?45736) = Custom Endpoint.

This property enables the use of any custom endpoint URL and is useful for using the AWS S3 SDK with any S3-compatible service, such as IBM COS, Oracle, MinIO, etc.

**Examples of Endpoints**

* Oracle
  + https://{mynamespace}.compat.objectstorage.{REGION}.oraclecloud.com
* IBM COS
  + https://s3.{REGION}.cloud-object-storage.appdomain.cloud/
* MinIO
  + https://{Server}:Port
    - Example: https://172.17.0.2:9000

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,).

### [See Also](#See+Also)

[Storage Endpoint property](https://wiki.genexus.com/commwiki/wiki?45736)


|  |
| --- |
| **Backlinks** |
| [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) | [Storage Provider property (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57448) |

---
