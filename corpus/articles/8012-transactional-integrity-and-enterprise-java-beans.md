---
title: "Transactional Integrity and Enterprise Java Beans"
source_id: 8012
source_url: https://wiki.genexus.com/commwiki/wiki?8012
genexus_version: "18"
---

# Transactional Integrity and Enterprise Java Beans

When an EJB is called from a web panel, a new [LUW](https://wiki.genexus.com/commwiki/wiki?2110,,) is created. It can be managed by either:

* The object (bean) itself
* The EJB Container where it runs.

An interesting advantage of the second option is that it allows a non [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) developer -usually someone with in-depth knowledge of the EJB Container- to configure the LUWs of this [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) EJB procedure.  
  
This feature makes the [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) EJBs more independent from the [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) Java applications because they can be called by an external client. In addition, their LUWs can be managed in the EJB Container.

Only Session Beans take into account the Transaction Type property value. Message Driven Beans are always generated with Transaction Type = Bean value, regardless the value of the property Transaction Type of the procedure.

### [Description](#Description)

In order to determine whether to use this feature or not, a new object property called **Transaction Type** was implemented. Its values are:  
  
**Container:** The LUW will be managed by the EJB Container. When this value is set, an attribute must be set for the Container. In this case, another property called Transaction Attribute is available to tell the Container how to manage the LUW of this bean.  
  
**Note:** In order to use this value (the default value, in fact) the connection to the database must be through a datasourse defined in the J2EE Server.  
  
**Object:** The bean behaves as usual, meaning that the object's programmer defines the size of the LUW using the commit and/or rollback commands, as well as the Commit on Exit property.  
  
When the LUW is managed by the EJB Container, the commit commands are ignored. The Container will always execute the commit at the end of the bean execution. But if a rollback exists, the commit will not be done.  
  
Two very **important** things are that, if an EJB procedure or any other procedure called by it has a:

* **commit**, the Container will ignore it and the commit will not be done.
* **rollback**, the Container will set a flag in order to remember at the end (not at this point) of the execution, that it doesn't have to do the commit.

When the Container value is set, a new property called **Transaction Attribute** is available. Its values are: Required, RequiresNew, Supports, Mandatory, NotSupported or Never.  
  
**Required**

Use the Required mode to have your bean always run in a transaction. If a transaction is already running, your bean joins in that transaction. If no transaction is running, the EJB container will start one.  
  
**RequiresNew**

Use the RequiresNew attribute to have a new transaction started every time your bean is called. If a transaction is already underway when your bean is called, that transaction will not be suspended during the bean invocation.  
  
Then, the Container launches a new transaction and delegates the call to the bean. The bean performs its operations and completes them.  
  
Finally, the Container commits or aborts the transaction and resumes the old transaction. Of course, if no transaction is running when your bean is called, then there is nothing to suspend or resume.  
  
**Supports**

When a bean is called with Supports, it only runs in a transaction if the client already has one running -it joins that transaction. If the client does not have a transaction, the bean will run with no transaction.  
  
**Mandatory**

Mandatory requires that a transaction be already running when the bean method is called.  
  
If there is no transaction running, then the javax.ejb.TransactionRe-quiredException exception is thrown back to the caller. If the client is local, the exception thrown is: javax.ejb.Transaction-RequiredLocalException.  
  
**NotSupported**

If you set your bean to use NotSupported, it can't be involved in a transaction.  
  
For example, in the case of two enterprise beans: A and B, when bean A begins a transaction and then calls bean B, if bean B is using the NotSupported attribute, the transaction started by A is suspended. When B is complete, then A's transaction is resumed.

None of B's operations are transactional, such as reads/writes to databases.  
  
**Never**

The Never transaction attribute means that your bean can't be involved in a transaction.  
  
Also, if the client calls your bean in a transaction, the Container throws an exception back to client:

* Remote: java.rmi.RemoteException
* Local: javax.ejb.EJBException

### [Scope](#Scope)

**Language:** Java  
**Objects:** Enterprise Java Bean Procedures


|  |
| --- |
| **Backlinks** |
| [Expose as Enterprise Java Bean property](https://wiki.genexus.com/commwiki/wiki?8011) | [Transaction Type property](https://wiki.genexus.com/commwiki/wiki?37259) |

---
