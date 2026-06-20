---
title: "Gradle Options property for Java Generator"
source_id: 54273
source_url: https://wiki.genexus.com/commwiki/wiki?54273
genexus_version: "18"
---

# Gradle Options property for Java Generator

Specifies additional parameters that can be passed to Gradle (the build system used to compile Java).

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

By default, it has the following command:

> -Dorg.gradle.jvmargs=-Xmx$(ALLOC\_SIZE)m

Where:

* *-Dorg.gradle.jvmargs=<arguments>*indicates the JVM arguments to be used by the daemon process. Possible arguments can be found in the [Java documentation](https://docs.oracle.com/javase/9/tools/javac.htm#JSWOR627).
* *$(ALLOC\_SIZE)*takes the value 1024, representing the maximum amount of memory that can be allocated to the process.

To disable the Gradle daemon and prevent the compilation process from running after GeneXus finishes, you can add the --no-daemon option. Note that the daemon is enabled by default.

See [Gradle documentation](https://docs.gradle.org/current/userguide/command_line_interface.html) for more information.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

No action is required to apply the corresponding changes when the property value is configured.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853).

### [See Also](#See+Also)

[Gradle and the Java Generator](https://wiki.genexus.com/commwiki/wiki?52359)


|  |
| --- |
| **Backlinks** |
| [Compilation process with the Java Generator](https://wiki.genexus.com/commwiki/wiki?52362) |

---
