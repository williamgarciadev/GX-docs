---
title: "Redundant Formulas"
source_id: 5962
source_url: https://wiki.genexus.com/commwiki/wiki?5962
genexus_version: "18"
---

# Redundant Formulas

The fact that an attribute which is defined as a global formula is not stored in a table, sometimes can cause some performance troubles because evaluating it can take a long time.  As an example, suppose you have thousands of invoices, each of them with also thousands of lines. If you often need to print their total amount, and these amounts are calculated in runtime, then GeneXus will need to navigate thousands of records until showing the final result. This may represent a very high performance price.

In order to solve this situation, GeneXus allows us to define a global formula attribute as **redundant**.  Making this kind of definition, the formula attribute will not be a virtual attribute any more; in spite of this, the attribute will be stored in its associated table and GeneXus will keep the knowledge that the attribute is a formula and how to calculate it. Thus, in run time, when executing a transaction with a redundant formula, the formula will be evaluated, calculated **and its result will be stored in the database**; then, when referring to a redundant formula attribute in order to query it, GeneXus will obtain the stored value from the database instead of spending time carrying out the calculation.

In order to know how to define a Formula as redundant, see [Redundant property - Attribute](https://wiki.genexus.com/commwiki/wiki?6661).


|  |
| --- |
| **Backlinks** |
| [Examples of Using Formulas](https://wiki.genexus.com/commwiki/wiki?5882) | [Features of Reorganizations](https://wiki.genexus.com/commwiki/wiki?3154) | [Global Formulas](https://wiki.genexus.com/commwiki/wiki?6440) |
|

---
