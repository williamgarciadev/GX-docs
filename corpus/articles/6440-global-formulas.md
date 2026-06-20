---
title: "Global Formulas"
source_id: 6440
source_url: https://wiki.genexus.com/commwiki/wiki?6440
genexus_version: "18"
---

# Global Formulas

A Global [Formula](https://wiki.genexus.com/commwiki/wiki?5861), also known as "formula attribute" is an attribute to which you can assign an associated calculation. Thus GeneXus has the knowledge to calculate the formula wherever the attribute is mentioned.

Only an attribute can be defined as a global formula (not a variable). Moreover, the only variables allowed inside the formula expression are those visible in all the KB, in every object, that is, system variables (such as &today).

Where do you define an attribute as a global formula? In the Transaction structure, when defining its name and data type. It is also possible to specify a formula with the Formula Editor. Look at the following image:

`[imagen omitida: wiki id 5863]`

The calculation itself, that is also known as **[formula](https://wiki.genexus.com/commwiki/wiki?5861)** itself, can be any [horizontal](https://wiki.genexus.com/commwiki/wiki?5864), [aggregate](https://wiki.genexus.com/commwiki/wiki?5868), or [compound](https://wiki.genexus.com/commwiki/wiki?5879) expression.

Global formula attributes are "**virtual attributes**" because they are not physically stored in a table by default (but you can change this if you want to, defining the attribute as [redundant](https://wiki.genexus.com/commwiki/wiki?5962)). In spite of this, for each object that references a global formula, GeneXus includes in its corresponding generated program the necessary code to calculate and display the result at runtime.

As it was said, global formula attributes aren't stored in a table. However, each global formula attribute has an associated table: the table that would belong to if it were not defined as a formula. In the above example, the associated table of *FlightInstancePrice* will be FLIGHTINSTANCE.

It represents the context of the formula. In other words, whenever the formula attribute is written, another attribute of the same table could have been written instead. That is, if the code is well programmed, at the moment the formula calculation triggers, you are positioned in a certain register of that table.

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [What are formulas?](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/what-are-formulas-v16?p=5361)  
`[imagen omitida: wiki id 20668]` [Inline formulas](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/inline-formulas-gx15?p=5253)


|  |
| --- |
| **Backlinks** |
| [Aggregate Formulas](https://wiki.genexus.com/commwiki/wiki?5868) | [Toc:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) | [Compound Formulas](https://wiki.genexus.com/commwiki/wiki?5879) |
| [Examples of Using Formulas](https://wiki.genexus.com/commwiki/wiki?5882) | [Expression data type](https://wiki.genexus.com/commwiki/wiki?6631) | [Find Formula](https://wiki.genexus.com/commwiki/wiki?6547) |
| [Category:Formulas](https://wiki.genexus.com/commwiki/wiki?5861) | [Toc:Formulas](https://wiki.genexus.com/commwiki/wiki?25327) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [GeneXus for SAP Systems First - Formulas](https://wiki.genexus.com/commwiki/wiki?34250) |
| [Horizontal Formulas](https://wiki.genexus.com/commwiki/wiki?5864) | [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441) | [Inline Formulas within a contextual table](https://wiki.genexus.com/commwiki/wiki?6426) | [Max, Min Formulas](https://wiki.genexus.com/commwiki/wiki?6502) |
| [Order clause](https://wiki.genexus.com/commwiki/wiki?6075) | [Redundant property - Attribute](https://wiki.genexus.com/commwiki/wiki?6661) | [SRC Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?38589) |
| [Stored attribute](https://wiki.genexus.com/commwiki/wiki?22501) | [Sum, Count, Average formulas](https://wiki.genexus.com/commwiki/wiki?6500) | [Udp method](https://wiki.genexus.com/commwiki/wiki?3964) | [Unique Clause](https://wiki.genexus.com/commwiki/wiki?24592) |
| [Unique clause in For Each command](https://wiki.genexus.com/commwiki/wiki?24593) |

---
