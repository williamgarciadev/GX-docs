---
title: "Dynamic Pattern Update Property"
source_id: 11605
source_url: https://wiki.genexus.com/commwiki/wiki?11605
genexus_version: "18"
---

# Dynamic Pattern Update Property

Allows for high performance when working in large Knowledge Bases with many Pattern instances.

### [Values](#Values)

**Yes:** Patterns are updated automatically.

**No:** Patterns are never applied automatically, not even when an object is opened. The disabled Pattern is applied automatically over the instances modified in the Build process.

The user can manually apply it by means of "Apply Pattern" option over the instance. Besides, when it has selected the "Apply this pattern on save" option in the Transaction, and the user modifies something that need to be impacted on the generated objects, then the instance will be automatically updated and reapplied.

**Default =** Yes

### [Description](#Description)

The development cycle is not viable with large Knowledge Bases and multiple Pattern instances due to the high cost involved in maintaining the instances updated.

When the value of the property is set to No, then:

* The Pattern is never applied automatically, not even when an object is opened. The purpose of this is to avoid confusions (because you can see what is being executed) and to know that it needs to be applied manually.
* The disabled Pattern is applied automatically over the instances modified in the Build process. The purpose of this is to have less keys in the development cycle. If an instance is modified and Run, Build, etc. is triggered, there’s a 99% chance that the aim is to see this instance updated.
* The change in Pattern Settings does not update instances automatically.
* The change in Pattern version does not update instances automatically.
* The change in template does not update instances automatically.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

Build All.

### [Scope](#Scope)

**Objects:** [Work With Pattern](https://wiki.genexus.com/commwiki/wiki?5636), [Category Pattern](https://wiki.genexus.com/commwiki/wiki?5752,,)

####


|  |
| --- |
| **Backlinks** |
| [Applying Patterns](https://wiki.genexus.com/commwiki/wiki?6551) |

---
