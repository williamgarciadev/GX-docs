---
title: "GXflow - GAM Integration"
source_id: 18454
source_url: https://wiki.genexus.com/commwiki/wiki?18454
genexus_version: "18"
---

# GXflow - GAM Integration

When GXflow is integrated with [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746), all user and role management (regarding security issues) are delegated to GAM. Even if GAM stores the information on Roles and Users, that information is stored in the GXflow tables as well.

As a consequence, Users and Roles have to be synchronized from GAM to GXflow or vice versa, to guarantee the right flow of the application. Roles are necessary for the GeneXus IDE to be assigned to Tasks. Users and roles need to be synchronized in GAM to handle the application security, and in the GXflow tables to assign the different scheduled tasks.

Synchronization can be made globally (synchronize a group of users and roles and their relation in any direction: from GXflow to GAM or vice versa), or it can be made interactively.

**Warning:** When you integrate GXflow with GAM, it will use only one kind of authentication, the one set as default in the repository configuration. Remember that GAM with Custom Authentication checks external credentials (e.g. through [LDAP](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?29473,,)). If you use the [Workflow APIs](https://wiki.genexus.com/commwiki/wiki?11364) for managing users must ensure that they are provided by the *credentials provider*.

## [Global Synchronization of Users and Roles](#Global+Synchronization+of+Users+and+Roles)

### [1. User synchronization](#1.+User+synchronization)

|  |  |
| --- | --- |
| **From GAM to GXflow** | **From GXflow to GAM** |
| 1. When you assign the role "GXflow public" to a user from GAM backoffice or using GAM API then this user is created in the GXflow database also. | 1. Users, roles, and their relations are synchronized to GAM by running the *apwfmigrateuserstogam* procedure (manual synchronization). |
| 2. Users are globally synchronized to GXflow by running the *apwfsynchronizegamusers* procedure (manual synchronization). | 2. Synchronization is automatically executed in the Build process.  *=== Migrate workflow users to GAM started ==========  .....  Migrate workflow users to GAM Success* |

**Notes**

* **Limitation**: When a GAM username is modified, GXflow treats it as a new user during the synchronization. In such a case, both usernames will coexist in GXFlow (the recently updated and the old one), but only the recently updated will correspond to the GAM user.
* The role "GXflow public" must be directly assigned to the user to allow them to log in. If a role that has "GXflow public" as a child role is assigned instead, the user won't be able to log in.

### [2. Role Synchronization](#2.+Role+Synchronization)

|  |  |
| --- | --- |
| **From GAM to GeneXus IDE** | **From GeneXus IDE to GAM** |
| 1. When the Knowledge Base is opened, Roles created, updated or deleted in the GAM will be created, updated or deleted in the GeneXus IDE.  You can see the roles through the [Workflow Preferences](https://wiki.genexus.com/commwiki/wiki?17839) >  [BPD Roles](https://wiki.genexus.com/commwiki/wiki?11864) option. In this case, GAM to GeneXus synchronization is automatically performed when the KB is opened. | 1. The automatic synchronization of Roles from GeneXus to GAM is done:  * the first time the KB is opened, * at Build all, * at Rebuild all, * at deployment.  You will notice the following messages on the Build output:  *===Export roles to GAM started ===  .....  Role RoleName1 successfully exported  Role RoleName2 successfully exported  .....  Export roles to GAM Success* 2. Manual synchronization of roles can only be done by running the *apwfmigraterolestogam* procedure.  This is available since GeneXus X Evolution 3 Upgrade 5. |
| 2. Synchronization can also be forced using the option Tools -> [Workflow Tools](https://wiki.genexus.com/commwiki/wiki?17111) -> [Synchronize GAM roles option](https://wiki.genexus.com/commwiki/wiki?18462) | 3. Synchronization can also be forced using the option Tools -> [Workflow Tools](https://wiki.genexus.com/commwiki/wiki?17111) -> [Synchronize GAM roles option](https://wiki.genexus.com/commwiki/wiki?18462) |

**Notes**

* To disable automatic synchronization, you can use the config.gx (If the file doesn´t exist, you need to create the file in the Model directory) with the *DisableGamRolesSync*property = True.

### 

## [How to run a manual synchronization](#How+to+run+a+manual+synchronization)

The procedure apwfmigraterolestogam migrates the Rol information from the GXflow database to the GAM database.

The procedure apwfmigrateuserstogam migrates the User information and also the Roles assigned to the user from the GXflow database to the GAM database. Also adds automatically the Rol GXflow Public to the user in the GAM database.

The procedure apwfsynchronizegamusers takes all the users defined in the GAM database which has the role GXflow Public and updates the user information and role assignment from the GAM database to the GXflow database.

**To run a manual synchronization, use the following command lines:**

### [Net](#Net)

The synchronization procedures are located in the \bin folder. You may run them as follows:

```
C:\Models\...\CSharpModel\web\bin>apwfmigraterolestogam.exe

C:\Models\...\CSharpModel\web\bin>apwfmigrateuserstogam.exe

C:\Models\...\CSharpModel\web\bin>apwfsynchronizegamusers.exe
```

### [NetCore](#NetCore)

The synchronization procedures are located in the \bin folder. You may run them as follows:

```
C:\Models\...\NetCoreModel\web\bin>dotnet apwfmigraterolestogam.dll

C:\Models\...\NetCoreModel\web\bin>dotnet apwfmigrateuserstogam.dll

C:\Models\...\NetCoreModel\web\bin>dotnet apwfsynchronizegamusers.dll
```

### [Java](#Java)

The synchronization procedures are located in the <application>\WEB-INF\classes\com\gxflow folder. To run them, set the current working directory to "\classes" level folder and execute them as follows:

```
C:\..\<application>\WEB-INF\classes>java -cp ".;..\lib\*" com.gxflow.apwfmigraterolestogam

C:\..\<application>\WEB-INF\classes>java -cp ".;..\lib\*" com.gxflow.apwfmigrateuserstogam

C:\..\<application>\WEB-INF\classes>java -cp ".;..\lib\*" com.gxflow.apwfsynchronizegamusers
```

When using Java, make sure you have the connection.gam file under C:\..\<application>\WEB-INF\classes. Otherwise, these error messages will be displayed:

```
"Invalid GAM repository, GXflow roles required" error or "Error 2: Repository not found. Please contact the application administrator".
​​​​​​java -cp ".;..\lib\*" com.gxflow.apwfsynchronizegamusers
Invalid GAM repository, GXflow roles required
java -cp ".;..\lib\*" com.gxflow.apwfmigraterolestogam
Role: GXflow Public
Error 30: The connection to GAM was not found. Please contact the application administrator.
Role: All
```

See [Troubleshooting the GXflow-GAM manual synchronization](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?29534,,)

## [Interactive synchronization of Users and Roles](#Interactive+synchronization+of+Users+and+Roles)

In versions older than [GeneXus X Evolution 3 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?29463,,), you need to use both the [GXflow API](https://wiki.genexus.com/commwiki/wiki?17230) and the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) to handle users and roles.

Since [GeneXus X Evolution 3 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?29463,,), the GXflow API to handle users and roles directly impacts on GAM users and roles. See [GXFlow API integrated to GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?29508,,). As a consequence, you just need to use the GXflow API of the GXflow management console.

### [User Nomination](#User+Nomination)

You can add users and roles from the GAM back office. Note that, when adding the "GXflow Public" role to a user, GXflow will try a user nomination during the login operation for that user (if the user has not been nominated yet).

#### [**Notes:**](#Notes%3A)

Since [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?33798,,):

* When adding the "GXflow Public" role to a user, it is created and if there is a nominated license available, it is tried to be nominated, too. In the case that a user is not created and you use the [GXFlow API integrated to GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?29508,,) or during the login operation, it will be created (if it does not exist) and attempted to be nominated.
* Every CRUD operation over users and roles in GAM Backend are automatically reflected in GXFlow Client, and vice versa. If you use previous GeneXus versions you are restricted to handle users and roles manually by using [GXFlow API integrated to GAM](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?29508,,).

## [See Also](#See+Also)

[GXflow - GAM Initialization](https://wiki.genexus.com/commwiki/wiki?33095)  
[GXflow Custom Client with GAM](https://wiki.genexus.com/commwiki/wiki?29533)  
[Business Process Deployer](https://wiki.genexus.com/commwiki/wiki?11607)


|  |
| --- |
| **Backlinks** |
| [Aspects to consider when using GeneXus BPM Suite with GAM](https://wiki.genexus.com/commwiki/wiki?43858) | [Category:BPD Roles](https://wiki.genexus.com/commwiki/wiki?11864) |
| [Table of contents:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |
| [GXflow - GAM Initialization](https://wiki.genexus.com/commwiki/wiki?33095) | [GXflow Backend](https://wiki.genexus.com/commwiki/wiki?25704) |

---
