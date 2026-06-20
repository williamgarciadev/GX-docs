---
title: "Servlet directory property"
source_id: 9122
source_url: https://wiki.genexus.com/commwiki/wiki?9122
genexus_version: "18"
---

# Servlet directory property

Sets the directory to which the generated servlets will be transferred. This property is read-only.

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

You can find this property in the [Preferences window](https://wiki.genexus.com/commwiki/wiki?7109) at the Back end Generator level.

This property is **read-only** and is generated based on the [Tomcat path property](https://wiki.genexus.com/commwiki/wiki?48354).

During the compilation of a web object, GeneXus automatically moves the compiled (.class) and configuration (.cfg) files to the folder set in this property.

Remember that any modification to the model properties will require re-generating and re-compiling at least one web object for the changes to take effect. In addition, for updates to be reflected at runtime, the Servlet server will need to be restarted.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

`[imagen omitida: wiki id 54711]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[HowTo: My first GeneXus Java Application](https://wiki.genexus.com/commwiki/wiki?45875)


|  |
| --- |
| **Backlinks** |
| [HowTo: My first GeneXus Java Application](https://wiki.genexus.com/commwiki/wiki?45875) | [HowTo: My first GeneXus Java Application (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55769) | [Category:Java Generator Properties set per User](https://wiki.genexus.com/commwiki/wiki?13930) |
| [Manually configuring Tomcat](https://wiki.genexus.com/commwiki/wiki?21382) | [Tomcat path property](https://wiki.genexus.com/commwiki/wiki?48354) | [User Properties](https://wiki.genexus.com/commwiki/wiki?25111) |

---
