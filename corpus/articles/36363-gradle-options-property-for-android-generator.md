---
title: "Gradle Options property for Android Generator"
source_id: 36363
source_url: https://wiki.genexus.com/commwiki/wiki?36363
genexus_version: "18"
---

# Gradle Options property for Android Generator

Specifies additional flags that can be passed to Gradle (the build system used to compile Android).
This property is for advanced developers only and they are responsible for using it correctly.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)  
**Level:** Generator

### [Description](#Description)

By default, it has the following command:

> --no-daemon --parallel -Dorg.gradle.jvmargs=-Xmx$(ALLOC\_SIZE)m

Where *$(ALLOC\_SIZE)* is 3072. To disable this behavior simply remove '--daemon' flag.

|  |  |
| --- | --- |
| **Flag** | **Description** |
| **--no-daemon** | Disables [gradle's daemon](https://docs.gradle.org/current/userguide/gradle_daemon.html). Alternatively, you can use --daemon flag for enabling it, significantly speeding up following builds significantly. By default is disabled so as not to interfere with other Android build processes. |
| **--parallel** | Indicates to execute the build task in parallel (i.e. compile mains projects in parallel). |
| **-Dorg.gradle.****jvmargs=<arguments>** | Indicates the JVM arguments to be used by the daemon process. Possible arguments can be found [here](http://docs.oracle.com/javase/7/docs/technotes/tools/solaris/java.html).  In particular, -Xmx2048m sets the maximum amount of memory (on 2GB) to allocate for Gradle Daemon. |

### [Notes](#Notes)

* Android's Gradle plugin will use a special option [DexInProcess](https://medium.com/google-developers/faster-android-studio-builds-with-dex-in-process-5988ed8aa37e#.d8gs5kol6) when Gradle's daemon VM has enough memory allocated to speed up its build time significantly. When the property [Multidex Build property](https://wiki.genexus.com/commwiki/wiki?35886) is enabled, the amount of memory required to enable [DexInProcess](https://medium.com/google-developers/faster-android-studio-builds-with-dex-in-process-5988ed8aa37e#.d8gs5kol6) increases by 1GB (since this property modifies the javaMaxHeapSize default value). Consequently, the *$(ALLOC\_SIZE)* is set to **3GB** (-Xmx3072m).Otherwise, the value used is 2GB (-Xmx2048m).
* As of [GeneXus 15 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?37491,,) daemon flag is disabled (--no-daemon).  
  Previous upgrades have this flag enable (--daemon).
* **--offline**:Specifies that the build should operate without accessing network resources. [DOC:Command-Line Interface.](https://docs.gradle.org/current/userguide/command_line_interface.html)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

* [Gradle](https://gradle.org/)


|  |
| --- |
| **Backlinks** |
| [Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449) | [Android Requirements (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55100) | [Android Requirements (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56500) |
|

---
