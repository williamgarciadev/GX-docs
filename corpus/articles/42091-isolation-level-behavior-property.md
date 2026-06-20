---
title: "Isolation Level behavior property"
source_id: 42091
source_url: https://wiki.genexus.com/commwiki/wiki?42091
genexus_version: "18"
---

# Isolation Level behavior property

Defines how the Data Store property value is calculated to preserve the Knowledge Base behavior (the 'Isolation Level' property is now defined in the Data Store instead of the Generator).

### [Values](#Values)

|  |  |
| --- | --- |
| **Inherit from Generator** | Data Store's Isolation Level is initialized with the value from the Generator. |
| **Read Committed** | Data Store's Isolation Level is initialized with the value 'Read Committed'. This is the default value for new KBs. |

### [Description](#Description)

This property exists for compatibility reasons. It is used to preserve the behavior of KBs created before [GeneXus 16 upgrade 2](https://wiki.genexus.com/commwiki/wiki?41525,,), and is only visible in those KBs.  
The default value for KBs created as of [GeneXus 16 upgrade 2](https://wiki.genexus.com/commwiki/wiki?41525,,) is 'Read Committed'.

### [See Also](#See+Also)

* [Isolation level property](https://wiki.genexus.com/commwiki/wiki?8991)
* [SAC 43993](https://www.genexus.com/developers/websac?,,,43993) includes conversion details
