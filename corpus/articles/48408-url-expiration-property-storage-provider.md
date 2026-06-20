---
title: "URL Expiration property (Storage Provider)"
source_id: 48408
source_url: https://wiki.genexus.com/commwiki/wiki?48408
genexus_version: "18"
---

# URL Expiration property (Storage Provider)

Expiration value (in minutes) after which a signed (private) URL will become invalid; it defaults to 24 hours.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

When storing private objects inside the Storage Provider, those objects cannot be accessed using a public URL.

Instead, a signed URL is mandatory in order to access the Resource via HTTP.

The URL Expiration property lets you specify how long a signed URL will be valid. After that time has elapsed, the URL will return an Access Denied error when trying to access the resource.

The value is specified in minutes.

Default Value = 1440 minutes

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48247,,).

### [See Also](#See+Also)

[Privacy property](https://wiki.genexus.com/commwiki/wiki?59172)  
[Privacy property (Object Ownership)](https://wiki.genexus.com/commwiki/wiki?59170)


|  |
| --- |
| **Backlinks** |
| [Privacy property (Object Ownership)](https://wiki.genexus.com/commwiki/wiki?59170) | [Privacy property of Amazon S3 Storage Provider (GeneXus 18 Upgrade 10 or prior)](https://wiki.genexus.com/commwiki/wiki?59162) | [Privacy property of Amazon S3 V1 Storage Provider](https://wiki.genexus.com/commwiki/wiki?48407) |
| [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) | [Storage Provider property (GeneXus 18 Upgrade 10 or prior)](https://wiki.genexus.com/commwiki/wiki?59174) | [Storage Provider property (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57448) |

---
