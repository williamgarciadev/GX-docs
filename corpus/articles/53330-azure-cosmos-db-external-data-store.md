---
title: "Azure Cosmos DB external data store"
source_id: 53330
source_url: https://wiki.genexus.com/commwiki/wiki?53330
genexus_version: "18"
---

# Azure Cosmos DB external data store

Azure Cosmos DB is accessed through an external [Data Store](https://wiki.genexus.com/commwiki/wiki?7117) of Service type.

**Summary**

* [Connection configuration](#Connection+configuration)

+ [Where to get the connection information](#Where+to+get+the+connection+information)

* [Data model](#Data+model)

+ [Scope](#Scope)
+ [Availability](#Availability)

## [Connection configuration](#Connection+configuration)

The configuration settings of the data store must be as follows:

* Data store provider: CosmosDB
* Server Name : The connection string for your Cosmos DB extracted from the azure portal.
* [Additional connection string attributes](https://wiki.genexus.com/commwiki/wiki?9037): It must include the following information separated by ";"  
    
  **Database**=<>;**ApplicationRegion**=<>

The Database and ApplicationRegion information is mandatory.

`[imagen omitida: wiki id 53648]`

The data store can be either created manually or by the [Cosmos DB Inspector](https://wiki.genexus.com/commwiki/wiki?53475).

### [Where to get the connection information](#Where+to+get+the+connection+information)

Go to the [Azure portal](http://portal.azure.com) and extract from there the connection string (to configure the *"Server name"* property of the data store).

`[imagen omitida: wiki id 53481]`

The ApplicationRegion can be extracted from here:

`[imagen omitida: wiki id 53483]`

## [Data model](#Data+model)

The data model can be created automatically by the [Cosmos DB Inspector](https://wiki.genexus.com/commwiki/wiki?53475), or you can create each transaction and its associated data view.

Given the Products transaction:

`[imagen omitida: wiki id 53331]`

Define a data view with the [Associated table property](https://wiki.genexus.com/commwiki/wiki?8063) = Products, and the [Datastore property](https://wiki.genexus.com/commwiki/wiki?8065) = <datastore defined previously>.

`[imagen omitida: wiki id 53332]`

Define the Service data store node:

`[imagen omitida: wiki id 53333]`

For each attribute, define the mapping at CosmosDB with its [External Name](https://wiki.genexus.com/commwiki/wiki?48445).

Important:

* The first attribute of the Primary Key must always be "id" because it should map with the [Item id](https://wiki.genexus.com/commwiki/wiki?53307).
* The second attribute of the PK, if it exists, will be taken as the [PartitionKey](https://wiki.genexus.com/commwiki/wiki?53307)

`[imagen omitida: wiki id 53334]`

The indexes defined in CosmosDB have to be mapped in the data view definition, as GeneXus uses that information at generation time.

**Important**: The indexes must have the Datastore of type service added at it's definition.

`[imagen omitida: wiki id 53346]`

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Availability](#Availability)

As since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853).


|  |
| --- |
| **Backlinks** |
| [Azure Cosmos DB execution errors](https://wiki.genexus.com/commwiki/wiki?53482) | [Toc:Cosmos DB](https://wiki.genexus.com/commwiki/wiki?53329) | [Cosmos DB Inspector](https://wiki.genexus.com/commwiki/wiki?53475) |
| [Getting Started with Cosmos DB](https://wiki.genexus.com/commwiki/wiki?53473) |

---
