---
title: "HowTo: Create New Repositories using GAM"
source_id: 18642
source_url: https://wiki.genexus.com/commwiki/wiki?18642
genexus_version: "18"
---

# HowTo: Create New Repositories using GAM

The purpose of this article is to explain the necessary steps to create New Repositories using GAM.

Bear in mind that only administrators of the [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) can create new [Repositories](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,).  
By using the [GAM Backend](https://wiki.genexus.com/commwiki/wiki?15935), you can connect as an administrator of [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) and create, update, and delete Repositories. The [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) provides the necessary methods to manage Repositories, so you can change the interface for these operations by changing the GAM Backend as desired.

### [Steps](#Steps)

**1.** [Connect to GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18625)

**2.** With "gamhome" of the GAM Backend running, select the "Repositories" option of the menu, under the "Settings" node (which calls the GAMExampleWWRepositories object). This option is available only when the current repository is "GAM Manager Repository".

There you can add, update, and delete repositories.

### [Creating a new Repository: basic settings](#Creating+a+new+Repository%3A+basic+settings)

`[imagen omitida: wiki id 51911]`

Then, you need to complete the following information (among other details):

* Use the current repository as the authentication master repository - See [GAM: Use the current repository as the authentication master repository](https://wiki.genexus.com/commwiki/wiki?46228).
* [Namespace](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18678,,) - Is the Namespace of the Repository. The Namespace is a way to group different Repositories which have something in common (e.g., the company they belong to). It is hidden if "Use the current repository as the authentication master repository" is checked.
* Connection User - The [Connection User](https://wiki.genexus.com/commwiki/wiki?15217) of the new Repository.
* Connection Password - The [Connection Password](https://wiki.genexus.com/commwiki/wiki?15218) of the new Repository.
* Authentication type name in current repository - It is shown in case "Use the current repository as the authentication master repository" is checked. It  refers to the authentication type for the Administrator User of the new Repository (e.g., local)
* Administrator User - The [Administrator User](https://wiki.genexus.com/commwiki/wiki?15215) of the new Repository.
* Administrator Password - The [Administrator Password](https://wiki.genexus.com/commwiki/wiki?15216) of the new Repository.  
    
  **Note:** If the administrator user is the same as any user of a different Repository that has the same Namespace as the new one, you have to specify this user's password. Otherwise, the following error will be thrown:

  ```
  Username already exists. (GAM49).
  ```

  This happens because users inherit the Namespace of the Repository where they belong. If a user is going to be defined in a Repository that has the same Namespace as any other, they are already an existing user.
  + It can be a specific role selected to be copied to the new repository (see 3. below).
  + It can also be a new role created automatically in the new repository. In this case, the role is called "Administrator", and it is assigned to the Role External Id = "is\_gam\_administrator". The main purpose of this is to enable users to access the GAM Web Backoffice. See [Restricted access to GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?18495). Afterwards, you may populate that role with all the [GAM Permissions](https://wiki.genexus.com/commwiki/wiki?15912) that you consider necessary.
* The administrator user is going to be assigned to the Administrator role of the repository. The Administrator role depends on the initialization of the repository.
* Update connection file - If checked, the *connection.gam* file is updated online. In this case, the *connection.gam* being used is merged with the connection information to connect to the new Repository. If you want to create a *connection.gam* file only with the connection information of the new Repository, see [HowTo: Get GAM Repository connection information](https://wiki.genexus.com/commwiki/wiki?19231).

The basic code to create a GAM repository is the following:

```
                &GUID = GUID.NewGuid().ToString()
                &RepositoryCreate.GUID                         = &GUID 
                &RepositoryCreate.Name                         = &Name 
                &RepositoryCreate.NameSpace                 = &NameSpace 
                &RepositoryCreate.Description                 = &Description 
                &RepositoryCreate.AdministratorUserName     = &AdministratorUserName 
                &RepositoryCreate.AdministratorUserPassword = &AdministratorUserPassword 
                &RepositoryCreate.AllowOauthAccess             = &AllowOauthAccess
                &RepositoryCreate.ConnectionUserName         = &ConnectionUserName 
                &RepositoryCreate.ConnectionUserPassword     = &ConnectionUserPassword 
                &RepositoryCreate.GenerateSessionStatistics    = &GenerateSessionStatistics
                &RepositoryCreate.GiveAnonymousSession         = True 
                &RepositoryCreate.AllowOauthAccess            = True
                &RepositoryCreate.CreateGAMApplication        = &CreateGAMApplication
                &isOK = &GAM.CreateRepository(&RepositoryCreate, &UpdateConnectionFile, &Errors) //&Errors is collection of GAMError.
                //RepositoryCreate is based on RepositoryCreate GAM object
                If &isOK
                      Commit
                Else
                      Do 'DisplayErrors'
                Endif
```

#### [**1.** CreateGAMApplication](#1.+CreateGAMApplication)

This property of the RepositoryCreate GAM object enables users to create the [GAM Backend Application](https://wiki.genexus.com/commwiki/wiki?29699) in the Repository that is going to be created.

If this Application isn't created, the users won't be able to execute the GAM Web Backoffice connected to that repository. Whether you need to activate CreateGAMApplication or not will depend on your particular case.

Code:

```
&RepositoryCreate.CreateGAMApplication        = &CreateGAMApplication
```

#### [**2.** Is the current user an administrator of the new repository?](#2.+Is+the+current+user+an+administrator+of+the+new+repository%3F)

It allows the logged user to be an administrator of the newly created repository.

See [gamadmin](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44937,,)and [admin](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44937,,) examples, where this property is explained in full detail.

**Important:** You can switch to any repository that was granted access using this checkbox (Is the current user an administrator of the new repository?). This checkbox uses the GAM.RepositoryUserEnable API method.

### [Creating a new Repository based on another one](#Creating+a+new+Repository+based+on+another+one)

You can initialize a repository using the settings of another one, by copying:

* The GAM Application (including menus and permissions)
* Roles (without permissions)
* Security Policies
* Role Permissions (the relation between permissions and roles)

`[imagen omitida: wiki id 51912]`

#### [**3.** CopyRoles](#3.+CopyRoles)

The Copy Roles option allows users to copy the roles of any repository (selected in the Repository Id combo) to the repository that is being created.

You must select the "Administrator Role Id", so the administrator user that is going to be created will belong to that role.

If you don't select an appropriate role, the following error is thrown:

```
You must configure an existing role in AdministratorRoleId property. (GAM39)
```

**Notes:**

* To add the roles' permissions, you must select the Copy Roles Permissions? option (see 5)
* If you don't copy roles from a repository, the "Administrator" role is created, and the "is\_gam\_administrator" External Role Id is added to that role. See [Restricted access to GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?18495).

#### [**4.** Copy Application?](#4.+Copy+Application%3F)

You can initialize the Repository with a GAM Application of another Repository (the repository selected in "Copy from Repository Id"). All the permissions and menus of that Application will be copied.  
You must enter an Application Id in the edit box "Copy from Application Id". Otherwise, it throws the error:

```
You must configure an existing application in the Repository x  (CopyFromRepositoryId). (GAM39)
```

#### [**5.** Copy Roles Permissions?](#5.+Copy+Roles+Permissions%3F)

If you need to copy the Roles-Permissions association, select this option.  
You must provide an Application Id (from where the Permissions are going to be copied), along with an Administrator Role Id (because all the Roles are going to be copied from one repository to the other and you have to indicate which is the Administrator role).  
The Administrator Role is used to know the role which is going to be assigned to the administrator user.

#### [**6.** Copy Security Policies?](#6.+Copy+Security+Policies%3F)

This option allows copying all the security policies from the repository indicated in "Copy from Repository Id".

### [Creating an application from scratch for the new repository](#Creating+an+application+from+scratch+for+the+new+repository+)

Instead of initializing a repository from the data of another one (copying the GAM Application of some repository), you can create a GAM Application from scratch, while simultaneously creating the repository and initializing that repository with the Application created.

In this scenario, the Application has to be populated with data afterwards.

**Note:** If you don't create any GAM Application in the repository before connecting to it, an error is thrown:

```
Application GUID unidentified. Please contact the application administrator. (GAM174).
```

In order to create an Application for the Repository, use the Application method of the GAMRepositoryCreate object.

**Example:**

```
GUID = GUID.NewGuid().ToString()
&RepositoryCreate.GUID                         = &GUID            //RepositoryCreate is based on RepositoryCreate GAM object
&RepositoryCreate.Name                         = &Name 
&RepositoryCreate.NameSpace                 = &NameSpace 
......
&GAMApplication.GUID = &GUIDApp  //&GAMApplication is based on GAMApplication GAM External Object
&GAMApplication.Name             = &Name
&GAMApplication.Description     = &AppDescription
&GAMApplication.Version         = "1.0"
&GAMApplication.AccessRequiresPermission             = TRUE
            
&RepositoryCreate.Application    = &GAMApplication
&isOK = &GAM.CreateRepository(&RepositoryCreate, TRUE, &Errors)
```

**Notes:**

* If you use the CopyFromApplicationId method, it overrides the Application method of the RepositoryCreate object.
* Another possibility is to import the Application data into an empty repository (using the [GAM Deploy Tool](https://wiki.genexus.com/commwiki/wiki?18608)).

### [See Also](#See+Also)

[HowTo: Create New Repositories from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20328)


|  |
| --- |
| **Backlinks** |
| [GAM - Multiple Repositories Scenarios](https://wiki.genexus.com/commwiki/wiki?18682) | [GAM - Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) | [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Connect to GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18625) | [HowTo: Create New Repositories from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20328) |
| [HowTo: Emulate SSO without using GAM remote authentication](https://wiki.genexus.com/commwiki/wiki?38116) | [HowTo: Get GAM Repository connection information and create a connection file](https://wiki.genexus.com/commwiki/wiki?19231) | [HowTo: Manage repositories using gamadmin user](https://wiki.genexus.com/commwiki/wiki?44904) |
|

---
