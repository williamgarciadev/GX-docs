---
title: "Application Configuration using Environment Variables"
source_id: 39459
source_url: https://wiki.genexus.com/commwiki/wiki?39459
genexus_version: "18"
---

# Application Configuration using Environment Variables

In various scenarios, it is common practice to read configuration information from environment variables, rather than configuration files. This document details the scenarios in which this practice is used and its advantages.

## [Scenarios](#Scenarios)

**1) Typical case and good practice using Docker Containers**

One of the main benefits of the use of containers is that they can be mounted on any boat.  
In technical terms: The idea is that the docker image that you use for testing could be used for production; this way you have certainty that what you tried, is what you execute in production.

The solution that the industry uses, in this case, is Environment Variables.  
In practice: When the container is instantiated, it is said to execute with these and those values for these and those environment variables. And the application that runs in the container reads those environment variables.

Without this, the connection options to the databases are hardcoded into a connection file that is part of the web app that goes into the docker image (the container). So the container that you use in your testing environment is not the one you can use in your production environment, where it has to be attached to another database with other credentials.

**2) Security, Independence of development and production teams:** Case of Deployment of a *war* or *zip*

Without the use of Environment Variables, the only way to reuse the deployment package for production is to know the Database credentials and other properties of production when you create the package using the GeneXus IDE, something that is not viable in many companies or projects.

**3) Cloud Native:** In a PaaS environment, when connecting against a Database service, Cloud providers propose specific environment variables maintained by them. With this, they guarantee that if they later change the Database service URI  (for example after a restore) requiring other credentials or connection options, the applications automatically take those new values without having to change other things in the web servers.

**4) Agility in testing:** If you run an application in a Docker container, you might want to run it with some configuration, and then with another; for example, to test how its behavior varies, or how it behaves depending to which Database is connected.

### [Configuration information that is not included](#Configuration+information+that+is+not+included)

There is some configuration information that must not be changed through environment variables. The reason is that not all the program parts (eg. gxcfg.js) take into account those changes and inconsistencies may arise.

This is a list of those exceptions (the names of the following configuration entries correspond to .NET):

* AppMainNamespace
* DateFormat
* YearLimit
* TimeAmPmFormat
* VER\_STAMP
* StorageTimeZone
* LANGUAGE
* LANG\_NAME
* DECIMAL\_POINT
* DATE\_FMT
* CTOD\_DATE\_FMT
* GX\_BUILD\_NUMBER
* DocumentType

### [Availability](#Availability)

This feature is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,)

### [See Also](#See+Also)

[Application Configuration using Environment Variables in .NET and Java](https://wiki.genexus.com/commwiki/wiki?53336)  
[Application Configuration using Environment Variables in Cloud Services](https://wiki.genexus.com/commwiki/wiki?53339)  
[HowTo: Deploy an Application to Docker](https://wiki.genexus.com/commwiki/wiki?36951)


|  |
| --- |
| **Backlinks** |
| [Application Configuration using Environment Variables in .NET and Java](https://wiki.genexus.com/commwiki/wiki?53336) | [Application Configuration using Environment Variables in Cloud Services](https://wiki.genexus.com/commwiki/wiki?53339) | [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) |
| [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [ConfigurationManager external object](https://wiki.genexus.com/commwiki/wiki?40085) | [Considerations for building and deploying applications to containers](https://wiki.genexus.com/commwiki/wiki?45309) | [CORS settings with environment variables](https://wiki.genexus.com/commwiki/wiki?52127) |
| [Docker Environment variables property](https://wiki.genexus.com/commwiki/wiki?40607) |

---
