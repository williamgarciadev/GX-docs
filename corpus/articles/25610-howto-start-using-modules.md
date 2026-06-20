---
title: "HowTo: Start using Modules"
source_id: 25610
source_url: https://wiki.genexus.com/commwiki/wiki?25610
genexus_version: "18"
---

# HowTo: Start using Modules

The purpose of this article is to explain the necessary steps to work with Modules.

### [Step 1 - Defining Modules](#Step+1+-+Defining+Modules)

The first step is to break down the problem into simpler sub-problems. Defining a [Module object](https://wiki.genexus.com/commwiki/wiki?22411) for each one of them, as explained in the article [HowTo: Create a Module Object](https://wiki.genexus.com/commwiki/wiki?25541), can be useful the first time you use the [Module object](https://wiki.genexus.com/commwiki/wiki?22411). The newly created [Module object](https://wiki.genexus.com/commwiki/wiki?22411)s may, in turn, be broken down into simpler sub-problems, and so on.  
This will create a Module hierarchy or organization.

**Tip:** The best way to break down a problem is to search for groups of similar requirements and arrange them into Modules. For example, Modules may be used to solve a set of business operations with conceptual cohesion.

### [Step 2 - Defining Module Interfaces](#Step+2+-+Defining+Module+Interfaces)

Following the definition of our Module organization, the process that defines each interface begins. In most cases, this may also be done further ahead. However, the sooner it’s done, the better. This process will define how Modules should interact in relation to one another.  
It should be kept in mind that the main purpose of the interface is to protect other Modules from the effects of the significant modification of objects, and the internal design decisions made to the Module, as well as to provide the services required.

See [Modules - Defining an interface](https://wiki.genexus.com/commwiki/wiki?22584).

### [Step 3 - Defining interactions between Modules](#Step+3+-+Defining+interactions+between+Modules)

To have things clearer, it is best to maintain the interaction between modules as minimum as possible. Use the [Module Diagram](https://wiki.genexus.com/commwiki/wiki?23922) for a clearer view of relationships between Modules, and then proceed to fine-tune the interaction.

### [Step 4 - Starting development](#Step+4+-+Starting+development)

Having defined the interaction, the interfaces, and the module structures, the development process may then begin.

### [See Also](#See+Also)

[HowTo: Merge two or more Knowledge Bases into one using Modules](https://wiki.genexus.com/commwiki/wiki?25613)


|  |
| --- |
| **Backlinks** |
| [HowTo: Merge two or more Knowledge Bases into one using Modules](https://wiki.genexus.com/commwiki/wiki?25613) | [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) |

---
