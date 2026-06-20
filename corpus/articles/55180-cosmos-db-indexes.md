---
title: "Cosmos DB indexes"
source_id: 55180
source_url: https://wiki.genexus.com/commwiki/wiki?55180
genexus_version: "18"
---

# Cosmos DB indexes

Taken from [Indexing policies in Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/index-policy):

*In Azure Cosmos DB, every container has an indexing policy that dictates how the container's items should be indexed.*

*The default indexing policy for newly created containers indexes every property of every item and enforces range indexes for any string or number.*

[Cosmos DB Inspector](https://wiki.genexus.com/commwiki/wiki?53475) reads the Range and Composite indexes defined at the Cosmos DB settings of each container.

When a container is inspected, all the Range and Composite indexes are defined in the dataview associated with the Transaction (all except Blob or Binary fields are considered).

GeneXus does not support the [Indexing mode](https://learn.microsoft.com/en-us/azure/cosmos-db/index-policy#indexing-mode) = None (it is ignored by the CosmosDB Inspector).

The index definition is needed in order to use the Order clause. See [Cosmos DB error spc0116](https://wiki.genexus.com/commwiki/wiki?53484).


|  |
| --- |
| **Backlinks** |
| [Toc:Cosmos DB](https://wiki.genexus.com/commwiki/wiki?53329) |

---
