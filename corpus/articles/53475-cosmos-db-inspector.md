---
title: "Cosmos DB Inspector"
source_id: 53475
source_url: https://wiki.genexus.com/commwiki/wiki?53475
genexus_version: "18"
---

# Cosmos DB Inspector

Cosmos DB Inspector is a tool that allows inspecting a Cosmos DB and creating the [Azure Cosmos DB external data store](https://wiki.genexus.com/commwiki/wiki?53330) automatically, along with the transactions and data views needed to build your application.

It can be accessed through the menu **Tools > Application Integration > External Datastore Service Import**.

## [Configuration](#Configuration)

There, select Service Provider = CosmosDB.

`[imagen omitida: wiki id 53640]`

If you do not have defined an external datastore, use the NEW button to define it. The datastore has to be assigned to go on with the following steps.

In Service URI, enter the connection string.

The connection string is taken from the [Azure portal](http://portal.azure.com)

`[imagen omitida: wiki id 53481]`

At Connection Info, enter:

```
container=<>;Database=<>;ApplicationRegion=<>
```

The container is optional. If not set, all the containers of the database will be shown.

The Database and ApplicationRegion information is mandatory.

**Note**: To create a new data store automatically, click on the "New" button.

## [Index inspection](#Index+inspection)

CosmosDB inspector reads the Range and Composite indexes defined in the Cosmos DB settings of each container. See [Indexing policies in Azure CosmosDB](http://Indexing policies in Azure Cosmos DB).

GeneXus does not support the Indexing mode = None (it is ignored by the CosmosDB Inspector).

When a container is inspected, all the Range and Composite indexes are defined in the dataview associated with the Transaction (all except Blob or Binary fields are considered).  
  
The index definition is needed in order to use the Order clause. See [Cosmos DB error spc0116](https://wiki.genexus.com/commwiki/wiki?53484).

## [Considerations on Cosmos DB inspector](#Considerations+on+Cosmos+DB+inspector)

* As Cosmos DB is a [schema-less database](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/modeling-data), the inspector does its best effort to create the transaction attributes and infer their data types.
* It loops over a set of data items (by default 15 items) in the table and adds to the transaction definition all the attributes it finds, inferring their data types from the data itself.
* If you want to change the number of items to be read to infer the structure, use the *importItems* connection info. E.g.: importItems=20.
* The transaction and data view can be adjusted manually if necessary.
* Only single-level transactions are created.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Availability](#Availability)

As since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853).


|  |
| --- |
| **Backlinks** |
| [Azure Cosmos DB external data store](https://wiki.genexus.com/commwiki/wiki?53330) | [Toc:Cosmos DB](https://wiki.genexus.com/commwiki/wiki?53329) | [Cosmos DB indexes](https://wiki.genexus.com/commwiki/wiki?55180) |

---
