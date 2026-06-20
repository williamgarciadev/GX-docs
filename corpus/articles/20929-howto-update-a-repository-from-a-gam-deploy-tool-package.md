---
title: "HowTo: Update a repository from a GAM deploy tool package"
source_id: 20929
source_url: https://wiki.genexus.com/commwiki/wiki?20929
genexus_version: "18"
---

# HowTo: Update a repository from a GAM deploy tool package

The purpose of this document is to explain how to import data in an existing repository, using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535). The method which is going to be used is UpdateRepository, which is one of the methods of GAMRepository Object.

### [UpdateRepository  method of GAMRepository Object](#UpdateRepository+method+of+GAMRepository+Object)

Here we show the steps to be followed:

* Create a pack (Export) with the [Deploy Tool](https://wiki.genexus.com/commwiki/wiki?18608), containing all the information necessary for updating an existing repository (roles, applications).

* Decompress the pack generated (.gpkg file) with any tool (for example: winzip). You need to decompress the Data directory only, which has all the information regarding the pack (.json files). This directory must be set in the &GAMUpdateRepositoryConfiguration.PackageDirectoryPath (see example below).
* Update the [connection.gam](http://www2.gxtechnical.com/portal/hgxpp001.aspx?15,4,61,O,E,0,,30451;S;0;A;0;0;CONNECTION.GAM;;;;;;;;;;;;;;;;A;%20%20/%20%20/%20%20;;0;9;;0;;99;;0;1;%200;N;N;S;B;P) file.  
  There are two possible ways to update a repository using the UpdateRepository method of GAMRepository object; one of them is by connecting to the [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617).  
  The other is to connect to the repository which is going to be updated. Both ways are valid.  
  So, update the connection.gam file to include the [Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) to the [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) or the Repository you want to update. You can see how to do it in the following link: [GAM Deploy Tool: Creating the connection.gam file](https://wiki.genexus.com/commwiki/wiki?18610).

The code to update a GAM repository has to include the following:

* Connection to the [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) or the Repository you are going to update.
* Set the values to a variable based on GAMUpdateRepositoryConfiguration object, where you can specify:

1. PackageDirectoryPath : Path where the Data directory of the package was decompressed and can be found.
2. ImportAllRoles (Boolean): True if you want to import all [Roles](https://wiki.genexus.com/commwiki/wiki?17569) of the package.
3. ImportAllApplications (Boolean):  True if you want to import all [Applications](https://wiki.genexus.com/commwiki/wiki?15910) of the package.
4. ApplicationsToImport : Based on a collection of GAMUpdateRepositoryConfigurationApplicationsToImportSDT, where you can specify the GUID of the Application you want to import.

Take into account that the import criteria is the same as the one explained in [GAM Deploy Tool: Export Data](https://wiki.genexus.com/commwiki/wiki?18872).

### [Example](#Example)

I. In this case we connect to the Repository where we want to perform the update. First update connection.gam with a connection to this Repository, in the example its name is "TestGAMdeployTool2".

```
&isOK = GAM.SetConnection('TestGAMdeployTool2', &Errors)//&Errors is collection of GAMError
if not &isOK
  do "process errors"
else
 
//Perform a Full Import
&GAMRepository.Load(&Id)
&GAMUpdateRepositoryConfiguration.ImportAllApplications = True
&GAMUpdateRepositoryConfiguration.ImportAllRoles = True
&GAMUpdateRepositoryConfiguration.PackageDirectoryPath = &PackageDirectoryPath
&isOK = &GAMRepository.UpdateFromPackage(&GAMUpdateRepositoryConfiguration, &Errors)

if &isOK
  &GAMRepository.Save()
  //continue the execution
else
  do "Process errors"
endif
endif

sub "Process errors"
  For &GAMError in &Errors
   msg("   " + &GAMError.Message + "(GAM:" + &GAMError.Code + ")")
  EndFor
endsub
```

II. In this case we connect to the GAM Manager Repository in order to update any other Repository. First update connection.gam with a connection to GAM Manager Repository.

```
&isOK = GAM.SetConnection('GAM-Manager', &Errors)
if not &isOK
  do "process errors"
else

// Perform a Full Import
&GAMRepository.Load(&Id)
&GAMUpdateRepositoryConfiguration.FullImport = True
&GAMUpdateRepositoryConfiguration.ImportAllApplications = True
&GAMUpdateRepositoryConfiguration.ImportAllRoles = True
&GAMUpdateRepositoryConfiguration.PackageDirectoryPath = &PackageDirectoryPath
&isOK = &GAMRepository.UpdateFromPackage(&GAMUpdateRepositoryConfiguration, &Errors)

if &isOK
   &GAMRepository.Save()
   //Continue the execution
else
  do "Process errors"
endif

endif
```

The GAMUpdateRepositoryConfiguration object has the FullImport property. For the time being a FullImport means importing roles and applications (permissions) only.

### [Note](#Note)

The method should be executed after the user logs in as an administrator user of the GAM Manager Repository.

### [See Also](#See+Also)

[HowTo: Create New Repositories from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20328)


|  |
| --- |
| **Backlinks** |
| [HowTo: Create New Repositories from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20328) |

---
