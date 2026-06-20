---
title: "Defining a JDBC Datasource"
source_id: 2112
source_url: https://wiki.genexus.com/commwiki/wiki?2112
genexus_version: "18"
---

# Defining a JDBC Datasource

When executing a web based application, the developer has the possibility of using a JDBC Datasource to connect to database.

Using a JDBC datasource means that the Application server is in charge of the database connection, the [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) implementation is not used.

In order to use this feature, enable the [Use Datasource for Web Based Applications Property](https://wiki.genexus.com/commwiki/wiki?9384,,).

### [Advantages and disadvantages of using a JDBC Datasource](#Advantages+and+disadvantages+of+using+a+JDBC+Datasource)

#### [**Advantages**](#Advantages)

* It is possible to monitor the application from J2EE server instead of changing client.cfg.
* Some datasources have important features like connection monitoring (in order to pull it off when killed).
* It is possible to use [JTA](https://wiki.genexus.com/commwiki/wiki?2111).
* It is possible to change connection parameters on run-time (in [Before Connect](https://wiki.genexus.com/commwiki/wiki?8997) event).
* You can configure that BC's TRN are managed by the container when Call Protocol property is set to Enterprise Java Bean value.

#### [**Disadvantages**](#Disadvantages)

* Some pools doesn't recycle connections.
* It doesn't keep a memory cache of prepared sentences (or it is done only one per request and all are killed at the end).

### [See also](#See+also)

[JDBC Datasource in Tomcat 8 (or higher)](https://wiki.genexus.com/commwiki/wiki?11820)  
[Tomcat](https://wiki.genexus.com/commwiki/wiki?2217,,)  
[Websphere](https://wiki.genexus.com/commwiki/wiki?2218,,)  
[Weblogic](https://wiki.genexus.com/commwiki/wiki?2219,,)  
[Oracle App Server 10g](https://wiki.genexus.com/commwiki/wiki?4095,,)  
[JDBC Datasource on JBoss](https://wiki.genexus.com/commwiki/wiki?4115,,)


|  |
| --- |
| **Backlinks** |
| [Deploying a Java application on a JBoss server](https://wiki.genexus.com/commwiki/wiki?46032) |

---
