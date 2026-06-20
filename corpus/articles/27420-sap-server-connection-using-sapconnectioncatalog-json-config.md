---
title: "SAP server connection using SAPConnectionCatalog.json configuration file"
source_id: 27420
source_url: https://wiki.genexus.com/commwiki/wiki?27420
genexus_version: "18"
---

# SAP server connection using SAPConnectionCatalog.json configuration file

Before invoking a BAPI via RFC, GeneXus applications must be connected to the SAP server where it is located.

A file called SAPConnectionCatalog.json is provided containing all the necessary data for this purpose.

The first time a BAPI is imported, GeneXus ERP Connector automatically generates a file of this type containing the data used in the connector.

The file is saved in the directory C:\Users\<User>\AppData\Roaming\Artech\GeneXus\10Ev3 (10Ev3 indicates the GeneXus version that is being used) with the name SAPConnectionCatalog.json.

This file can be used with the application that is being generated. To do it, copy it to the application's web directory and change the connection data (if it's necessary).

The following connection data has to be entered:

|  |  |
| --- | --- |
| AppHost | Name of SAP application server to which we will be connecting |
| ClientId | Number of SAP client |
| ConnectionName | Name that the connection will receive |
| Language | Language used in the connection (eg. "EN" "ES") |
| Password | User's password |
| Router String | IP of SAP server router (if it's needed) |
| SAPGUI | "0" |
| SystemID | Identifier of the SAP system to be connected |
| SystemNumber | Number of instance within the server |
| User Name | SAP user to be used in the connection |

The structure of the SAPConnectionCatalog.json file is as follows:

```
{"AppHost":"<SAPServer>","ClientId":"<ClientIdNumber>","ConnectionName":"<AnyString>","Language":"<ConnectionLanguage>",
"Password":"<Password>","RouterString":"\/H\/<RouterIP>\/S\/<Port>\/H\/","SAPGUI":"0","SystemID":"<SistemIdentification>",
"SystemNumber":"<SystemNumber>","UserName":"<SAPUserName>"}
```

When the generated application needs to execute a BAPI via RFC and the file exists, it takes its data, makes the connection and then invokes the BAPI.

With this connection option, only one user is used (and one SAP server) for all the application's connections.
