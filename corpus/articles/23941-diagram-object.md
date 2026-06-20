---
title: "Diagram object"
source_id: 23941
source_url: https://wiki.genexus.com/commwiki/wiki?23941
genexus_version: "18"
---

# Diagram object

Creates a diagram to include [Tables](https://wiki.genexus.com/commwiki/wiki?7120), [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Modules](https://wiki.genexus.com/commwiki/wiki?22414) inside it and automatically see their relationships.

In the [New object](https://wiki.genexus.com/commwiki/wiki?9931) dialog, you can find it under the 'Documentation' category.

When a new Diagram object is created, it will be empty initially. Next, just drop a few Tables, Transactions, or Modules from the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) into the Diagram, and relationships will be shown automatically.  
  
You can move the objects inside the Diagram as you wish, or you can right-click inside the Diagram and select **Arrange Nodes**.  
  
Adding objects to a Diagram can be done in any of the following ways:

* Drag and drop from KB Explorer
* When you have already included Tables or Transactions in a Diagram, you can right-click inside the Diagram and select:
  + **Add superordinated**
  + **Add subordinated**
  + **Add [all] related**
* When you have already included Modules, you can right-click inside the Diagram and select:
  + **Add SubModules opSubmodulestion:**Adds all the direct Submodules.
  + **Add All SubModules:**Adds all the direct submodules but the process is recursive, so, all the modules that are submodules to the one selected are also added to the Diagram.
  + **Add References:** Adds all the direct Referenced Modules.
  + **Add All References:** Adds all the Referenced Modules and recursively the Modules referenced by them.

### Diagrams are dynamic

Every time the Diagram object is opened, it shows the current relationship between the Tables or Transactions that belong to that Diagram. That is to say, if the referential integrity between two tables changes when the Diagram containing those tables is reopened, it will show the new relationship (adding or removing arrows).

Diagrams can also be saved as images or copied to the clipboard for further use.

## [See Also](#See+Also)

[Table Diagrams](https://wiki.genexus.com/commwiki/wiki?8927)   
[Transactions Diagrams](https://wiki.genexus.com/commwiki/wiki?8926)
