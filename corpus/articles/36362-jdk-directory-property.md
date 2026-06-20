---
title: "JDK Directory property"
source_id: 36362
source_url: https://wiki.genexus.com/commwiki/wiki?36362
genexus_version: "18"
---

# JDK Directory property

Specifies the path where the JDK is located in the local file system.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

To be able to compile a GeneXus Android application, you have to complete the JDK Directory property with the path where the JDK is located.

#### [Troubleshooting](#Troubleshooting)

If the following error is displayed:

========== Android Compilation started ==========  
error: An invalid version of the JDK was found. Please set the property 'JDK Directory' to a JDK version 11.0 major exactly (64-bit if you are on a 64-bit OS).  
Failed: Android Compilation

You must install the [JDK 11](https://jdk.java.net/java-se-ri/11) and indicate the installation path for this property.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449)
