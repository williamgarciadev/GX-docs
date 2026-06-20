---
title: "Deploy to cloud property"
source_id: 15041
source_url: https://wiki.genexus.com/commwiki/wiki?15041
genexus_version: "18"
---

# Deploy to cloud property

Facilitates cloud prototyping by deploying the application to the GeneXus cloud.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | This is the default value. |
| **Yes** | Sets default values to deploy the application to the GeneXus Cloud. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

You can find this property in the [Knowledge Base Preferences window](https://wiki.genexus.com/commwiki/wiki?7109) of a certain [Environment](https://wiki.genexus.com/commwiki/wiki?7115) for backend generators. Remember that it is used for prototyping purposes only; it should not be used to host applications in production that might require another SLA.

By setting this property to 'Yes', the [Database name](https://wiki.genexus.com/commwiki/wiki?9080), [Web root](https://wiki.genexus.com/commwiki/wiki?9287), [Deploy Virtual Directory](https://wiki.genexus.com/commwiki/wiki?18342), [Deploy Server URL](https://wiki.genexus.com/commwiki/wiki?15042), and [Services URL](https://wiki.genexus.com/commwiki/wiki?21146) properties are automatically set with default values to deploy the application to the GeneXus cloud. Once the application is run, it is deployed to the GeneXus cloud.

#### [Note](#Note)

The [GAM](https://wiki.genexus.com/commwiki/wiki?14960) repository and application are also deployed to the cloud. This means that the GAM database will be automatically created in the cloud.

#### [Steps](#Steps)

1. Set related properties

   1. Review affected properties ([Database name property](https://wiki.genexus.com/commwiki/wiki?9080), [Web Root property](https://wiki.genexus.com/commwiki/wiki?9287), [Deploy Virtual Directory property](https://wiki.genexus.com/commwiki/wiki?18342) and [Deploy Server URL property](https://wiki.genexus.com/commwiki/wiki?15042), [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146)). You may want to point to other [Servers available for Cloud prototyping](https://wiki.genexus.com/commwiki/wiki?26157,,).
   2. Apple Specific: You may need to configure [App Transport Security property group](https://wiki.genexus.com/commwiki/wiki?29368) if [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146) uses SSL.
   3. Angular Specific: If the [Run Target property](https://wiki.genexus.com/commwiki/wiki?49730) is set to 'Default' (this is the default value), when setting the **Deploy to cloud property** = Yes, the Angular frontend is deployed to the cloud and it runs from there.
   4. Java Specific: Review the [Use annotations for servlet definition property](https://wiki.genexus.com/commwiki/wiki?29399).
2. Create Database.
3. Rebuild all Objects.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Deploy to cloud: Step by Step](https://wiki.genexus.com/commwiki/wiki?18250)


|  |
| --- |
| **Backlinks** |
| [Android Copy APK to Cloud property](https://wiki.genexus.com/commwiki/wiki?36621) | [Android specific properties](https://wiki.genexus.com/commwiki/wiki?31449) | [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) |
| [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [CI integrated to GeneXus and GXserver](https://wiki.genexus.com/commwiki/wiki?46966) | [Category:Cloud prototyping](https://wiki.genexus.com/commwiki/wiki?15046) | [Deploy Server URL property](https://wiki.genexus.com/commwiki/wiki?15042) |
| [Deploy to Cloud: Deployed Applications Administration](https://wiki.genexus.com/commwiki/wiki?27696) | [Deploy to cloud: Step by Step](https://wiki.genexus.com/commwiki/wiki?18250) | [Deploy to GeneXus Prototyping Cloud - FAQ](https://wiki.genexus.com/commwiki/wiki?18292) | [Deploy Virtual Directory property](https://wiki.genexus.com/commwiki/wiki?18342) |
| [HowTo: Create a deployment pipeline for an application using GXflow](https://wiki.genexus.com/commwiki/wiki?49176) | [HowTo: Prepare a Mac with ARM architecture for GeneXus](https://wiki.genexus.com/commwiki/wiki?51149) |
| [IIS Version property](https://wiki.genexus.com/commwiki/wiki?17521) | [Run Target property](https://wiki.genexus.com/commwiki/wiki?49730) | [User Properties](https://wiki.genexus.com/commwiki/wiki?25111) |
| [Web Server property](https://wiki.genexus.com/commwiki/wiki?9017) |

---
