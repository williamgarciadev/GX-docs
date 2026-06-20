---
title: "Features of Reorganizations"
source_id: 3154
source_url: https://wiki.genexus.com/commwiki/wiki?3154
genexus_version: "18"
---

# Features of Reorganizations

This article describes the main features and aspects related to [database creation and reorganizations](https://wiki.genexus.com/commwiki/wiki?5288).

GeneXus generates automatically programs and scripts to maintain the database structure and that includes the maintenance of the schema and also the required data transformations associated with it.

The database is maintained in the 3rd Normal Form, although [redundancy](https://wiki.genexus.com/commwiki/wiki?5962) is supported for performance reasons. (See also [GeneXus and Relational Databases: the Essence](https://wiki.genexus.com/commwiki/wiki?6720,,))

### [Schema Changes](#Schema+Changes)

GeneXus maintains (creates, alters, drops) the following objects of a database

* [SQL Tables](https://en.wikipedia.org/wiki/Table_(database)), [Views](https://en.wikipedia.org/wiki/View_(SQL)), Functions, and [Attributes](https://en.wikipedia.org/wiki/Column_(database))
  + In the [KB](https://wiki.genexus.com/commwiki/wiki?2428), defined by GeneXus as [Table](https://wiki.genexus.com/commwiki/wiki?7120) and [Attributes](https://wiki.genexus.com/commwiki/wiki?7240), inferred automatically from the [Transactions](https://wiki.genexus.com/commwiki/wiki?1908) (and [Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062), and Attributes) defined by the user
* [Indexes](https://en.wikipedia.org/wiki/Database_index), and Constraints
  + In the KB, defined as [Indexes](https://wiki.genexus.com/commwiki/wiki?7121). Primary Keys and Foreign Keys are inferred automatically from definitions in Transactions and [Subtypes](https://wiki.genexus.com/commwiki/wiki?20206); Candidate keys, and secondary indexes are defined by the user as Unique or Duplicate Indexes.

GeneXus creates also the database if needed, in some DBMSes (eg.: SQL Server) or the Schema (eg.: Oracle).

Although several [Data Stores](https://wiki.genexus.com/commwiki/wiki?7117) can be accessed by the generated programs, GeneXus only generates reorganizations for the default data store. The schema of the other data sources are supposed to be maintained by other Knowledge bases or systems.)

SQL sentences and syntax depends on target DBMS and DBMS version in order to achieve maximal efficiency.

### [Efficient data transformations](#Efficient+data+transformations)

As for Schema changes, data transformations and the associated syntax used in the reorganizations depend on target DBMS and DBMS version in order to achieve maximal efficiency.  
Scenarios, where temporary tables are used for data transformations, are [minimal](https://wiki.genexus.com/commwiki/wiki?19529), data flowing between the server and the client is minimal too, and 'ALTER TABLE' commands are used whenever possible.

##### [Examples](#Examples)

1) Adding a NOT NULL column to a table in SQL Server executes two statements. The example shows how a CustomerEmail not nullable column is added to the Customer table:

```
ALTER TABLE [CUSTOMER] ADD [CustomerEmail] varchar(40) NOT NULL CONSTRAINT CustomerEmail_DEFAULT DEFAULT ' '
ALTER TABLE [CUSTOMER] DROP CONSTRAINT CustomerEmail_DEFAULT
```

2) Changing the table where a NOT NULL attribute is stored requires three statements. The example shows how CustomerEmail attribute is moved from the Invoice table to the Customer table.

```
ALTER TABLE [CUSTOMER] ADD [CustomerEmail] varchar(40) NOT NULL CONSTRAINT CustomerEmail_DEFAULT DEFAULT ''
UPDATE [CUSTOMER] SET [CustomerEmail] = T.[CustomerEmail] FROM 
 (SELECT [CustomerEmail], [CustomerId] FROM [INVOICE]) T WHERE [CUSTOMER].CustomerId = T.CustomerId 
ALTER TABLE [CUSTOMER] DROP CONSTRAINT CustomerEmail_DEFAULT
```

3) Adding a new column, using IIF() in its initial value executes three statements. The example shows how the reorg resolves to add the  attribute ProductCategory with initial value = iif(ProductPrice > 1000, "Category 1", "Category 2") to the table PRODUCT

```
ALTER TABLE [Product] ADD [ProductCategory] char(20) NOT NULL CONSTRAINT ProductCategoryProduct_DEFAULT DEFAULT ''
UPDATE [Product] SET [ProductCategory]=T.[ProductCategory] FROM 
 (SELECT [ProductId], CASE WHEN [ProductPrice] > 1000 THEN 'Category 1' ELSE 'Category 2' END AS ProductCategory 
  FROM [Product]) T
 WHERE [Product].ProductId= T.ProductId
ALTER TABLE [Product] DROP CONSTRAINT ProductCategoryProduct_DEFAULT
```

Avoiding temporary tables, in addition to improving performance, keeps the changes you manually made to table definitions. For example, if you added permissions to a table, when a temporary table is used, the table is deleted and re-created, so all the security settings are lost. If the table is not deleted because no temporary table was used, no settings are lost.

### [**Partitioned Reorganizations**](#Partitioned+Reorganizations)

Reorganization code is generated in independent modules that can be executed in parallel. This allows you to radically improve the performance of reorganizations in servers with multiple processors.  
  
To be able to partition the reorganization, GeneXus identifies code-blocks that can be executed independently and the reorganization runs them in different threads. Achieving this involved a redesign of the reorganization process with a nice side effect: code is very easy to read, especially if you try to view the steps needed to reorganize a table.

Informix Note: This feature is supported for all DBMS of GeneXus, unless Informix. The limitation in ANSI databases of Informix is that they don't support the autocommit. The autocommit is necessary to run in multi-threads, in order to manage the connections used by the different UTLs and avoid any deadlock.

Changing the number of parallel threads: By default, the reorg is executed in 5 parallel threads. Depending on the number of processors you may want to change this. You do it changing the SUBMIT\_POOL\_SIZE in the reorg.cfg (java) or the REORG\_MAX\_THREADS in the client.exe.config (.net)

### [**SQL Statements**](#SQL+Statements)

Together with the Impact Analysis Report, you can see the SQL statements that will be executed in the database. This lets you have a better idea of what GeneXus will do to reorganize each table. A script (ReorganizationScript.txt) containing all reorganization statements in the order they will be executed is created in the model directory. The content of this file is not executed by GeneXus. it is created for documentation purposes only.

### [Display the number of records of each table to be reorganized](#Display+the+number+of+records+of+each+table+to+be+reorganized)

One of the first steps in the default reorganization process is to count and show the number of records in each table to be reorganized. Besides, you can run the reorganization program only to count records. Executing the reorganization program with the "-recordcount" parameter will count records in all tables to be reorganized, display the results and stop. This may be used to estimate how long the reorganization may take.

The -recordcount parameter, and many other reorganization options described in this document, can be set in GeneXus at the model preferences, under the group 'Build Process - Advanced - Reorganization Options'. By default, this option is set with the value -nogui.

### [User-defined pre/post reorganization script](#User-defined+pre%2Fpost+reorganization+script)

Sometimes you may need to execute SQL statements before and/or after the reorganization. For example, you may want to run a backup process and truncate some large table(s) before the reorganization and restore its data after it.  
  
If the reorganization process finds a file named "beforeReorganizationScript.txt" in the same (current) directory as the reorganization program, it will try to execute its SQL statements before the reorganization. The same occurs if there is a file named "afterReorganizationScript.txt" that is executed after the reorganization process.  
  
Both files must have SQL statements only. The SQL statements must be separated by a semicolon (";") as in the following script sample:

```
TRUNCATE TABLE [FirstBigTable];
TRUNCATE TABLE [SecondBigTable];
```

### [Resume after failure](#Resume+after+failure)

A reorganization process may fail for several reasons. Power failures, running out of disk space, lack of authorizations are just a few common causes. In many failure situations there is no need to restore the database but just fix the problem (wait for power, free some disk space, authorize, etc.) and restart from the point of failure. Restarting saves time and work.  
  
The reorganization process has a built-in resume after failure. That is, if it starts executing after a failure it will skip all steps already accomplished and will actually start executing the step that failed in the previous execution. As a result, recovering from a reorganization failure is easy: fix the problem and restart the reorganization. It is important to notice that the resume after failure feature includes statements in the pre/post reorganization scripts. If, for example, the reorganization fails in the third SQL statement in beforeReorganization.txt, when resuming, the first two statements will not be executed.

#### [How to prevent the reorganization from resuming after a failure](#How+to+prevent+the+reorganization+from+resuming+after+a+failure)

In some failure recovery situations, you may want to start over and run the reorganization process from the very beginning. Running the reorganization process with the -ignoreresume parameter makes the reorganization process to execute while ignoring any resume information.

### [Database schema verification](#Database+schema+verification)

Reorganizations change the database schema. They create and remove tables, change their structure, add indexes and constraints, move data among tables, etc. Every statement or procedure used during a specific reorganization may fail if the database schema is not the expected one. For example, if the reorganization has to create a new table it should fail if that table already exists.  
  
The reorganization process searches the current database schema for possible inconsistencies between what's expected and what's actually there. We named this process "Database Schema Verification".  
  
By the time this article is written, the following verifications are being made:

* If a new table has to be created, it is verified that there are no tables or views with the same name
* If a table is dropped, it is verified that it exists
* If a table is renamed, it is verified that the new table (or a view with the same name) does not already exist, and that the old one exists
* If an attribute has to be created, it is verified that it does not already exist
* If an attribute is dropped, it is verified that it exists (see more [here](14301'.html)).

**Note:** All verifications are made against the actual DBMS catalog.

#### [How to avoid the database schema verification](#How+to+avoid+the+database+schema+verification)

If, for any reason, you do not want the database schema to be verified, use the -noverifydatabaseschema parameter when running the reorganization.

There are two model preferences where this value can be set: "Create Database Options" and "Reorganization Options" for reorganizations that are run directly from GeneXus. The default value is different in each case:

* Reorganization Options default value = -nogui
* Create Database Options default value = -nogui -noverifydatabaseschema

#### [DBMS version verification](#DBMS+version+verification)

The DBMS version verification consists of verifying that the reorganization is running on a DBMS version equal to or greater than the DBMS version configured in GeneXus. This verification is performed in any type of reorganization, including Create database.

For example, if the SQL server version to be connected is 2000, and the "SQL server Version" property of GeneXus is set with the "2005 or higher" value, the following message is given:

> *An error was found in the database schema verification process. Reorganization code was generated to run on DBMS versions higher than the current one.  
> **DBMS should be at least in version 2005** or you may regenerate and re-run the reorganization after changing the corresponding DBMS version property.  
> The reorganization process was not successfully completed.  
> **Reorganization Failed***

**Note:** This verification cannot be avoided

### How to run the reorganization twice

In order to avoid accidental executions of reorganizations that already finished successfully, the second time you run a reorganization you will get a message "No reorganization needed". But if you really need to run a reorganization that has already been executed and finished successfully before, you can run it with the '-force' flag.

### [Steps involved in a Reorganization](#Steps+involved+in+a+Reorganization)

In general terms, a reorganization process consists of

* Check the existence of the beforeReorganizationScript.txt file.
* Database schema verification depending on the [reorganization options](https://wiki.genexus.com/commwiki/wiki?9016).
* Verify if the reorganization should resume from the latest entry point.
* Execute the reorganization.
  + Execute the code to reorganize the database based on the IAR analysis including Table creation and data conversion.
  + Create Indices and Referential Integrity.
* Check the existence of the afterReorganizationScript.txt file.
* Update the Knowledge Base.

### [See Also](#See+Also)

* [Database Reorganization cases where a temporary table is created](https://wiki.genexus.com/commwiki/wiki?19529)
* [Reorganizations associated to Data Views](https://wiki.genexus.com/commwiki/wiki?43272)
* [Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062)
* [Scenario of backward compatible reorganizations](https://wiki.genexus.com/commwiki/wiki?48715)


|  |
| --- |
| **Backlinks** |
| [Create Database Options property](https://wiki.genexus.com/commwiki/wiki?9016) | [Database Reorganization cases where a temporary table is created](https://wiki.genexus.com/commwiki/wiki?19529) | [DB2 for iSeries requirements](https://wiki.genexus.com/commwiki/wiki?26977) |
| [Export Reorganization](https://wiki.genexus.com/commwiki/wiki?34476) | [Category:Reorganization](https://wiki.genexus.com/commwiki/wiki?5288) |
| [Reorganization Options property](https://wiki.genexus.com/commwiki/wiki?36454) | [Scenario of backward compatible reorganizations](https://wiki.genexus.com/commwiki/wiki?48715) |

---
