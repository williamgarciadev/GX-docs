---
title: "Data types of attributes in the DBMS"
source_id: 3297
source_url: https://wiki.genexus.com/commwiki/wiki?3297
genexus_version: "18"
---

# Data types of attributes in the DBMS

Mapping between the different Data Types defined in GeneXus and the types created in the Data Base in each DBMS.

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **DBMS /**  **GeneXusDataType** | **[SQL Server](https://wiki.genexus.com/commwiki/wiki?1967)** | **[PostgreSQL](https://wiki.genexus.com/commwiki/wiki?1966)** | **[MySQL](https://wiki.genexus.com/commwiki/wiki?1964)** | **[Informix](https://wiki.genexus.com/commwiki/wiki?1963,,)** | **[DB2 for iSeries](https://wiki.genexus.com/commwiki/wiki?1962,,)** | **[Oracle](https://wiki.genexus.com/commwiki/wiki?1965)** | **[Dameng](https://wiki.genexus.com/commwiki/wiki?50988)(7)** | **[DB2 Universal Database](https://wiki.genexus.com/commwiki/wiki?1961)** | **[SQLite](https://wiki.genexus.com/commwiki/wiki?22810,,)** | **[SAP Hana](https://wiki.genexus.com/commwiki/wiki?31713)** (3) |
| **Character(n)** | CHAR(n) | CHAR(n) | CHAR(n) | CHAR(n) | CHAR(n) | CHAR(n) | CHAR(n)(6) | CHAR(n)  WHEN n <= 253 | TEXT COLLATE RTRIM | VARCHAR(n) |
|  |  |  |  |  |  |  |  | VARCHAR(n)  WHEN n > 254 |  |  |
| **Character(n)**  **WHEN [Enable NLS](https://wiki.genexus.com/commwiki/wiki?11500)=True** | NCHAR(n) | CHAR(n)    NLS not implemented | NATIONAL CHAR(n) | CHAR(n)    NLS not implemented | GRAPHIC(n) CCSID 13488 | NCHAR(n)(4) | NCHAR(n)(6) | GRAPHIC(n)  n < 128 | TEXT COLLATE RTRIM | NVARCHAR(n) |
|  |  |  |  |  |  |  |  | VARGRAPHIC(n)  WHEN n >= 128 |  |  |
| **Boolean** | BIT | BOOLEAN | BOOL | BOOLEAN | DECIMAL(1) | NUMERIC(1) | NUMERIC(1) | NUMERIC(1) | INTEGER | TINYINT |
| **Blob** | VARBINARY(MAX)  WHEN Version >= 2005 | BYTE | LONGBLOB | BYTE | BLOB | BLOB | BLOB | BLOB(2G) NOT LOGGED | TEXT | BLOB |
|  | IMAGE  WHEN Version < 2005 |  |  |  |  |  |  |  |  |  |
| **Date** | DATETIME | DATE | DATE | DATETIME Year to Day | CHAR(8) | DATE | DATE | DATE | TEXT | DATE |
| **DateTime** | DATETIME | TIMESTAMP without time zone | DATETIME | DATETIME Year to Second | TIMESTAMP | DATE | TIMESTAMP | TIMESTAMP | TEXT | SECONDDATE |
| **GUID** | UNIQUEIDENTIFIER | CHAR(36) | CHAR(36) | CHAR(36) | CHAR(36) | CHAR(36) | CHAR(36) | CHAR(36) | CHAR(36) | VARCHAR(36) |
| **VarChar(n)** | VARCHAR(n) | VARCHAR(n) | VARCHAR(n) | VARCHAR(n) | VARCHAR(n) | VARCHAR(n)(5) | VARCHAR(n)(6) | VARCHAR(n) | TEXT COLLATE RTRIM | VARCHAR(n) |
|  |  |  |  | VARCHAR(n, a) |  | VARCHAR2(n)  WHEN [Declare Varchar as Varchar2](https://wiki.genexus.com/commwiki/wiki?7369) = True | VARCHAR2(n)  WHEN [Declare Varchar as Varchar2](https://wiki.genexus.com/commwiki/wiki?7369) = True |  |  |  |
| **VarChar(n)**  **WHEN [Enable NLS](https://wiki.genexus.com/commwiki/wiki?11500)=True** | NVARCHAR(n) | VARCHAR(n)    NLS not implemented | NATIONAL VARCHAR(n) | VARCHAR(n) | VARCHAR(n)(1)  VARGRAPHIC(X) CCSID 13488(2) | VARCHAR(n)(5) | VARCHAR(n)(6) | VARGRAPHIC(n) | TEXT COLLATE RTRIM | NVARCHAR(n) |
|  |  |  |  | VARCHAR(n, a)    NLS not implemented |  | NVARCHAR2(n)  WHEN [Declare Varchar as Varchar2](https://wiki.genexus.com/commwiki/wiki?7369) = True | NVARCHAR2(n)(6)  WHEN [Declare Varchar as Varchar2](https://wiki.genexus.com/commwiki/wiki?7369) = True |  |  |  |
| **LongVarChar(n)** | VARCHAR(MAX)  WHEN Version >= 2005 | TEXT | TEXT  WHEN n < 65535 | TEXT | CLOB | CLOB | CLOB | CLOB(n) | TEXT COLLATE RTRIM | CLOB |
|  | TEXT  WHEN Version < 2005 |  | MEDIUMTEXT  WHEN 65535 >= n  AND n < 16777215 |  |  |  |  |  |  |  |
|  |  |  | LONGTEXT  WHEN n >= 16777215 |  |  |  |  |  |  |  |
| **LongVarChar(n)**  **WHEN [Enable NLS](https://wiki.genexus.com/commwiki/wiki?11500)=True** | NVARCHAR(MAX)  WHEN Version >= 2005 | TEXT | TEXT CHARACTER SET utf8  WHEN n < 65535 | TEXT | CLOB(1)  DBCLOB CCSID 13488(2) | CLOB | NCLOB | DBCLOB(n) | TEXT COLLATE RTRIM | NCLOB |
|  | NTEXT  WHEN Version < 2005 |  | MEDIUMTEXT CHARACTER SET utf8    WHEN 65535 >= n  AND n < 16777215 |  |  |  |  |  |  |  |
|  |  |  | LONGTEXT CHARACTER SET utf8  WHEN n >= 16777215 |  |  |  |  |  |  |  |
| **Numeric(L.0)** | SMALLINT  WHEN L < 5 | SMALLINT  WHEN L < 5 | SMALLINT  WHEN L < 5 | SERIAL(s)  WHEN L < 5  AND [Autonumber](https://wiki.genexus.com/commwiki/wiki?6798) = True | DECIMAL(L) | NUMBER(L) | NUMBER(L) | NUMERIC(L) | INTEGER WHEN L < 19 | SMALINT When N < 5 |
|  | INT  WHEN 5 >= L < 10 | INTEGER  WHEN 5 >= L < 10 | MEDIUMINT  WHEN 5 >= L < 7 | SERIAL8(s)    WHEN 5 >= L < 10  AND [Autonumber](https://wiki.genexus.com/commwiki/wiki?6798) = True |  |  |  |  | NUMERIC WHEN L >= 19 | INTEGER When 5 >= L < 10 |
|  | DECIMAL(L)  WHEN L >= 10 | BIGINT  WHEN 10 >= L < 19 | INT  WHEN 7 >= L < 10 | INT  WHEN L < 5  AND Subtype of  [Autonumber](https://wiki.genexus.com/commwiki/wiki?6798) = True |  |  |  |  |  | BIGINT When L >= 10 |
|  |  | NUMERIC(L)  WHEN L >= 19 | BIGINT  WHEN 10 >= L < 19 | INT8  WHEN 5 >= L < 10                AND Subtypeof  [Autonumber](https://wiki.genexus.com/commwiki/wiki?6798) = True |  |  |  |  |  |  |
|  |  |  | NUMERIC(L)  WHEN L >= 19 | SMALLINT  WHEN L < 5  ANDAutonumber = False |  |  |  |  |  |  |
|  |  |  |  | INT  WHEN 5 >= L < 10  AND [Autonumber](https://wiki.genexus.com/commwiki/wiki?6798) = False |  |  |  |  |  |  |
|  |  |  |  | DECIMAL(L)  WHEN L >= 10 |  |  |  |  |  |  |
| **Numeric(L.D)** | SMALLMONEY  WHEN 0 < D < 4  AND L-D-1 < 6 | NUMERIC(L-1,D) | NUMERIC(L-1,D) | DECIMAL(L-1,D) | DECIMAL(L-1,D) | NUMBER(L-1,D) | NUMBER(L-1,D) | NUMERIC(L-1,D) | NUMERIC | DEC(L.D) |
|  | MONEY  WHEN 0 < D < 4  AND 6 >= L-D-1 < 15 |  |  |  |  |  |  |  |  |  |
|  | DECIMAL(L-1,D)  WHEN D >= 4  OR L-D-1 >= 15 |  |  |  |  |  |  |  |  |  |

(1) - Up to GeneXus X Evolution 2 Upgrade #5 and GeneXus X Evolution 3 Upgrade #1.  
(2) - Since GeneXus X Evolution 2 Upgrade #6 and GeneXus X Evolution 3 Upgrade #2.  
(3) - Since GeneXus 15.  
(4) - Up to 2000 characters when NLS is disabled and 1000 characters when NLS is enabled.  
(5) - Up to 4000 characters when NLS is disabled and 2000 characters when NLS is enabled.  
(6) - Up to 1900 characters, detail [here](https://eco.dameng.com/docs/zh-cn/faq/faq-sql-gramm.html#DM-%E6%95%B0%E6%8D%AE%E5%BA%93-VARCHAR2-%E7%9A%84%E9%95%BF%E5%BA%A6%E6%9C%80%E5%A4%A7%E6%98%AF%E5%A4%9A%E5%B0%91).  
(7) - Since GeneXus 17 Upgrade #11.

### [See Also](#See+Also)

* [Attribute and Variable Data types mapping by Generator](https://wiki.genexus.com/commwiki/wiki?21392)


|  |
| --- |
| **Backlinks** |
| [Attribute and Variable Data types mapping by Generator](https://wiki.genexus.com/commwiki/wiki?21392) | [LongVarChar data type](https://wiki.genexus.com/commwiki/wiki?7371) | [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) |

---
