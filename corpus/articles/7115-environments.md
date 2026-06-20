---
title: "Environments"
source_id: 7115
source_url: https://wiki.genexus.com/commwiki/wiki?7115
genexus_version: "18"
---

# Environments

One of the benefits of using GeneXus is that it makes possible the generation of applications running on many different platforms (from a Web interface, a watch, cell phone, tablet or TV, to cloud server farms). It generates code in different programming languages and stores the application data in different databases.

An Environment allows you to set and store all the information related to a certain implementation of your application, for example: the generators you want to use to generate the Back end of your application, the generators to be used to generate the Front end, the database information, etc.

When creating a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), a default Environment is created.

The "New Knowledge Base" dialog —in addition to asking you for the Knowledge Base name and path— it requests you to select the programming language to be used to generate the code corresponding to the application Back end, as well as the programs to create/modify the database structure (called [Reorganization](https://wiki.genexus.com/commwiki/wiki?5288) programs). The rest of the Environment information must be configured through its properties.

`[imagen omitida: wiki id 54583]`

So, after the Knowledge Base creation, you can verify the default Environment is created by selecting the [Preferences](https://wiki.genexus.com/commwiki/wiki?7109) tab located next to the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) tab:

`[imagen omitida: wiki id 54584]`

The default Environment name (i.e. ".NET Environment", "Java Environment", etc.) can be changed by editing the Name property. In the same way, if you want to change the programming language, you can modify the Language property. And so you can set the different Environment properties.

An Environment is made up of the following nodes:

1. **Back end:**It refers to everything related to the application server, the accesses to the database, and the services.
2. **Front end:**It refers to everything related to the UI (what is shown and used to interact) and connects with the **Back end**. So, the resources to generate (and set) these are .NET, Java, Angular, Android, Apple.
3. **Deployment:**It refers to the [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886)s defined in the KB Version.

### [1. Back end](#1.+Back+end)

The Back end node defines:

* The programming language(s) that will be used to generate the code corresponding to the application Back end as well as the programs to create/modify the database structure. There is a Default language (in the shown example is .NET given that it was selected at the Knowledge Base creation time) and it is possible to define more generators for specific scenarios. Learn more about [GeneXus Generators](https://wiki.genexus.com/commwiki/wiki?7116).
* The Default [Data Store](https://wiki.genexus.com/commwiki/wiki?7117) to set the information to access to the database associated with your generated application. It is also possible to create other Data Stores to read external databases.
* The Services node, whose properties allow you to configure the handling of services, storage settings, notifications, etc.

### [2. Front end](#2.+Front+end)

It shows the generators available to generate the Front end of the application so that you can configure their properties. By default, the generators shown are: .NET, Android, and Apple. You can add the Angular generator by setting the Front end **Generate Angular property** to Yes.

### [3. Deployment](#3.+Deployment)

This node allows you to define different [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886)s.

## [Working with several Environments](#Working+with+several+Environments)

Each Environment stores the details corresponding to a specific application implementation.

To define a new Environment, being positioned on the KB Version node or on the Default Environment node, right-click and select "New Environment". The [New Environment dialog](https://wiki.genexus.com/commwiki/wiki?24702) will be opened.

Only one Environment can be active at a time, which means that will be the one used to generate the application, reorganize the database, and run when pressing F5.

The one active by default is the Default Environment.

To get an Environment "active", right-click on its name (over the root node of the environment tree) and click on "Set As Current Environment". When it becomes active, the name of the Environment is highlighted with bold case and the icon next to the name shows an orange arrow (i.e. "PLAY" symbol) to indicate that that Environment will be the one used.

An inactive Environment is indicated with its name case not bold that shows that the Environment will not be used in generating, nor in connecting to a database.

## [Considerations](#Considerations)

When changing Environment properties usually a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691) is needed, for more details check [Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719).


|  |
| --- |
| **Sub Categories** |
| [Category:Data Stores](https://wiki.genexus.com/commwiki/wiki?7117) | [Category:GeneXus Generators](https://wiki.genexus.com/commwiki/wiki?7116) | [Category:GeneXus Generators (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55944) |
| [Category:Workflow Environment Preferences](https://wiki.genexus.com/commwiki/wiki?13601) |

---

|  |
| --- |
| **Pages** |
| [Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719) | [Layout Metadata Directory property](https://wiki.genexus.com/commwiki/wiki?24561) | [Temp media directory property](https://wiki.genexus.com/commwiki/wiki?7628) |

---
