---
title: "Log Format property"
source_id: 53005
source_url: https://wiki.genexus.com/commwiki/wiki?53005
genexus_version: "18"
---

# Log Format property

Sets the log output format.

### [Values](#Values)

|  |  |
| --- | --- |
| **Json** | Semi-structured log formats. |
| **Text** | Default value. Unstructured log formats. |

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

An unstructured format (text) is easy for humans to read but it is difficult for machine parsers to analyze and extract.

The simplicity and flexibility of JSON make it an ideal candidate for generating structured log statements; log data can be extracted and analyzed programmatically while messages remain easy for humans to understand.

JSON is the recommended log output format for most cases.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute [Build any object](https://wiki.genexus.com/commwiki/wiki?17719) with the purpose of generating the \*.config files.

### [Availability](#Availability)

This property is available since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081) | [HowTo: Observability of your GeneXus applications](https://wiki.genexus.com/commwiki/wiki?53767) |

---
