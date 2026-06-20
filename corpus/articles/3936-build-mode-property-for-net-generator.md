---
title: "Build Mode property for .NET generator"
source_id: 3936
source_url: https://wiki.genexus.com/commwiki/wiki?3936
genexus_version: "18"
---

# Build Mode property for .NET generator

Controls the application build process.
One objective is to simplify the build process to isolate the developer from "what needs to be compiled" to run an application. A second objective is to provide a mechanism to increase development prototyping by compiling on demand.

### [Values](#Values)

|  |  |
| --- | --- |
| **MSBuild** | In MSBuild mode, MSBuild is used to compile instead of the CSC compiler. This is the default value for KBs created from GeneXus 16 Upgrade 10. |
| **Standard** | In Standard Build Mode, given an entry point to compile, its call tree is analyzed (including other called entry points) and compiled. This is the default value for KBs created up to GeneXus 16 Upgrade 9. |
| **Incremental** | In Incremental Build Mode, only a selected entry point is compiled. Programs called by the entry point are compiled as needed (i.e. when they are called). |

### [Scope](#Scope)

**Generators:** .NET  
**Level:** Generator

### [Description](#Description)

#### [Considerations](#Considerations)

* The MSBuild mode has been added in [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,). It is the default one for knowledge bases created with [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,) or higher and it has the best build performance. More information in this article: [Compile using MSBuild instead of CSC](https://wiki.genexus.com/commwiki/wiki?42661).
* Dynamic calls are not supported in Incremental Build Mode. If an object is called via a dynamic call, it is not automatically compiled.
* Applications generated with Incremental Build Mode should **not** be deployed to production or stress test environments.  
  The generated code does not scale well. It is intended for prototyping where there is no contention and the analysis made to check the required compilation is not an issue.
* The server requires special permissions to compile classes before runtime (production environments do not usually have these permissions, unlike development environments).

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [See Also](#See+Also)

[Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719)


|  |
| --- |
| **Backlinks** |
| [Compile using MSBuild instead of CSC](https://wiki.genexus.com/commwiki/wiki?42661) |

---
