---
title: "GAM - Applications deployment"
source_id: 21219
source_url: https://wiki.genexus.com/commwiki/wiki?21219
genexus_version: "18"
---

# GAM - Applications deployment

The purpose of this document is to explain how to take binaries to production, in an application using [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746).   
To import the data of the GAM Database into production, refer to [Deploy Tool](https://wiki.genexus.com/commwiki/wiki?18608).

### [Step by step](#Step+by+step)

1. Set up a pre-production environment.

It's advisable to have a pre-production environment where you can set up the application binaries and data before going into production.

* In the pre-production environment, you can use GeneXus to create the GAM Database from scratch, and do a build all prior to taking it to production. The GAM permissions will be created in the build all process because the permissions don't exist in the Database.
* In the GeneXus pre-production environment, configure a new [Connection User Name](https://wiki.genexus.com/commwiki/wiki?15217) and [Connection User Password](https://wiki.genexus.com/commwiki/wiki?15218), to create a new [GAM connection](https://wiki.genexus.com/commwiki/wiki?16150) with those credentials. This [GAM connection](https://wiki.genexus.com/commwiki/wiki?16150) will be different from the one configured for the test environment.
* Use the GAM Deploy Tool to do an export from the test environment, in order to import it into the pre-production Database. You may export the GAM Applications, [GAM Roles](https://wiki.genexus.com/commwiki/wiki?17569), [GAM Permissions](https://wiki.genexus.com/commwiki/wiki?15912), and GAM Security policies.  
  An alternative to using the GAM Deploy Tool, is using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) to populate your GAM pre-production database (creating, for example, GAM Roles and GAM Security policies).

**Notes:**

* In general, except in special cases, you will not export the GAM users from the test environment. Special care must be put in not carrying out to production users with high privileges that were created for test purposes only.
* You will always have a [GAM Application](https://wiki.genexus.com/commwiki/wiki?15910) related to your Knowledge Base (web GAM Application). At pre-production, you should define the KB with the same name as in the test environment. Otherwise, upon exporting the GAM Applications from test and importing at pre-production, you will have two different GAM Applications for Web.

2. Create the deploy file.

1. After doing the necessary test at pre-production, use the  [Applications Deploy tool](https://wiki.genexus.com/commwiki/wiki?32092) to create the deployment. The deployment includes the application.gam and the connection.gam files, required to connect to the GAM Repository. The deployment would include or not the GAM Backend binaries, depending on the [Include GAM Backend property](https://wiki.genexus.com/commwiki/wiki?44996).
2. At production: one possibility is, for the first time, to back up the database at pre-production and restore it at production.  
   Another option is to use the Deploy Tool. In such case, if you use the [GAM deploy tool command line](https://wiki.genexus.com/commwiki/wiki?43623,,), you will first have to create the database tables using the script distributed by GeneXus (under <GX Folder>\GAM\Platforms). Then you will do a full export at pre-production and a full import at production. You should use the "import" option with the "-new\_rep\_create" flag.  
   If you create a new connection.gam in production, you must bear in mind that, the next time you make changes to production, you will not overwrite the connection.gam.  Another possibility is to copy the GAM connections from pre-production to production, using the "-imp\_connections" flag. In this case, the connection.gam is valid for both environments, so you will not need to make changes to the deployment.

In sum, depending on the method used, you will have different options for completing the process of going into production.

Consider, in all cases, that:

* You should use the [Applications deploy tool](https://wiki.genexus.com/commwiki/wiki?32092) to build the deployment package, and deploy it to the cloud if desired.
* After having the new [Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) is created in the production database, you may update [connection.gam](https://www.genexus.com/developers/websac?en,,,30451) file using Deploy Tool. The connection.gam file is located under the web directory.
* For security reasons, consider: [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [GAM platforms](https://wiki.genexus.com/commwiki/wiki?22119) |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) |

---
