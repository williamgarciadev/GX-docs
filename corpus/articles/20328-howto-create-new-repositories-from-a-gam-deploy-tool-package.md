---
title: "HowTo: Create New Repositories from a GAM deploy tool package"
source_id: 20328
source_url: https://wiki.genexus.com/commwiki/wiki?20328
genexus_version: "18"
---

# HowTo: Create New Repositories from a GAM deploy tool package

This document explains how to create New Repositories from a GAM deploy tool package and provides a brief overview about it.

There are some scenarios where creating repositories without the presence of a user is necessary. To do this, you need to use the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535).

To achieve this, you must be able to execute a process capable of the creation of a repository and initialize it with certain users, roles and permissions, and afterwards, if needed, leave the user connected to that repository that was created.

One possible scenario where such functionality becomes necessary is in multi-tenant applications, where it is possible to create a repository with different [Repository Namespace](https://wiki.genexus.com/commwiki/wiki?18678,,) for each company, with the corresponding [GAM - Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150).

In order to do this, the CreateRepositoryFromPackage method of GAM object is used.

### [CreateRepositoryFromPackage GAM method](#CreateRepositoryFromPackage+GAM+method+)

These are the steps to be followed:

**1.** Create a pack (Export) with the [GAM - Deploy Tool](https://wiki.genexus.com/commwiki/wiki?18608), containing all the information necessary for initializing the repository to be created (users, roles, permissions, etc.).

**2.** Decompress the pack generated (.gpkg file) with any tool (for example: winzip), you need to decompress the Data directory only, which has all the information regarding the pack (.json files). This folder must be set in the &GAMImportRepositoryConfiguration.PackageDirectoryPath, (see example below).

**3.** Update the [connection.gam](http://www2.gxtechnical.com/portal/hgxpp001.aspx?15,4,61,O,E,0,,30451) file to include the [GAM - Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) to the [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617), as it is required to perform a connection to the GAM Manager Repository before executing the CreateRepositoryFromPackage method. You can see how to do it, [HowTo: Connect to GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18625).

**4.** Create a procedure for the configuration and creation of the new repository. Such procedure must include the following steps:

**1.** The first thing to do is connect to the [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617).

**2.** Set the data of the repository to be created (GUID, NameSpace, Description, etc.)  
This is done in an SDT based on the *GAMRepositoryCreate* data type.   
  
**Important:**

* Note that you need to specify a user name and user password which will be newly created. This user will be an administrator of the Repository which is being created, and will be associated to the Role that you indicate to be the administrator Role of the package being imported.The administrator Role is indicated through the *GAMImportRepositoryConfiguration* SDT, explained below.
* In this step you also specify a connection user and connection password, so a new [GAM - Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) will be created for the new repository, with the information given.

**3.** Perform the configuration of the repository.  
Here you can indicate the location of the pack with the data for initializing it. This is done in an SDT based on the *GAMImportRepositoryConfiguration*. In this step you need to indicate the GUID of the administrator Role of the package, by executing &GAMImportRepositoryConfiguration.AdministratorRole = <GUID>.  
In this step you also specify if you want to update the connection.gam file with the [GAM - Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) created.  
Note: In case that the application is running in a load balancing environment, only the connection.gam of the node of the cluster where the program executes is updated. The connection.gam has to be replicated manually to the other nodes of the cluster.

**4.** Perform the creation of the repository by executing the CreateRepositoryFromPackage method of GAM External Object.  
  
`[imagen omitida: wiki id 20475]`

**5.** If needed, do the connection of the newly-created repository. You need to have updated the connection.gam file if you want to connect to the new repository. The login to the new repository (\*) will work only if any of the [GAM - Applications](https://wiki.genexus.com/commwiki/wiki?15910) imported in this new repository have the same GUID as the Application GUID specified in the application.gam file of the running application.

### [Samples](#Samples)

The code below shows how to program a procedure including all the steps described for creating a repository with the GAM’s API, and leaving the user connected to the repository created.

```
// SetConnection to the GAM Manager Repository 
&isOK = GAM.SetConnection('GAM-Manager', &Errors)

// New Repository Data
&GAMRepositoryCreate.GUID = &GAMGUID //&GAMGUID is GAMGUID data type
&GAMRepositoryCreate.NameSpace = 'TestNameSpace'
&GAMRepositoryCreate.CanRegisterUsers = true
&GAMRepositoryCreate.GiveAnonymousSession = true
&GAMRepositoryCreate.Name = 'TestName'
&GAMRepositoryCreate.Description = 'Test Description'
//Administrator user which is going to be created in the repository
&GAMRepositoryCreate.AdministratorUserName = 'admin'
&GAMRepositoryCreate.AdministratorUserPassword = 'admin123'
//Connection user which is going to be created in the new repository
&GAMRepositoryCreate.ConnectionUserName = 'test'
&GAMRepositoryCreate.ConnectionUserPassword = 'test123'
&GAMRepositoryCreate.AllowOauthAccess = true

// New Repository Configuration
&GAMImportRepositoryConfiguration.PackageDirectoryPath = &PackageDirectoryPath // for example: 'C:\GAM\Data'
&GAMImportRepositoryConfiguration.RepositoryCreate = &GAMRepositoryCreate
&GAMImportRepositoryConfiguration.UpdateConnectionFile = true //do you want to update the connection.gam file online?
&GAMImportRepositoryConfiguration.AdministratorRole = '9c4dcb46-3a86-4a3f-85fb-04a25f91f87c' //GAM GUID of "Administrator" Role in the package

// New Repository creation
&isOK = GAM.CreateRepositoryFromPackage(&GAMImportRepositoryConfiguration, &Errors) //&Errors is collection of GAMError
do "Process Errors"

//If needed, SetConnection to the New Repository
&isOK = GAM.SetConnection('TestName', &Errors)
do "Process Errors"

// Login to the New Repository (*) if needed
&isOK = GAMRepository.Login(&User, &Password, &AdditionalParameter, &Errors)
do "Process Errors"

Sub "Process Errors"
For &Error in &Errors
 Msg(Format(!"%1 (GAM%2)", &Error.Message, &Error.Code))
EndFor
EndSub
```

#### [**Notes:**](#Notes%3A)

* The CreateRepositoryFromPackage method does not create the GAM database tables. The GAM has to exist with its structure and its metadata (the [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) has to exist in the GAM database). One possible way to create the GAM database structure and initialize its metadata is by running the [GAM - Deploy Tool](https://wiki.genexus.com/commwiki/wiki?18608) and selecting the "Create GAM database tables" option.
* For security reasons, this method should be executed after the user logs in as an administrator user of GAM-Manager Repository. The Genexus user has to make the final user to login with an administrator user of GAM Manager Repository. If the object which executes the method requires authentication, and if the user is not logged in, the login will be requested when you establish the connection to GAM Manager, and the user will have to login with the credentials of an administrator user of GAM Manager Repository.

### [See Also](#See+Also)

[HowTo: Update a repository from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20929)  
[HowTo: Create New Repositories using GAM](https://wiki.genexus.com/commwiki/wiki?18642)


|  |
| --- |
| **Backlinks** |
| [HowTo: Create New Repositories using GAM](https://wiki.genexus.com/commwiki/wiki?18642) | [HowTo: Update a repository from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20929) |

---
