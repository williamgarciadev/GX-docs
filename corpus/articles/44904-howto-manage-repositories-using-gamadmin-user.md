---
title: "HowTo: Manage repositories using gamadmin user"
source_id: 44904
source_url: https://wiki.genexus.com/commwiki/wiki?44904
genexus_version: "18"
---

# HowTo: Manage repositories using gamadmin user

As explained in [HowTo: Create New Repositories using GAM](https://wiki.genexus.com/commwiki/wiki?18642), by using the [GAM Backend](https://wiki.genexus.com/commwiki/wiki?15935) you can connect as an administrator of [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) and create, update, and delete Repositories. Then, this user can only edit the repository options of the newly created repositories.

In a [multitenant scenario](https://wiki.genexus.com/commwiki/wiki?18682) where the gamadmin user creates new repositories, they may need to perform certain actions that they cannot excecute as gamadmin in a new repository.

In these cases, when the user [sets a connection](https://wiki.genexus.com/commwiki/wiki?19245) to the repository, and tries to execute any API to the new connection, the login is shown.

To avoid logging in again, use the following method to enable the gamadmin user in the repository created.

```
(Boolean) GAM.RepositoryUserEnable(Numeric: RepositoryId,GAMUser: GAMUser, Numeric: AdministratorRoleId, GAMErrors Errors)
```

Consider the following:

* This method can be executed in a GAM Manager session, and the GAMUser specified in this case must be gamadmin.
* The parameter AdministratorRoleId indicates the Id of the administrator role, so the gamadmin user will be enabled in the repository using that role.

**Note:** The user has to be enabled in a repository where an Application has already been created. Otherwise, it will throw the following error:

```
 Application GUID RepId:x - AppGUID:y unidentified. Please contact the application administrator. (GAM174)
```

The following method allows disabling the user of the repository.

```
(Boolean) GAM.RepositoryUserDisable(Numeric: RepositoryId,GAMUser: GAMUser, Numeric: AdministratorRoleId, GAMErrors Errors)
```

In sum, the gamadmin user can also be enabled in other repositories (different from the GAM Manager repository). This allows the user to perform actions in the repository as if they were an administrator of that repository. The main purpose is to avoid forcing the user to log into the repository after setting the new connection.

### [Samples](#Samples)

Take a look at the GAMExampleRepositoryEntry object, where the following code is included after creating a new repository, enabling the gamadmin user to that repository.

```
&RepositoryNew = GAMRepository.GetByGUID(&GUID, &Errors) //&Errors is GAMError collection.
&GAMUser = GAMUser.Get()
&isOK = GAM.RepositoryUserEnable(&RepositoryNew.Id, &GAMUser, &AdministratorRoleId, &Errors)
```

Afterwards, the user can change the working repository (set the connection to that repository), and they won't be asked to log into that repository when trying to perform any GAM API action.

### [See Also](#See+Also)

[HowTo: Manage repositories using an admin user](https://wiki.genexus.com/commwiki/wiki?44937,,)


|  |
| --- |
| **Backlinks** |
| [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) |

---
