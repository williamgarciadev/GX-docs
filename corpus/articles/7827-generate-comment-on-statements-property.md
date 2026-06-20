---
title: "Generate COMMENT ON statements property"
source_id: 7827
source_url: https://wiki.genexus.com/commwiki/wiki?7827
genexus_version: "18"
---

# Generate COMMENT ON statements property

Controls the generation of comments (SQL COMMENT ON statement) in the database creation/reorganization process.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | The creation/reorganization programs will not generate comments in the database created for the application. This is the default value. |
| **Yes** | The creation/reorganization programs will generate comments in the database for each table and attribute. |

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** Iseries, DB2 UDB, ORACLE, POSTGRESQL  
**Platforms:** Web(.Net, Java)

### [Description](#Description)

When set to Yes, the description specified by the user will be the one used for tables and attributes. For example:

CREATE TABLE TestPropGenCom (TestCod smallint NOT NULL , TestDesc CHAR(50) NOT NULL , PRIMARY KEY(TestCod))  
**COMMENT ON** TABLE TestPropGenCom IS 'Test property Generate comments on'  
**COMMENT ON** COLUMN TestPropGenCom.TestCod IS 'Test Code'  
**COMMENT ON** COLUMN TestPropGenCom.TestDesc IS 'Test Description'

This process may cause an additional delay in the creation/reorganization process.

#### [Notes:](#Notes%3A)

If the value of this configuration option is changed (from Yes to No or vice versa), a total database reorganization (to generate or eliminate comments) is NOT forced. The change applies to the creation/reorganization processes that take place afterwards and only on the tables affected by these processes. In other words, changes made to this configuration option will be gradually reflected in the database once its tables have been reorganized.

GeneXus will not reorganize the database if the description of the attribute or table changes, even though the generation of comments is active. If this new description is to take effect, then it will be necessary to reorganize all the tables where the attribute is used.

#### [How to apply changes](#How+to+apply+changes)

Create Database

### [Compatibility](#Compatibility)

SQL Server is supported since GeneXus 16 upgrade 7.


|  |
| --- |
| **Backlinks** |
| [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) |

---
