---
title: "Monolithic systems"
source_id: 55516
source_url: https://wiki.genexus.com/commwiki/wiki?55516
genexus_version: "18"
---

# Monolithic systems

A monolithic system contains the entire implementation, which means that all functionalities are grouped together and share the same resources.

In GeneXus, this implies that there is one [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and, at runtime, there is one webapp with the data stored in a single database.

However, having a single webapp doesn't mean that it can't have several channels. It can be multi-experience and include a web part, a mobile part, applications that run on watches or TV, etc.

There is a service layer (business logic) and a database.

`[imagen omitida: wiki id 55563]`

### [Advantages and disadvantages of a monolithic system](#Advantages+and+disadvantages+of+a+monolithic+system)

#### [**Advantages**](#Advantages)

ACID (atomicity, consistency, isolation, durability) features are present in the data and ensure that it is persisted correctly. All operations are performed on the same database; therefore, regardless of the complexity of what needs to be addressed, the results will be accurate because the system will be highly cohesive.

The concept of [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029) can be used, there is a good performance when making joins, etc.  
  
All screens will have the same style and will use the same [Design System](https://wiki.genexus.com/commwiki/wiki?40108), so there will be a strong cohesion.

#### [**Disadvantages**](#Disadvantages)

One of the disadvantages of this type of system is that the webapp is either running or not running. In addition, the deployment involves the entire application, so at some point, it will require the application to be taken down and then brought back up. In some scenarios, this can be troublesome.

Furthermore, if there is a performance issue (for example, someone performs a full scan on a database table and blocks that table), it affects the whole database because there is only one database.

Lastly, monolithic systems must be scaled horizontally with the entire application and database. This drawback can cause problems as systems grow and their functionalities need to be more flexible.

### [Example of a monolithic system created with GeneXus](#Example+of+a+monolithic+system+created+with+GeneXus)

The [Coronavirus UY](https://www.genexus.com/en/community/webinars/people-ideas-tools-what-is-behind-coronavirus-uy)  application was a monolithic system when it was first released.

There was only one Knowledge Base, and the same webapp had all the services (for the backoffice, for mobile applications, etc.).

Having implemented it as a monolithic system, allowed creating that first version in less than one week.  
  
Then it was migrated to a [miniservices architecture](https://wiki.genexus.com/commwiki/wiki?55518) to avoid testing the entire system before distributing it and to achieve agility with the modules that required it.

### [Tooling offered by GeneXus to implement this kind of systems](#Tooling+offered+by+GeneXus+to+implement+this+kind+of+systems)

* [Modules](https://wiki.genexus.com/commwiki/wiki?22414)

It is very important to build a KB using modules. Including the objects in modules helps to organize the KB and lets developers know what modules they have to work on; this will give them flexibility to package those modules and distribute them (this is a key aspect to be able to change the architecture, if necessary, from a monolithic system to the other options).

* [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746)

It is GeneXus’ solution for everything related to application authentication and authorization (security).

* [Log API](https://wiki.genexus.com/commwiki/wiki?37872)

It allows creating log files with information about one or several processes during their execution. For example, this is very useful to find at what point an error or a certain behavior occurs when processing large numbers of records.

* [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092)

The [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886) defines the set of objects that will be deployed together. It is recommended to use this object even when working with a monolithic system. Later on, this will make it easier to migrate to another architecture.

* [Scalability and Performance of GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?45280)

Consider this information for scaling your monolithic system.


|  |
| --- |
| **Backlinks** |
| [Macroservices and Miniservices systems](https://wiki.genexus.com/commwiki/wiki?55518) | [Toc:Modeling Complex Systems with GeneXus](https://wiki.genexus.com/commwiki/wiki?55502) | [Typical architectures to model GeneXus Mission-Critical systems](https://wiki.genexus.com/commwiki/wiki?55503) |

---
