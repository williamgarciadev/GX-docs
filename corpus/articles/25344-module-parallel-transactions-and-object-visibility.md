---
title: "Module - Parallel Transactions and Object Visibility"
source_id: 25344
source_url: https://wiki.genexus.com/commwiki/wiki?25344
genexus_version: "18"
---

# Module - Parallel Transactions and Object Visibility

As of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,) it is possible to work with [Module objects](https://wiki.genexus.com/commwiki/wiki?22414). This opens the possibility of defining [Parallel Transactions](https://wiki.genexus.com/commwiki/wiki?20209) in different Modules. This document explains the expected behavior when working with Parallel Transactions, and the effect of the [Object Visibility property](https://wiki.genexus.com/commwiki/wiki?22473) on accessing Attributes — this is also valid when working with one Transaction only.

The first thing to make clear is that the [Module objects](https://wiki.genexus.com/commwiki/wiki?22414) feature supports the definition of [Parallel Transactions](https://wiki.genexus.com/commwiki/wiki?20209).

**Note**: if different transactions with the same name but different primary key are defined, different tables will be created for each—the name of the tables created will add a number at the end to distinguish. For instance tables if we create two transactions called "Customer" with different primary key then tables: Customer and Customer1 will be created.

### [Object visibility of Attributes, Tables and Transactions](#Object+visibility+of+Attributes%2C+Tables+and+Transactions)

The granularity to which access to Data may be denied is a Table. This means it is not possible to have different Attributes of the same Table as Public and Private, since all attributes are either Public or Private.

Access to all Table Attributes will be denied if:

* The Object visibility property of **all** Parallel Transactions is set to *Private.*
* The attribute is used by an Object whose Module is different from all Parallel Transactions' Modules — and its child modules.

In other words, having just one Parallel Transaction defined with Object Visibility = Public will enable access to any of the attributes of the table for all objects in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

When access is denied, the specification will fail with the following error:

```
error: spc0209: Table '%1' cannot be accessed.
```

### [Example](#Example)

We will use the transactions' structure as defined in the following wiki document: [Parallel Transactions](https://wiki.genexus.com/commwiki/wiki?20209).  
And with the following Module organization:

#### 

#### [Example 1](#Example+1)

If all transactions — Company, Supplier and Client, have the Object Visibility property set to "Public", then all the attributes contained in the Company Table will be accessible from any object in the Knowledge Base.

#### [Example 2](#Example+2)

If all transactions — Company, Supplier and Client, have the Object Visibility property set to "Private", then all the attributes contained in the Company Table will be accessible **only** from objects in Modules "A" or "B" — and their child modules, if any. Access from the "C" or [Root module](https://wiki.genexus.com/commwiki/wiki?22439) will be denied.

#### [Example 3](#Example+3)

If **any** of the transactions — Company, Supplier or Client, has the Object Visibility property set to "Public", then all attributes contained in the Company Table will be accessible from any object in the Knowledge Base.

### [See Also](#See+Also)

[Parallel Transactions](https://wiki.genexus.com/commwiki/wiki?20209)

[Object Visibility property](https://wiki.genexus.com/commwiki/wiki?22473)


|  |
| --- |
| **Backlinks** |
| [HowTo: Merge two or more Knowledge Bases into one using Modules](https://wiki.genexus.com/commwiki/wiki?25613) | [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) |

---
