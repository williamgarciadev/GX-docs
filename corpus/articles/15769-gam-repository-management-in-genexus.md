---
title: "GAM repository management in GeneXus"
source_id: 15769
source_url: https://wiki.genexus.com/commwiki/wiki?15769
genexus_version: "18"
---

# GAM repository management in GeneXus

To get the [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568) ready to be used, some steps have to be executed from the GeneXus IDE.

This behavior results from the fact that when pressing F5 (Build All), GeneXus checks if it's necessary to create [GAM](https://wiki.genexus.com/commwiki/wiki?24746) database tables or execute a reorganization in the GAM database, or if there is nothing to do (because the GAM repository already exists and is up to date).

When pressing F5, a connection is established to the database specified in GAM [Data Store](https://wiki.genexus.com/commwiki/wiki?7117) (using the connection properties of this Data Store: database name, user ID, user password), and checks the existence of some tables and GAM version. If these tables don't exist, the GAM database tables are created with the [Repository ID](https://wiki.genexus.com/commwiki/wiki?15802) specified.

If these tables already exist, the necessary reorganization is executed. Next, an initialization is done where [Repository ID Environment property](https://wiki.genexus.com/commwiki/wiki?15802), [Administrator User Name property](https://wiki.genexus.com/commwiki/wiki?15215), [Administrator User Password property](https://wiki.genexus.com/commwiki/wiki?15216), [Connection User Name property](https://wiki.genexus.com/commwiki/wiki?15217), and [Connection User Password property](https://wiki.genexus.com/commwiki/wiki?15218) are checked.

In addition, upgrading the GAM version, changing the GAM data store, or creating a new environment are actions where some considerations should be taken into account.

This article sums up some of these situations and the considerations to be taken.

### [Case A. Creating the GAM repository](#Case+A.+Creating+the+GAM+repository)

See [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701)

### [Case B. Updating GAM (installing an upgrade)](#Case+B.+Updating+GAM+%28installing+an+upgrade%29)

Suppose you have a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) where [GAM is activated](https://wiki.genexus.com/commwiki/wiki?19946), but a new GeneXus build is installedand GAM has changed. Therefore, the GAM objects and the GAM repository need to be updated.

This update is done automatically. After performing a "Build All" in the KB, the following happens:

1. The [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) is imported.

2. The necessary reorganization is executed in the GAM repository.

### [Case C. Changing GAM Data Store properties or generator](#Case+C.+Changing+GAM+Data+Store+properties+or+generator)

After changing the GAM Data Store properties or the environment generator, you have to "Rebuild All" and all the GAM execution files (connection.gam and application.gam) are moved to the model directory.  
The database is reorganized if necessary.

### [Case D. Creating a secondary Environment in a KB where GAM is activated](#Case+D.+Creating+a+secondary+Environment+in+a+KB+where+GAM+is+activated)

If a new [Environment](https://wiki.genexus.com/commwiki/wiki?7115) is created in a KB where GAM is already activated, it is possible that the new environment uses the same GAM.

GeneXus detects when the database specified in the "Database name" property for the Reorg data store already has a GAM repository. If so, the [Administrator User Name Property](https://wiki.genexus.com/commwiki/wiki?15215), [Administrator User Password Property](https://wiki.genexus.com/commwiki/wiki?15216), [Connection User Name Property](https://wiki.genexus.com/commwiki/wiki?15217) and [Connection User Password Property](https://wiki.genexus.com/commwiki/wiki?15218) are not initialized, and the GeneXus user has to set those properties manually.

In this case, the [Repository ID Environment property](https://wiki.genexus.com/commwiki/wiki?15802) remains the same as the previous environment.

So, if in this new Environment, you specify the same database name as another existing environment of the KB, the connection properties have to be set manually.

If you specify a different GAM database, it's the same as explained in case A.

### [Case E. Connecting to an existing external GAM repository](#Case+E.+Connecting+to+an+existing+external+GAM+repository)

When connecting to an external GAM repository, the [Repository ID](https://wiki.genexus.com/commwiki/wiki?15802) property has to be set. In this case, when "Build All" is done, GeneXus detects that this repository (with the connection properties associated with it) is a valid GAM repository and there is no need to create a new GAM database or to make reorganizations to this database. This is the typical case of using GXserver, where many KBs will use the same GAM repository.

See [HowTo: Use the same GAM Database by different applications](https://wiki.genexus.com/commwiki/wiki?16151)

### [Case F. Managing more than one GAM Repository in GeneXus at prototyping time](#Case+F.+Managing+more+than+one+GAM+Repository+in+GeneXus+at+prototyping+time)

See [Managing GAM Repositories and GAM Applications in GX development time](https://wiki.genexus.com/commwiki/wiki?18685,,)


|  |
| --- |
| **Backlinks** |
| [GAM - Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) | [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) | [HowTo: Develop Secure REST Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?15918) |
| [HowTo: Use the same GAM Database by different applications](https://wiki.genexus.com/commwiki/wiki?16151) | [Repository ID Environment property](https://wiki.genexus.com/commwiki/wiki?15802) | [Require Access Permissions Application Property](https://wiki.genexus.com/commwiki/wiki?18512) |

---
