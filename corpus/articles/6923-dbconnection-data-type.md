---
title: "DBConnection Data Type"
source_id: 6923
source_url: https://wiki.genexus.com/commwiki/wiki?6923
genexus_version: "18"
---

# DBConnection Data Type

Allows the configuration options for the connections to the database to be determined in execution time.

### [Description](#Description)

In order to be able to modify the configuration options of the different data stores, from a GeneXus object and in execution time, a DBConnection data type variable must be defined. To do this, you associate this variable with a specific connection (a GeneXusdata store) using the GetDataStore function, and then you manage this connection using the available properties and methods.

### [Notes](#Notes)

* In Web applications, you should only change connection settings in a procedure referenced by the [Before Connect](https://wiki.genexus.com/commwiki/wiki?8997) property. This is because Database connections in Web applications are handled using a pool. You should not change connection settings in an event of a Web object, or a procedure called by an event of a Web Object.
* For [Command Line Procedures](https://wiki.genexus.com/commwiki/wiki?7947) it must be taken into account that the Connect()/Disconnect() methods close the cursors which are opened in the connection they apply to. Because of this, Connect() and/or Disconnect() methods must not be called within the scope of a For each command. The developer is responsible for using the connection/disconnection at the right moment. E.g.: if the disconnection is done in the middle of a procedure that afterward requires the connection, the execution may be canceled.

### [Properties](#Properties)

|  |  |
| --- | --- |
| [ConnectionData](https://wiki.genexus.com/commwiki/wiki?6968) | [ODBCDatasourceName](https://wiki.genexus.com/commwiki/wiki?6922,,) |
| ConnectionMethod Property | [ODBCDriverName](https://wiki.genexus.com/commwiki/wiki?6976,,) |
| [DatastoreName](https://wiki.genexus.com/commwiki/wiki?7006) | [ODBCFileDatasourceName](https://wiki.genexus.com/commwiki/wiki?6955,,) |
| [ErrCode](https://wiki.genexus.com/commwiki/wiki?6930) | [ShowPrompt](https://wiki.genexus.com/commwiki/wiki?6993,,) |
| [ErrDescription](https://wiki.genexus.com/commwiki/wiki?6931) | [UseExternalDatasource](https://wiki.genexus.com/commwiki/wiki?7746) |
| [ExternalDatasourceName](https://wiki.genexus.com/commwiki/wiki?7747) | [UserName](https://wiki.genexus.com/commwiki/wiki?7001) |
| [JDBCDriverName](https://wiki.genexus.com/commwiki/wiki?6951) | [UserPassword](https://wiki.genexus.com/commwiki/wiki?7038,,) |
| [JDBCDriverURL](https://wiki.genexus.com/commwiki/wiki?7003) |  |

### [Methods](#Methods)

|  |  |
| --- | --- |
| [Connect](https://wiki.genexus.com/commwiki/wiki?7086) | [Disconnect](https://wiki.genexus.com/commwiki/wiki?7101) |

**Important:** If the [Before Connect](https://wiki.genexus.com/commwiki/wiki?8997) property is set, the Connect() method executes that procedure, except when it is referenced within that object (to avoid an infinite loop).

### [Example​​​​​](#Example%E2%80%8B%E2%80%8B%E2%80%8B%E2%80%8B%E2%80%8B)

1) Setting a JDBC Connection in a command-line procedure

&MyConn is a variable of DBConnection type

```
      &myConn = GetDataStore(!"Default")
      &myConn.UserName = trim(&User)
      &myConn.UserPassword = trim(&Password)
      &myConn.JDBCDriverName=!'com.inet.tds.TdsDriver'
      &myConn.JDBCDriverURL=!'jdbc:inetdae:barbanegra:1433?database=testemp2'
      &myConn.ShowPrompt = 2
      &Res = &myConn.Connect()
      Do case
        Case &Res = 0
              &ConnOk = !'Y'
              return
         Otherwise
              &ConnOk = !'N'
              msg('Unsuccessful connection, retry...')
      Endcase
```

2) Changing connection settings in a procedure referenced by the Before Connect Property: See [Before connect property](https://wiki.genexus.com/commwiki/wiki?8997)

### [Scope](#Scope)

**Objects:** [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916)  
**Languages:** .Net, Java

### [Security Tips](#Security+Tips)

-Avoid setting external user's data to the properties or methods, or sanitize accordingly the entries

### [See Also](#See+Also)

[GetDataStore Function](https://wiki.genexus.com/commwiki/wiki?7007)


|  |
| --- |
| **Backlinks** |
| [Before connect property](https://wiki.genexus.com/commwiki/wiki?8997) | [Connect method](https://wiki.genexus.com/commwiki/wiki?7086) | [ConnectionData Property](https://wiki.genexus.com/commwiki/wiki?6968) |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [DatastoreName Property](https://wiki.genexus.com/commwiki/wiki?7006) | [Disconnect method](https://wiki.genexus.com/commwiki/wiki?7101) | [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) |
| [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) | [ErrDisplay Property](https://wiki.genexus.com/commwiki/wiki?6929) | [Error Codes and Messages for DBConnection](https://wiki.genexus.com/commwiki/wiki?6945) | [ExternalDatasourceName Property](https://wiki.genexus.com/commwiki/wiki?7747) |
| [GetDataStore function](https://wiki.genexus.com/commwiki/wiki?7007) | [JDBCDriverName Property](https://wiki.genexus.com/commwiki/wiki?6951) | [JDBCDriverURL Property](https://wiki.genexus.com/commwiki/wiki?7003) |
| [UseExternalDatasource Property](https://wiki.genexus.com/commwiki/wiki?7746) |
| [UserName Property](https://wiki.genexus.com/commwiki/wiki?7001) |

---
