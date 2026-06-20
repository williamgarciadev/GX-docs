---
title: "Continuous Integration"
source_id: 38331
source_url: https://wiki.genexus.com/commwiki/wiki?38331
genexus_version: "18"
---

# Continuous Integration

You achieve **Continuous Integration** when you integrate in an automatic way the tasks of coding, build and test in your process.

Continuous integration should ensure that if a developer writes code, that code is tested and works first individually and then integrated into the entire system, and also ensure that the code that was written will not break anything in the system.

The idea of ​​Continuous Integration is that the work is integrated frequently, so as to avoid conflicts as far as possible and if they appear, they are small and easy to fix.

All this must be done automatically. Therefore, Continuous Integration is a very important point in the [DevOps](https://wiki.genexus.com/commwiki/wiki?42794,,) process.

In order to integrate your development, you have [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?31337,,), which together with the [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908) allows you to automate all the steps related to the Continuous Integration of the application. For each task that you can execute from GeneXus you have an MSBuild task that allows you to do the same but automatically.

For example, when a developer makes a change to an object and commits that change to GeneXus Server, you can have automated tasks that update that object to the production [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), perform the build, run the tests defined in the Knowledge Base, perform the deploy of the package (war) and leave it available on the server soon to be executed. In each step of the process, you have to include tests, whether they are [Unit Test objects](https://wiki.genexus.com/commwiki/wiki?38401), integration tests, etc.

For this you have several tasks that you must automate: code integration, build execution and execution of unit tests.

### [See Also](#See+Also)

[CI integrated to GeneXus and GXserver](https://wiki.genexus.com/commwiki/wiki?46966)  
[GXtest](https://wiki.genexus.com/commwiki/wiki?13183,,)


|  |
| --- |
| **Pages** |
| [CI / CD integration for Unit Tests](https://wiki.genexus.com/commwiki/wiki?38332) | [How to create a unit test and add a task using the GeneXus Jenkins Plugin](https://wiki.genexus.com/commwiki/wiki?38359) | [MSBuild Tasks for Running Tests (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54200) |
| [MSBuild Tasks for Running Tests (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56137) | [Running MSbuild using GXtest Target](https://wiki.genexus.com/commwiki/wiki?40739) | [Running MSbuild using GXtest Target (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54203) |
| [Running Unit tests](https://wiki.genexus.com/commwiki/wiki?38345) | [Typical GeneXus development cycle for Agile](https://wiki.genexus.com/commwiki/wiki?38329) | [Unit Testing](https://wiki.genexus.com/commwiki/wiki?38334) |

---
