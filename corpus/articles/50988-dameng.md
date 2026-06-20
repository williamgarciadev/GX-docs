---
title: "Dameng"
source_id: 50988
source_url: https://wiki.genexus.com/commwiki/wiki?50988
genexus_version: "18"
---

# Dameng

[Dameng Database](https://eco.dameng.com/) is a professional database products provider and technology service.

Here you will not get detailed information about this DBMS, check [the manufacturer](https://eco.dameng.com/docs/zh-cn/start/index.html) for more detail. However, it is a brief usage introduction from the GeneXus perspective.

At least you need to configure the following properties to get started:

* [Server Name Property](https://wiki.genexus.com/commwiki/wiki?9117)
* [User ID Property](https://wiki.genexus.com/commwiki/wiki?9039,,)
* [User Password Property](https://wiki.genexus.com/commwiki/wiki?9040,,)

`[imagen omitida: wiki id 50990]`

Supported DM 8.0 and above; just prototype as usual.

## [Considerations](#Considerations)

* Available for the GeneXus Java generator.
* Geodatabase functionality is not supported by the DBMS.
* The [Enable connection pooling property](https://wiki.genexus.com/commwiki/wiki?9385) in false is not supported.
* The preview of [Query](https://wiki.genexus.com/commwiki/wiki?9026) and [Dashboard](https://wiki.genexus.com/commwiki/wiki?36769) objects will display sample data.
* [Database Reverse Engineering](https://wiki.genexus.com/commwiki/wiki?6634) not supported yet.

### [Reserved Words](#Reserved+Words)

The following list of escaped words by GeneXus when reorganizing are:

```
USER
UPDATE
DEFAULT
DESC
LEVEL
SESSION
ORDER
```

Check the list of [reserved words](https://eco.dameng.com/docs/zh-cn/pm/sql-appendix.html), the following error may appear when reorganizing

```
dm.jdbc.driver.DMException: line X, column Y, nearby [SomeReservedWord] has error:
Syntax error
```

## [Useful Information](#Useful+Information)

Some useful SQL commands to interect with the DBMS. Once the software is installed the default super-user is *SYSDBA*.

### [User Manipulation](#User+Manipulation)

To [create a user](https://eco.dameng.com/docs/zh-cn/start/dm-user-tablespace.html) and generic user manipulation:

```
# Create a user
CREATE USER name IDENTIFIED BY pwd
GRANT RESOURCE TO name
# Delete a user
DROP USER name CASCADE
```

Each user has a default schema with the same name. To access tables, views, etc. in its own schema, it is not necessary to add a schema name. To access objects in other schemas, a schema name is required; use the [Schema Name Property](https://wiki.genexus.com/commwiki/wiki?9471,,).

```
# Create a schema
CREATE SCHEMA name AUTHORIZATION SYSDBA;
# Drop a schema
DROP SCHEMA name CASCADE;
```

### [Data Manipulation](#Data+Manipulation)

A couple of standard SQL DML sentences:

```
SELECT * FROM tablename
INSERT INTO tablename(att1, att2) VALUES(1, 'one')
TRUNCATE TABLE tablename
DROP TABLE tablename CASCADE CONSTRAINTS
```

### [General](#General)

A couple of queries to get parameters, connections and related information from the database.

```
# Configuration
SELECT * FROM SYS."V$VERSION"
SELECT * FROM SYS."V$DATABASE"
SELECT * FROM SYS."V$INSTANCE"
SELECT * FROM SYS."V$DM_INI" WHERE PARA_NAME LIKE '%SomeFilter%'
SELECT * FROM SYS."V$PARAMETER" WHERE NAME LIKE '%SomeFilter%'
# Connections
SELECT * FROM SYS."V$CONNECT"
SELECT * FROM V$SESSIONS
# Close a connection
call sp_close_session (SESSIONID);
```

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?49972,,).

## [See Also](#See+Also)

[Datatypes](https://eco.dameng.com/docs/zh-cn/sql-dev/dmpl-sql-datatype.html)  
[Migration from other DBMSs](https://eco.dameng.com/docs/zh-cn/start/migrate-oracle-dm.html)


|  |
| --- |
| **Backlinks** |
| [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) | [Data types of attributes in the DBMS](https://wiki.genexus.com/commwiki/wiki?3297) | [GAM platforms](https://wiki.genexus.com/commwiki/wiki?22119) |
| [GeneXus and the DBMSes](https://wiki.genexus.com/commwiki/wiki?1772) | [Query Object Considerations](https://wiki.genexus.com/commwiki/wiki?12038) | [Query Object Considerations (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54655) |

---
