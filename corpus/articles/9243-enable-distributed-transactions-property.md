---
title: "Enable Distributed Transactions property"
source_id: 9243
source_url: https://wiki.genexus.com/commwiki/wiki?9243
genexus_version: "18"
---

# Enable Distributed Transactions property

Is used to enable or disable the JTA support.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | Disable the JTA support. This is the default value. |
| **Yes** | Enable the JTA support. |

### [Description](#Description)

One important benefit of this feature is that it supports distributed transactions.

**Note:** If this property is set to Yes, this implementation can be used only when there is more than one Data store, in which case a distributed transaction makes sense. The conditions are the following:

• The web application must use a server datasource to connect to the database. In DBMS options, the property 'Use datasource for web based applications' must be set to True, and a JNDI name defined in the server must be given.  
• The server must have JTA support. Many J2EE servers have JTA support, for example Websphere, Oracle Application Server, etc. Other application servers, like Jakarta - Tomcat do not have; however, there are classes with the necessary JTA support that can be added to the classpath in order to use it. It can be downloaded from Sun's Site.

**Note:**When JTA is used you must use the XA drivers which close the cursors in the commit operations.

**Access Technology:**JDBC (using JNDI Datasource)

### [Samples](#Samples)

Let's see what happens in the following scenario: the model accesses two (or more) data stores, and a commit is performed, then the commit will be executed first in database 1 and then in database 2. If everything is ok, the transaction ends. Now, what happens if an error occurs in database 2? With [JTA](https://wiki.genexus.com/commwiki/wiki?2111), if an error occurs, the rollback will be done in both databases. On the other hand, without JTA, the commit on database 1 was definitly done and the rollback will be done just in database 2.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [Scope](#Scope)

**Objects:** Procedure, Transaction  
**Platforms:** Web(Java)

### [See Also](#See+Also)

[Access technology to set property](https://wiki.genexus.com/commwiki/wiki?9030)  
[Use Datasource for Web Based Applications Property](https://wiki.genexus.com/commwiki/wiki?9384,,)
