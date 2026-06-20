---
title: "Java Artifact Version property"
source_id: 53866
source_url: https://wiki.genexus.com/commwiki/wiki?53866
genexus_version: "18"
---

# Java Artifact Version property

Determines the version of the Java Artifact ID that implements the External Object.

### [Scope](#Scope)

**Objects:** [External Object](https://wiki.genexus.com/commwiki/wiki?5669)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This property is enabled if a value is assigned to the [Java Artifact Id property](https://wiki.genexus.com/commwiki/wiki?53865).

If it is not specified, the Generator Standard Classes Version is used. The Generator Standard Classes Version that is being used is the value of the [Standard classes specific version property](https://wiki.genexus.com/commwiki/wiki?51259).

Java Artifact Version is a number used to uniquely identify a package. This number should follow the format established by Gradle, which includes three numbers separated by dots. The format is as follows:

Major.Minor.Patch[-Suffix]

More information: <https://docs.gradle.org/current/userguide/single_versions.html>

### [Samples](#Samples)

1.0.0 means that the package with the exact version 1.0 will be referenced.  
1.0.+ means that the package with the highest existing version with major 1 will be used.  
1.0.- means that the package with the smallest version >= 1.0 found in the repository (that is, Gradle) will be referenced.  
1.0.0 <= x < 1.1.0 means that a reference is being made to a version that is greater than or equal to 1.0.0 and less than 1.1.0.  
1.+ < 2.0 means that any version greater than or equal to 1.0.0 and less than 2.0.0 is being referenced.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853).


|  |
| --- |
| **Backlinks** |
| [Compilation process with the Java Generator](https://wiki.genexus.com/commwiki/wiki?52362) | [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853) | [Java Artifact Id property](https://wiki.genexus.com/commwiki/wiki?53865) |

---
