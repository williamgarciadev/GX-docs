---
title: "Include GXflow backoffice property"
source_id: 49569
source_url: https://wiki.genexus.com/commwiki/wiki?49569
genexus_version: "18"
---

# Include GXflow backoffice property

If true, the GXflow backoffice will be deployed with your application.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Level:** Deploy Target Options

### [Description](#Description)

To view this property, you need to have defined a [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486) in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

Then, you can find it by clicking on the Options link in the dialog that is opened when using the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092).

The property's default value is True.

If this property is set to True and a Business Process Diagram is added to the deployment, the GXflow backoffice is included when deploying your application.

Otherwise, when the property is set to False or there isn't a Business Process Diagram in the deployment, the GXflow backoffice is not included during deployment. This can be useful if you have developed a custom inbox and you are not using GXflow. You can see an example in [GXflow Web Custom Client based on Unanimo design system](https://wiki.genexus.com/commwiki/wiki?48897).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/wiki?49301,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [HowTo: Deploy a Workflow-based Application](https://wiki.genexus.com/commwiki/wiki?19848) |

---
