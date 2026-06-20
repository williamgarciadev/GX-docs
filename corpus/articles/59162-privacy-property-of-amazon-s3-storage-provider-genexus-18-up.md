---
title: "Privacy property of Amazon S3 Storage Provider (GeneXus 18 Upgrade 10 or prior)"
source_id: 59162
source_url: https://wiki.genexus.com/commwiki/wiki?59162
genexus_version: "18"
---

# Privacy property of Amazon S3 Storage Provider (GeneXus 18 Upgrade 10 or prior)

Specifies whether stored multimedia resources are Public or Private; that is, if they can be accessed publicly (by everyone) or privately.
If Private, a Signed URL will be automatically generated.

### [Values](#Values)

|  |  |
| --- | --- |
| **Public Read** | Multimedia files can be accessed by a public URL. Anyone with the link can access them. Default value. |
| **Private** | Multimedia files can only be accessed using a signed URL that expires after some time. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

The Privacy property enables you to specify whether multimedia files can be accessed through a public or a restricted link.

GeneXus will save resources into the Storage provider with the following security configuration:

* Attributes
  + Multimedia
    - Image: Privacy Value\*
    - Audio: Privacy Value\*
    - Video: Privacy Value\*
    - BlobFile: Privacy Value\*
  + Blob: Always private
* Temporary files:
  + Web Uploads: Always private
  + SmartDevice Upload: Always private
  + File Upload Control: Always private

Thus, the Privacy property enables the Developer to specify the security configuration for certain resources, such as Multimedia files.

Privacy can be:

* **Public**:
  + All multimedia resources can be accessed by anyone with the link.
* **Private**:
  + All multimedia resources can only be accessed with a signed URL link. These links expire after the time set in the Expiration Property has elapsed.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48247,,).

### [See Also](#See+Also)

[URL Expiration property (Storage Provider)](https://wiki.genexus.com/commwiki/wiki?48408)


|  |
| --- |
| **Backlinks** |
| [Storage Provider property (GeneXus 18 Upgrade 10 or prior)](https://wiki.genexus.com/commwiki/wiki?59174) | [Storage Provider property (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57448) |

---
