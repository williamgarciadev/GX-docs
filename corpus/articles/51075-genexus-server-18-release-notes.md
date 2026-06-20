---
title: "GeneXus Server 18 Release Notes"
source_id: 51075
source_url: https://wiki.genexus.com/commwiki/wiki?51075
genexus_version: "18"
---

# GeneXus Server 18 Release Notes

GeneXus Server 18 is the team development tool for GeneXus: it provides easy collaboration while keeping track of changes on any knowledge base (SCM). Besides being the basis for coordinating and integrating work among multiple developers on any project, it’s also the core for the release and evolution workflows of the project life-cycle. These workflows may also be fully automated (CI / CD), and GeneXus Server provides multiple integration points with automation servers.

GeneXus Server 18 includes multiple improvements both to its core functionality and to its integration capabilities to enable fully automated DevOps on any kind of project, ranging from the simplest scenarios to the most sophisticated ones.

### [Support for GeneXus 18 and previous versions](#Support+for+GeneXus+18+and+previous+versions)

Since GeneXus versions and their upgrades add functionalities that may involve new object types, parts, or properties, GeneXus Server is also updated so it can recognize and correctly handle these components that previous versions could not support.

In a similar way, the GeneXus Server web console is extended to properly display the knowledge base content, including any new components or features.

Upgrading to GeneXus Server 18 ensures full support for projects that are developed using GeneXus 18 and make use of any object type, part or property that might not be available for previous versions.

At the same time, it provides full backward compatibility for projects that may still be developed with previous GeneXus versions. GeneXus Server 18 may host KBs and properly interop with different GeneXus installations on any version and upgrade, from version 15 up to version 18.

### [Automated DevOps Integration](#Automated+DevOps+Integration)

GeneXus allows integration automation through a complete set of MSBuild tasks, covering operations such as updating a knowledge base from a GeneXus Server, modifying properties or objects, committing changes, building, deploying, etc.

### [Jenkins Integration](#Jenkins+Integration)

In particular for [Jenkins](https://www.jenkins.io/), a widely used open source automation server, the [GeneXus Plugin provides](https://github.com/jenkinsci/genexus-plugin) support for GeneXus Server. With this plugin, it’s easy to catalog different GeneXus installations as tools and link pipelines to GeneXus Server as their SCM so that Jenkins can track changes and fire integrations.

Since version 17 of GeneXus and GeneXus Server, there is also a built-in integration so that basic pipelines can automatically be created and monitored directly from GeneXus IDE or GeneXus Server web console.

This provides basic update & build continuous integration cycles, but both these pipelines and the template it’s used to maintain them can be easily customized or extended to cover more scenarios, such as email notifications, packaging and deployment.

Some of the most recent developments on this plugin include:

**Support for Java 11:** Beginning with Jenkins 2.357 [Jenkins requires Java 11 or newer](https://www.jenkins.io/blog/2022/06/28/require-java-11/). In anticipation of these changes, the GeneXus Plugin was refactored and tested to support Java 11 and the newest Jenkins version.

**Support for master-slave configurations:** Jenkins allows a master installation to distribute its workload among multiple slave agents on separate machines, usually with different capabilities (operating system versions, installed tools, compute power, etc.). The plugin was extended to support declarative pipelines on master-slave architectures.

### [Azure DevOps](#Azure+DevOps)

Azure DevOps Server is a Microsoft product that also provides automated builds, testing and release management capabilities, among others. In this document, you can find a step by step guide on how to set up Azure DevOps pipeline tooling for continuous integration and deployment of GeneXus Knowledge Bases.

Configuring this integration allows GeneXus Server to trigger Update & Build pipelines on Azure DevOps. These builds update and publish new application unit binaries and trigger a Release pipeline that deploy them to the proper Azure target (Azure Web Apps, Azure Storage Static Websites, Azure Functions or Azure Serverless).

### [GeneXus Server client library](#GeneXus+Server+client+library)

The GeneXus Plugin for Jenkins uses a Java implementation of web service clients to communicate to any GeneXus Server installation. This includes, for example, checking the knowledge bases and their info, and getting the information about the commits performed on any version.

This implementation was recently published as a separate Java library ([gxserver-client](https://github.com/genexuslabs/gxserver-client)) that is also available as open source so it can be used for any Java development that may need to get info from a GeneXus Server.


|  |
| --- |
| **Backlinks** |
| [Automated DevOps with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51574) | [Toc:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 Suite Release Notes](https://wiki.genexus.com/commwiki/wiki?56923) |

---
