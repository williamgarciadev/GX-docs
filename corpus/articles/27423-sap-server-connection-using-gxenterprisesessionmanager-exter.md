---
title: "SAP server connection using GXEnterpriseSessionManager External Object"
source_id: 27423
source_url: https://wiki.genexus.com/commwiki/wiki?27423
genexus_version: "18"
---

# SAP server connection using GXEnterpriseSessionManager External Object

Before invoking a BAPI via RFC, GeneXus applications must be connected to the SAP server where it is located.

An External Object called GXEnterpriseSessionManager is provided to make the connection.

The first time a BAPI is imported, GeneXus ERP Connector automatically generates this External Object.

GXEnterpriseSessionManager has a Connect method and the following parameters:

|  |  |  |
| --- | --- | --- |
| UserName | Char(40) | SAP user to be used in the connection |
| Password | Char(40) | User's password |
| InstanceNumber | Char(10) | Instance number within the server |
| AppServer | Char(512) | Name of SAP application server to which we will be connecting |
| RouterString | Char(512) | IP of SAP server |
| ClientNumber | Char(10) | Number of SAP client |
| SystemId | Char(10) | Identifier of the SAP system to be connected |
| SessionName | Char(40) | Name that the connection will receive |
| ErrorCode | Num(5.0) | Error code when attempting to connect |
| ErrorMessage | Char(255) | Error message when attempting to connect |

The connection can be made as shown below (&SAPSessionManager is a variable based on GXEnterpriseSessionManager):

```
&SAPSessionManager.AppServer      = "<SAPServer>"
&SAPSessionManager.ClientNumber   = "<ClientIdNumber>"
&SAPSessionManager.RouterString   = "/H/<RouterString>/S/<Port>/H/"
&SAPSessionManager.SystemId       = "<SystemIdentification>"
&SAPSessionManager.InstanceNumber = "<SystemNumber>"
&SAPSessionManager.SessionName    = "<AnyStirng>"
&SAPSessionManager.UserName       = "<SAPUser>"
&SAPSessionManager.Password       = "<SAPPassword>"

&SAPSessionManager.Connect()
if &SAPSessionManager.ErrorCode.IsEmpty()
  <CallAnyBapi>
else
  msg('Log in error ' + &SAPSessionManager.ErrorCode.ToString() + ': ' + &SAPSessionManager.ErrorMessage)
endif
```

This connection option allows changing, at any time during runtime, the user and SAP server used by the application to connect.

### [Using a SAP Destination to connect](#Using+a+SAP+Destination+to+connect)

In SAP BTP, [destinations](https://developers.sap.com/tutorials/cp-cf-create-destination.html) are used to define connections for outbound communication from your application to remote systems that can be on-premises or in the cloud.

A destination has a name, a URL, authentication details, and some other configuration details.

From GeneXus v18 U3 onwards (only Java), GXEnterpriseSessionManager has a ConnectSesion method with the following parameters:

|  |  |  |
| --- | --- | --- |
| Session | Char(255) | (Access Type: In) SAP Destination Name |
| Scope | Char(255) | (Access Type: In) Dummy, you can leave it blank |

Insted of set all the connection data you only have to indicate the name of the Destination.

```
&GXEnterpriseSessionManager.ConnectSession("<DestinationName>", "")
```

### [Operatin Commit](#Operatin+Commit)

Some BAPIs do not run a database Commit, which means that the application must trigger the Commit so that the changes are read to the database

Example code with BAPI SalesOrder (using method CreateFromDat2)

```
&GXEnterpriseSessionManager.TransactionBegin()

&SalesOrder.CreateFromDat2(.....)

if <no error>
     &GXEnterpriseSessionManager.TransactionCommit()
```

Where &GXEnterpriseSessionManager is of GXEnterpriseSessionManager type (External Object) and

&SalesOrder is of BUS2032 type (contains BAPI methods imported).

Both are external objects automatically added  by GeneXus when the selected BAPI is imported.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus ERP Connector](https://wiki.genexus.com/commwiki/wiki?26013) | [GeneXus ERP Connector - Invoking a BAPI through RFC](https://wiki.genexus.com/commwiki/wiki?27311) |

---
