---
title: "Preserve Table Casing property"
source_id: 8844
source_url: https://wiki.genexus.com/commwiki/wiki?8844
genexus_version: "18"
---

# Preserve Table Casing property

When creating the Database, it uses exactly the same table casing as shown in the GeneXus IDE; otherwise, it creates the tables using the uppercase function.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Level:** [Environment](https://wiki.genexus.com/commwiki/wiki?7115)

### [Description](#Description)

The Default value is True. However, when [converting a KB from GeneXus 9.0](https://wiki.genexus.com/commwiki/wiki?5464,,), the False value is assigned to [maintain compatibility](https://wiki.genexus.com/commwiki/wiki?6528,,).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

#### [**True value**](#True+value)

When creating the Database, it uses exactly the same table casing as shown in the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272).

SQL statements are also generated using the same table casing shown in the GeneXus IDE.

**Example:**

reorg.cs: " CREATE TABLE <Transaction1> (<AaA>  smallint NOT NULL , <BbB>  char(20) NOT NULL , PRIMARY KEY(<AaA>))  "

transaction1.cs: "SELECT <AaA>, <BbB> FROM <Transaction1> WITH (UPDLOCK) WHERE <AaA> = @AaA "

#### [**False value**](#False+value)

When creating the database, it creates the tables using the uppercase function. The same criterion is used for table casing in SQL statements.

**Example:**

reorg.cs: " CREATE TABLE <TRANSACTION1> (<AaA>  smallint NOT NULL , <BbB>  char(20) NOT NULL , PRIMARY KEY(<AaA>))  "

transaction1.cs= "SELECT <AaA>, <BbB> FROM <TRANSACTION1> WITH (UPDLOCK) WHERE <AaA> = @AaA "

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, execute [Create Database Tables](https://wiki.genexus.com/commwiki/wiki?7158) and after that execute [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691). |
