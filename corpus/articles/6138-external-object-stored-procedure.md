---
title: "External Object: Stored Procedure"
source_id: 6138
source_url: https://wiki.genexus.com/commwiki/wiki?6138
genexus_version: "18"
---

# External Object: Stored Procedure

[External Objects](https://wiki.genexus.com/commwiki/wiki?5669) (EO) whose [Type property](https://wiki.genexus.com/commwiki/wiki?53690) = "Stored Procedure" (SP) store all the information (name, parameters, etc.) about how to access a set of Stored Procedures located in a DBMS.

In this type of EO, several methods with their corresponding parameters can be defined. Each method maps to a Stored Procedure defined in the DBMS.

`[imagen omitida: wiki id 53712]`

## [Properties](#Properties)

### [External Object](#External+Object)

`[imagen omitida: wiki id 53713]`

* **Name:**Name of the Stored Procedure object.
* **Description:**Description of the Stored Procedure object.
* **[Type](https://wiki.genexus.com/commwiki/wiki?53690):**Type of EO (Stored Procedure).
* **Datastore:**[Data Store](https://wiki.genexus.com/commwiki/wiki?7117) that points to the DBMS where the Stored Procedures are defined.
* **[Module/Folder](https://wiki.genexus.com/commwiki/wiki?25540):**Folder where the EO is located.
* **[Object Visibility](https://wiki.genexus.com/commwiki/wiki?22473):** Accessibility from other objects in different Modules.

### [Methods](#Methods)

`[imagen omitida: wiki id 53714]`

* **Internal Name:**Internal name to be given to the method in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).
* **Description:** Description of the method.
* **Type:** Data type returned by the method, if applicable.
* **External Name:** Name of the Stored Procedure as defined in the DBMS.

### [Parameters](#Parameters)

`[imagen omitida: wiki id 53715]`

* **Access Type:**InOut, In only, or Out only.
* **Internal Name:**Internal name to be given to the parameter.
* **Description:**Description of the parameter.
* **Type:**Data type of the parameter.
* **External Name:**External name of the parameter defined in the Stored Procedure.

## [Use](#Use)

Suppose you have created an EO of SP type called MySQL\_SP and defined a MySQL\_SP variable called &mysps.

Then, in your code you can do the following:

```
Event 'Count'
  &mysps.get_count_university(&count) //&count is a variable based on the Numeric(8.0) data type. It is loaded with the number of universities in the DB University table
  msg(&count.ToString())
EndEvent
```

get\_count\_university is the Internal Name given to the Stored Procedure sp\_get\_count\_university.

**Considerations**

* Only variables and/or constants are accepted as parameters when calling Stored Procedures. [Expressions](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) are not supported. So, if necessary, you can assign an expression to a variable and pass the variable as a parameter.
* To generate all the necessary code to call the Stored Procedure, GeneXus will map the method's Internal Name with its External Name, and the parameters' Internal Name with their corresponding External Name, taking into account the parameter type and their Access Types. Therefore, external names must be correctly defined; otherwise, errors such as "PLS-00306: wrong number or types of arguments in call to ' ...' " may appear.
* If the Stored Procedure modifies the database, like an insert, update, or delete, you have to explicitly use a commit command. For example:

```
Event 'DeleteUser'
    &mysps.delete_user(10)
    commit
EndEvent
```

## [Deployment](#Deployment)

When the application is deployed, take into account that if the SP(s) are running on an iSeries DB2, the gx400dcl.exe (.net) or crtjdbccalls.class (java) files must be executed to declare them. See [SAC #26620](https://www.genexus.com/es/developers/websac?data=26620) for more details.

## [Compatibility](#Compatibility)

It is possible to call Stored Procedures as it was done in previous versions; that is:  
  
call('sp\_get\_count\_university',&count)  
  
In addition, declaring the list of Stored Procedures used in the property List of external Stored Procedures at the Data Store level is also possible.  
This calling method is deprecated, and a warning like this will appear: spc0145, 'Calling stored procedure ''%1'' in data store ''%2'' via the call keyword is deprecated.'

## [Restrictions](#Restrictions)

* Some complex data types are not supported. For example:
  + [Basic data types](https://wiki.genexus.com/commwiki/wiki?6905) with the collection property set to True.
  + [Extended data types](https://wiki.genexus.com/commwiki/wiki?6560) and [Structured Data Types](https://wiki.genexus.com/commwiki/wiki?10021).
  + Vector and Matrix.
* When the Stored Procedure returns a Recordset data type, GeneXus doesn't provide a compatible data type to map it.
* Null value as an argument for a Stored Procedure method is not supported.
* Stored Functions (Oracle) are not supported; use Stored Procedures with InOut or Out parameters.


|  |
| --- |
| **Backlinks** |
| [Category:External Object](https://wiki.genexus.com/commwiki/wiki?5669) | [Category:External Object (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57996) | [Specification Codes from spc0100 to spc0149](https://wiki.genexus.com/commwiki/wiki?6433) |
| [Type property in External Object](https://wiki.genexus.com/commwiki/wiki?53690) |

---
