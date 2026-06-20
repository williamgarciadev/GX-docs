---
title: "Modules vs. Folders"
source_id: 22470
source_url: https://wiki.genexus.com/commwiki/wiki?22470
genexus_version: "18"
---

# Modules vs. Folders

[Module Objects](https://wiki.genexus.com/commwiki/wiki?22414) and [Folder object](https://wiki.genexus.com/commwiki/wiki?9757)s are used to organize objects in a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836). Together, they create a hierarchy tree whose root is the [Root module](https://wiki.genexus.com/commwiki/wiki?22439). The hierarchy is shown in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210). There are, however, conceptual differences between Modules and Folders.

`[imagen omitida: wiki id 32330]`

A Module is a GeneXus object designed to make it easier to understand, maintain and integrate a Knowledge Base.

• Understanding: Using Modules, developers can model how they logically break down a large, Enterprise wide, Knowledge Base.  
• Maintenance: Modules can be used to clearly define how its functionality must be used and hide how it is implemented.  
• Integration: Using Modules, developers can focus on their area of expertise and seamlessly interact with other modules

The use of modules does not change the data model.

* Modules are part of the [Qualified Name property](https://wiki.genexus.com/commwiki/wiki?22477), Folders are not.

This allows different objects to have the same [Name property](https://wiki.genexus.com/commwiki/wiki?6985) value if they are in different Modules.

* Modules may have child Folders but Folders cannot have child Modules

### [How to decide whether to use a Folder or a Module](#How+to+decide+whether+to+use+a+Folder+or+a+Module)

Use Modules for [encapsulation](http://en.wikipedia.org/wiki/Encapsulation_%28object-oriented_programming%29). Use Folders for organization within Modules.


|  |
| --- |
| **Backlinks** |
| [Category:Folder object](https://wiki.genexus.com/commwiki/wiki?9757) | [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) | [Object Visibility property](https://wiki.genexus.com/commwiki/wiki?22473) |

---
