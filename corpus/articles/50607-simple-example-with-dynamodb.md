---
title: "Simple example with DynamoDB"
source_id: 50607
source_url: https://wiki.genexus.com/commwiki/wiki?50607
genexus_version: "18"
---

# Simple example with DynamoDB

Consider the following Table defined using [NoSQL Workbench](https://wiki.genexus.com/commwiki/wiki?50641,,).

`[imagen omitida: wiki id 50608]`

The Customer table has 3 elements.

Id is the simple primary key.

First, you need to export the data from NoSQL Workbench.

Next, [import the data into GeneXus](https://wiki.genexus.com/commwiki/wiki?50498).

Once the import process of the storage service is complete, the Customer Transaction is created.

`[imagen omitida: wiki id 50609]`

As you can see in the image:

* GeneXus takes care of applying the naming rules to the attributes. They all start with the name Customer followed by the subject category.
* The data types are converted to the most appropriate ones. If you wish, you can modify data types. For example: define CustomerTimestap of [DateTime type](https://wiki.genexus.com/commwiki/wiki?7370) and CustomerAccount as [Email](https://wiki.genexus.com/commwiki/wiki?14650). You can even define your own Domains.

When you [run it](https://wiki.genexus.com/commwiki/wiki?5692), the impact analysis will show a [warning](https://wiki.genexus.com/commwiki/wiki?47288) of type [spc0116](https://wiki.genexus.com/commwiki/wiki?6433) (read about the [restrictions](https://wiki.genexus.com/commwiki/wiki?50640) for more details). Consequently, in the form the data is not sorted by Primary Key.

`[imagen omitida: wiki id 50610]`

When you click on Susan, for example, you will be able to see all her data and make updates if you need to. Any changes you make to the data will be reflected in DynamoDB.

Also, if you enter a new customer it is automatically saved in DynamoDB.

`[imagen omitida: wiki id 50611]`

In the above image, you can see that Susan's Service was updated and the customer Jake was entered into the DynamoDB Database.

You can freely define queries that can be executed not only by executing the Transactions’ forms but also by making reference to them as [Base Transaction](https://wiki.genexus.com/commwiki/wiki?25418) in [For Each commands](https://wiki.genexus.com/commwiki/wiki?24744), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270). In addition, it is possible to apply the Work With [Patterns](https://wiki.genexus.com/commwiki/wiki?2814) to the generated Transactions. Furthermore, the Transactions’ attributes can be used as regular attributes in Printblocks, Conditions, etc., in a transparent way.

**Note:** Due to restrictions of DynamoDB queries and the way GeneXus interacts with it, it is not possible to add an order when the [partition key](https://wiki.genexus.com/commwiki/wiki?50601,,) is not instantiated.


|  |
| --- |
| **Backlinks** |
| [Toc:DynamoDB](https://wiki.genexus.com/commwiki/wiki?50659) | [DynamoDB Support in GeneXus](https://wiki.genexus.com/commwiki/wiki?50498) |

---
