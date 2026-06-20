---
title: "Should Await For Completion property (GeneXus 18 Upgrade 7)"
source_id: 57562
source_url: https://wiki.genexus.com/commwiki/wiki?57562
genexus_version: "18"
---

# Should Await For Completion property (GeneXus 18 Upgrade 7)

Determines whether to wait for the outcome of the operation returned by the external function or method before proceeding with the rest of the code.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [External Object](https://wiki.genexus.com/commwiki/wiki?5669)  
**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

A method of an [External Object with Type property 'Native Object'](https://wiki.genexus.com/commwiki/wiki?6148) may return results asynchronously. To control this behavior, the **Should Await For Completion property** can be set to:

* **True:**To wait for the completion of the operation before proceeding with the code execution.
* **False:**To continue executing the code without waiting for the operation to complete. This is the default value.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

No action is required to apply the corresponding changes when the property value is configured.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241).
