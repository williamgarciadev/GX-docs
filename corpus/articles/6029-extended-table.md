---
title: "Extended Table"
source_id: 6029
source_url: https://wiki.genexus.com/commwiki/wiki?6029
genexus_version: "18"
---

# Extended Table

The **extended table** of a given [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) is a virtual table composed of the **base table** itself plus all the tables that have N-1 relationships, either directly or indirectly, starting from the given **base table**.

For example, consider the following Bachman Diagram:

`[imagen omitida: wiki id 6030]`

* The INVOICE **base table** will have the following **extended table**: {INVOICE, CUSTOMER, COUNTRY}
* The CUSTOMER **base table** will have the following **extended table**: {CUSTOMER, COUNTRY}
* The COUNTRY **base table** will have the following **extended table**: {COUNTRY}

The INVOICE **extended table**includes not only its own data but also data from the CUSTOMER and COUNTRY tables. This is because, starting from the INVOICE table (**base table**), there is an N-1 relationship with the CUSTOMER table; and starting from the CUSTOMER table, there is an N-1 relationship with the COUNTRY table. Note that if you take one record from INVOICE, you find only one record from CUSTOMER related to it (and no more than one); and if you take one record from CUSTOMER, you find only one record from COUNTRY related to it (and no more than one).

Following the same reasoning, the CUSTOMER **extended table** includes not only its own data but also data from the COUNTRY table. This is because, starting from the CUSTOMER table (**base table**) there is an N-1 relationship with the COUNTRY table. Note that if you take one record from CUSTOMER, you find only one record from COUNTRY related to it (and no more than one).

The COUNTRY **extended table** contains only itself. This is because, starting from it, there is no N-1 relationship either directly or indirectly.

The **extended table** concept simplifies access to multiple tables when working from a specific [Base Table](https://wiki.genexus.com/commwiki/wiki?6347).

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Base and Extended table](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/base-and-extended-table)


|  |
| --- |
| **Backlinks** |
| [Attributes and Tables that can be Involved in Formulas](https://wiki.genexus.com/commwiki/wiki?6490) | [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) | [Base Transaction clause](https://wiki.genexus.com/commwiki/wiki?25418) |
| [Business Component variables properties](https://wiki.genexus.com/commwiki/wiki?2276) | [Conditions property](https://wiki.genexus.com/commwiki/wiki?9763) | [Conditions property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55966) | [Data Selectors in For each command](https://wiki.genexus.com/commwiki/wiki?5312) |
| [Determining the Base Table for each Grid in a Web Panel](https://wiki.genexus.com/commwiki/wiki?6105) | [Example: New Command](https://wiki.genexus.com/commwiki/wiki?6742) | [Category:Formulas](https://wiki.genexus.com/commwiki/wiki?5861) | [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
| [Horizontal Formulas](https://wiki.genexus.com/commwiki/wiki?5864) | [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441) | [Inline Formulas outside a contextual table](https://wiki.genexus.com/commwiki/wiki?6442) | [Load event](https://wiki.genexus.com/commwiki/wiki?8188) |
| [Macroservices and Miniservices systems](https://wiki.genexus.com/commwiki/wiki?55518) | [Microservices systems](https://wiki.genexus.com/commwiki/wiki?55526) | [Monolithic systems](https://wiki.genexus.com/commwiki/wiki?55516) | [Nested For each commands to implement a Control Break](https://wiki.genexus.com/commwiki/wiki?30878) |
| [New command](https://wiki.genexus.com/commwiki/wiki?6714) | [Null function](https://wiki.genexus.com/commwiki/wiki?8421) | [Offline Database Object conditions](https://wiki.genexus.com/commwiki/wiki?23570) | [Rules in Transactions](https://wiki.genexus.com/commwiki/wiki?8213) |
| [Category:Subtype Group object](https://wiki.genexus.com/commwiki/wiki?20206) | [Udp method](https://wiki.genexus.com/commwiki/wiki?3964) | [Unique Clause](https://wiki.genexus.com/commwiki/wiki?24592) |
| [Unique Clause (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57977) | [Update rule](https://wiki.genexus.com/commwiki/wiki?21430) | [Where clause](https://wiki.genexus.com/commwiki/wiki?8578) |

---
