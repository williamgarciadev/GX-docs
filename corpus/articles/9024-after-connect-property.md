---
title: "After connect property"
source_id: 9024
source_url: https://wiki.genexus.com/commwiki/wiki?9024
genexus_version: "18"
---

# After connect property

The purpose is to allow calling a GeneXus procedure immediately after assigning the connection in an application. This implementation makes it possible to support audit mechanisms.

### [Description](#Description)

The idea is that right after taking a connection, a call must be made to a procedure that saves the necessary data to make the connection, such as username, time, action, etc. For example, in the connection it allows indicating the logical user instead of the physical one (the application user instead of the database user).  This allows us to meet a frequent requirement for displaying the actual user even though all users connect with the same generic user account required to use the connection pool.

As for its scope, the implementation is valid for any type of applications including web, win 2-tier and win 3-tier applications. It applies both to the connection with the GeneXus pool and with an external one connecting with a server datasource when Java is used (read [Use Datasource for Web Based Applications Property](https://wiki.genexus.com/commwiki/wiki?9384,,)).

#### [Procedure requirements](#Procedure+requirements)

The procedure associated with the After Connect property must receive an In parameter of String type (Char).

```
parm(in:&datastore); //&datastore is of Char type
```

Internally, in this parameter we send the name of the data store to which it is connecting (it is used by GeneXus when calling the procedure and the user doesn't have to worry about it besides defining the string parameter).

If the logic is to be identified depending on whether we’re connecting to one data store or another, a case can be programmed within the procedure, asking for the value of the parameter received.

#### [When is After Connect executed?](#When+is+After+Connect+executed%3F)

For Java, read [SAC #34245](http://www2.gxtechnical.com/portal/hgxpp001.aspx?15,4,61,O,S,0,,34245)

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build with this Only of the object.

### [See Also](#See+Also)

[Before connect property](https://wiki.genexus.com/commwiki/wiki?8997)


|  |
| --- |
| **Backlinks** |
| [Before connect property](https://wiki.genexus.com/commwiki/wiki?8997) |

---
