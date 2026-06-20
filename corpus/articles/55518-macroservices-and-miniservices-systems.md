---
title: "Macroservices and Miniservices systems"
source_id: 55518
source_url: https://wiki.genexus.com/commwiki/wiki?55518
genexus_version: "18"
---

# Macroservices and Miniservices systems

**Note**: macroservices and miniservices architectures are implemented in the same way. The particularity of macroservices is that they run in the same container (like Apache Tomcat).

In GeneXus, a macroservices / miniservices system can be implemented with only one [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) that should be organized with [Modules](https://wiki.genexus.com/commwiki/wiki?22414).

Unlike [monolithic systems](https://wiki.genexus.com/commwiki/wiki?55516), in these cases, a system is distributed in several webapps. That is, there are several subsystems (several business logics). This provides flexibility.

There is a single database with which all the subsystems work.

`[imagen omitida: wiki id 55564]`

### [Advantages and disadvantages of this architecture](#Advantages+and+disadvantages+of+this+architecture)

#### **Advantages**

ACID (atomicity, consistency, isolation, durability) features are present in the data and ensure that it is persisted correctly. All operations are performed on the same database; therefore, regardless of the complexity of what needs to be addressed, the results will be accurate because the system will be highly cohesive.  
  
The concept of [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029) can be used, there is a good performance when making joins, etc.

All screens will have the same style and will use the same [Design System](https://wiki.genexus.com/commwiki/wiki?40108).

Each webapp is independently deployed. This is a benefit because, for example, if the mobile services webapp has to be deployed, this does not affect the back office services webapp or other webapps.

#### **Disadvantages**

Having a single database implies that any problems that occur in it will affect all the webapps.  
   
When the database is reorganized, it will be necessary to ensure that all the webapps continue working (when the database is reorganized, if only one webapp is moved and any change affects another webapp that was not updated, errors will occur).

Scalability will depend on the database.

Integration between webapps will be needed (if from one webapp you need to call an object that is in another webapp, the solution is to use a [Dynamic link](https://wiki.genexus.com/commwiki/wiki?8446) to solve it).

### [Example of a miniservices system created with GeneXus](#Example+of+a+miniservices+system+created+with+GeneXus)

The [Coronavirus UY](https://www.genexus.com/en/community/webinars/people-ideas-tools-what-is-behind-coronavirus-uy)  application was a monolithic application when it was first released. In its second release, the application was moved to a miniservices architecture.

The single KB with N modules where all developers work was kept. To transform the architecture to miniservices, separate [Deployment Units](https://wiki.genexus.com/commwiki/wiki?38886) were defined (one Deployment Unit for mobile services, one Deployment Unit for batch processes, one for the back office, and another for the front office). This made deployment much easier. To update part of a given webapp, only that Deployment Unit has to be distributed again.

### [Tooling offered by GeneXus to implement this kind of systems](#Tooling+offered+by+GeneXus+to+implement+this+kind+of+systems)

* [Modules](https://wiki.genexus.com/commwiki/wiki?22414)
* [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) as identity provider.
* [GAM's Single Sign On](https://wiki.genexus.com/commwiki/wiki?25385) can be used in these systems to provide a single user login between different webapps.
* [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092)
* [Dynamic links](https://wiki.genexus.com/commwiki/wiki?8446) to call an object that is in a certain webapp from another webapp.
* Backward Reorganization Warning

As in these kinds of systems, there are several webapps (to be able to update a webapp without having to update the others) and they all work on the same database, the changes to be done in the database must be backward compatible. This means that reorganizations must be done with caution avoiding changes that are useful for a webapp but damage other webapps. A feature that can be helpful is to turn information notifications shown in the [Impact Analysis Report](https://wiki.genexus.com/commwiki/wiki?31023) into errors to avoid certain changes. Read more in [Warnings treated as errors property](https://wiki.genexus.com/commwiki/wiki?8010).


|  |
| --- |
| **Backlinks** |
| [Toc:Modeling Complex Systems with GeneXus](https://wiki.genexus.com/commwiki/wiki?55502) | [Monolithic systems](https://wiki.genexus.com/commwiki/wiki?55516) |

---
