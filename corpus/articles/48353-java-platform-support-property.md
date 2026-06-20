---
title: "Java platform support property"
source_id: 48353
source_url: https://wiki.genexus.com/commwiki/wiki?48353
genexus_version: "18"
---

# Java platform support property

Determines the Java Platform to choose according to the server version used. If you don't know which server your application will use, select the 'Both Platforms' option.

### [Values](#Values)

|  |  |
| --- | --- |
| **Both Platforms** | The framework used on the server side can be Jakarta EE or Java EE. |
| **Jakarta EE** | The framework used on the server side is Jakarta EE. |
| **Java EE** | The framework used on the server side is Java EE. |

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

Default value depends on the property [Tomcat version property](https://wiki.genexus.com/commwiki/wiki?48352). If [Tomcat version property](https://wiki.genexus.com/commwiki/wiki?48352) is 10 or higher default value will be Jakarta EE otherwise the default value will be Java EE

It is recommended to always specify either Jakarta EE or Java EE when possible.

Both platforms value is recommended only for cases when it is not known the server that the application will be run, for example when generating a module that will be distributed to other KBs.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,).


|  |
| --- |
| **Backlinks** |
| [Deploy to SAP Cloud Foundry - SAP BTP](https://wiki.genexus.com/commwiki/wiki?49572) | [Deploy to SAP Cloud Foundry - SAP BTP (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54602) | [HowTo: Deploy an application to Google App Engine](https://wiki.genexus.com/commwiki/wiki?32211) |
| [Support for Jakarta EE and Java EE](https://wiki.genexus.com/commwiki/wiki?48018) |

---
