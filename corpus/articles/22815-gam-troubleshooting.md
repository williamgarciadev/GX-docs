---
title: "GAM - Troubleshooting"
source_id: 22815
source_url: https://wiki.genexus.com/commwiki/wiki?22815
genexus_version: "18"
---

# GAM - Troubleshooting

This page summarizes some of the errors related to the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) that may be encountered through the various stages (during the build process or at runtime). It explains the causes of those errors and how to solve them.

### [In the Build process](#In+the+Build+process)

#### [**1. GAM(): Repository connection failed for user.**](#1.+GAM%28%29%3A+Repository+connection+failed+for+user.)

Detailed error:

```
error: Cannot connect with GAM repository with the given Administrator or Connection user.
error: GAM(): Connection not found.
error: GAM(): Repository connection failed for user.
Integrated Security Initialization Failed
error: Build canceled.
error: Operation Canceled by the user
Run Developer Menu Failed
```

**Cause:** Must specify information on [Administrator User Name property](https://wiki.genexus.com/commwiki/wiki?15215), [Administrator User Password property](https://wiki.genexus.com/commwiki/wiki?15216), [Connection User Name property](https://wiki.genexus.com/commwiki/wiki?15217), or [Connection User Password property](https://wiki.genexus.com/commwiki/wiki?15218).  
This may happen when the GAM’s database already exists and the GAM’s corresponding Administrator user and Connection user were not specified in the properties.  
In the case of a KB with an environment ('Env1') with enabled GAM (Enable Integrated Security property= True), if a new environment ('Env2') is created.  
If the setting of the GAM’s datastore of Env2 is the same as that of the datastore of Env1; for example, when the database name of the main datastore of Env2 setting is equal to the database name of environment Env1, and if default values are always taken, then the database of the GAM datastore of Env2 will be the same as that of Env1.  
Another case is the creation of a KB where the GAM’s datastore (database name) is set to point to a DB that already contains a [GAM - Repository](https://wiki.genexus.com/commwiki/wiki?17568).  
When F5 is run without previously assigning Administrator User Name Property, Administrator User Password Property, Connection User Name Property, or Connection User Password Property, the above error will occur.

#### [**2. GAM(): Repository password failed for user x.x.**](#2.+GAM%28%29%3A+Repository+password+failed+for+user+x.x.)

Detailed error:

```
error: Cannot connect with GAM repository with the given Administrator or Connection user.
error: GAM(): Repository password failed for user testreg1.testreg1.
Integrated Security Initialization Failed
error: Build canceled.
error: Operation Canceled by the user
Run Developer Menu Failed
```

**Cause:** [Connection User Password property](https://wiki.genexus.com/commwiki/wiki?15218) wrongly set up.

#### [**3. GAM(): Repository connection failed for user testreg1.testreg.**](#3.+GAM%28%29%3A+Repository+connection+failed+for+user+testreg1.testreg.)

Detailed error:

```
error: Cannot connect with GAM repository with the given Administrator or Connection user.
error: GAM(): Connection not found.
error: GAM(): Repository connection failed for user testreg1.testreg.
Integrated Security Initialization Failed
error: Build canceled.
error: Operation Canceled by the user
Run Developer Menu Failed
```

**Causes:**  
• Setting of [Connection User Name property](https://wiki.genexus.com/commwiki/wiki?15217), or [Connection User Password property](https://wiki.genexus.com/commwiki/wiki?15218) wrong or does not exist for that database in the GAM.  
• Wrong setting of the GAM’s [Repository ID Environment property](https://wiki.genexus.com/commwiki/wiki?15802).

#### [**4. GAM(): User password incorrect.**](#4.+GAM%28%29%3A+User+password+incorrect.)

Detailed error:

```
error: Cannot connect with GAM repository with the given Administrator or Connection user.
error: GAM(): User password incorrect.
Integrated Security Initialization Failed
error: Build canceled.
error: Operation Canceled by the user
Run Developer Menu Failed
```

**Cause:** [Administrator User Password property](https://wiki.genexus.com/commwiki/wiki?15216) wrongly set up.

#### [**5. GAM(): User unknown.**](#5.+GAM%28%29%3A+User+unknown.)

Detailed error:

```
error: Cannot connect with GAM repository with the given Administrator or Connection user.
error: GAM(): User unknown.
Integrated Security Initialization Failed
error: Build canceled.
error: Operation Canceled by the user
Run Developer Menu Failed
```

**Cause:** [Administrator User Password property](https://wiki.genexus.com/commwiki/wiki?15216) wrongly set up, does not exist. Note that the Administrator user is created only when the GAM’s database is created. If the database already exists, then the user specified in the corresponding property must exist in the database.

#### [**6. Application environment not found. (GAM133)**](#6.+Application+environment+not+found.+%28GAM133%29)

```
GAM Permissions Creation
Reading KB Applications ...
Application environment not found. (GAM133)
```

**Cause:**  
[GAM Permissions](https://wiki.genexus.com/commwiki/wiki?15912) are generated in association with each GAM Application. This error may occur if, upon generating permissions, the GAM does not find an application in the GAM’s database that is identified by the value set in the [Application ID property](https://wiki.genexus.com/commwiki/wiki?18667). The value of this property is auto-assigned when a KB is created and the GAM is enabled. It is editable to allow a KB to point to an existing DB in the GAM and use an existing application.

#### [**7. Your password has expired, please change it now. (GAM24)**](#7.+Your+password+has+expired%2C+please+change+it+now.+%28GAM24%29)

```
Registering 'Dashboard1'...Your password has expired, please change it now. (GAM24)
error: Cannot register the application in GAM repository.
error: GAM(): Your password has expired, please change it now.
Failed
```

**Cause:** The password of the administrator user shown in the Administrator User Name Property has expired. You must go through the [GAM - Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) to change the password and then assign that value to the Administrator User Password Property.

#### [**8. Unable to load DLL 'libmySQL.dll': The specified module could not be found.**](#8.+Unable+to+load+DLL+%27libmySQL.dll%27%3A+The+specified+module+could+not+be+found.)

```
========== Retrieve GAM Version From Database started ==========
error: Unable to load DLL 'libmySQL.dll': The specified module could not be found. (Exception from HRESULT: 0x8007007E)
Current GAM version:
Retrieve GAM Version From Database Success
```

**Cause:** GAM processes running in the GeneXus IDE useC#and ADO.NET to connect to the GAM’s database (detect GAM version in the database, record applications, generate permits).  
This is why the ADO.NET client corresponding to the DBMS used is required; for MySQL, download it from [here](https://wiki.genexus.com/commwiki/wiki?2041,,). You need to install the driver for 32 bits because the processes inside GX IDE use 32 bits; therefore, the 32-bit libmysql.dll has to be copied to the c:\windows\syswow64 folder. At runtime, you can use the driver for 64 bits.

### [In compilation](#In+compilation)

#### [**1. error CS0006: Metadata file 'bin\Artech.Security.dll' could not be found.**](#1.+error+CS0006%3A+Metadata+file+%27bin%5CArtech.Security.dll%27+could+not+be+found.)

```
error CS0006: Metadata file 'bin\Artech.Security.dll' could not be found
Compiling gamsdlogin_gamlogin_section_general...failed ( error code=1)
Microsoft (R) Visual C# 2008 Compiler version 3.5.30729.5420 for Microsoft (R) .NET Framework version 3.5
Copyright (C) Microsoft Corporation. All rights reserved.
```

**Solution:** Must have GAM enabled in the model when consolidating objects that refer to the GAM’s external objects. Also, in NET models, Compiler Flags must be set with value /r:bin\Artech.Security.API.Common.dll.

### [At runtime](#At+runtime)

#### [**1.  Repository password failed for user x.x. (GAM33).**](#1.+Repository+password+failed+for+user+x.x.+%28GAM33%29.)

A failure occurred when verifying the Repository Connection.  
The connection.gam file is not correct according to the connections defined in that Repository.

#### [**2. Connection not found. (GAM30)**](#2.+Connection+not+found.+%28GAM30%29)

connection.gam not found in the web application.

#### [**3. Application GUID unidentified, please contact the administrator. (GAM174).**](#3.+Application+GUID+unidentified%2C+please+contact+the+administrator.+%28GAM174%29.)

application.gam file not found.

#### [**4. Repository not found, please contact the application's administrator. (GAM2).**](#4.+Repository+not+found%2C+please+contact+the+application%27s+administrator.+%28GAM2%29.)

The information on the connection.gam does not match the information on the GAM’s Repository table. Verify that the connection.gam located in the application’s directory is the right one.

#### [**5. The connection password for user% 1 is not correct, please contact the GAM administrator. (GAM33).**](#5.+The+connection+password+for+user%25+1+is+not+correct%2C+please+contact+the+GAM+administrator.+%28GAM33%29.)

**Cause:** the connection.gam is not in accordance with the Repository Connections. Specifically, there is a difference in the connection password for the user.

Probably, one of the following is happening:

* The password of the connection user has changed, and you haven't changed it in the "Connection User Password property" accordingly.

By default, the password is <name of the KB>123, see [Connection User Password property](https://wiki.genexus.com/commwiki/wiki?15218).

If it has been changed, you need to know the new password. Otherwise, you have to generate a new [Repository Connection](https://wiki.genexus.com/commwiki/wiki?16150).

* The connection.gam is not correct or is not updated. In this case, you can remove it from the web folder so it can be generated again by the [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

For additional information, see [this](https://www5.genexus.com/meeting2017/gx27.session.aspx?es,GAM-Herramientas-fundamentales-para-el-desarrollo) link.

#### [**6. Error in webservice response, the service is not responding, please contact the application's administrator. (GAM40).**](#6.+Error+in+webservice+response%2C+the+service+is+not+responding%2C+please+contact+the+application%27s+administrator.+%28GAM40%29.)

Go to [GAM - How to debug errors when using External Web Service Authentication Type](https://wiki.genexus.com/commwiki/wiki?19715,,).

#### [**7. Authentication service error, please contact the application's administrator.(GeneXus.Programs.gamwslogin in agamwslogin.dll not found) (GAM12).**](#7.+Authentication+service+error%2C+please+contact+the+application%27s+administrator.%28GeneXus.Programs.gamwslogin+in+agamwslogin.dll+not+found%29+%28GAM12%29.)

With [Custom Authentication Type](https://wiki.genexus.com/commwiki/wiki?21751), the error is thrown when the authentication type is misconfigured.

If the external Procedure is called "gamwslogin", the error is thrown when the class name is set to gamwslogin instead of agamwslogin.

#### [**8. Http 1.00 - Connection has been shutdown: javax.net.ssl.SSLHandshakeException.**](#8.+Http+1.00+-+Connection+has+been+shutdown%3A+javax.net.ssl.SSLHandshakeException.)

If the application authenticates using Facebook, you get the following error:

**Http 1.00 - Connection has been shutdown: javax.net.ssl.SSLHandshakeException**:sun.security.validator.validatorException:PKIX path building failed:sun.security.provider.certpath:SunCertPathBuilderException: unable to find valid certification path to request target - StatusCode:0

Check that Java 1.7 or higher is installed on the application server. See [GAM Facebook Authentication Type](https://wiki.genexus.com/commwiki/wiki?16516,,) (Software Requirements).

#### [**9. Repository connection failed for user XXX. Please contact the application administrator. (GAM32).**](#9.+Repository+connection+failed+for+user+XXX.+Please+contact+the+application+administrator.+%28GAM32%29.)

Sometimes this error could appear. The problem is related to the decrypt algorithm when trying to decrypt the GAM User. See [SAC #36371](https://www.genexus.com/en/developers/websac?data=36371;;) for further information.

#### [**10. Java.sql.DataTruncation: Data truncation.**](#10.+Java.sql.DataTruncation%3A+Data+truncation.)

When using iSeries, take into account that the date data type fields in GAM tables are created as char data types, so the [Date data type definition property](https://wiki.genexus.com/commwiki/wiki?53796) must be set to Char, not to Date.

Otherwise, the application throws the exception: java.sql.DataTruncation: Data truncation. For more information, see [SAC 36455](https://www.genexus.com/en/developers/websac?data=36455;;).

#### [**11. GAM\_ApplicationClientRevoked: Application client revoked.**](#11.+GAM_ApplicationClientRevoked%3A+Application+client+revoked.)

Deploying to a server shows the GAM111 error when executing the GAMRepository.GetOuthAccessToken method. Verify that the machine's Timezone configuration is consistent. Otherwise please check the [SAC #45012: GAM111 - Application Client Revoked](https://www.genexus.com/en/developers/websac?data=45012;;) notes.

### [GAM Deploy Tool](#GAM+Deploy+Tool)

**1. The selected database does not have a GAM database schema.**

In the user's temp directory (by default: C:\UsersName) verify the generated log (example: GamLog\_3cc7a1cb-54f5-427a-a78c-36c94d1db266.log).

**Cause:**

* The Template.client.exe.config file is not found in the corresponding platform directory.
* The client.exe.config file is not being accessed due to a permissions problem.

 Both errors are shown in the log generated in the temp directory mentioned above.

**Solution:**

The Template.client.exe.config file is not found in the corresponding platform directory:

* Locate the "Template.client.exe.config" file located by default in: C:\<yourPath>\Library\GAM\Platforms.
* Copy this file to: C:\<yourPath>\GAM Deploy Tool\Resources\Platforms.

The client.exe.config file is not being accessed due to a permissions problem:

* Verify the permissions that you have on the file in question, if it is possible to give it all the permissions.

### [**Note**](#Note)

Since GeneXus 15 upgrade 4, to generate a trace for the processes that run within the IDE, do the following:

* Activate the .NET or Java log (depending on the environment)
* If you indicate a relative path to the log, it's generated under <data model>\Library\GAM

For older versions of GeneXus:

Edit the file <GeneXus>\library\gam\gamclient.exe.config.template and modify: <log4net threshold="All">.  
The generated log file is located in the model directory (more specifically at <data model>\Library\GAM\gamclient.log).

### [See Also](#See+Also)

[HowTo: Generate GAM trace](https://wiki.genexus.com/commwiki/wiki?25395,,)  
[HowTo: Generate trace of GAM Deploy Tool](https://wiki.genexus.com/commwiki/wiki?26297)  
[Error Codes and Messages for GAM](https://wiki.genexus.com/commwiki/wiki?27734,,)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Generate GAM trace](https://wiki.genexus.com/commwiki/wiki?50469) | [HowTo: Generate trace of GAM Deploy Tool](https://wiki.genexus.com/commwiki/wiki?26297) |

---
