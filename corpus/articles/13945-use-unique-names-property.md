---
title: "Use unique names property"
source_id: 13945
source_url: https://wiki.genexus.com/commwiki/wiki?13945
genexus_version: "18"
---

# Use unique names property

Defines whether you want to automatically generate a log file or use a fixed name.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Description](#Description)

When unique names are not used; the [JDBC Log File property](https://wiki.genexus.com/commwiki/wiki?13946,,) property is enabled to set the log file full path. In this case, the log is always generated using the same filename. This is the default value.

When unique names are used; the [Path For Log Files property](https://wiki.genexus.com/commwiki/wiki?13949,,) is enabled to set the path name where the log files will be generated. The filename format is automatically generated using the following pattern:

"gx\_" + MMDD + "\_" + HHMMSS + <namespace> + "\_" + <datastore> + "\_" + <connection> + ".log"

### [Scope](#Scope)

**Platforms:** Web(Java)

### [See Also](#See+Also)

* [Path For Log Files property](https://wiki.genexus.com/commwiki/wiki?13949,,)
* [Enable buffering property](https://wiki.genexus.com/commwiki/wiki?13947)
* [JDBC Log File property](https://wiki.genexus.com/commwiki/wiki?13946,,)
* [Detail property](https://wiki.genexus.com/commwiki/wiki?13948)


|  |
| --- |
| **Backlinks** |
| [Detail property](https://wiki.genexus.com/commwiki/wiki?13948) | [Enable buffering property](https://wiki.genexus.com/commwiki/wiki?13947) | [HowTo: Enable Log for GXflow runtime](https://wiki.genexus.com/commwiki/wiki?24568) |
| [Log JDBC Activity property](https://wiki.genexus.com/commwiki/wiki?9135) |

---
