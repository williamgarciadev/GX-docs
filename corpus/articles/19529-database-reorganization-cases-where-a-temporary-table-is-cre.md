---
title: "Database Reorganization cases where a temporary table is created"
source_id: 19529
source_url: https://wiki.genexus.com/commwiki/wiki?19529
genexus_version: "18"
---

# Database Reorganization cases where a temporary table is created

The cases requiring the creation of a temporary table when executing a database reorganization are those that cannot be solved only with SQL statements. The generator used to run the database reorganization will create and execute a conversion program during the reorganization; these reorganizations are detailed [here](https://wiki.genexus.com/commwiki/wiki?3154).

You will identify these kind of database reorganizations in the IAR (Impact Analysis Report); for these cases a temporary table will be created and a GeneXus program or SQL statement will be used to copy the data to the new structures.

Each table conversion will generate a <TableName>conversion file detailing the following:

```
CREATE TABLE [GXA0001] ( .... )
Run conversion program for table <TableName>
DROP TABLE [<TableName>]
CALL sp_rename('[GXA0001]', '<TableName>')
ALTER TABLE [<TableName>] ....
```

**Note**: in this case the database reorganization sample is associated to SQLServer, you will notice some differences when executing with other DBMS.  
In short the database reorganization does the following:

* A temporary table *GXA0001* is created with the new table structure.
* A conversion program is executed to populate the temporary structure.
* The old table "Tablename" is deleted.
* The temporary table is renamed with the correct "TableName".
* The table restrictions are set.

The generator will create and execute the conversion program during the database reorganization using the following pattern for each table:

*<TableName>conversion.cs* for C# generator.  
*<TableName>conversion.java* for Java generator.  
*<TableName>conversion.rb* for Ruby generator.

## [**Samples**](#Samples)

### [1. Adding a BLOB attribute to a transaction (using SQLServer until version X Evolution 2 upgrade 3)](#1.+Adding+a+BLOB+attribute+to+a+transaction+%28using+SQLServer+until+version+X+Evolution+2+upgrade+3%29)

Note: Since version X Evolution 2 Upgrade 3, this reorg has been optimized, and an "Alter table" is used instead of creating a temporal table (see SAC #32631 for more information) 

```
CREATE TABLE [GXA0001] (
  [Transaction1Id]       SMALLINT     NOT NULL,
  [Transaction1Num]   SMALLINT     NOT NULL,
  [Transaction1Blob]     VARBINARY(MAX)     NOT NULL)

Run conversion program for table Transaction1

DROP TABLE [Transaction1]

CALL sp_rename('[GXA0001]', 'Transaction1')

ALTER TABLE [Transaction1]
ADD     PRIMARY KEY ( [Transaction1Id] )
```

### [2. Altering the key of the table, when any other field accepts nulls of the DBMS.](#2.+Altering+the+key+of+the+table%2C+when+any+other+field+accepts+nulls+of+the+DBMS.)

When the key of the table Transaction1 wants to be modified (for example changing a N(5) to a N(6)), an alter table cannot be performed. In this case, a temporary table is created, and the data is copied to the temporary table in an optimized way:

INSERT INTO GXA0001 (a, b, c) SELECT a, b, c FROM Transaction1

If the table Transaction1 has an attribute which has [Nullable property - Attribute](https://wiki.genexus.com/commwiki/wiki?7642) = TRUE, this optimization cannot be done so the copy is done defining a cursor for querying the data from one table (Transaction1) and another cursor for inserting in the other table.

### [3. The significant attribute or table name length is extended](#3.+The+significant+attribute+or+table+name+length+is+extended)

For example, you decided to modify the following:

* [Significant attribute name length property](https://wiki.genexus.com/commwiki/wiki?7248)
* [Significant Table Name Length Property](https://wiki.genexus.com/commwiki/wiki?7249,,)

The reorganization consists of:

* Create a temporary table with the new attribute name length
* Copy records from the old table to the new temporary one
* Rename the table to the new name
* Update table integrity restrictions

### [Other cases](#Other+cases)

* Changing the property nullable from yes to no
* Case of Informix  - when the rgz0005 is given
* Case of Oracle  - when more than a table is navigated to load data of a table
* Case of Informix - when the table to be loaded has to navigate itself


|  |
| --- |
| **Backlinks** |
| [Features of Reorganizations](https://wiki.genexus.com/commwiki/wiki?3154) |

---
