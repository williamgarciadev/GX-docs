---
title: "Tomcat path property"
source_id: 48354
source_url: https://wiki.genexus.com/commwiki/wiki?48354
genexus_version: "18"
---

# Tomcat path property

Sets the path where Tomcat is installed.

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

By default, it selects the latest version tomcat that matches the [Tomcat version property](https://wiki.genexus.com/commwiki/wiki?48352).

If the property is changed to a different tomcat the [Tomcat version property](https://wiki.genexus.com/commwiki/wiki?48352) needs to be changed manually to match the version of the new tomcat server

[Servlet directory property](https://wiki.genexus.com/commwiki/wiki?9122) and [Static content directory seen from client property](https://wiki.genexus.com/commwiki/wiki?9124) are now read-only and generated based on this property

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

No action is required to apply the corresponding changes when the property value is configured.

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,).


|  |
| --- |
| **Backlinks** |
| [HowTo: Change Windows Registry values for Tomcat](https://wiki.genexus.com/commwiki/wiki?21926) | [HowTo: My first GeneXus Java Application](https://wiki.genexus.com/commwiki/wiki?45875) | [HowTo: My first GeneXus Java Application (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55769) |
| [Java Framework property](https://wiki.genexus.com/commwiki/wiki?55711) | [Manually configuring Tomcat](https://wiki.genexus.com/commwiki/wiki?21382) | [Servlet directory property](https://wiki.genexus.com/commwiki/wiki?9122) | [Static content directory seen from client property](https://wiki.genexus.com/commwiki/wiki?9124) |
| [Support for Jakarta EE and Java EE](https://wiki.genexus.com/commwiki/wiki?48018) | [Tomcat version property](https://wiki.genexus.com/commwiki/wiki?48352) | [Tomcat version property (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54343) |

---
