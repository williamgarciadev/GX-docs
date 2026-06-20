---
title: "GAM deploy tool command line (only windows)"
source_id: 30642
source_url: https://wiki.genexus.com/commwiki/wiki?30642
genexus_version: "18"
---

# GAM deploy tool command line (only windows)

The  [GAM - Deploy Tool](https://wiki.genexus.com/commwiki/wiki?18608) performs the task of importing/exporting a package via command line. Its behavior is similar when running in UI mode. All the information requested from the user through the UI can be specified using the argument indicated for this purpose.

This tool only runs in Windows (gamdeploytool.exe), and it's distributed stand-alone.

### [Valid Arguments](#Valid+Arguments)

•    -apps mode: It allows specifying which applications will be imported. The values admitted are: none, all, {app\_guid1,...,app\_guidn}. With the "all" value, all the applications included in the package will be imported. The "none" value indicates the opposite action, meaning that no application will be imported. It can also be applied to one of the applications to be inserted, separating their GUID by commas.  
•    -config\_file\_path name: If specified, it indicates where to copy the configuration file (client.exe.config) created for executing the GX processes.  
•    -conn\_string\_additional\_args args: Additional arguments taken into account when building the connection string to the DB.  
•    -connection\_gam\_file dir: Name of the directory where the connection.gam file will be saved with the inserted data.  
•    -dbms code \*: It matches the code of the DBMS managed by GeneXus.  
•    -db\_name name: Name of the DB where the GAM scheme resides.  
•    -db\_pass password: User’s password to connect to the DBMS.  
•    -db\_user user: Username to connect to the DBMS.  
•    -gam\_pass password: Password of the GAM administrator user.  
•    -gam\_user user: Username of the GAM administrator (by default, it is "gamadmin")  
•    -gen\_def\_rep\_conn: If specified, it indicates that a new connection must be created to the inserted/updated repository.  
•    -help: It displays a help message indicating the supported arguments.  
•    -import type: It indicates the import mode and the entities that will have to be updated. The possible values are: full or a combination of the following keys separated by a comma between '{}': repository, users, roles, sec\_policies; for example "-import {roles,users,repository}" is valid.  
•    -informix\_srv instance: It indicates the name of the Informix server instance.  
•    -log\_file name: It stores the output of the tool in the specified file. By default, it is generated in %USER\_TEMP\_DIR%\GamLog.log  
•    -file path\_package: It indicates the path to the package file to be imported.  
•    -srv\_host server: Name or IP address of the database server to connect to.  
•    -srv\_port port: It indicates the DBMS listening port.  
•    -use\_exported\_conns: If specified, it indicates that the exported repository connections will have to be taken into account for importing it.  
•    -use\_nt\_sec: If specified, it indicates that it must connect to the DBMS using the authentication mode provided by Windows NT.  
•    -verbose: If specified, it indicates that the application's output must be also redirected to the console. The GamLog.log file will also be generated (or the one specified)

### [Configuring the input for the GAM deploy tool](#Configuring+the+input+for+the+GAM+deploy+tool)

The GAM deploy tool can take the input from an XML file.

Entering the arguments through the console is only valid for the import operation; in the other cases, you should use the XML file as the input. Below is the configuration schema of the input XML file.

```
<?xml version="1.0" encoding="Windows-1252"?>

<xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="GamDeployTool">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="GeneralSettings">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="ProcessType" type="xs:string" />
              <xs:element name="GamAdminName" type="xs:string" />
              <xs:element name="GamAdminPass" type="xs:string" />
              <xs:element name="Verbose" type="xs:boolean" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name="DbmsSettings">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="DbmsCode" type="xs:unsignedByte" />
              <xs:element name="ServerHost" type="xs:string" />
              <xs:element name="ServerPort" type="xs:unsignedShort" />
              <xs:element name="UseWindowsNT" type="xs:boolean" />
              <xs:element name="DbmsUser" type="xs:string" />
              <xs:element name="DbmsPass" type="xs:string" />
              <xs:element name="DbName" type="xs:string" />
              <xs:element name="AdditionalStrings" />
              <xs:element name="InformixInstance" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name="ExportSettings" minOccurs="0" maxOccurs="1">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="PackageFilePath" type="xs:string" />
              <xs:element name="ExportType" type="xs:string" />
              <xs:element name="ExportRepositorySettings" type="xs:boolean" />
              <xs:element name="ExportRoles" type="xs:boolean" />
              <xs:element name="ExportSecurityPolicies" type="xs:boolean" />
              <xs:element name="ExportUsers" type="xs:boolean" />
              <xs:element name="RepositoryGuid" type="xs:string" />
              <xs:element name="Platforms">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element maxOccurs="unbounded" name="Platform" type="xs:unsignedByte" />
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
              <xs:element name="Applications">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element maxOccurs="unbounded" name="AppId" type="xs:string" />
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name="ImportSettings" minOccurs="0" maxOccurs="1">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="PackageFilePath" type="xs:string" />
              <xs:element name="ImportType" type="xs:string" />
              <xs:element name="ImportRepositorySettings" type="xs:boolean" />
              <xs:element name="ImportRoles" type="xs:boolean" />
              <xs:element name="ImportSecurityPolicies" type="xs:boolean" />
              <xs:element name="ImportUsers" type="xs:boolean" />
              <xs:element name="ImportConnections" type="xs:boolean" />
              <xs:element name="ImportAuthenticationTypes" type="xs:boolean" />
              <xs:element name="GenerateDefaultConnection" type="xs:boolean" />
              <xs:element name="ImportRepositoryAction" type="xs:string" />
              <xs:element name="RepositoryGuid" />
              <xs:element name="NewRepositorySettings">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="Name" type="xs:string" />
                    <xs:element name="Namespace" type="xs:string" />
                    <xs:element name="Description" type="xs:string" />
                    <xs:element name="AdminUserName" type="xs:string" />
                    <xs:element name="AdminUserPass" type="xs:string" />
                    <xs:element name="ConnectionUserName" type="xs:string" />
                    <xs:element name="ConnectionUserPass" type="xs:string" />
                    <xs:element name="AllowOauthAccess" type="xs:boolean" />
                    <xs:element name="GiveAnonymousSessions" type="xs:boolean" />
                    <xs:element name="CanRegisterUsers" type="xs:boolean" />
                    <xs:element name="AdministratorRoleGuid" type="xs:string" />
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
              <xs:element name="Applications">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="Application">
                      <xs:complexType>
                        <xs:sequence>
                          <xs:element name="Id" type="xs:string" />
                          <xs:element name="ImportPermissions" type="xs:string" />
                        </xs:sequence>
                      </xs:complexType>
                    </xs:element>
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name="GenerateConnectionFile" minOccurs="0" maxOccurs="1">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="ConnectionFileDir" type="xs:string" />
              <xs:element name="Connections">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="Connection">
                      <xs:complexType>
                        <xs:sequence>
                          <xs:element name="RepositoryId" type="xs:string" />
                          <xs:element name="Name" type="xs:string" />
                        </xs:sequence>
                      </xs:complexType>
                    </xs:element>
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

### 

The sections ExportSettings, ImportSettings, and GenerateConnectionFile are optional depending on the process (property ProcessType inside the GeneralSettings).

Download the [GAM deploy tool XSD input file](https://wiki.genexus.com/commwiki/wiki?30643,,). This file specifies the valid values and restrictions for the fields.

Download a [GAM deploy tool XML input file sample](https://wiki.genexus.com/commwiki/wiki?30644,,).

### [Examples](#Examples)

1. Perform a “Full Import” against SQL Server in a DB called GamDb. Windows NT authentication is used.

```
> GamDeployTool.exe -file c:\pack.gpkg -dbms 12 -srv_host localhost -use_nt_sec -db_name GamDb -gam_user gamadmin -gam_pass gamadmin123 -import full -connection_gam_file c:\connection.gam -use_exported_connections
```

2. Perform a “Custom Import” against MySQL in a DB called GamDb. The guid application is imported: '54fdaafd-cb9f-4786-b7d6-f9b20e20a8e2'

```
> GamDeployTool.exe -file c:\pack.gpkg -dbms 18 -srv_host localhost -db_user root -db_pass root -db_name GamDb -gam_user gamadmin -gam_pass gamadmin123 -import repository,roles -apps 54fdaafd-cb9f-4786-b7d6-f9b20e20a8e2 -connection_gam_file c:\connection.gam -gen_def_rep_conn -verbose
```

3. Example using an XML input file:

```
> GamDeployTool.exe -xml_config_path c:\arguments.xml
```

The following is a sample XML file where the application is asked to create a connection.gam file with the connection to the [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617)

```
<GamDeployTool>

<GeneralSettings>
 
  <ProcessType>GenerateConnectionFile</ProcessType>
 
  <GamAdminName>gamadmin</GamAdminName>

  <GamAdminPass>gamadmin123</GamAdminPass>
  <Verbose>false</Verbose>
</GeneralSettings>

<DbmsSettings>
 
  <DbmsCode>18</DbmsCode>
  
  <ServerHost>localhost</ServerHost>

  <ServerPort>3306</ServerPort>
  
  <UseWindowsNT>false</UseWindowsNT>
 
  <DbmsUser>root</DbmsUser>
 
  <DbmsPass>root</DbmsPass>

  <DbName>gamtestplatform_gam</DbName>

  <AdditionalStrings></AdditionalStrings>
 
  <InformixInstance></InformixInstance>
</DbmsSettings>

<GenerateConnectionFile>

  <ConnectionFileDir>c:\</ConnectionFileDir>

  <Connections>
   <Connection>

    <RepositoryId>92b783a2-2a50-4261-8ba7-684fb780967d</RepositoryId>

    <Name>GAM-Manager</Name>
   </Connection>
  </Connections>
</GenerateConnectionFile>
</GamDeployTool>
```

### List of DBMS codes

* DB2\_UDB = 5
* ORACLE = 7
* DB2\_ISERIES = 9
* INFORMIX = 11
* SQL\_SERVER = 12
* POSTGRESQL = 15
* MYSQL = 18


|  |
| --- |
| **Backlinks** |
| [GAM - Deploy Tool](https://wiki.genexus.com/commwiki/wiki?18608) |

---
