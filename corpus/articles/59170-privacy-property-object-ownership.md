---
title: "Privacy property (Object Ownership)"
source_id: 59170
source_url: https://wiki.genexus.com/commwiki/wiki?59170
genexus_version: "18"
---

# Privacy property (Object Ownership)

Specifies whether stored multimedia resources are Public or Private; that is, whether they can be accessed by everyone or restricted. If Private, a Signed URL will be automatically generated.

### [Values](#Values)

|  |  |
| --- | --- |
| **Private, bucket owner enforced (ACL disabled - Recommended)** | Multimedia files are private and can only be accessed by the bucket owner. Access control lists (ACLs) are disabled, ensuring all content remains fully private within the bucket. |
| **Public, bucket owner enforced (ACL disabled - Recommended)** | Multimedia files are publicly accessible, allowing anyone with the link to access them. Access control lists (ACLs) are disabled, making the entire bucket uniformly public without individual permissions. |
| **Public Read (ACL Enabled)** | Multimedia files can be accessed by a public URL. Anyone with the link can access them. Default value. |
| **Private (ACL Enabled)** | Multimedia files can only be accessed using a signed URL that expires after some time. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

The Privacy property enables you to specify whether multimedia files can be accessed through a public or a restricted link.

The property becomes available by setting the ****Amazon S3**** value in the [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121)****.****

When using ****Amazon S3**** you can opt out of ACLs, which means that a bucket must be either fully private or fully public.

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

Thus, the Privacy property enables you to specify the security configuration for certain resources, such as Multimedia files.

Privacy can be:

* **Public**: All multimedia resources can be accessed by anyone with the link.
* **Private**: All multimedia resources can only be accessed with a signed URL link. These links expire after the time set in the Expiration Property has elapsed.

This can be configured in two ways:

* **Private (with ACLs enabled)**: Each file in the bucket can have specific permissions, allowing controlled access at the file level. This means that some files can have permissions for specific users while others are kept private.
* **Private - Bucket owner enforced (no ACLs, recommended)**: The entire bucket is private, and only the bucket owner has access to the files. It is not possible to set specific permissions for individual files. This simplifies security management and ensures that all files in the bucket share the same level of privacy, eliminating the risk of inconsistent permission settings.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[URL Expiration property (Storage Provider)](https://wiki.genexus.com/commwiki/wiki?48408)  
[Privacy property of Amazon S3 V1 Storage Provider](https://wiki.genexus.com/commwiki/wiki?48407)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 upgrade 11](https://wiki.genexus.com/commwiki/wiki?54245) | [Privacy property](https://wiki.genexus.com/commwiki/wiki?59172) |
| [Privacy property of Amazon S3 Storage Provider (GeneXus 18 Upgrade 10 or prior)](https://wiki.genexus.com/commwiki/wiki?59162) | [Privacy property of Amazon S3 V1 Storage Provider](https://wiki.genexus.com/commwiki/wiki?48407) | [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) | [URL Expiration property (Storage Provider)](https://wiki.genexus.com/commwiki/wiki?48408) |

---
