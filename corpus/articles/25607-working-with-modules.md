---
title: "Working with Modules"
source_id: 25607
source_url: https://wiki.genexus.com/commwiki/wiki?25607
genexus_version: "18"
---

# Working with Modules

The basis of the [Module](https://wiki.genexus.com/commwiki/wiki?22414) feature is explained here: [encapsulation](http://en.wikipedia.org/wiki/Encapsulation_%28object-oriented_programming%29). In other words, the purpose of [Modules](https://wiki.genexus.com/commwiki/wiki?22411)s is to make the process of designing applications easier by making it possible to organize a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) into different sections — [Module object](https://wiki.genexus.com/commwiki/wiki?22411)s — focused on providing a reduced series of highly specialized services. All such sections cooperate towards achieving a more complex service. This enables developers to focus on developing functionalities without the need to know about the rest of the application, nor its interactions. So, the [Module object](https://wiki.genexus.com/commwiki/wiki?22411) enables designers to break down a problem into two or more sub-problems of the same (or related) type. These sub-problems are simple enough to allow for a direct solution, which is then combined with the solutions to other sub-problems using the Interfaces defined to find the solution to the original problem.

During the development stage, [GeneXus objects](https://wiki.genexus.com/commwiki/wiki?1866) are most likely to change, making the design and definition of the right interface something essential to protect other [Modules](https://wiki.genexus.com/commwiki/wiki?22411) from those changes. It is highly recommended that following the definition of the group of objects belonging to the interface, changes made in them be kept at a minimum. This ensures that maintenance and development will be as simple and fast as possible.

A [Module](https://wiki.genexus.com/commwiki/wiki?22411)’s interface may be defined using the [Object Visibility property](https://wiki.genexus.com/commwiki/wiki?22473) — read [Modules - Defining an interface](https://wiki.genexus.com/commwiki/wiki?22584) for further information. Then, the interface may be examined using the [Module Interface Tab](https://wiki.genexus.com/commwiki/wiki?23935).

As development continues and services become available, the interaction between Modules begins. More often than not, it is not easy to see how [Modules](https://wiki.genexus.com/commwiki/wiki?22411) interact with one another. To make this task easier, we could define Diagrams showing the relationships between Modules — read [Module Diagram Tab](https://wiki.genexus.com/commwiki/wiki?23922).

By knowing these interactions, designers can fine-tune interfaces and create a more efficient and understandable solution, in addition to making an early diagnosis regarding the possible misuse of services.

The Module feature will not change the way in which objects are called or used when defined in the [Root module](https://wiki.genexus.com/commwiki/wiki?22439), nor the generated code when no module is defined. However, when objects belong to a Module, we must consider the following:

* [Modules - Grammar](https://wiki.genexus.com/commwiki/wiki?25609)
* [How are partially qualified object names resolved](https://wiki.genexus.com/commwiki/wiki?22438)
* [Modules - URL Syntax](https://wiki.genexus.com/commwiki/wiki?25224)
* [Modules - Dynamic calls](https://wiki.genexus.com/commwiki/wiki?22585)
* [Modules - GAM Integration](https://wiki.genexus.com/commwiki/wiki?25570)
* [Modules - GXflow integration](https://wiki.genexus.com/commwiki/wiki?25597,,)

### [See Also](#See+Also)

[Module Interface Tab](https://wiki.genexus.com/commwiki/wiki?23935)  
[Module Diagram Tab](https://wiki.genexus.com/commwiki/wiki?23922)  
[Modules - Defining an interface](https://wiki.genexus.com/commwiki/wiki?22584)  
[Modules - Object names](https://wiki.genexus.com/commwiki/wiki?22483)


|  |
| --- |
| **Backlinks** |
| [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) |

---
