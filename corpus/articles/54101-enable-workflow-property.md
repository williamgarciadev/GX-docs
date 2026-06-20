---
title: "Enable Workflow property"
source_id: 54101
source_url: https://wiki.genexus.com/commwiki/wiki?54101
genexus_version: "18"
---

# Enable Workflow property

Imports a Workflow to your KB. In addition, you can choose to install the GXflow client, which allows you to run business processes with the Inbox out of the box.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Level:** [Version](https://wiki.genexus.com/commwiki/wiki?7860)

### [Description](#Description)

The default value of this property is False.

When setting this property to True:

The Workflow API will be imported, and the Workflow engine tables will be created.  
Additionally, you can choose to install the [GXflow Client](https://wiki.genexus.com/commwiki/wiki?17835), which allows you to run a diagram.

When converting a KB from a previous version, if this KB has a BPM diagram or the Workflow API, the property will automatically be set to True and the client will be installed.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853).

### [See Also](#See+Also)

[HowTo: Enable Workflow](https://wiki.genexus.com/commwiki/wiki?54173,,)
