---
title: "Order clause"
source_id: 6075
source_url: https://wiki.genexus.com/commwiki/wiki?6075
genexus_version: "18"
---

# Order clause

Indicates the order in which the query will be returned. It applies to [For Each command](https://wiki.genexus.com/commwiki/wiki?24744), [Data provider groups](https://wiki.genexus.com/commwiki/wiki?25082), [Data Selectors](https://wiki.genexus.com/commwiki/wiki?5271) and [grids](https://wiki.genexus.com/commwiki/wiki?24817).

### [Syntax](#Syntax)

**order** <*att1*>, ..., <*attN***>** [ **when** *<Condition>*] | {**order none** [ **when** *<Condition>*]...

**Where:**

*att1*, ..., *attN*

It is a list of attributes separated by a comma; each mentioned attribute must be a knowledge base attribute that may be written with or without round brackets. When an order attribute appears between round brackets, it indicates a descending order for this attribute.

Here you can mention extended table attributes and [formula attributes](https://wiki.genexus.com/commwiki/wiki?6440). However, if you're working in a centralized platform you can only use the attributes stored in the for each [Base Table](https://wiki.genexus.com/commwiki/wiki?6347). Formula attributes need to be evaluated in the server.

*Condition*

For centralized platforms, you can specify one order clause at the most, with no condition ('when'). For client/server platforms, you can define **several conditional order clauses**, and **one unconditional order clause**, which should be the last one listed; the reason for this is that as only one of these order clauses will take effect, their conditions (the when conditions) are evaluated one by one until the first True one is reached, which is the one that will be chosen. If none of them are found to be True and there is an unconditional clause (that is, one without a 'when'), the order taken will be that of the unconditional clause. If there is no such clause, the order will be **undefined**, which means that it will depend on the platform, and it may even vary from one execution to the next. The reason for writing conditional order clauses is motivated by query optimization.

**[order none](https://wiki.genexus.com/commwiki/wiki?8619)**

For cases in which you are not interested in a particular order and want it to remain undefined.

### [Do Order clauses determine the exact order really used by the DBMS in order to solve the query?](#Do+Order+clauses+determine+the+exact+order+really+used+by+the+DBMS+in+order+to+solve+the+query%3F)

The final order that will be generated could be slightly different from that specified by the user because other considerations are taken into account by the GeneXus Specifier in order to optimize the database access.

Basically, the following information is considered to **generate** the order clause (the low level specification in the code):

* **Attributes** of the order clause specified by the user.
* **Restrictions** that apply to the level: attributes instanced by parameter, attributes instanced in the context (such as higher level for eachs, groups, grids), explicit conditions (such as 'where' conditions when for eachs or groups, or 'conditions' properties when grids or data selectors or 'conditions' selector when general conditions).
* Existence of **indexes** on such attributes.

In summary, with the order clause, you indicate the order in which you want the records to be processed and retrieved, and they will. But to perform the actual processing, the Specifier could alter that clause, supplemented with contextual info (if there exists defined indexes, conditions for equality, etc) in order to be more performant, although DBMS itself ends up being the one who decides the execution plan. Nevertheless, it is important to understand the data will be retrieved in the explicit order. See the [Order Clause Specification](https://wiki.genexus.com/commwiki/wiki?5100) for more details.

### [Centralized Platforms](#Centralized+Platforms)

The above considerations do not necessarily apply to centralized platforms. In those cases, GeneXus searches for an index in the level's base table considering the attribute list. If it does not exist, a temporary index will be created every time the program is executed. As temporary index creation may be too slow in some cases, this is when the creation of a [user index](https://wiki.genexus.com/commwiki/wiki?7121) is recommended.

If no order is specified:

* If level is nested into another level: GeneXus will try to find the index that matches all outer orders, optimizing performance.
* Otherwise: the Primary Key of the Base Table will be chosen.

**Note**: Since [GeneXus X Evolution 3 Help](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22413,,), the keyword "order" cannot be ommited in the order clause. See [Base Transaction in For Each command](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?23945,,) for more information.

### [See Also](#See+Also)

[Support of Expressions in the Order clause](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59224,,) (Since GeneXus Next)


|  |
| --- |
| **Backlinks** |
| [Azure Cosmos DB execution errors](https://wiki.genexus.com/commwiki/wiki?53482) | [Cosmos DB error spc0116](https://wiki.genexus.com/commwiki/wiki?53484) |
| [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) | [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
| [Nested For Each commands to implement a Control Break](https://wiki.genexus.com/commwiki/wiki?30878) | [Order Clause Specification](https://wiki.genexus.com/commwiki/wiki?5100) | [Order None clause](https://wiki.genexus.com/commwiki/wiki?8619) | [Order property](https://wiki.genexus.com/commwiki/wiki?9842) |
| [Order rule](https://wiki.genexus.com/commwiki/wiki?8256) | [Orders property](https://wiki.genexus.com/commwiki/wiki?25472) | [Orders property (GeneXus 18 upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55997) | [When clause](https://wiki.genexus.com/commwiki/wiki?8629) |
| [Where clause](https://wiki.genexus.com/commwiki/wiki?8578) |

---
