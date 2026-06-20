---
title: "Object Visibility property"
source_id: 22473
source_url: https://wiki.genexus.com/commwiki/wiki?22473
genexus_version: "18"
---

# Object Visibility property

Defines whether objects in other Modules can access the object. It can be specified either at the Module or object level.

Setting a value at the Module level changes the default value for all objects in the Module.

### [Values](#Values)

|  |  |
| --- | --- |
| **Public** | Any object in any module can access a public object. |
| **Private** | Only objects in the same module (and its child modules) can access private objects. |
| **Internal** | Only objects that have a common root module (child of the one named 'Root Module') can access internal objects |

The default value for a given object is inherited from its parent [Module object](https://wiki.genexus.com/commwiki/wiki?22414).

### [Description](#Description)

One goal, when designing a [Module object](https://wiki.genexus.com/commwiki/wiki?22414), is to define how it is going to be used (i.e. how other modules can interact with the one that is being defined). Some Module objects may be accessed elsewhere in the Knowledge Base and some may not.

By setting the appropriate value of the Object visibility property a developer can control how each object can be accessed outside its Module, that is, design the Module interface.

### [Example](#Example)

Root Module  
|-- ProcRoot  
|-- ModuleA  
|--  |-- ProcA  
|--  |-- ModuleA1  
|--  |    |-- ProcA1 //Public  
|--  |    |-- ModuleA11  
|--  |         |-- ProcA11\_Internal //Internal  
|--  |         |-- ProcA11\_Private // Private  
|--  |-- ModuleA2  
|--       |-- ProcA2

In this example

* ProcRoot can call ProcA1. It cannot call ProcA11\_Internal and ProcA11\_Private
* ProcA, ProcA1 and ProcA2 can call ProcA11\_Internal. They cannot call ProcA11\_Private
* ProcA11\_Internal can call ProcA11\_Private
* When [packaging](https://wiki.genexus.com/commwiki/wiki?31376) ModuleA1, only ProcA1 is part of its interface.

### [How to apply changes](#How+to+apply+changes)

When an object's visibility is changed, all the objects that have references to it are automatically specified by the next Build operation. They may not need to be generated.

### [Availability](#Availability)

This property is available as of [GeneXus Tilo Beta 1](https://wiki.genexus.com/commwiki/wiki?22217,,).  
The value 'Internal' is available as of [GeneXus 15 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?33278,,)

### [See also](#See+also)

[Modules](https://wiki.genexus.com/commwiki/wiki?22414)  
[Modules vs. Folders](https://wiki.genexus.com/commwiki/wiki?22470)  
[Modules - Dynamic calls](https://wiki.genexus.com/commwiki/wiki?22585)


|  |
| --- |
| **Backlinks** |
| [Category:API object](https://wiki.genexus.com/commwiki/wiki?46151) | [External Object: Java Session Bean](https://wiki.genexus.com/commwiki/wiki?6197) | [External Object: Native Object](https://wiki.genexus.com/commwiki/wiki?6148) |
| [External Object: Native Object (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?56447) | [External Object: Stored Procedure](https://wiki.genexus.com/commwiki/wiki?6138) | [External Object: WSDL - Web Service](https://wiki.genexus.com/commwiki/wiki?6154) |
| [HowTo: Add an object to a Module](https://wiki.genexus.com/commwiki/wiki?25548) | [IDE Icon overlay](https://wiki.genexus.com/commwiki/wiki?17803) | [Category:Menu object](https://wiki.genexus.com/commwiki/wiki?16321) | [Module - Parallel Transactions and Object Visibility](https://wiki.genexus.com/commwiki/wiki?25344) |
| [Module Diagram Tab](https://wiki.genexus.com/commwiki/wiki?23922) | [Module Interface Tab](https://wiki.genexus.com/commwiki/wiki?23935) | [Category:Module object](https://wiki.genexus.com/commwiki/wiki?22411) | [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) |
| [Modules - Defining an interface](https://wiki.genexus.com/commwiki/wiki?22584) | [Modules - Dynamic calls](https://wiki.genexus.com/commwiki/wiki?22585) | [Modules Distribution in GeneXus](https://wiki.genexus.com/commwiki/wiki?31376) | [Package Module with database access for Solutions extensibility scenarios](https://wiki.genexus.com/commwiki/wiki?42900) |
| [Private object](https://wiki.genexus.com/commwiki/wiki?22591) | [Public object](https://wiki.genexus.com/commwiki/wiki?22589) | [Query Object Properties](https://wiki.genexus.com/commwiki/wiki?18471) |
| [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) | [Working with Modules](https://wiki.genexus.com/commwiki/wiki?25607) |

---
