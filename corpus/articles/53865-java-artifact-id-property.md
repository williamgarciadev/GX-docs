---
title: "Java Artifact Id property"
source_id: 53865
source_url: https://wiki.genexus.com/commwiki/wiki?53865
genexus_version: "18"
---

# Java Artifact Id property

Sets the ID of the Java Artifact associated with the External Object.

### [Scope](#Scope)

**Objects:** [External Object](https://wiki.genexus.com/commwiki/wiki?5669)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

Java Artifact Id is a string of text that follows the Gradle format:

GroupName:ArtifactName

* Group Name: This is the name of the organization or group that publishes the package. For example, "com.example."
* Artifact Name: This is the name of the package itself. For example, "my-library."

More information: [https://docs.gradle.org/current/userguide/declaring\_dependencies.html](http://More information: https://docs.gradle.org/current/userguide/declaring_dependencies.html)

Keep in mind the points below when configuring the property:

1. Avoid using unsupported characters, such as spaces and special characters.
2. The property is case-sensitive.

Also, this property can be used instead of or in addition to the [Java Artifact Version property](https://wiki.genexus.com/commwiki/wiki?53866). If both are specified, both will be considered.

### [Samples](#Samples)

com.genexus:gxwebsocket  
com.dameng:DmJdbcDriver18

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853).


|  |
| --- |
| **Backlinks** |
| [Compilation process with the Java Generator](https://wiki.genexus.com/commwiki/wiki?52362) | [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853) | [Java Artifact Version property](https://wiki.genexus.com/commwiki/wiki?53866) |

---
