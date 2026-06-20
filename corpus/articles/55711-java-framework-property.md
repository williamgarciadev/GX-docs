---
title: "Java Framework property"
source_id: 55711
source_url: https://wiki.genexus.com/commwiki/wiki?55711
genexus_version: "18"
---

# Java Framework property

Specifies the framework to build Java applications.

### [Values](#Values)

|  |  |
| --- | --- |
| **None** | Default value. Keeps the existing configuration without adding an additional framework. |
| **Spring Boot** | Uses Spring Boot as framework to build applications and uses an embedded Tomcat server. |

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

"None" allows maintaining the existing functionality with the current configuration, while "Spring Boot" introduces automation and convenience by incorporating a specific framework, which can speed up the development of Java applications in GeneXus.  
  
The main difference when using Spring Boot is that you don't need to have Tomcat or another separate server installed to run your application. Spring Boot comes with an embedded Tomcat server, so the application will run on an internal web server provided by Spring Boot without requiring additional server configurations. This significantly simplifies the development and deployment process, as you don't need to worry about installing and configuring an external Tomcat server. For more information, go to [Spring Boot in Java Application Development](https://wiki.genexus.com/commwiki/wiki?55782).  
  
On the other hand, when you select None, you must download Tomcat and configure the [Tomcat path property](https://wiki.genexus.com/commwiki/wiki?48354) and [Tomcat version property](https://wiki.genexus.com/commwiki/wiki?48352) to run your application.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240).


|  |
| --- |
| **Backlinks** |
| [Spring Boot in Java Application Development](https://wiki.genexus.com/commwiki/wiki?55782) |

---
