---
title: "Cloud Database"
source_id: 31685
source_url: https://wiki.genexus.com/commwiki/wiki?31685
genexus_version: "18"
---

# Cloud Database

*"A cloud database is a database that typically runs on a cloud computing platform. There are two common deployment models: users can run databases on the cloud independently, using a virtual machine image, or they can purchase access to a database service, maintained by a cloud database provider. Of the databases available on the cloud, some are SQL-based and some use a NoSQL data model." source <https://en.wikipedia.org/wiki/Cloud_database>*

When it's being run independently in a Virtual Machine Image, there is not much to add to the typical considerations to manage a database instance. It becomes interesting when the database is provided as a service.

With GeneXus you can build solutions (cloud-based or not) that run with these cloud databases provided by PaaS providers like Amazon, IBM, Google, Microsoft or others.

The following is a list of relational cloud databases that are supported by GeneXus and the corresponding Datastore property value you have to set.

| Cloud Database | GeneXus Datastore to set |
| --- | --- |
| SAP Hana DB on SAP Cloud Platform | SAP Hana |
| [SAP Hana DB on Amazon EC2 and Amazon EBS](https://aws.amazon.com/marketplace/pp/B009KA3CRY/ref=ads_c0f426cd-130f-1469574566) | SAP Hana |
| [SQL Database on Microsoft Azure](https://azure.microsoft.com/en-us/services/sql-database/) | SQL Azure |
| [Google Cloud SQL](https://cloud.google.com/sql/) | MySQL |
| [Amazon RDS / MySQL](https://aws.amazon.com/rds/mysql/) | MySQL |
| [Amazon RDS / SQL Server](https://aws.amazon.com/rds/sqlserver/) | SQL Server |
| [Amazon RDS / PostgreSQL](https://aws.amazon.com/rds/postgresql/) | PostgreSQL |
| [Amazon RDS / Aurora for MySQL](https://aws.amazon.com/rds/aurora/) | MySQL |
| [Amazon RDS / Aurora for PostgreSQL](https://aws.amazon.com/rds/aurora/) | PostgreSQL |
| [Amazon RDS / MariaDB](https://aws.amazon.com/rds/mariadb/) | MySQL |
| [Amazon RDS / Oracle](https://aws.amazon.com/rds/oracle/) | Oracle |
| [DB2 on Cloud / IBM Bluemix](https://console.ng.bluemix.net/catalog/services/ibm-db2-on-cloud/) | DB2 Universal Database |
| [PostgreSQL by Compose / IBM Bluemix](https://console.ng.bluemix.net/catalog/services/postgresql-by-compose/) | PostgreSQL |
| [SQL Database / IBM Bluemix](https://console.ng.bluemix.net/catalog/services/sql-database/) | DB2 Universal Database |
| [ClearDB MySQL database / SuccessBricks, Inc. DBA ClearDB / in IBM Bluemix console](https://console.ng.bluemix.net/catalog/services/cleardb-mysql-database/) | MySQL |
| [ElephantSQL / 84codes AB / in IBM Bluemix console](https://console.ng.bluemix.net/catalog/services/elephantsql/) | PostgreSQL |

Disclaimer: This is not a complete list of the supported relational cloud databases, it just shows some of the cloud databases that are available and have been tested in some way (some fully, some partially) by the GeneXus team, or are being used (or have been for some time) by some GeneXus Community members.

See Also

* <https://blogs.gartner.com/adam-ronthal/2019/06/23/future-database-management-systems-cloud/>


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?58946) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55768) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) |
| [GeneXus and the DBMSes](https://wiki.genexus.com/commwiki/wiki?1772) | [Category:GeneXus Java Generator](https://wiki.genexus.com/commwiki/wiki?12258) | [HowTo: Deploy an Application to AWS Elastic Beanstalk](https://wiki.genexus.com/commwiki/wiki?32104) | [MariaDB](https://wiki.genexus.com/commwiki/wiki?31692) |

---
