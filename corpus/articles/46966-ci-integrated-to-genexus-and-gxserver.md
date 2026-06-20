---
title: "CI integrated to GeneXus and GXserver"
source_id: 46966
source_url: https://wiki.genexus.com/commwiki/wiki?46966
genexus_version: "18"
---

# CI integrated to GeneXus and GXserver

As of GeneXus 17, it is possible to create and monitor continuous integration processes from the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272) and the [GeneXus Server Console](https://wiki.genexus.com/commwiki/wiki?26410,,).

In this way, it is very easy to set from GeneXus that for a certain KB in GeneXus Server, a process is created that creates its own working KB. Also, that it periodically checks if there have been new commits, in which case it can update the local KB, run a build, do [Deploy to Cloud](https://wiki.genexus.com/commwiki/wiki?15041) of what is generated, and run tests contained in the KB.

[GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911) solves all communication and coordination with a Jenkins server, which in turn is in charge of executing the processes and reporting their results. Developers can access most of the information and tasks directly in GeneXus and GeneXus Server or access Jenkins for more details or more advanced configurations.

In order to enable this feature some configurations must be made, please refer to document: [How to configure GeneXus Server for Continuous Integration](https://wiki.genexus.com/commwiki/wiki?46996)

## [Continuous Integration in GeneXus](#Continuous+Integration+in+GeneXus)

In the GeneXus IDE, within the [Knowledge Manager Team Development](https://wiki.genexus.com/commwiki/wiki?20864) window, a new tab called Continuous Integration is shown.

`[imagen omitida: wiki id 46969]`

From here it is possible to create new pipelines and also monitor the execution of the defined pipelines.

## [Continuous Integration in GeneXus Server console](#Continuous+Integration+in+GeneXus+Server+console)

In the GeneXus Server console, a new option is added to the menu called Continuous Integration\Pipelines where you can see all the defined pipelines and also create new ones.

Also at the KB level, it is possible to access the pipelines defined for that KB.

`[imagen omitida: wiki id 46970]`

By clicking on a pipeline it is possible to see the number of times it was executed and its status.

`[imagen omitida: wiki id 46971]`

### [See Also](#See+Also)

* [CI: Create Pipeline](https://wiki.genexus.com/commwiki/wiki?46972)
* [CI: Pipeline Execution](https://wiki.genexus.com/commwiki/wiki?46989)
* [CI: User Permission](https://wiki.genexus.com/commwiki/wiki?46994,,)
* [How to configure GeneXus Server for Continuous Integration](https://wiki.genexus.com/commwiki/wiki?46996)


|  |
| --- |
| **Backlinks** |
| [Category:Continuous Integration](https://wiki.genexus.com/commwiki/wiki?38331) | [Toc:DevOps in GeneXus](https://wiki.genexus.com/commwiki/wiki?38363) |
| [HowTo: Create a deployment pipeline for an application using GXflow](https://wiki.genexus.com/commwiki/wiki?49176) |

---
