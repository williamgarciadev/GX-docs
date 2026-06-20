---
title: "Download content in Offline applications property"
source_id: 40907
source_url: https://wiki.genexus.com/commwiki/wiki?40907
genexus_version: "18"
---

# Download content in Offline applications property

Indicates if the content of a multimedia or Blob attribute will be downloaded to the device when synchronizing an Offline Database.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240)

### [Description](#Description)

When multimedia or Blob attributes exist in an Offline Database, there are two options regarding the storage of their content:

1. Save the content in the device.
2. Save a reference (link) to the content in an external source.

If the property is set to False (default value), only an external reference to the attribute content is stored in the database. This reference is an URL to the external resource (i.e. *http**://<url>*) or a local reference (i.e. *file://<local path>*) when working with media inserted from the device itself (after synchronizing, this local reference will be changed for an external one).

If the property is set to True, a copy of the attribute content is downloaded and saved in a local directory associated with the Offline Database and a local reference stored in the database table.

Note:

* The property is available for iOS since GeneXus 16 Upgrade #1
* The property is available for Android since GeneXus 16 Upgrade #5

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [Compatibility](#Compatibility)

In previous versions, all multimedia and blob content not inserted as an external reference was downloaded to the device.

### [See Also](#See+Also)

[Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?20286)  
[External Storage for Multimedia](https://wiki.genexus.com/commwiki/wiki?31120)


|  |
| --- |
| **Backlinks** |
| [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |

---
