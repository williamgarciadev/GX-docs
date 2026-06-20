---
title: "Docker base image property"
source_id: 37047
source_url: https://wiki.genexus.com/commwiki/wiki?37047
genexus_version: "18"
---

# Docker base image property

Docker base image for this Dockerfile.

### [Description](#Description)

This is the base image on which the new [Docker image](https://wiki.genexus.com/commwiki/wiki?37050) will be created.

Reference: To find public Docker images for Tomcat, for example, refer to <https://hub.docker.com>.

**NOTE:**

* In the case of Java, the Base Image property is set with a default value in the GeneXus deployment dialog, which does not depend on the value of the Application Server property. You should enter a value according to the Application Server and the Java version you use.
* If the deployment unit has a Main procedure with [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) = "Command line", change the Base Image default value accordingly.  
  For example, in the case of Java, it can be OpenJDK:15. The same for the [Docker Image App location property](https://wiki.genexus.com/commwiki/wiki?37049) value.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?36778,,).

### [See Also](#See+Also)

* [HowTo: Deploy an Application to Docker](https://wiki.genexus.com/commwiki/wiki?36951)


|  |
| --- |
| **Backlinks** |
| [HowTo: Deploy an Application to Docker](https://wiki.genexus.com/commwiki/wiki?36951) | [HowTo: Deploy an Application to Docker (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54337) |

---
