---
title: "Target release property"
source_id: 14017
source_url: https://wiki.genexus.com/commwiki/wiki?14017
genexus_version: "18"
---

# Target release property

Establishes the operating system (OS) release on which the generated objects will be used.

### [Values](#Values)

|  |  |
| --- | --- |
| **Current** | Indicates that the OS version used to compile the programs will be used to execute them. This is the default value. |
| **Previous** | Depends on the current OS version used to compile. The generated objects will be used on the OS release previous to the one used to compile. |
| **Version 2 Release 2 M0** |
| **Version 2 Release 3 M0** |
| **Version 3 Release 0 M5** |
| **Version 3 Release 1 M0** |
| **Version 3 Release 2 M0** |
| **Version 3 Release 4 M0** |
| **Version 3 Release 6 M0** |
| **Version 3 Release 7 M0** |
| **Version 4 Release 1 M0** |
| **Version 4 Release 2 M0** |
| **Version 4 Release 3 M0** |
| **Version 4 Release 4 M0** |
| **Version 4 Release 5 M0** |
| **Version 5 Release 1 M0** |
| **Version 5 Release 2 M0** |
| **Version 5 Release 3 M0** |
| **Version 5 Release 4 M0** |
| **Version 6 Release 1 M0** |
| **Version 7 Release 1 M0** |

### [Scope](#Scope)

**Generators:** Cobol, RPG  
**Level:** Generator

### [Description](#Description)

The rest of the possible values (except for Current and Previous) correspond to the OS supported and existing versions. As long as IBM releases new versions, compiling the programs with observability is recommended.  
More information in [SAC 49181 - IBM and new releases of iSeries OS](https://www.genexus.com/developers/websac?,,,49181)

Notes:

* This property value will NOT change in any way the generated code (as the property OS for iSeries version does).
* Each OS version supports a specific group of values for previous versions. It may occur, for example, that if the OS version used to compile is V3R7M0, it is not possible to set this property with value V2R2M0 because it is no longer supported. This problem will occur during compilation, stating that the TGTRLS is not valid.
* If this property value is changed, all programs must be force-generated. In addition, creating the database again is recommended so that the modification is applied over the programs that load and update redundancies as well as the Save File creation.
* Values V5R1, V6R1 and V7R1 are available since GeneXus X Evolution 2 Upgrade 2.
* This property affects the TGTRLS parameter of the compilation command for each object.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691). |
