---
title: "Main program property"
source_id: 7407
source_url: https://wiki.genexus.com/commwiki/wiki?7407
genexus_version: "18"
---

# Main program property

Sets an object as main object, which means it can be executed as a standalone application.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Work With](https://wiki.genexus.com/commwiki/wiki?15974)  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)

### [Description](#Description)

Default value: False.

Defines an object as [Main](https://wiki.genexus.com/commwiki/wiki?5770). This has a different meaning depending on the platform:

* An executable file will be generated for C# Windows environments containing all other objects called directly or indirectly by it. When a main object is called from another object, GeneXus generates a call to an executable file.
* A class containing a main method will be generated for Java Windows environments, making it a possible entry point for the application.
* In Web environments, it depends on the [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947).
* For [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s, it will create an installable application on the selected platform.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [See Also](#See+Also)

[Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817)


|  |
| --- |
| **Backlinks** |
| [Access Token property (Mercado Pago)](https://wiki.genexus.com/commwiki/wiki?44769) | [AddString method](https://wiki.genexus.com/commwiki/wiki?7063) |
| [Auto-register Anonymous User property](https://wiki.genexus.com/commwiki/wiki?19912) | [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) | [Deploy Application Targets](https://wiki.genexus.com/commwiki/wiki?42079) | [DesignOps - Sample - Travel Agency web back-office](https://wiki.genexus.com/commwiki/wiki?47052) |
| [GAM - Auto-register anonymous user - Panel usage example](https://wiki.genexus.com/commwiki/wiki?19911) | [GAM - Events subscription](https://wiki.genexus.com/commwiki/wiki?32698) | [Generator property](https://wiki.genexus.com/commwiki/wiki?7957) |
| [Getting Started with tvOS](https://wiki.genexus.com/commwiki/wiki?40787) | [HowTo: Configure Push Notifications in Apple Applications](https://wiki.genexus.com/commwiki/wiki?17451) | [HowTo: Configure Push Notifications in Apple Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54517) | [HowTo: Deploy a Workflow-based Application](https://wiki.genexus.com/commwiki/wiki?19848) |
| [HowTo: Deployment of a Command Line Procedure in Java](https://wiki.genexus.com/commwiki/wiki?55200) | [HowTo: Download a file using HTTP Protocol](https://wiki.genexus.com/commwiki/wiki?14144) | [HowTo: Integrate a new WhatsApp partner into a GeneXus Chatbot](https://wiki.genexus.com/commwiki/wiki?46271) | [HowTo: invoke a main Procedure that uses GAM's API in a Java environment](https://wiki.genexus.com/commwiki/wiki?54205) |
| [HowTo: Start a Process from an External Application](https://wiki.genexus.com/commwiki/wiki?9988) | [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) | [LocalNotifications external object](https://wiki.genexus.com/commwiki/wiki?39554) | [Location property](https://wiki.genexus.com/commwiki/wiki?7956) |
| [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) | [Category:Menu object](https://wiki.genexus.com/commwiki/wiki?16321) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) | [PDF Reports](https://wiki.genexus.com/commwiki/wiki?13531) |
| [PDF Reports (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54937) | [PDF Reports (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55935) | [Public Key property (Mercado Pago)](https://wiki.genexus.com/commwiki/wiki?44768) | [Registration Handler property](https://wiki.genexus.com/commwiki/wiki?22981) |
| [Use PDF Reports property](https://wiki.genexus.com/commwiki/wiki?42887) | [Used to property](https://wiki.genexus.com/commwiki/wiki?29584) | [What is a Master Page](https://wiki.genexus.com/commwiki/wiki?17088) |

---
