---
title: "Build/Rebuild/Run"
source_id: 5692
source_url: https://wiki.genexus.com/commwiki/wiki?5692
genexus_version: "18"
---

# Build/Rebuild/Run

These are the most frequently used build options. They work with a selected [Main Object](https://wiki.genexus.com/commwiki/wiki?5770), which can either be the [Startup Object](https://wiki.genexus.com/commwiki/wiki?5394) or the Main object pointed to with the mouse. The typical scenario is one where you have a Main object set as the Startup Object, you change some objects and then press F5 (assigned by default to the Run command) to test the changes.

These options include the following steps:

|  |  |
| --- | --- |
| Steps | Comments |
| Save any unsaved objects | The step stops on errors |
| Reorganize the database if necessary | The step stops on errors |
| Specify only objects that have changed (Build) or force the specification of all objects (Rebuild) belonging to the selected Main object call tree (\*).  Consider also objects references in the properties of KB Version (except Startup Object), Environment and Generator, with their call tree. | The step stops on errors |
| Generate | The step does **not** stop on errors |
| Compile the selected Main object | The step stops on errors |
| Deploy | The step stops on errors |
| Execute the selected Main object (Run) |  |

(\*)The call tree of a Main object is "cut" on every other Main object found unless the [Call tree for build option](https://wiki.genexus.com/commwiki/wiki?18996) is set to full.

### [See also](#See+also)

[Build All/Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691)  
[Build/Run With This Only](https://wiki.genexus.com/commwiki/wiki?5693)  
[Run Without Building](https://wiki.genexus.com/commwiki/wiki?20689)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Build process](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/build-process-v16?p=5474)


|  |
| --- |
| **Backlinks** |
| [.NET Generator Standard Classes](https://wiki.genexus.com/commwiki/wiki?51442) | [Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719) | [Build All/Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691) |
| [Category:Build Menu](https://wiki.genexus.com/commwiki/wiki?5690) | [Build/Run With This Only](https://wiki.genexus.com/commwiki/wiki?5693) | [Call tree for build option](https://wiki.genexus.com/commwiki/wiki?18996) | [Category:Cloud prototyping](https://wiki.genexus.com/commwiki/wiki?15046) |
| [Compilation process with the Java Generator](https://wiki.genexus.com/commwiki/wiki?52362) | [Compilation process with the Java Generator (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?53881) | [Configuration.ExternalStorage External Object](https://wiki.genexus.com/commwiki/wiki?45913) | [Emulation for Android](https://wiki.genexus.com/commwiki/wiki?18270) |
| [Execution for Android Using the Device](https://wiki.genexus.com/commwiki/wiki?14910) | [Execution for Android Using the Device (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?56063) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [GXflow license scheme](https://wiki.genexus.com/commwiki/wiki?37204) |
| [How to execute an app using Angular Generator](https://wiki.genexus.com/commwiki/wiki?42544) | [HowTo: My first GeneXus Java Application](https://wiki.genexus.com/commwiki/wiki?45875) | [HowTo: My first GeneXus Java Application (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55769) | [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) |
| [Java Generator Standard Classes](https://wiki.genexus.com/commwiki/wiki?52361) | [KB:PlantCare - ECommerce Sample](https://wiki.genexus.com/commwiki/wiki?50476) | [KB:PlantCare and SweetWorld - ECommerce Sample (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?56139) |
| [Prototyping an API with Swagger](https://wiki.genexus.com/commwiki/wiki?50008) | [Prototyping device selection - Android](https://wiki.genexus.com/commwiki/wiki?20441) | [Run Without Building](https://wiki.genexus.com/commwiki/wiki?20689) |
| [Simple example with DynamoDB](https://wiki.genexus.com/commwiki/wiki?50607) | [Spring Boot in Java Application Development](https://wiki.genexus.com/commwiki/wiki?55782) | [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) |
| [Troubleshooting 'Execution failed' message when running a Web app](https://wiki.genexus.com/commwiki/wiki?49557) | [KB:WanderNest - Online Booking Sample](https://wiki.genexus.com/commwiki/wiki?55028) |

---
