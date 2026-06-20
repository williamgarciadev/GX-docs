---
title: "Getting Started with Cosmos DB"
source_id: 53473
source_url: https://wiki.genexus.com/commwiki/wiki?53473
genexus_version: "18"
---

# Getting Started with Cosmos DB

To get started using CosmosDB, create an Azure Cosmos DB account at the [azure portal](http://portal.azure.com).

Make sure to select Azure Cosmos DB for NoSQL.

`[imagen omitida: wiki id 53474]`

By the time being, GeneXus does not create the CosmosDB container or maintain its structure (ie. Index settings).

Go through the Data Explorer menu option and create a new container.

`[imagen omitida: wiki id 53477]`

Set the [PartitionKey](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview#choose-partitionkey) for this container and define any Unique Keys you need.

`[imagen omitida: wiki id 53479]`

Check the Indexing policy to see if it covers your needs.  
If the Partition Key is diferent than the "id" you need to define a composite index including both:

`[imagen omitida: wiki id 55235]`

The connection string data (needed to configure the [data store settings](https://wiki.genexus.com/commwiki/wiki?53330)) can be extracted from the Keys menu option.

`[imagen omitida: wiki id 53481]`


|  |
| --- |
| **Backlinks** |
| [Toc:Cosmos DB](https://wiki.genexus.com/commwiki/wiki?53329) |

---
