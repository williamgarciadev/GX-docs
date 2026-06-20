---
title: "GAM Deploy Tool command line (Windows and Unix-like operating systems)"
source_id: 37764
source_url: https://wiki.genexus.com/commwiki/wiki?37764
genexus_version: "18"
---

# GAM Deploy Tool command line (Windows and Unix-like operating systems)

The GAM Deploy Tool command line is designed to perform various security-related operations in GeneXus applications. It is compatible with both Windows and Unix-like operating systems.

Note that while the GAM Deploy Tool supports many functions of the UI tool, it does not handle the creation and reorganization of GAM database tables. These tasks must be managed by the DBA using dedicated reorganization scripts.

### [**Important note**](#Important+note)

For security reasons, the GAM Deploy Tool (GDT) will no longer automatically be included in the applications. The GDT is distributed with GeneXus where it was usually distributed (<GeneXusInstallation/Library/GAM/Platforms/<Generator&DBMS>), within each platform there will be a GAMDeployTool.zip file that will contain everything necessary to run this tool independently.

### [Functions and actions](#Functions+and+actions)

This tool allows running several types of actions, so the call must have this format:

```
JAVA: <unzip_GDT_folder>/library
java -cp ./* genexus.security.api.agamdeploytool "<Action> <Corresponding Flags>"

.NET Framework: <unzip_GDT_folder>/bin
agamdeploytool.exe "<Action> <Corresponding Flags>"

.NET: <unzip_GDT_folder>/bin
 dotnet agamdeploytool.dll "<Action> <Corresponding Flags>"
```

### [JAVA](#JAVA)

The configuration files for connection to the database must be in the current directory (where the commands will be executed), these files are client.cfg and the application.key and **must be copied to the GDT Library folder**.

* The client.cfg file it's located under: *<application\_server>/webapps/<your\_webapp>/WEB-INF/<your\_app\_package>*
* The application.key file it's located under: *<application\_server>/webapps/<your\_webapp>/WEB-INF*

### [.NET Framework](#.NET+Framework)

The configuration files for connection to the database must be in the current directory (where the commands will be executed), these files are client.exe.config and application.key and **must be copied to the GDT BIN folder**.

* The client.exe.config file it's located under: *<application\_server>/<your\_virtual\_directory>/bin*
* The application.key file it's located under: *<application\_server>/<your\_virtual\_directory>/bin*

The tool doesn't ask for the GAM database connection settings (such as the server, port, user, and password) because that information is taken from the configuration files mentioned before.

It's distributed together with the GAM libraries, for each corresponding DBMS.

### [.NET Core](#.NET+Core)

The configuration files for connection to the database must be in the current directory (where the commands will be executed), these files are client.exe.config and application.key and **must be copied to the GDT BIN folder**.

* The client.exe.config file it's located under: ...*/<KB\_Name>/<Environment>/Library/GAM*
* The application.key file it's located under: ...*/<KB\_Name>/<Environment>/Web/bin*

The tool doesn't ask for the GAM database connection settings (such as the server, port, user, and password) because that information is taken from the configuration files mentioned before.

It's distributed together with the GAM libraries, for each corresponding DBMS.

**Note**: In case you have configured any procedure in the Event Handling properties of the Generator, see the following [SAC](https://www.genexus.com/developers/websac?en,,,60675).

### [Important Note](#Important+Note)

If you need the GAMDeployTool to generate LOG, you must copy the log.console.config and log.config files to the GAMDeployTool BIN folder in the case of .Net or NetFramework and the log4j2.xml file to the Library folder in the case of Java.

If you need more information about Logging in GeneXus, see the following document: [Log level property](https://wiki.genexus.com/commwiki/wiki?36304)

## [Tool parameters](#+Tool+parameters)

The actions provided by the tool are as follows:

|  |  |
| --- | --- |
| **Action** | **Description** |
| [-Initialize](#Initialize) | Initializes the GAM database with its metadata |
| [-Import](#Import) | Imports a package |
| -UpgradeGAM | Updates the GAM database version. If a reorganization is necessary, the user will have to previously perform it and then run this tool action. |
| -Help | Shows the actions available in the tool. |
| [-Export](#Export) | Exports a GAM database data and stores it in a .gpkg package. |
| [-GetConnections](#GetConnections) | Obtains the connections grouped by Repository. This function is useful to obtain the repository GUIDs and connection names that will be sent as parameters in the UpdateConnectionFile option. |
| [-UpdateConnectionFile](#UpdateConnectionFile) | Updates/Creates the Connection.gam file with the connection data it obtains. |
| -xml\_config\_file | This is a special flag that only receives an XML file in which all the parameters to enter in the tool are loaded, including the action. The XML format is the one given by the -GenerateXML flag. |
| -GenerateXML | Generates a sample XML and displays it in standard output. It's a sample XML that can be used as input for the tool, changing the corresponding tag values. |

For each action, different flags are expected:

### [Initialize](#Initialize)

|  |  |
| --- | --- |
| **Flag** | **Description** |
| -admin\_name | It's the GAM admin name (default: gamadmin) |
| -admin\_pass | It's the GAM admin password (default: gamadmin123) |
| -xml\_config\_file  string | Indicates the path to the XML file that has all the parameters configured. If this flag is set, all the others are automatically ignored and only the file parameters are taken into account. |
| -help | Shows the flags expected for this action. |

### [UpgradeGAM](#UpgradeGAM)

|  |  |
| --- | --- |
| **Flag** | **Description** |
| -admin\_name *(\*)* | It's the GAM admin name |
| -admin\_pass *(\*)* | It's the GAM admin password |
| -xml\_config\_file  string | Indicates the path to the XML file that has all the parameters configured. If this flag is set, all the others are automatically ignored and only the file parameters are taken into account. |
| -help | Shows the flags expected for this action. |

(\*)required flag.

### [Export](#Export)

|  |  |
| --- | --- |
| **Flag** | **Description** |
| -admin\_name *(\*)* | It's the GAM admin name. |
| -admin\_pass *(\*)* | It's the GAM admin password. |
| -target *(\*)* | It's the target directory where the package is to be stored. |
| -rep\_guid *(\*)* | GUID of the repository to be exported. |
| -pkg\_name *(\*)* | It's the name that will be given to the exported package. |
| -full\_export (true/false) | If this flag is set to true, a full export is made, as follows: All roles, users, and applications. |
| -exp\_users (true/false) | Indicates if the users are to be exported (it only works if full\_export  = false) |
| -exp\_roles (true/false) | Indicates if the roles are to be exported (it only works if full\_export  = false) |
| -exp\_eve\_subscriptions  (true/false) | Indicates if the event subscriptions data will be exported (it only works if full\_export  = false). Available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?39737,,). |
| -verbose (true/false) |  |
| -apps | It's the list of GUIDs of applications to be exported. Format: App\_Guid\_1,App\_Guid\_2,App\_Guid\_3 |
| -roles | It's the list of GUIDs of roles to be exported. Format: Role\_Guid\_1,Role\_Guid\_2,Role\_Guid\_3 |
| -xml\_config\_file | Indicates the path to the XML file that has all the parameters configured. If this flag is set, all the others are automatically ignored and only the file parameters are taken into account. The format is the same as that of the import SDT. |

*(\*)**required flag*.

### [Import](#Import)

|  |  |
| --- | --- |
| **Flag** | **Description** |
| -file\_path\_package | Receives the package to import. |
| -admin\_name *(\*)* | It's the GAM admin name. |
| -admin\_pass *(\*)* | It's the GAM admin password. |
| -admin\_user\_name | It's the administrator user name. |
| -admin\_role\_guid*(\*\*)* | GUID of the administrator role. |
| -upd\_rep (true/false) | Indicates if an update of the existing repository is to be made. |
| -upd\_rep\_guid | Indicates the GUID of the repository to update. It is used if the flag -upd\_rep = true. |
| -new\_rep\_create (true/false) | Indicates if a new repository is to be created. |
| -new\_rep\_name *(\*\*)* | It's the name of the new repository. |
| -new\_rep\_namespace*(\*\*)* | It's the namespace of the new repository. |
| -new\_rep\_guid *(\*\*)* | It's the GUID of the new repository. |
| -new\_rep\_admin\_name *(\*\*)* | It's the name of the new repository admin. |
| -new\_rep\_admin\_pass *(\*\*)* | It's the password of the new repository admin. |
| -new\_rep\_conn\_usr\_name *(\*\*)* | It's the new repository connection user name. |
| -new\_rep\_conn\_usr\_pass *(\*\*)* | It's the password of the new repository connection user. |
| -imp\_auth\_types (true/false) | Indicates if the authentication types are to be imported. |
| -imp\_sec\_policies (true/false) | Indicates if the security policies are to be imported. |
| -imp\_users (true/false) | Indicates if the users are to be imported. |
| -imp\_roles (true/false) | Indicates if the roles are to be imported. |
| -imp\_full (true/false) | Indicates that all the entities will be imported (auth\_types, sec\_policies, users, roles, apps, connections, eve\_subscriptions). Available since GeneXus 16 upgrade 6. |
| -disable\_upd\_role\_prm (true/false) | Indicates whether the permissions of the roles that already exist in the Database should be imported  The default value is false. |
| -imp\_apps (full/none/custom) | It's the level with which the applications are imported.   * full: all applications are imported with all permissions * none: nothing is imported in relation to applications * custom: they are configured according to -imp\_apps\_details. |
| -imp\_apps\_details *(\*\*\*)* | It's the list of "GUID,Boolean" pairs of (applicationsGuids,ImportPermissionsOfThatApplication) to be imported.  Format: App\_Guid\_1,Imp\_Prms\_App1;App\_Guid\_2,Imp\_Prms\_App2;App\_Guid\_3,Imp\_Prms\_App3 |
| -imp\_connections | Import the package connections. The connection name is changed to <original name> + Repository Id.  For new repositories, a new connection is always created, regardless of the value of this flag.  If the repository is being updated, and -imp\_connections=true, the connections are imported if they don't have the same connection user name of an existing connection. In other words, the connections are not updated. |
| -imp\_eve\_subscriptions | Import the events subscriptions data. Available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?39737,,) |
| -verbose (true/false) |  |
| -connection\_gam\_file\_path | It's the target directory where the connection.gam file is to be generated. |
| -xml\_config\_file | Indicates the path to the XML file that has all the parameters configured. If this flag is set, all the others are automatically ignored and only the file parameters are taken into account. |
| -help |  |

*(\*) required flag.  
(\*\*) flags required if flag new\_rep\_create = true.  
(\*\*\*) flags required if imp\_apps = custom.*

**Note:** After the import of the first user repository you will need to get the connection.gam from where it was configured to be generated in the tool (-connection\_gam\_file\_path). If you need to copy the connection.gam file to production take it from this path, and if you need to define an environment variable you must open this file (connection.gam) and copy the Key tag value in the environment variable [GX\_GAMCONNECTIONKEY](https://wiki.genexus.com/commwiki/wiki?59028). Additionally, if the GAMDeployTool does not include the drivers for the DBMS used, these must also be copied manually to ensure proper operation.

### [GetConnections](#GetConnections)

|  |  |
| --- | --- |
| **Flag** | **Description** |
| -admin\_name *(\*)* | It's the GAM admin name (for example: gamadmin). |
| -admin\_pass *(\*)* | It's the GAM admin password (for example: gamadmin123). |
| -xml\_config\_file | Indicates the path to the XML file that has all the parameters configured. If this flag is set, all the others are automatically ignored and only the file parameters are taken into account. |
| -help | Shows the flags expected for this action. |

*(\*) required flag.*

### [UpdateConnectionFile](#UpdateConnectionFile)

|  |  |
| --- | --- |
| **Flag** | **Description** |
| -admin\_name *(\*)* | It's the GAM admin name (for example: gamadmin). |
| -admin\_pass *(\*)* | It's the GAM admin password (for example: gamadmin123). |
| -target | It's the target directory where the connection.gam file is to be generated. |
| -connections *(\*)* | It's a list with the following format: <GuidRepoA>,<NameOfAConnectionOfRepoA>;<GuidRepoB>,<NameOfAConnectionOfRepoB> |
| -xml\_config\_file | Indicates the path to the XML file that has all the parameters configured. If this flag is set, all the others are automatically ignored and only the file parameters are taken into account. |

*(\*) required flag.*

## [Samples of how to execute the tool](#Samples+of+how+to+execute+the+tool)

The default password for gamadmin user is gamadmin123.

### [Initializa GAM database (JAVA)](#Initializa+GAM+database+%28JAVA%29)

<unzip\_GDT\_folder>/library> java -cp ./\* genexus.security.api.agamdeploytool -initialize -admin\_name gamadmin -admin\_pass <your\_gamadmin\_pass>

### [Initialize GAM database (.NET)](#Initialize+GAM+database+%28.NET%29)

```
<unzip_GDT_folder>/bin> dotnet agamdeploytool.dll -initialize -admin_name gamadmin -admin_pass <your_gamadmin_pass>
```

### [Upgrade GAM database version (.NET)](#Upgrade+GAM+database+version+%28.NET%29)

```
<unzip_GDT_folder>/bin> dotnet agamdeploytool.dll -upgradegam -admin_name gamadmin -admin_pass <your_gamadmin_pass>
```

### [Upgrade GAM database version (JAVA)](#Upgrade+GAM+database+version+%28JAVA%29)

```
<unzip_GDT_folder>/library>java -cp ./* genexus.security.api.agamdeploytool -upgradegam -admin_name gamadmin -admin_pass <your_gamadmin_pass>
```

### [Upgrade GAM database version (.NET Framework)](#Upgrade+GAM+database+version+%28.NET+Framework%29)

```
<unzip_GDT_folder>/bin> agamdeploytool.exe -upgradegam -admin_name gamadmin -admin_pass <your_gamadmin_pass>
```

### [Get connections  (.NET Framework)](#Get+connections+%28.NET+Framework%29)

```
<unzip_GDT_folder>/bin> agamdeploytool.exe -getconnections -admin_name gamadmin -admin_pass <your_gamadmin_pass>
```

### [Updating connection file (.NET Framework)](#Updating+connection+file+%28.NET+Framework%29)

```
<unzip_GDT_folder>/bin> agamdeploytool.exe -updateconnectionfile -admin_name gamadmin -admin_pass <your_gamadmin_pass> -target C:\Models\TestGDT\CSharpModel\web\ -connections 92b783a2-2a50-4261-8ba7-684fb780967d,GAM-Manager
```

### [Creating a new repository (JAVA)](#Creating+a+new+repository+%28JAVA%29)

```
<unzip_GDT_folder>/library>java -cp ./* genexus.security.api.agamdeploytool -import -admin_name gamadmin -admin_pass <your_gamadmin_pass> -file_path_package /home/sabrina/test.gpkg -new_rep_create true -new_rep_name testrepo -new_rep_namespace testrepo -new_rep_admin_name adminnew -new_rep_admin_pass admin123 -new_rep_guid 19bd e07d-8b37-4668-8c65-4cab29d8a38c -verbose true -new_rep_conn_usr_name newconn -new_rep_conn_usr_pass newconn123 -admin_role_guid 2a984733-5308-4444-b893-473200d40eda -imp_connections true
```

### [Exporting a repository (JAVA)](#Exporting+a+repository+%28JAVA%29)

```
<unzip_GDT_folder>/library>java -cp ./* genexus.security.api.agamdeploytool -export -target /home/sabrina -admin_name gamadmin -admin_pass <your_gamadmin_pass> -full_export TRUE -pkg_name test -rep_guid 1e89a9ca-bc52-482b-a344-c4cda4a9cc8f
```

## [Important notes](#Important+notes)

* You may need to copy the client.cfg to the classes directory if you have a package.
* If you are getting errors of access denied when connecting to the DBMS when executing one of the tool actions, please check the following: [SAC#43289](https://www.genexus.com/developers/websac?es,,,43289).


|  |
| --- |
| **Backlinks** |
| [GAM deploy tool command line (windows and unix-like OS) (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57888) | [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
