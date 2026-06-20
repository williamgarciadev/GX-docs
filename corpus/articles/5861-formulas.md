---
title: "Formulas"
source_id: 5861
source_url: https://wiki.genexus.com/commwiki/wiki?5861
genexus_version: "18"
---

# Formulas

Formulas are [expressions](https://wiki.genexus.com/commwiki/wiki?51320,,) that, once evaluated, return a certain value.

When an attribute or variable value can be calculated from other attributes, variables, constants, methods, arithmetic operations, etc., it can be defined as a **Formula**. In addition, when this assignment is done associated with an attribute definition (that is, for the attribute, inside the [Transaction Structure](https://wiki.genexus.com/commwiki/wiki?7661) where it is specified), the attribute itself is known as a [Global Formula](https://wiki.genexus.com/commwiki/wiki?6440).   
  
There are two ways to define formulas:

1. [Global Formulas](https://wiki.genexus.com/commwiki/wiki?6440) (Global definition, at the Knowledge Base level)
2. [Local / Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441) (Local definition, within objects' code)

### [Classification of Formulas by navigation type](#Classification+of+Formulas+by+navigation+type)

Formulas can be classified into three groups, depending on the type of calculation needed. This classification is valid either for global or local formulas.

* [Horizontal Formulas](https://wiki.genexus.com/commwiki/wiki?5864): Allow defining many kinds of expressions (such as arithmetic, among others) involving **a single** **record** and its associated [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029).
* [Aggregate Formulas](https://wiki.genexus.com/commwiki/wiki?5868): Allow defining some calculations or searches involving **many** **records** of a table (and its related data that belong to the [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029)).
* [Compound Formulas](https://wiki.genexus.com/commwiki/wiki?5879): Several Horizontal and/or Aggregate expressions combined.

All these kinds of formulas may have trigger conditions.

**Note**: When defining a formula, you don't need to indicate if it belongs to one classification or another. This is only an external classification.

### [Base table of a Formula](#Base+table+of+a+Formula)

The table that is **navigated** in order to evaluate the formula is known as its **base table**. Depending on the kind of formula, the evaluation will consider only one record (horizontal formula) or many (aggregate formula).

### [Optimized generated code](#Optimized+generated+code)

Defining formulas is even better than writing [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)s and invoking them.

When you define a formula, GeneXus has the knowledge of its definition and is able to generate optimized sentences by combining the formula query with the query in which the formula is present.

On the other hand, if you define a Procedure and invoke it, the Procedure code is not "visible" from the invoker, and GeneXus can't combine the knowledge and generate the most optimized code.

### [See Also](#See+Also)

[Formulas/Generating SQL](https://wiki.genexus.com/commwiki/wiki?3155)  
[Changes in Formulas terminology](https://wiki.genexus.com/commwiki/wiki?25367)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Defining Attributes as Formulas](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/defining-attributes-as-formulas-6104727)


|  |
| --- |
| **Pages** |
| [Aggregate Formulas](https://wiki.genexus.com/commwiki/wiki?5868) | [Attributes and Tables that can be Involved in Formulas](https://wiki.genexus.com/commwiki/wiki?6490) | [Changes in Formulas terminology](https://wiki.genexus.com/commwiki/wiki?25367) |
| [Compound Formulas](https://wiki.genexus.com/commwiki/wiki?5879) | [Data Selectors in Aggregations](https://wiki.genexus.com/commwiki/wiki?5432) | [Examples of Using Formulas](https://wiki.genexus.com/commwiki/wiki?5882) |
| [Find Formula](https://wiki.genexus.com/commwiki/wiki?6547) | [Formulas/Generating SQL](https://wiki.genexus.com/commwiki/wiki?3155) | [Global Formulas](https://wiki.genexus.com/commwiki/wiki?6440) |
| [Horizontal Formulas](https://wiki.genexus.com/commwiki/wiki?5864) | [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441) | [Inline Formulas outside a contextual table](https://wiki.genexus.com/commwiki/wiki?6442) |
| [Inline Formulas within a contextual table](https://wiki.genexus.com/commwiki/wiki?6426) | [Max, Min Formulas](https://wiki.genexus.com/commwiki/wiki?6502) | [Redundant Formulas](https://wiki.genexus.com/commwiki/wiki?5962) |
| [Sum, Count, Average formulas](https://wiki.genexus.com/commwiki/wiki?6500) |

---
