---
title: "Scenario of multi-tenant application with GXflow and GAM"
source_id: 44766
source_url: https://wiki.genexus.com/commwiki/wiki?44766
genexus_version: "18"
---

# Scenario of multi-tenant application with GXflow and GAM

The purpose of this document is to provide a solution for the scenario of a multi-tenant application that uses GXflow and GAM, where the application is also to be deployed in the same Web Application, using the same database with the system’s and the GAM’s tables for all Tenants in the application.

### [Architecture](#Architecture)

Since GXflow does not support a multi-tenant schema where all tenants share the same database, the architecture recommended for such a scenario is the following:

* There is a database with the tables corresponding to the system and the GAM.
* A GXflow database is necessary for each tenant.
* The application’s binaries are deployed in the same Web Application, meaning that, the binaries of the application, and of the GAM and GXflow will be executed on the same Web Application.

#### [Notes:](#Notes%3A)

* For this scenario, it is recommended to set up the GXflow licenses on a protection server, in order to centralize their administration.
* It is not possible to use the SQL statement cache in this scenario.

### [Setting up the development environment](#Setting+up+the+development+environment)

Below is a description of the steps to follow in setting up the development environment.

1. Activate GAM and create a database with tables in the application and the GAM.
2. Modify the connection.gam to allow the possibility of creating multiple repositories.
   1. Go to the option: Tools\GeneXus Access Manager\Update connection file, enter with user gamadmin, and select both repositories. (For further details on how to set up the GAM in this scenario, read [Multiple Repository Scenario: The same application installation is shared by many companies](https://wiki.genexus.com/commwiki/wiki?18710,,)).
   2. This will enable the possibility of access with user gamadmin to create new repositories for each Tenant.
3. Create GXflow datastore and indicate a database name different from that of the Default datastore.
4. Create some process diagrams to enable GXflow in the KB.
5. In the Environment properties, set up the "Deploy business processes on build" property with value No.
6. Export the processes created with the BPDeployer tool.
7. Execute the BPDeployer tool and import the exported processes. This tool will create the database the first time, as well as the GXflow tables, in addition to impacting the exported processes.
8. A procedure must be created to associate the Before Connect event, where information on the session is read to define the company, and based on it, you obtain the logic on which is the name of the GXflow database that corresponds to that company.  
   1. This is an example of how this procedure could be done, assuming that the session variable 'CompanyId' was previously set up in the system’s login screen and that the name of the GXflow database is parameterized for each company.
   2. ```
      &CompanyId = val(&Session.Get('CompanyId'))

      For Each
      Where CompanyId = &CompanyId
            &Database = CompanyDatabaseName
      Endfor

      If not &Database.IsEmpty()
         &dbconn = GetDatastore('GXflow')
         &dbconn.ConnectionData = 'DATABASE=' + &Database.Trim()
      Endif
      ```
9. Disabling the automatic synchronization that the IDE does between the GAM and GXflow is recommended. To that end, a config.gx file must be created in the KB’s root directory, with content  DisableGamRolesSync= True
10. Edit the file client.exe.config with the information of the GXflow datastore so that it will point to the new database.
11. Execute, by commands line, the **apwfinitializegam.exe** program, passing, as a parameter, the name of the repository created in step 1. This will be initiating the roles of GXflow, the permits, and the subscriptions to events within the GAM.

### [Impact of changes on the processes](#Impact+of+changes+on+the+processes)

When you want to include changes at the process level, the following is required:  
  
1.    Create an export of the changes with the option **Tools > Workflow > Create business deploy file** and select the processes to be exported. This will also take the information of the Roles defined in the IDE.  
2.    Use the Business Process Deployer tool to import the file generated in the previous step, connecting to the GXflow base.  
3.    To synchronize the new roles with the GAM you must:

1.    Edit the client.exe.config file with the information of the GXflow datastore so that it will point at the GXflow database.  
2.    Execute, commands line, the apwfmigraterolestogam.exe program, passing, as a parameter, the name of the GAM’s repository against which you want to synchronize.

### [Process for adding a new Tenant](#Process+for+adding+a+new+Tenant)

The following steps indicate what must be done on the GAM side and on the GXflow in order to add a new Tenant to the system:

1. Create a new repository in the GAM.
2. Export, with the BPDeployer tool, the corresponding processes for the new Tenant.
3. Use the BPDeployer tool and select the file generated in step 2.
   1. This tool will create the database if it does not exist, as well as the GXflow tables for the first time. It will also impact the processes and roles within the GXflow tables.
4. Edit the client.exe.config file with the information of the GXflow datastore so that it will point at the new GXflow database.
5. Execute, by commands line, the apwfinitializegam.exe program, passing, as a parameter, the name of the repository created in step 1.
6. Execute, by commands line, the apwfmigraterolestogam.exe program, passing, as a parameter, the name of the repository created in step 1, to synchronize the roles defined in GXflow towards the GAM repository.
7. Go to the GXflow License Manager Web and set up the licenses.
8. Following the previous steps, you may start creating users that will be part of the processes and assign to them the "GXflow Public" role, in addition to the typical roles of the processes.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
