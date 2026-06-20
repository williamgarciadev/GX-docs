---
title: "Expose as Enterprise Java Bean property"
source_id: 8011
source_url: https://wiki.genexus.com/commwiki/wiki?8011
genexus_version: "18"
---

# Expose as Enterprise Java Bean property

Exposes a GeneXus Procedure as EJB when set to True.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** Procedure  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

There are two ways to generate GeneXus [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) as EJB; one way is by setting its **'Expose as Enterprise Java Bean'** property to TRUE. The Procedure will be generated as a session bean (stateless) and as a message-driven bean, and can be called as any of them from external applications.

#### [Note](#Note)

The **'Expose as Enterprise Java Bean'** object property must be set in order to expose the GeneXus Procedure as EJB.  
If the object has its [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) = “Enterprise Java Bean”, by default the object can be called from GeneXus objects and from external objects automatically. But if you want to only expose it for external objects, and use the Procedure in GeneXus as a common Procedure, then the [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) can keep an internal value, and the **'Expose as Enterprise Java Bean'** property = TRUE.

#### [Requirements](#Requirements)

Some EJB support libraries must be added to the classpath. Each J2EE server provides this support; for example, in WebSphere you find it in the j2ee.jar located in the lib folder. These classes are necessary to compile the EJB Procedures.

[LUW](https://wiki.genexus.com/commwiki/wiki?2110,,)s (Logical Unit of Work) can be managed by the object itself or by the EJB Container. An advantage of the second option is that it allows the GeneXus EJB Procedures to be used with external applications. Also, the management of their LUWs can be configured by the EJB Container administrator, so it's totally independent of GeneXus.

This feature can be configured in the new object property called Transaction Type. The default value is Container, which means that the LUWs are managed by the EJB Container.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [See Also](#See+Also)

[Transactional Integrity and Enterprise Java Beans](https://wiki.genexus.com/commwiki/wiki?8012)  
[Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947)


|  |
| --- |
| **Backlinks** |
| [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) |

---
