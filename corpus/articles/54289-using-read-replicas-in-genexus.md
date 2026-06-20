---
title: "Using Read Replicas in GeneXus"
source_id: 54289
source_url: https://wiki.genexus.com/commwiki/wiki?54289
genexus_version: "18"
---

# Using Read Replicas in GeneXus

A Read Replica is a copy of a database that is used to improve the performance of applications accessing the database.

Read Replicas work by creating copies of a primary database (also known as a "primary database instance") that are kept synchronized through the use of data replication techniques. When a data update or insert is performed on the primary instance, it is automatically replicated to the Read Replicas.

Thus, in a read/write database environment, write requests are sent to a primary database instance, while read requests can be sent to one or more Read Replicas.

Read Replicas are used to increase the performance and scalability of a database. By sending read requests to Read Replicas instead of to the primary instance, the load on the primary instance is reduced, allowing the database to handle more requests more efficiently. In addition, since Read Replicas are used only to read data, they do not have to handle write requests, which makes them more efficient at reading data.

Read replicas are commonly used in environments involving:

* Distributed database environments,
* Applications requiring fast and efficient access to large datasets, and
* High data read capacity.

### [How to use Read Replicas in GeneXus](#How+to+use+Read+Replicas+in+GeneXus)

To use Read Replicas in GeneXus, follow the steps below:

1. Create a new [Data Store](https://wiki.genexus.com/commwiki/wiki?7117) or open an existing one.
2. Go to the Data Store properties and set the [Read Replica property](https://wiki.genexus.com/commwiki/wiki?54190) to "Default Data Store".
3. Create a [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) and set its [Use Read Replica property](https://wiki.genexus.com/commwiki/wiki?54189) with the name of one of the Data Stores you have defined to work as a Read Replica.
4. Define a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) with a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) that includes the [USING clause](https://wiki.genexus.com/commwiki/wiki?5312) invoking the Data Selector created in step 3.

**Notes**:

* You can use a Data Selector that accesses a Read Replica not only in [For Each command](https://wiki.genexus.com/commwiki/wiki?24744)s, but also in any database request like in [Panel](https://wiki.genexus.com/commwiki/wiki?24829) Grids, [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) Grids, [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082)s, etc.
* If an [Inline Formula](https://wiki.genexus.com/commwiki/wiki?6441) navigation is contained within a navigation that is using a Read Replica, then the formula will also use that Read Replica. It is not possible to define within the formula to access a specific Read Replica with the USING clause.
* To avoid error [spc0238](https://wiki.genexus.com/commwiki/wiki?6774), do not use a Data Selector with a Read Replica which in turn has another Data Selector defined with a different Read Replica.

### [Read Replicas with GeneXus - FAQ](#Read+Replicas+with+GeneXus+-+FAQ)

**In what scenarios is the use of Read Replicas useful?**

The use of Read Replicas is beneficial in scenarios where the database has reached its capacity limit and it is crucial to manage its activity. Read Replicas reduce the load on the main database, which is especially useful in situations of complex batch tasks that access the database and can generate CPU peaks.   
By using Replicas, all these operations are directed to a Replica, without affecting the main database.  
In addition, the use of Read Replicas is also useful to reduce crashes that occur in the main database. Together, these advantages allow changing, in some cases radically, the scalability and the level of concurrency that the solution can handle.

**What considerations should be made when using Read Replicas?**

There are several important considerations when using Read Replicas in an application:

* **Possible out-of-date information:** Due to the time required to synchronize the replicas with the original database, there may be a slight delay in updating the information in the replicas. This means that the data in the replicas may be out of date for a few seconds. In many cases, this delay does not represent a significant problem in the system.
* **Careful selection of where to enable replicas:** Enabling read replicas throughout the application and for all objects could be risky. Developers should be selective and aware of where to activate them. It is important to understand where out-of-date information may not be consistent and cause problems.
* **Impact on sensitive operations:** Some operations in the application, such as complex calculations, formula execution, or data insertion, may depend on the most up-to-date information available in the original database. Reading from a replica that is not up to date may cause data consistency problems and affect the integrity of the system.

**On which objects is it common to use this mechanism?**

It is expected that in objects where high scalability may be required, displaying out-of-date data (for a few seconds) is not a problem. Objects that simply display data, or objects that make extensive use of APIs, may be candidates to use replicas. This is not the case for objects involving many data updates and calculations based on the stored data.

**Is the Read Replica a copy of the original database? Does it require synchronization maintenance when there are changes in the structure?**

Yes. A Read Replica database by definition is an identical copy of the original database. As for synchronization, it is handled automatically by the database management system. When there are changes in the structure of the original database, the replica also needs to be updated to reflect those changes. In environments such as the cloud, a replica is created with a single click and the cloud service provider automatically handles synchronization, thus making it easier to maintain.

### [Scope](#Scope)

**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Availability](#Availability)

This feature is available since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853).


|  |
| --- |
| **Backlinks** |
| [Read Replica property](https://wiki.genexus.com/commwiki/wiki?54190) | [Use Read Replica property](https://wiki.genexus.com/commwiki/wiki?54189) |

---
