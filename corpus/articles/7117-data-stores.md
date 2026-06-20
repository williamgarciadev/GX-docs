---
title: "Data Stores"
source_id: 7117
source_url: https://wiki.genexus.com/commwiki/wiki?7117
genexus_version: "18"
---

# Data Stores

A Data Store defines the information to access a certain database (the properties of a Data Store allow you to define the connection data to the database, such as the server name, database name, user, password, version of the database, etc.).

Multiple Data Stores are most commonly used for the following scenario:

* One Data Store defines the information to access to the database associated with your generated application.
* It is also possible to define other Data Stores to define the information to access other databases to read information.

So, each [Environment](https://wiki.genexus.com/commwiki/wiki?7115) can have a list of Data Stores defined under the **Data Stores**node. The first Data Store on the list is always used by default and taken into account when F5 is pressed.  
  
`[imagen omitida: wiki id 46833]`

You can add new ones:

`[imagen omitida: wiki id 46834]`

To change the DBMS of a certain Data Store, you have to right-click on the desired one, then click on **Change Data Store** and select the most suitable one.

To delete a DBMS from the list created, right-click on the desired one and choose the Delete option. The default Data Store cannot be deleted; and those cross-referenced (i.e. [Data Views](https://wiki.genexus.com/commwiki/wiki?1914) to external databases) cannot be deleted either.

### [Data Store Properties](#Data+Store+Properties)

Each Data Store has a set of properties containing information about the connection, creation and/or reorganization of databases and tables, etc.

`[imagen omitida: wiki id 5795]`


|  |
| --- |
| **Sub Categories** |
| [Category:iSeries Native Data Store Properties](https://wiki.genexus.com/commwiki/wiki?14036,Category%3AiSeries+Native+Data+Store+Properties,) | [Category:PostgreSQL Data Store Properties](https://wiki.genexus.com/commwiki/wiki?14037,Category%3APostgreSQL+Data+Store+Properties,) | [Category:SQL Server Data Store Properties](https://wiki.genexus.com/commwiki/wiki?13299,Category%3ASQL+Server+Data+Store+Properties,) |

---

|  |
| --- |
| **Pages** |
| [Access technology to set property](https://wiki.genexus.com/commwiki/wiki?9030) | [Additional connection string attributes property](https://wiki.genexus.com/commwiki/wiki?9037) | [Connect to server property](https://wiki.genexus.com/commwiki/wiki?8536) |
| [Create All Pool Connections at Startup Property](https://wiki.genexus.com/commwiki/wiki?18888,Create+All+Pool+Connections+at+Startup+Property,) | [Create Save File Property](https://wiki.genexus.com/commwiki/wiki?9434,Create+Save+File+Property,) | [Data Library Name Property](https://wiki.genexus.com/commwiki/wiki?9432,Data+Library+Name+Property,) |
| [Data types of attributes in the DBMS](https://wiki.genexus.com/commwiki/wiki?3297) | [Database name property](https://wiki.genexus.com/commwiki/wiki?9080) | [Database Schema Property](https://wiki.genexus.com/commwiki/wiki?9081,Database+Schema+Property,) |
| [Database type property](https://wiki.genexus.com/commwiki/wiki?9119) | [DB2 for iSeries requirements](https://wiki.genexus.com/commwiki/wiki?26977) | [DB2 UDB Version property](https://wiki.genexus.com/commwiki/wiki?10479) |
| [DB2UDB version property](https://wiki.genexus.com/commwiki/wiki?9397) | [DBMS Options](https://wiki.genexus.com/commwiki/wiki?9067) | [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) |
| [Declare referential integrity property](https://wiki.genexus.com/commwiki/wiki?9093) | [Default indices storage area property](https://wiki.genexus.com/commwiki/wiki?7155) | [Default Tables Storage Area property](https://wiki.genexus.com/commwiki/wiki?9088) |
| [Default Temporary Storage Area Property](https://wiki.genexus.com/commwiki/wiki?9087) | [Generate COMMENT ON statements property](https://wiki.genexus.com/commwiki/wiki?7827) | [Informix Version property](https://wiki.genexus.com/commwiki/wiki?9399) |
| [JDBC Datasource Property](https://wiki.genexus.com/commwiki/wiki?17892,JDBC+Datasource+Property,) | [Library list property](https://wiki.genexus.com/commwiki/wiki?9401,Library+list+property,) | [List of external stored procedures property](https://wiki.genexus.com/commwiki/wiki?9393) |
| [Lock Mode property](https://wiki.genexus.com/commwiki/wiki?9091,Lock+Mode+property,) | [Lock time-out (seconds) property](https://wiki.genexus.com/commwiki/wiki?9116) | [MySQL version property](https://wiki.genexus.com/commwiki/wiki?9420) |
| [Name of Journal Property](https://wiki.genexus.com/commwiki/wiki?9435,Name+of+Journal+Property,) | [Oracle version property](https://wiki.genexus.com/commwiki/wiki?9112) | [Order Attributes in File Property](https://wiki.genexus.com/commwiki/wiki?9436,Order+Attributes+in+File+Property,) |
| [Primary Key Definition Property](https://wiki.genexus.com/commwiki/wiki?7826,Primary+Key+Definition+Property,) | [Primary key Index Clustering Data Stores Property](https://wiki.genexus.com/commwiki/wiki?7130) | [Programs Library Name Property](https://wiki.genexus.com/commwiki/wiki?9433,Programs+Library+Name+Property,) |
| [Read Replica property](https://wiki.genexus.com/commwiki/wiki?54190) | [Recycle Type Property](https://wiki.genexus.com/commwiki/wiki?9388,Recycle+Type+Property,) | [Server Name Property](https://wiki.genexus.com/commwiki/wiki?9117) |
| [Server property](https://wiki.genexus.com/commwiki/wiki?9398) | [Show Connection Dialog in WinForms Property](https://wiki.genexus.com/commwiki/wiki?9038,Show+Connection+Dialog+in+WinForms+Property,) | [Size property](https://wiki.genexus.com/commwiki/wiki?10585) |
| [SQL server version property](https://wiki.genexus.com/commwiki/wiki?9114) | [Unlimited size property](https://wiki.genexus.com/commwiki/wiki?9386) | [Use Custom JDBC URL Property](https://wiki.genexus.com/commwiki/wiki?9381) |
| [Use Datasource for Web Based Applications Property](https://wiki.genexus.com/commwiki/wiki?9384,Use+Datasource+for+Web+Based+Applications+Property,) | [Use trusted connection property](https://wiki.genexus.com/commwiki/wiki?9418) | [User ID Property](https://wiki.genexus.com/commwiki/wiki?9039,User+ID+Property,) |
| [User Password Property](https://wiki.genexus.com/commwiki/wiki?9040,User+Password+Property,) | [Using Read Replicas in GeneXus](https://wiki.genexus.com/commwiki/wiki?54289) |

---
