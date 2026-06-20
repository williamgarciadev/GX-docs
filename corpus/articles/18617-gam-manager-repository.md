---
title: "GAM Manager Repository"
source_id: 18617
source_url: https://wiki.genexus.com/commwiki/wiki?18617
genexus_version: "18"
---

# GAM Manager Repository

A [GAM](https://wiki.genexus.com/commwiki/wiki?14960) database can allocate more than one [Repository](https://wiki.genexus.com/commwiki/wiki?18463,,). In fact, there are always at least two Repositories in a GAM database.  
The "GAM Manager Repository" is a predefined repository in GAM. This is where administrator users of all repositories are defined.

The default administrator user of  "GAM Manager Repository" (created when the [GAM metadata is initialized](https://wiki.genexus.com/commwiki/wiki?15769)), is "gamadmin", whose password is "gamadmin123" by default. 

### [gamadmin user](#gamadmin+user)

This is the default user (created in GAM metadata initialization) of the GAM Manager Repository. This user's password has to be changed when going into production.  
You can define new users in the GAM Manager Repository (as many as you want).

The purpose of the "gamadmin" user is to do the following tasks:

* Manage users of "GAM Manager Repository"
* [Create new Repositories](https://wiki.genexus.com/commwiki/wiki?18642)
* Use the [GAMDeployTool](https://wiki.genexus.com/commwiki/wiki?18608) to create [GAM Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) in the connection.gam file. See [GAM Deploy Tool: Creating connection.gam file](https://wiki.genexus.com/commwiki/wiki?18610)
* Use the [GAMDeployTool](https://wiki.genexus.com/commwiki/wiki?18608) to [export data from any Repository and import data into any other](https://wiki.genexus.com/commwiki/wiki?18872).
* Edit the repository options of other repositories (such as General, User, and Session properties). See the screenshots below:

`[imagen omitida: wiki id 44950]`

`[imagen omitida: wiki id 44951]`

The gamadmin user isn't allowed by default to perform other actions in the repositories (such as listing the users of the repository). So, the admin user of each reposiory is compelled to log into that repository to execute those actions.

For an scenario where the gamadmin user manages several repositories (a multitenant scenario), and you need that he can perform actions as an administrator of the repository, see [HowTo: Manage repositories using gamadmin user](https://wiki.genexus.com/commwiki/wiki?44904).

### [Note](#Note)

Any repository can also behave as the GAM Manager although it isn't the GAM Manager. See [HowTo: Manage repositories using an admin user](https://wiki.genexus.com/commwiki/wiki?44937,,).

### [See Also](#See+Also)

[HowTo: Connect to GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18625)


|  |
| --- |
| **Backlinks** |
| [GAM deploy tool command line (only windows)](https://wiki.genexus.com/commwiki/wiki?30642) | [GAM Deploy Tool: Creating the connection.gam file](https://wiki.genexus.com/commwiki/wiki?18610) | [GAM Deploy Tool: Export Data](https://wiki.genexus.com/commwiki/wiki?18872) |
| [GAM Deploy Tool: Import Data](https://wiki.genexus.com/commwiki/wiki?21974) | [GAM repository creation for the first time from GeneXus](https://wiki.genexus.com/commwiki/wiki?29701) | [GetAliveSessionCount method](https://wiki.genexus.com/commwiki/wiki?34397) |
| [GetSessionLogsCount method](https://wiki.genexus.com/commwiki/wiki?45864) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [HowTo: Connect to GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18625) | [HowTo: Create New Repositories from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20328) |
| [HowTo: Create New Repositories using GAM](https://wiki.genexus.com/commwiki/wiki?18642) | [HowTo: Get GAM Repository connection information and create a connection file](https://wiki.genexus.com/commwiki/wiki?19231) | [HowTo: Manage repositories using gamadmin user](https://wiki.genexus.com/commwiki/wiki?44904) |
| [HowTo: Update a repository from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20929) | [Login Object for SD property](https://wiki.genexus.com/commwiki/wiki?16589) |

---
