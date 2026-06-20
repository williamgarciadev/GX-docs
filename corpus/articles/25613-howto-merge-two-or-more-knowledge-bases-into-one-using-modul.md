---
title: "HowTo: Merge two or more Knowledge Bases into one using Modules"
source_id: 25613
source_url: https://wiki.genexus.com/commwiki/wiki?25613
genexus_version: "18"
---

# HowTo: Merge two or more Knowledge Bases into one using Modules

The purpose of this article is to explain the steps necessary for merging two or more Knowledge Bases using Module objects.

Merging [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)s is now easier since, with the Modules feature, the value of an object’s [Name property](https://wiki.genexus.com/commwiki/wiki?6985) must be unique among all objects in the Module, though it may be repeated in a different Module.

**Note**: remember to back up your Knowledge Bases before making any changes to them.

### [Step 1 - Creating the Knowledge Base](#Step+1+-+Creating+the+Knowledge+Base)

* If any of the Knowledge Bases was created with [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,), then you should use it as the 'base Knowledge Base' to merge. Otherwise, go to the next bullet.  
  Create a new [Module object](https://wiki.genexus.com/commwiki/wiki?22411) and move all imported objects to it —see [HowTo: Add an object to a Module](https://wiki.genexus.com/commwiki/wiki?25548).  
  Go to Step 2.
* If the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)s are from previous versions, then the first step should be to convert one of them into [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,) —read [Converting Knowledge Bases to GeneXus 16, 17 or higher](https://wiki.genexus.com/commwiki/wiki?10903,,) for further details. Then use it as the 'base Knowledge Base' to merge, create a new [Module object](https://wiki.genexus.com/commwiki/wiki?22411) and move all imported objects to it —read [HowTo: Add an object to a Module](https://wiki.genexus.com/commwiki/wiki?25548).

### [Step 2 - Creating the Module organization](#Step+2+-+Creating+the+Module+organization)

For each of the remaining Knowledge Bases:

* Open the old Knowledge Base and [export](https://wiki.genexus.com/commwiki/wiki?3942) all the [GeneXus objects](https://wiki.genexus.com/commwiki/wiki?1866) necessary. An .XPZ file will be created containing these objects.  
  This is a good opportunity to get rid of unused objects. It is recommended cleaning up the Knowledge Base before exporting its objects or exporting only used objects.
* Open the new Knowledge Base—where the merge is being performed—and create a new Module Object for containing the exported objects.
* [Import](https://wiki.genexus.com/commwiki/wiki?3179) the .XPZ file generated before in the Knowledge Base where the merge is being performed.
* Move all imported objects to the new [Module object](https://wiki.genexus.com/commwiki/wiki?22411)—read [HowTo: Add an object to a Module](https://wiki.genexus.com/commwiki/wiki?25548).

When this process is over, the Knowledge Base will have a new Module organization, where each [Module object](https://wiki.genexus.com/commwiki/wiki?22411) will contain all the [GeneXus objects](https://wiki.genexus.com/commwiki/wiki?1866) of every Knowledge Base that needed to be merged.

### [Step 3 - Defining Module Interfaces](#Step+3+-+Defining+Module+Interfaces)

After defining the Module organization, the process that will define each interface begins, since most of the Knowledge Bases being merged did not use the Modules feature. This process will determine how Modules should interact with one another.  
In defining the interface, you should bear in mind that its main purpose is to protect other Modules from the effects of the significant modification of objects, and the internal design decisions made in the Module, as well as to provide the services required.

See article [Modules - Defining an interface](https://wiki.genexus.com/commwiki/wiki?22584) for recommendations on how to define a Module interface. Also, read the article [Module - Parallel Transactions and Object Visibility](https://wiki.genexus.com/commwiki/wiki?25344) to better understand how parallel Transactions will behave when you use Modules.

### [Step 4 - Defining interaction between Modules](#Step+4+-+Defining+interaction+between+Modules)

To have things clearer, it is best to maintain the interaction between modules to the minimum. Use the [Module Diagram](https://wiki.genexus.com/commwiki/wiki?23922) for a clearer view of relationships between Modules, and then proceed to fine-tune the interaction.

### [Step 5 - Defining a Module organization for each new Module](#Step+5+-+Defining+a+Module+organization+for+each+new+Module)

Since most of the Knowledge Bases merged did not use the Modules feature, it is highly recommended that you arrange the inner structure to also use the Modules feature. In the future, this will help keep maintenance and development as simple and fast as possible. Below are the steps required to achieve that:

* If the Knowledge Base was organized using [Folder object](https://wiki.genexus.com/commwiki/wiki?9757)s, then an initial approach would be to convert those Folders into Modules — read [HowTo: Convert a Folder into a Module](https://wiki.genexus.com/commwiki/wiki?25231).
* Arrange objects by the type of service they provide, where the same 'type' should belong to the same Module.

### [Step 6 - Continuing development work](#Step+6+-+Continuing+development+work)

Done! Now your Knowledge Bases should be merged, so that you may continue developing new services. By using the Modules feature, you may increase your development speed while keeping maintenance simple.

### [See Also](#See+Also)

[HowTo: Start using Modules](https://wiki.genexus.com/commwiki/wiki?25610)


|  |
| --- |
| **Backlinks** |
| [HowTo: Start using Modules](https://wiki.genexus.com/commwiki/wiki?25610) | [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) |

---
