---
title: "Microservices systems"
source_id: 55526
source_url: https://wiki.genexus.com/commwiki/wiki?55526
genexus_version: "18"
---

# Microservices systems

A microservices system in GeneXus is implemented with several [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)s, more precisely, with as many Knowledge Bases as subsystems are needed.

In addition, there will be several databases.

This architecture has some variations in which databases will be consistent or eventually consistent.

## [1. Implementation with consistent databases](#1.+Implementation+with+consistent+databases)

N Knowledge Bases are created (one for each subsystem) and each one will have its own tables.

The tables can be in a single database instance and in separate schemas, and there is no replication of tables. This means, for example, that if you have a customers/billing subsystem and a staff/employees subsystem, there will be two KBs, each one with its own database containing its own tables (and the customer table will be only in the database related to the customers/billing KB).

There is data consistency (for both saving and reading).

From one subsystem that is in a KB, it must be possible to access the data of another subsystem that is in another KB.

### [Options for accessing the data of one subsystem from another subsystem](#Options+for+accessing+the+data+of+one+subsystem+from+another+subsystem)

**1)** It is possible to export [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s from KBN to KB1 (through the [Export](https://wiki.genexus.com/commwiki/wiki?3942) and [Import](https://wiki.genexus.com/commwiki/wiki?3179) options offered in the [Knowledge Manager](https://wiki.genexus.com/commwiki/wiki?5679) option of GeneXus’ main menu).

In the KB1 you have to define [Data View object](https://wiki.genexus.com/commwiki/wiki?1914)s related to the imported Transactions. In this way, the Transactions imported into KB1 do not create physical tables in the database associated with KB1, but access the tables of the KBN database instead. In KB1 it is possible to use the imported Transactions as usual, including their attributes in any object (the generated programs will access the external tables of the KBN database). This allows reading and saving data in the tables of the subsystem corresponding to KBN from KB1.

`[imagen omitida: wiki id 55548]`

**2)** The second alternative to access data from one subsystem to another is to work with modules.

For example, suppose that in KBN you create a [Module](https://wiki.genexus.com/commwiki/wiki?22411) containing a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) that allows making insertions, deletions, and updates on the customers table (using [Business Component](https://wiki.genexus.com/commwiki/wiki?5846)s). This module is [packaged and distributed (published)](https://wiki.genexus.com/commwiki/wiki?46751). Then this module is imported into KB1 (through the Knowledge Manager > [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) option).

When from KB1 it is necessary to save data in the customers table of the database associated with KBN, it will be possible to use the Procedure. Since it uses Business Components, all the business rules that were defined in KBN will be executed.

Here the possibility of making definitions in KB1 involving data structures of KBN (navigations, etc.) is lost, but data consistency is ensured.

`[imagen omitida: wiki id 55549]`

**3)** The third alternative to access the data of a subsystem from another one consists of using the two previous alternatives. Through alternative 1 Transaction objects are imported, and this allows defining [For Each command](https://wiki.genexus.com/commwiki/wiki?24744)s and joins, as well as using the concept of [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029) with the power to make free definitions. In addition, alternative 2) is also used and by importing the module you can access and update data of another subsystem while maintaining consistency. In this way, you can have the best of both worlds.

### 

## [2. Implementation with eventually consistent databases](#2.+Implementation+with+eventually+consistent+databases)

N Knowledge Bases are created (one for each subsystem) and there will be N databases (as in the [implementation with consistent databases](https://wiki.genexus.com/commwiki/wiki?55526) described above).

The difference is that in this case there will be data replication. That is, the customers table that is in subsystem 1 will also be in subsystem N (for reasons such as performance or because microservices must have their own data).

Therefore, in this schema, the data is eventually consistent.

### [Options for maintaining the eventual consistency of data](#Options+for+maintaining+the+eventual+consistency+of+data)

#### [**1) Synchronous mechanism**](#1%29+Synchronous+mechanism)

When something changes in the database of subsystem 1 it will be necessary to call a service (an [API](https://wiki.genexus.com/commwiki/wiki?46151) exposed by subsystem N) to save those same changes in the database of subsystem N containing the replicated table. This is a synchronous mechanism (every time something changes in one place, it is replicated in the other place).

To use this mechanism, it is necessary to know which subsystem is the "owner of the data". If the owner is going to save data in one table of its database, then it has to call a service (an [API](https://wiki.genexus.com/commwiki/wiki?46151) exposed by the other subsystem) to save the same data in the table that is a replica.

`[imagen omitida: wiki id 55553]`

**Considerations:**

* The replication mechanism must be idempotent (that is, the result must be the same whether the same operation is performed many times or only once —for example, an insert with the same data executed several times should only insert once—). Therefore, idempotency rules must be programmed in the service that implements the API.
* Consider what happens if for some reason the replication cannot be executed.

#### **2) Asynchronous mechanism**

When something changes in a database table of subsystem 1, to update the database table that is a replica in subsystem N, an [asynchronous mechanism](https://wiki.genexus.com/commwiki/wiki?51735) can be used (for example, [Event Messaging API](https://wiki.genexus.com/commwiki/wiki?55334)).

The "owner of the data" has to record an event in an event bus (indicating, for example, that for the customer topic it inserted customer 54 with its data and publishes it in the event bus). Then, all the subsystems subscribed to that topic in that event buswill receive the notification that an event was recorded, retrieve that data, and do what is necessary in their own databases.

`[imagen omitida: wiki id 55552]`

## [Tooling](#Tooling)

For both implementations (with consistent databases and with eventually consistent databases) GeneXus offers:

* [Modules](https://wiki.genexus.com/commwiki/wiki?22414)
* [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) as identity provider and [GAM's Single Sign On](https://wiki.genexus.com/commwiki/wiki?25385) to provide a single user login between different webapps. To understand this, you can think about Google's scenario: It uses an identity provider in one webapp, then Gmail is in another webapp, Google Drive in another webapp, and Single Sign On is used to keep the user logged in when moving from one to the other webapp.
* [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092)
* [Dynamic links](https://wiki.genexus.com/commwiki/wiki?8446) to call an object that is in a certain webapp from another webapp.
* Backward Reorganization Warning  
    
  As in these kinds of systems, there are several webapps (to be able to update a webapp without having to update the others) and they all work on the same database, the changes to be done in the database must be backward compatible. This means that reorganizations must be done with caution avoiding changes that are useful for a webapp but damage other webapps. A feature that can be helpful is to turn information notifications shown in the [Impact Analysis Report](https://wiki.genexus.com/commwiki/wiki?31023) into errors to avoid certain changes. Read more in [Warnings treated as errors property](https://wiki.genexus.com/commwiki/wiki?8010).
* [Package Module](https://wiki.genexus.com/commwiki/wiki?46751) option
* [Repository Manager](https://wiki.genexus.com/commwiki/wiki?46750,,)  
    
  It is possible to create your own module repository and make it available to the entire organization. For example, a Software House that develops a KB has many modules, and those modules are packaged and uploaded to a single, centralized repository. From Knowledge Manager > Manage Module References it is possible to connect to your own repository and work with the modules and import them.

In addition, for implementations with eventually consistent databases you have:

* For **synchronous replication**: [Generate the services with Rest interfaces](https://wiki.genexus.com/commwiki/wiki?28213) and have them exposed as Open API.
* [Sockets to communicate two services](https://wiki.genexus.com/commwiki/wiki?22442).

* For **asynchronous replication**: Apache, Kafka API.
* It is mandatory to use the [API object](https://wiki.genexus.com/commwiki/wiki?46151), which allows defining microgateways and a mediation layer in GeneXus. This allows defining an interface for the API.

## [Sample of a microservices system created with GeneXus](#Sample+of+a+microservices+system+created+with+GeneXus)

[FestivalTickets - High Scalability Sample](https://wiki.genexus.com/commwiki/wiki?51266)


|  |
| --- |
| **Backlinks** |
| [Microservices systems](https://wiki.genexus.com/commwiki/wiki?55526) | [Toc:Modeling Complex Systems with GeneXus](https://wiki.genexus.com/commwiki/wiki?55502) |
| [Typical architectures to model GeneXus Mission-Critical systems](https://wiki.genexus.com/commwiki/wiki?55503) |

---
