---
title: "Generate developer menu makefile property"
source_id: 8940
source_url: https://wiki.genexus.com/commwiki/wiki?8940
genexus_version: "18"
---

# Generate developer menu makefile property

Allows indicating whether you want to generate the .rsp for the Developer menu program.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | Does not generate the .rsp for the Developer menu program. |
| **Yes** | Generates the .rsp for the Developer menu program. This is the default value. |

### [Description](#Description)

#### [Notes](#Notes)

* When working with a big Knowledge Base the Developer menu’s .rps file may become too large, slowing generation time. So, if the Developer Menu is not frequently used, setting this property to NO saves considerable time during generation.
* These files are created during generation and store information about the main programs' call tree which is used later at compilation time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Re-Build All.

### [Scope](#Scope)

**Platforms:** Web(.Net)


|  |
| --- |
| **Backlinks** |
| [Build All/Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691) | [Developer Menu](https://wiki.genexus.com/commwiki/wiki?18484) |

---
