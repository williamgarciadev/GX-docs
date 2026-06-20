---
title: "Data View object"
source_id: 1914
source_url: https://wiki.genexus.com/commwiki/wiki?1914
genexus_version: "18"
---

# Data View object

Defines all the information related to an external table to access it like any other table created by GeneXus.

As you all know, upon defining [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s, tables are created in the database that is associated with an Environment. In some cases, you may need to work with existing tables that are not included in our data model, and which are called "external tables." They may belong to another model or version, or they may not be created by GeneXus.

Even though GeneXus cannot reorganize these tables, it can query them and make additions, deletions, and changes.

There are two ways to work with an external table: with an associated Transaction to make additions, deletions, and changes to this table, or without an associated Transaction. In this case, these operations can only be made through [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)s, and not with the usual commands but with others. The most common reasons for which Data Views are defined without an associated Transaction are when it's necessary to access an external table that has no indexes, or when it's necessary to access external tables, only once, just to define load processes (that is, batch processes that run through external tables and load tables of the Environment). Clearly, in these cases, it's not necessary to have interactive access to the external tables, but only through batch load processes; and lastly, another reason to do so is when you don't need this file to participate in the data model normalization.

### [Note](#Note)

Data Views do not necessarily handle a table that belongs to a database; even though it happens most of the time, it can also be a text file or another type of file.


|  |
| --- |
| **Pages** |
| [Associated table property (in Data Views)](https://wiki.genexus.com/commwiki/wiki?8063) | [Data View Composition](https://wiki.genexus.com/commwiki/wiki?9494) | [Data View concepts](https://wiki.genexus.com/commwiki/wiki?9467) |
| [Data View Index Information](https://wiki.genexus.com/commwiki/wiki?9496) | [Datastore property](https://wiki.genexus.com/commwiki/wiki?8065) | [Location property](https://wiki.genexus.com/commwiki/wiki?7956) |
| [Record Format Property](https://wiki.genexus.com/commwiki/wiki?9468,Record+Format+Property,) | [Schema Name Property](https://wiki.genexus.com/commwiki/wiki?9471,Schema+Name+Property,) | [Use external name property](https://wiki.genexus.com/commwiki/wiki?9465,Use+external+name+property,) |
| [Xfor First command](https://wiki.genexus.com/commwiki/wiki?8601) | [Xnew command](https://wiki.genexus.com/commwiki/wiki?8640) |

---
