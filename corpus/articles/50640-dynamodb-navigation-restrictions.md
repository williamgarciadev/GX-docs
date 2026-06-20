---
title: "DynamoDB - Navigation restrictions"
source_id: 50640
source_url: https://wiki.genexus.com/commwiki/wiki?50640
genexus_version: "18"
---

# DynamoDB - Navigation restrictions

[DynamoDB](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50601,,) provides [Query](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html) and [Scan](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Scan.html) operations, for querying and browsing.

For each navigation, GeneXus uses the most appropriate operation.

Note that every navigation must have an order compatible with one of the table [indexes](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50601,,) (either the PK index or one of the Duplicate indexes). The PK index is associated with the [Primary Key](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50601,,) of the DynamoDB Table. Duplicate indexes are associated with the [Secondary Indexes](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50601,,) of the DynamoDB Table.

The first attribute of the index in the dataview is the Partition Key, and the second is the Range Key (if it exists).

To be able to sort, the [PartitionKey](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?50601,,) should also be instantiated (this is a DynamoDB requirement).

When sorting by [Primary Key](https://wiki.genexus.com/commwiki/wiki?1868), the specifier does not require the PartitionKey to be instantiated. However, if it is not instantiated, the result will NOT be sorted.

If the order cannot be resolved, the message [spc0116](https://wiki.genexus.com/commwiki/wiki?6433) will be displayed.

The web interface of any [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) usually offers navigation buttons to view the records (next, previous, last, first). With DynamoDB, it is not possible to sort the records if the PartitionKey is not instantiated. Therefore, these navigation buttons will not work properly by default because if the data is not sorted, the "next" record of a given record cannot be calculated correctly.

The filter conditions are evaluated in DynamoDB after running the Query but before returning the data. If the specifier determines that the condition cannot be evaluated in DynamoDB, it is marked with an exclamation mark (!) in the navigation diagram of the object. Lastly, the client evaluates whether each record meets the filter criteria, as in any other DBMS.


|  |
| --- |
| **Backlinks** |
| [Table of contents:DynamoDB](https://wiki.genexus.com/commwiki/wiki?50659) | [DynamoDB Support in GeneXus](https://wiki.genexus.com/commwiki/wiki?50498) | [Simple example with DynamoDB](https://wiki.genexus.com/commwiki/wiki?50607) |

---
