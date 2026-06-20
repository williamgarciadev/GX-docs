---
title: "GAM - Deploy Tool"
source_id: 18608
source_url: https://wiki.genexus.com/commwiki/wiki?18608
genexus_version: "18"
---

# GAM - Deploy Tool

GAM Deploy Tool is a tool that has multiple purposes, all of them related to the manage and deployment of data updates using [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746).

The GAM DeployTool can be executed from inside GeneXus (Tools > GAM > Create Deploy File) or in stand-alone mode (see the Download below).

The tool is aimed at taking into production the information which needs to be updated in the GAM Database.  
It is not an export/import utility as it is known, but it represents a tool that has the knowledge of the GAM Database structure and relations and gives the possibility to import data in a gradual way keeping the consistency of the GAM data model.

After exporting data from the GAM Database, a package is obtained containing all or some of the entities which are going to be taken into the production Database (which can use a different DBMS).

The end-user has the ability to select the desired entities that are going to be imported into the Database (Applications, Roles, Users, etc).  
Although records of some tables could not be present in the export package and may be present in the production Database, the import process does not remove those records.

The data is not removed in general, but it is updated if necessary (which makes the difference with the usual import/export utilities of the DBMS).

The tool does not remove relations between records, but it adds or updates relations. For example, if a role is exported with its permissions, it can happen that this role already exists in the production Database. In this case, if some of the permissions are not related to the role, the relation to these permissions is created, but the other relations to the permissions table of this role (which existed prior to the import) are not removed.

During the import, the hierarchy of permissions and roles is considered, so as it keeps the same relation as it exists in the Database from where the data was exported.

GAM Users are entities related to one or more GAM repositories and when imported, this fact is taken into consideration, see [GAM Deploy Tool - Import Users](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22017,,) for more information.

The following are the different options that can be executed using the GAM DeployTool.

* Export data - Export data from any existing repository, see [GAM Deploy Tool: Export Data](https://wiki.genexus.com/commwiki/wiki?18872)
* Import data - Import data to a new or existing repository, see [GAM Deploy Tool: Import Data](https://wiki.genexus.com/commwiki/wiki?21974)
* Create GAM Database - In order to create GAM Database from outside GeneXus and initialize its metadata you can select the "Create GAM Database" option in the first window of the GAMDeployTool wizard.
* Update GAM schema - Update the GAM Database structure.
* Generate connection file - See [GAM Deploy Tool: Creating the connection.gam file](https://wiki.genexus.com/commwiki/wiki?18610)

It supports all platforms (SQL Server, Mysql, Postgresql, Oracle, DB2). The tool uses ADO to connect to the Database, so you need the corresponding ADO client of the DBMS you want to connect to, in the case of Iseries, the client V6R1 is required.

In the case of Oracle, the port and database name have to be specified in the tnsnames.ora file.

When executing the tool, a log file (GamLog.log) is saved in the temporary directory of the user.

### [Important notes](#Important+notes)

* To do any actions with the GAM deploy tool, you should use the user "gamadmin"  (predefined in repository 1).
* To export data from any GAM Database you have to use the GAM deploy tool corresponding to the version of GAM.   
  For example, in the case of [GAM database version 3.0.6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?25352,,) download the tool from [here](https://www.genexus.com/en/developers/downloadcenter?data=5316;gam%20deploy%20tool;).   
  In sum, the GAM deploy tool has the knowledge of the Database schema of its own version.
* To update the GAM Database structure, you can use the Update Schema option of the tool. For example, to update to [Database version 4.0.3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?34457,,) you can use the GAM deploy tool which supports that version, and Update the Database schema of a GAM Database of a prior version.
* If you import a package exported from a [Database version 4.0.3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?34457,,) using the GAM Deploy tool of 4.0.3 into a 3.0.6 Database, a reorg will be done to change the Database structure. That's another way of updating the Database schema.

### [See Also](#See+Also)

[GAM Deploy Tool command line (Windows and Unix-like operating systems)](https://wiki.genexus.com/commwiki/wiki?37764)


|  |
| --- |
| **Backlinks** |
| [Deploying a Java application on a JBoss server](https://wiki.genexus.com/commwiki/wiki?46032) | [GAM - Applications deployment](https://wiki.genexus.com/commwiki/wiki?21219) |
|
| [GAM - Update Connection File](https://wiki.genexus.com/commwiki/wiki?18690) |
| [GAM deploy tool command line (only windows)](https://wiki.genexus.com/commwiki/wiki?30642) | [GAM Deploy Tool command line (Windows and Unix-like operating systems)](https://wiki.genexus.com/commwiki/wiki?37764) | [GAM Deploy Tool: Creating the connection.gam file](https://wiki.genexus.com/commwiki/wiki?18610) | [GAM Deploy Tool: Export Data](https://wiki.genexus.com/commwiki/wiki?18872) |
| [GAM Deploy Tool: Import Data](https://wiki.genexus.com/commwiki/wiki?21974) | [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [GeneXus SAP Systems Deployment to a Production Environment](https://wiki.genexus.com/commwiki/wiki?35466) |
| [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [HowTo: Connect to GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18625) | [HowTo: Create New Repositories from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20328) |
| [HowTo: Create New Repositories using GAM](https://wiki.genexus.com/commwiki/wiki?18642) | [HowTo: Emulate SSO without using GAM remote authentication](https://wiki.genexus.com/commwiki/wiki?38116) | [HowTo: Generate trace of GAM Deploy Tool](https://wiki.genexus.com/commwiki/wiki?26297) |
| [HowTo: Update a repository from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20929) |

---
