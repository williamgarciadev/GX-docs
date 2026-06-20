---
title: "Versioning the application by Modules"
source_id: 20937
source_url: https://wiki.genexus.com/commwiki/wiki?20937
genexus_version: "18"
---

# Versioning the application by Modules

Versioning the application by Modules is one of the [Version Management and Work Methodology with GeneXus Server](https://wiki.genexus.com/commwiki/wiki?20649,,) scenarios.

In this case, the development team works on a Knowledge Base divided into several modules (purchase module, cashier module, etc.) and one or several testing teams. The main idea is to have independent [Knowledge Base Versions](https://wiki.genexus.com/commwiki/wiki?5680,,) for each module.

### [Version Management](#Version+Management)

The method is similar to the [Versioning the application to manage the different stages of Validation or Approval](https://wiki.genexus.com/commwiki/wiki?20938) scenario, except for the fact that the team must define a version for each module.

All the versions associated with the modules are set parallel to one another and based on the General [Knowledge Base Versions](https://wiki.genexus.com/commwiki/wiki?5680,,) (or Trunk), where we have the whole application.

The developer(s) of a module work on a local Knowledge Base connected to the Knowledge Base's version associated with the module.

### [Work Methodology](#Work+Methodology)

In each module we must apply the following methodology:

* Each developer collaborates with a local Knowledge Base connected to GeneXus Server, on the corresponding Module version. Each developer must perform a [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626) operation to consolidate changes with the Knowledge Base in GeneXus Server. When a developer needs to obtain the changes done by another developer, must perform an [Update From GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10627) operation.
* When the entire version needs to be updated, the developer must execute a [Bring Changes](https://wiki.genexus.com/commwiki/wiki?20912,,) of the module on the development version, and then do [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626) of this module located in [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911).

If in addition to having a testing team to test modules separately, we also need to perform an integrated test, we must define a version to integrate all the modules, based on the General version. This version is updated in a way similar to what has been explained (doing Bring Changes of the test versions of each module and doing Commit on the integrated test version).

The figure below shows that one version was defined for each module in the application, and another version was established for each testing team, and how each of these versions is updated.

`[imagen omitida: wiki id 35346]`
