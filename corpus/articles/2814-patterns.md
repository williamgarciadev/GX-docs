---
title: "Patterns"
source_id: 2814
source_url: https://wiki.genexus.com/commwiki/wiki?2814
genexus_version: "18"
---

# Patterns

When developing applications, you can note that some application parts are quite similar but not exactly the same. For example, in an application involving Customers and Products, it is only natural to have a Form to list Customers, and another Form to do the same for Products. Even though Customers and Products are totally different, these two Forms have many things in common: a grid, a fieldset to filter data, ordering, actions, etc.

This is called a "pattern" and has been a very popular topic in the software industry lately (see [What Is a Software Pattern](https://wiki.genexus.com/commwiki/wiki?1840,,) for more info).

These ideas are considered in GeneXus. So, what exactly is a pattern in GeneXus? And why is it useful? Before answering these questions, you must first address some of the limitations of patterns today:

* **Passive.** They exist only in books; the only way to use them is to read the books and use these ideas while coding.
* **At coding level.** Even though patterns are usually referenced as "Design Patterns", they are mainly aimed at helping with coding.

Since GeneXus works at knowledge level instead of coding level, patterns are used as a way to enable knowledge reuse, not just code reuse. So, GeneXus offers a framework for patterns whose design goals are as follows:

* **Active.** An "active" pattern isn't just a guideline; you can "instantiate" it (meaning that the framework generates all the GeneXus objects needed to implement a pattern instance). See the Pattern Instantiation concept.
* **Knowledge reuse.** GeneXus has always tried to encourage knowledge reuse, but with the use of patterns you can deliver a new level of knowledge reuse: the same knowledge can be reused in many different situations. For example, a "specialized pattern" can be instantiated to Products, but also to Menus.
* **Open.** Anyone can generate his/her own patterns (or modify an existing one).
* **Developer-friendly.** To use a pattern you don't need to be an expert in this area. (Note: If you also want to develop your own pattern, a deeper knowledge of the subject is needed).

GeneXus Patterns are the result of these efforts. This extension is included in the GeneXus IDE and if you define a new Pattern you will also view it as a new option in the GeneXus [IDE](https://wiki.genexus.com/commwiki/wiki?5272).  
The extension itself comes with a set of "built-in" patterns such as [Work With Patterns](https://wiki.genexus.com/commwiki/wiki?5636) and [others](https://wiki.genexus.com/commwiki/wiki?6491) so the developer can start using patterns without the need to develop a pattern him/herself.

The framework also helps developers create their own patterns.

After you define your Pattern structure the Pattern engine generates typed classes of your instances to use in the templates and in your custom code.

### [Why and When to Use a Pattern](#Why+and+When+to+Use+a+Pattern)

Going back to the question of why Patterns are useful for a GeneXus developer: a big boost in productivity and application quality is expected with the use of this tool. For example, a typical use scenario is when developers need to migrate a Knowledge Base from green screen or Windows forms to Web forms. In this case the [Work With Patterns](https://wiki.genexus.com/commwiki/wiki?5636) can be applied to generate most of the web objects needed for a nice-looking and user-friendly web application.

See [People And Organizations Knowledge Base](http://wiki.gxtechnical.com/commwiki/servlet/hwiki?People+And+Organizations+Knowledge+Base) for an example.

### [How Do Patterns Work?](#How+Do+Patterns+Work%3F)

Patterns are fully integrated into the GeneXus IDE. GeneXus has built-in [Work With](https://wiki.genexus.com/commwiki/wiki?5636) and [others](https://wiki.genexus.com/commwiki/wiki?6491).

The implementation is based on the built infrastructure to create defaults for each object part. Basically, this means that now you don't need to apply the pattern and import the result. When you change a property in the pattern definition, objects will automatically react to the change without the need to recreate them.

Every part of every object can have a default value. You can have default Web Panel forms, Web Panel events, etc. The default for each part can be different for each specific object. You can have a Web Panel with one template set as default for the form, and another with a different one.

The [Work With Patterns](https://wiki.genexus.com/commwiki/wiki?5636) implementation creates a set of empty objects with specific default templates set in each object. It creates a “WW<Transaction>" Web Panel with a default template that reads the transaction structure and creates a grid. This means that every time you add an attribute to the transaction, it will also be added to the Web Panel without the need to apply the pattern again.

### [Documentation](#Documentation)

* [Applying Patterns](https://wiki.genexus.com/commwiki/wiki?6551)
* [Dynamism between Transactions and Patterns](https://wiki.genexus.com/commwiki/wiki?6622)
* [Pattern settings](https://wiki.genexus.com/commwiki/wiki?6546)
* [Deleting Pattern Instances](https://wiki.genexus.com/commwiki/wiki?6492)
* [Built-in Patterns](https://wiki.genexus.com/commwiki/wiki?6491)
* [Working on large KBs and multiple Pattern instances](https://wiki.genexus.com/commwiki/wiki?11699,,)
* [Creating a New Pattern](https://wiki.genexus.com/commwiki/wiki?9689,,)
* [Creating a Fork of the Work With Pattern](https://wiki.genexus.com/commwiki/wiki?11971,,)
* [Debugging options for Patterns](https://wiki.genexus.com/commwiki/wiki?9551,,)
* [Patterns Gallery](http://marketplace.genexus.com/home.aspx?Patterns)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Using Patterns](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/using-patterns-6104753)


|  |
| --- |
| **Sub Categories** |
| [Category:Patterns preferences](https://wiki.genexus.com/commwiki/wiki?7118) |

---

|  |
| --- |
| **Pages** |
| [Applying Patterns](https://wiki.genexus.com/commwiki/wiki?6551) | [Built-in Patterns](https://wiki.genexus.com/commwiki/wiki?6491) | [Category Pattern](https://wiki.genexus.com/commwiki/wiki?5752,Category+Pattern,) |
| [Deleting Pattern Instances](https://wiki.genexus.com/commwiki/wiki?6492) | [Dynamism between Transactions and Patterns](https://wiki.genexus.com/commwiki/wiki?6622) | [HowTo: Create a New Pattern](https://wiki.genexus.com/commwiki/wiki?6496) |
| [HowTo: Install a Pattern in GeneXus](https://wiki.genexus.com/commwiki/wiki?13472) | [Patterns MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?12559) | [Setting the Category Pattern](https://wiki.genexus.com/commwiki/wiki?6499,Setting+the+Category+Pattern,) |
| [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) | [Work With for Web Selection Node](https://wiki.genexus.com/commwiki/wiki?5640) | [Work With for Web View node](https://wiki.genexus.com/commwiki/wiki?5646) |
| [Work With Patterns](https://wiki.genexus.com/commwiki/wiki?5636) |

---
