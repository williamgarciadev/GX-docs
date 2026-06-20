---
title: "Modules - Defining an interface"
source_id: 22584
source_url: https://wiki.genexus.com/commwiki/wiki?22584
genexus_version: "18"
---

# Modules - Defining an interface

When working on an application [Module](https://wiki.genexus.com/commwiki/wiki?22411) you should decide how it will be used by other modules. This is known as the Module's interface. It basically describes which module objects can be accessed by other modules.

A Module Interface is described by setting the value of the [Object Visibility property](https://wiki.genexus.com/commwiki/wiki?22473) of its objects.

* [Public object](https://wiki.genexus.com/commwiki/wiki?22589)s are part of the public interface, they can be accessed by any object of any module.
* [Private object](https://wiki.genexus.com/commwiki/wiki?22591)s are not part of any interface, they can only be accessed by objects in the same module (and its child objects).
* Internal objects can be accessed by objects that have the same root module (child of the one named 'Root Module')

### [Tips on how to defining the interface](#Tips+on+how+to+defining+the+interface)

An interface must be easy to use and to learn, and hard to misuse. It must be kept in mind that its main purpose is to expose a set of functionalities in order to satisfy a set of requirements. It is advised to be thought to keep it easy to read, maintain, and extend, the best way to doing so is keeping it simple.

* Use the [Module Interface Tab](https://wiki.genexus.com/commwiki/wiki?23935) to have a clearer vision of the interface.
* Keep it well documented, it is the 'face' of the [Module object](https://wiki.genexus.com/commwiki/wiki?22411), it should be easy to understand by anyone.
* Keep it simple, minimize changes. Keep in mind though that it will possibly change, therefore make changes as friendly as possible.
* Use decriptive names — for objects, methods, parameters, etc.  
  And consistently name them.
* The implementation details should not be exposed in the interface.

### [See also](#See+also)

* [Module Interface Tab](https://wiki.genexus.com/commwiki/wiki?23935)
* [Module Diagram Tab](https://wiki.genexus.com/commwiki/wiki?23922)


|  |
| --- |
| **Backlinks** |
| [HowTo: Merge two or more Knowledge Bases into one using Modules](https://wiki.genexus.com/commwiki/wiki?25613) | [HowTo: Start using Modules](https://wiki.genexus.com/commwiki/wiki?25610) | [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) |
| [Modules Distribution in GeneXus](https://wiki.genexus.com/commwiki/wiki?31376) | [Working with Modules](https://wiki.genexus.com/commwiki/wiki?25607) |

---
