---
title: "Tomcat version property"
source_id: 48352
source_url: https://wiki.genexus.com/commwiki/wiki?48352
genexus_version: "18"
---

# Tomcat version property

Sets the Tomcat version where the code will run.

### [Values](#Values)

|  |
| --- |
| **7** |
| **8 or 9** |
| **10.0** |
| **10.1 or higher** |

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

The main function of the Tomcat Version property is to facilitate the initialization of the [Java platform support](https://wiki.genexus.com/commwiki/wiki?48353) and [Tomcat path](https://wiki.genexus.com/commwiki/wiki?48354) properties.

This property is only relevant in the development environment and does not affect the generation of the final programs. For this reason, it is hidden when using the [Spring Boot framework](https://wiki.genexus.com/commwiki/wiki?55782), since a local Tomcat server is not required in that case.

The default value is the value of the latest Tomcat version detected.

You must use JDK 11 or higher when you set the value "10.1 or higher".

When this property is changed, [Tomcat path property](https://wiki.genexus.com/commwiki/wiki?48354) will change to the latest Tomcat installed with the same version.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

No action is required to apply the corresponding changes when the property value is configured.


|  |
| --- |
| **Backlinks** |
| [Deploy Java application to Docker and Kubernetes using Redis](https://wiki.genexus.com/commwiki/wiki?57627) | [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853) | [HowTo: My first GeneXus Java Application](https://wiki.genexus.com/commwiki/wiki?45875) |
| [HowTo: My first GeneXus Java Application (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55769) | [Java Framework property](https://wiki.genexus.com/commwiki/wiki?55711) | [Java platform support property](https://wiki.genexus.com/commwiki/wiki?48353) | [Support for Jakarta EE and Java EE](https://wiki.genexus.com/commwiki/wiki?48018) |
| [Tomcat path property](https://wiki.genexus.com/commwiki/wiki?48354) | [Tomcat version property (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54343) | [Troubleshooting 'Execution failed' message when running a Web app](https://wiki.genexus.com/commwiki/wiki?49557) |

---
