---
title: "Azure Cosmos DB execution errors"
source_id: 53482
source_url: https://wiki.genexus.com/commwiki/wiki?53482
genexus_version: "18"
---

# Azure Cosmos DB execution errors

The following is a table that helps troubleshooting some errors that can be thrown when using Azure Cosmos DB.

|  |  |  |
| --- | --- | --- |
| Error | **Explain** | **Details/Actions** |
| CosmosDB Execution failed. Status code:  BadRequest. Message: Response status code does not indicate success:  BadRequest(400);  Reason:(Message:{"Errors":["The order by query does not have a corresponding index that it can be served from."]} | "Order by" is supported only if it exists an index. See [here](https://learn.microsoft.com/en-us/azure/cosmos-db/index-overview). | GeneXus infers an index to be used, according to what is explained in [Order clause](https://wiki.genexus.com/commwiki/wiki?6075).  You can see at the [Navigation report](https://wiki.genexus.com/commwiki/wiki?7178) which is the index to be taken.  Create the index at Cosmos DB to avoid the error ([ref](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/how-to-manage-indexing-policy?tabs=dotnetv3%2Cpythonv3)) |
| ApplicationRegion configuration '' is not a valid Azure region or the current SDK version does not recognize it. | The ApplicationRegion must be specified at the connection string. | See [Azure Cosmos DB external data store](https://wiki.genexus.com/commwiki/wiki?53330). |
| NotFound (404);  Reason: (Message: {"Errors":["Owner resource does not exist"]} | The connection string is not valid, either the database or the container does not exist. |  |
| CosmosDB Execution failed. Status code: NotFound.  Message: Response status code does not indicate success: NotFound (404); Reason:(Message:{"Errors":["Resource Not Found.Learn more:https:\/\/aka.ms\/cosmosdb-tsg-not-found"]} | The container was not found. |  |
| Status code: BadRequest. BadRequest (400);  Message: {"Errors":["PartitionKey extracted from document doesn't match the one specified in the header. Learn more: https:\/\/aka.ms\/CosmosDB\/sql\/errors\/wrong-pk-value"]} | The [PartitionKey](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview#choose-partitionkey) taken for the requests does not match with the PartitionKey defined at the container. | The Partition Key taken for each request is the second attribute of the Primary Key (if it's a composite PK), otherwise, the first attribute is taken.  In this last case, the [id](https://wiki.genexus.com/commwiki/wiki?53307) is equal to the PartitionKey. |
| Partitionkey can be double, bool or string. | Azure CosmosDB supports double, bool or string partition keys only. By now NET generator does not support double data type for the partition key. |  |


|  |
| --- |
| **Backlinks** |
| [Toc:Cosmos DB](https://wiki.genexus.com/commwiki/wiki?53329) |

---
