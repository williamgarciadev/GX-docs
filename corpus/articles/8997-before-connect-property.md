---
title: "Before connect property"
source_id: 8997
source_url: https://wiki.genexus.com/commwiki/wiki?8997
genexus_version: "18"
---

# Before connect property

Sets the Procedure object that dynamically changes the connection properties just before the application accesses the database at runtime.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)  
**Level:** Generator

### [Description](#Description)

The [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) configured in the 'Before connect' property must be defined in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

In this Procedure, you have to state/change the properties of the Data Store to which the application must connect.

The Procedure is executed just before the application establishes a connection to the database, ensuring that the connection parameters are adjusted according to the specific needs of each run.

It can only receive one **INOUT** variable, which must be based on the **DBConnection**data type:

```
parm(INOUT: &dbconn); //&dbconn is a DBConnection type variable
```

In 3 Tier models, the [Execute in new LUW property](https://wiki.genexus.com/commwiki/wiki?8008) must be set to Yes. In Web environments, it must be set to No.

The Procedure receives the &dbconn variable with the Data Store details, and you can modify those details according to any logic needed. For example, you can change the Data Store details depending on the user executing the application.

In addition, it must not access the database. So, do not use any functionality that does it, like:

* [For each command](https://wiki.genexus.com/commwiki/wiki?24744)
* Business Components
* GAMSession.Get() or any method that internally accesses the database
* Calling a procedure that accesses the database

This is because any operation that accesses the database within that Procedure will not trigger the *BeforeConnect* Procedure (otherwise it would result in an infinite loop).

The Procedure can either run independently (standalone) or be executed through the 'Before connect' property.

When the Procedure is invoked from the 'Before connect' property, the received variable already contains the instantiated connection data. Therefore, **do not use** the [GetDataStore function](https://wiki.genexus.com/commwiki/wiki?7007) to initialize it.

The [GetDataStore function](https://wiki.genexus.com/commwiki/wiki?7007) and the [Connect method](https://wiki.genexus.com/commwiki/wiki?7086) can be used in standalone Procedures. Avoid using them in Procedures used in the 'Before connect' property, as these Procedures will be executed for every connection (that is, for each Data Store the application connects to), and their use in that context is likely to cause errors.

If you have more than one Data Store, it is important to include in the code the necessary evaluations (if / do case) to consider only the intended Data Store.

How often the BeforeConnect method is invoked in Java depends on whether the type of connection pool used is the server pool or the GeneXus pool.

* **If the server pool is used (similar to .NET):** The Procedure indicated in the 'Before connect' property is called before executing any database access within each [Logical Unit of Work (LUW)](https://wiki.genexus.com/commwiki/wiki?7963). This means that during a server request, such as an action in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), a [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), or a service that performs database operations (for example, For each, Commit, Update, Delete, among others), BeforeConnect will be executed once. However, if a Procedure object starts a new LUW during execution, a new connection to the database will be opened, and BeforeConnect will be executed again.
* **If the GeneXus pool is used:** BeforeConnect is called before each database operation. This is because, when using the GeneXus pool, a connection to the pool is requested before every operation. Even if the pool may return a previously used connection, BeforeConnect will be executed in each operation that interacts with the database.

### [Connection Pooling Details](#Connection+Pooling+Details)

In .NET, the connection pool uses the connection string as a key, which is automatically managed by the framework. If a different username is assigned in the Data Store for each user, connections will not be reused between them.

In Java, for the connection pool to be shared among users, the username must be the same. Otherwise, each user will use an independent connection without taking advantage of the shared pool.

#### [Additional considerations](#Additional+considerations)

When using different connection strings for each user, it is important to assess the implications. If this strategy is chosen, a viable alternative is to use a common connection string while modifying only the database for each tenant. Auditing of the logged-in user can be handled through an auxiliary table or the web session.

#### [Performance impact](#Performance+impact)

The use of BeforeConnect should not have a significant impact, as long as the operations performed within the procedure are lightweight. It is crucial that these operations, such as modifying connection data in the Data Store, remain efficient to avoid performance issues.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

#### [**Multi-company application**](#Multi-company+application)

Suppose that the Login [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) sets the end user that has logged in to a web session:

```
&Session.Set('UserID', str(&UserID))
```

Also, you want to connect to different databases depending on the logged-in user.

For this purpose, define a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293), which must be stated in the 'Before connect' property:

#### [**JAVA Sample**](#JAVA+Sample)

#### [**Sample I**](#Sample+I)

Procedure object implementation

*Rules*

```
Parm(inout: &dbconn);
```

*Source*

```
If &dbconn.DatastoreName = !"DEFAULT"
   &UserID = val(&Session.Get('UserID')) 
  //select the Database depending on UserID
   Do Case
      Case &UserID = 1 
           &DataBase  = "companyone" 
      Case &UserID = 2 
           &DataBase  = "companytwo" 
      Otherwise 
           &DataBase  = "companyone" //default database 
  EndCase
Endif

&dbconn.JDBCDriverName = "com.microsoft.jdbc.sqlserver.SQLServerDriver" 
&dbconn.JDBCDriverURL = "jdbc:microsoft:sqlserver://MyServer:1433;databaseName=" + trim(&DataBase) + ";SelectMethod=cursor" 
&dbconn.UserName = 'username' 
&dbconn.UserPassword = 'userpassword'
```

Below is the same case using JDBC driver:

```
&dbconn.JDBCDriverName = "net.sourceforge.jtds.jdbc.Driver"
&dbconn.JDBCDriverURL = "jdbc:jtds:sqlserver://MyServer:1433/"+ &database.Trim()
```

#### [**Sample II**](#Sample+II)

Alternatives for connecting to an external data source and using the GeneXus connection pool at runtime.

Procedure object implementation

*Rules*

```
Parm(inout: &dbconn);
```

*Source*

```
if &dbconn = 'JNDI'
   &dbconn.UseExternalDatasource = 1
   &dbconn.ExternalDatasourceName = 'java:/comp/env/jdbc/myoracle' 
else
   &dbconn.UseExternalDatasource = 0
   &dbconn.JDBCDriverName = "oracle.jdbc.driver.OracleDriver"
   &dbconn.JDBCDriverURL = "jdbc:oracle:thin:@Testorcl:1521:testorcl"
   &dbconn.UserName = &UserId.Trim()
   &dbconn.UserPassword = &UserPwd.Trim()
endif
```

#### [**.NET Sample**](#.NET+Sample)

Procedure object implementation

*Rules*

```
Parm(inout: &dbconn);
```

*Source*

```
If &dbconn.DatastoreName = !"DEFAULT"
  &UserID = val(&Session.Get('UserID')) 
  //select the Database depending on UserID 
  Do Case
   Case &UserID = 1 
        &DataBase  = "companyone" 
   Case &UserID = 2 
        &DataBase  = "companytwo" 
   Otherwise 
        &DataBase  = "companyone" //default database 
  EndCase
Endif

//Change connection properties  
&dbconn.UserName = 'username' 
&dbconn.UserPassword = 'userpassword'
&dbconn.ConnectionData = "DATABASE=" + &DataBase.Trim() //SQLServer 
//&dbconn.ConnectionData = "Data Source=" + &DataBase.Trim()  //MySQL
```

**Note:** If your application uses two Data Stores (for example, Default and GAM), and you assign a Procedure to the 'Before connect' property, that Procedure will be called for both the Default and GAM connections.

Without an IF that evaluates the Data Store, any access to the database by a GAM object will call that Procedure and overwrite GAM's connection data with the Default connection data (note that the &dbConn parameter is INOUT).

Therefore, using IF or CASE to check for multiple Data Stores makes sense in that case. However, they can also be used as a defensive measure, even if only one Data Store is defined.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute [Build any object](https://wiki.genexus.com/commwiki/wiki?17719) with the purpose of generating the \*.config files.

### [See Also](#See+Also)

[DBConnection Data Type](https://wiki.genexus.com/commwiki/wiki?6923)  
[After connect property](https://wiki.genexus.com/commwiki/wiki?9024)


|  |
| --- |
| **Backlinks** |
| [After connect property](https://wiki.genexus.com/commwiki/wiki?9024) | [DBConnection Data Type](https://wiki.genexus.com/commwiki/wiki?6923) | [Defining a JDBC Datasource](https://wiki.genexus.com/commwiki/wiki?2112) |
|

---
