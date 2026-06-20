---
title: "Attributes and Tables that can be Involved in Formulas"
source_id: 6490
source_url: https://wiki.genexus.com/commwiki/wiki?6490
genexus_version: "18"
---

# Attributes and Tables that can be Involved in Formulas

Every defined [formula](https://wiki.genexus.com/commwiki/wiki?5861) has a [base table](https://wiki.genexus.com/commwiki/wiki?6347), and some has a contextual table also. 

[horizontal formulas](https://wiki.genexus.com/commwiki/wiki?5864) not only have a base table (as do all formulas) but also have a **contexutal table**. For the formula be well defined, it is needed its base table belongs to the contextual extended table. Thus, you can include all the attributes you need as long as they belong to the formula base table and its [extended table](https://wiki.genexus.com/commwiki/wiki?6029).

[Aggregate Formulas](https://wiki.genexus.com/commwiki/wiki?5868) base table is the table to be navigated by the formula in order to make the calculation. Besides, the formula may be in a context where there is an instantiated table (the contextual table), which may or may not have some relationship with the formula base table.Thus, when you define an Aggregate Formula you can involve in its definition:

> - attributes that belong to the contextual base table and its extended table  
> - attributes that belong to the desired navigated table (base table) and its extended table

The **navigated table** in an Aggregate formula is inferred by GeneXus through the attributes mentioned in the formula, among those not belonging to the contextual base table and its extended. 

In general, as we said, in an Aggregate formula you can involve all the attributes you need as long as they belong to the formula contextual table and its extended table (because they are available when the formula is triggered). Besides, when you define the Aggregate formula, you know which must be the navigated table in order to make the calculation, so you can include in its definition all the attributes you need as long as they belong to the desired navigated table and its extended table.

If you define a formula using attributes that don't fullfil these rules, an error will be reported in the resulting navigation report at specification time.

### [Important note:](#Important+note%3A)

As of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,) we have changed the terminology. What we used to call formula base table, is now contextual table, and what we used to call navigated table is now formula base table.


|  |
| --- |
| **Backlinks** |
| [Find Formula](https://wiki.genexus.com/commwiki/wiki?6547) | [Toc:Formulas](https://wiki.genexus.com/commwiki/wiki?25327) |

---
