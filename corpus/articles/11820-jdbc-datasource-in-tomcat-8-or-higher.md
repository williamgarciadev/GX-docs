---
title: "JDBC Datasource in Tomcat 8 (or higher)"
source_id: 11820
source_url: https://wiki.genexus.com/commwiki/wiki?11820
genexus_version: "18"
---

# JDBC Datasource in Tomcat 8 (or higher)

This document describes step by step How to configure a Java model in **GeneXus 8.0 or higher** to use a **SQL Server** JDBC datasource in **Tomcat 8**, using driver **JTDS.**

1. Configure **\conf\context.xml** of your tomcat installation

Add the following code between the <Context> and </Context> tag:

```
    <Resource name="jdbc/testsql"
                        auth="Container"
                        type="javax.sql.DataSource"
                        validationQuery="select 1"
                        driverClassName="net.sourceforge.jtds.jdbc.Driver"
                        url="jdbc:jtds:sqlserver://yourServerName:1433/yourDBName"
                        username="yourUserName"                        
                        password="yourPassword"
                        maxActive="8"
                        maxIdle="4"  />
```

The fields marked in bold should be replaced with your particular data connection information. The resource name can be anyone, this is an example, and just consider to remember this name in order to use it later in Genexus.

2. Configure **\webapps\yourWebapp\web-inf\web.xml**

Add the following code between the <web-app> and </web-app> tag:

```
 <resource-ref>
     <description>DB Connection</description>
     <res-ref-name>jdbc/testsql</res-ref-name>
     <res-type>javax.sql.DataSource</res-type>
     <res-auth>Container</res-auth>
</resource-ref>
```

3. **Copy the driver** (jtds1-2.jar) to the \lib folder of your tomcat installation

4. **Configure your java model** in Genexus:

Edit the application DBMS Options and set the following properties:  
  
Use datasource for web based applications = True  
JDBC datasource = java:comp/env/jdbc/testsql  
  
Where jdbc/testsql is the JNDI name of the JDBC Datasource.

### [Note](#Note)

In case of Oracle Database, you should also set the JNDI name as follows: java:/comp/env/jdbc/myoracle after you've defined the datasource in your Context (\conf\context.xml of your tomcat installation).

```
<Resource name="jdbc/myoracle" auth="Container"
              type="javax.sql.DataSource" driverClassName="oracle.jdbc.driver.OracleDriver"
              url="jdbc:oracle:thin:@testorcl:1521:testorcl"
              username="yourUserName" password="yourPassword" maxActive="20" maxIdle="10"
              maxWait="-1"/>
```

### [Interesting links](#Interesting+links)

Here is the official documentation of how to do this in Tomcat 6, also with other dbms samples, like MySql, Postgresql, and Oracle:

[jndi-datasource-examples-howto.html](http://tomcat.apache.org/tomcat-6.0-doc/jndi-datasource-examples-howto.html)


|  |
| --- |
| **Backlinks** |
| [Defining a JDBC Datasource](https://wiki.genexus.com/commwiki/wiki?2112) |

---
