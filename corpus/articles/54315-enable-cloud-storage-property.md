---
title: "Enable Cloud Storage property"
source_id: 54315
source_url: https://wiki.genexus.com/commwiki/wiki?54315
genexus_version: "18"
---

# Enable Cloud Storage property

Defines whether a document accepts cloud-hosted documents.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Document](https://wiki.genexus.com/commwiki/wiki?10344)

### [Description](#Description)

The default value of this property is False.

When this property is set to True:

It will be possible to upload document instances of this document definition to the cloud. In addition to setting this property to True, you need to configure the cloud storage platform at runtime. You can do this on the Client by going to Server Settings > Advanced > Document Management. In addition, if you have already uploaded documents of this definition, you can migrate them to the cloud by executing the apwfmigratedocumentstocloud util.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, select Tools > Workflow > [Deploy business processes](https://wiki.genexus.com/commwiki/wiki?17111).

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853).

### [See Also](#See+Also)

[HowTo: Work with documents in GXflow](https://wiki.genexus.com/commwiki/wiki?11856)


|  |
| --- |
| **Backlinks** |
| [HowTo: Work with documents in GXflow](https://wiki.genexus.com/commwiki/wiki?11856) |

---
