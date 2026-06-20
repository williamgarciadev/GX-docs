---
title: "SecurityLevel annotation"
source_id: 55437
source_url: https://wiki.genexus.com/commwiki/wiki?55437
genexus_version: "18"
---

# SecurityLevel annotation

Sets the security level required to access a method defined in an API object.

### [Syntax](#Syntax)

```
'['SecurityLevel(None|Authorization|Authentication)']'
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*None*  
     Indicates that the method is an open entry point. This means that no login or additional permissions are required to access the method. Any end user can invoke the method without restrictions.

*Authorization*  
    The system checks if the end user has the appropriate permissions before allowing the method to execute. So, end user must be logged in and have the necessary permissions to perform the operation.

*Authentication*Requires the end user to be authenticated before the method can be used. The end user must be logged in to access the method, but they do not need to have additional specific permissions.

### [Description](#Description)

When an API object has the set the [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) to True and [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) set to Authentication or Authorization, all methods require some level of security for access. However, some cases may require an open entry point method, with no OAuth login or token required. To achieve this, the SecurityLevel attribute is used to define the specific security level for each method.

### [Sample](#Sample)

Suppose you have an API object called APICustomer that provides services related to customers of an application. This object has the following methods defined:

* [ListCustomers](https://wiki.genexus.com/commwiki/wiki?50051): Lists all registered customers in the database.
* [Insert](https://wiki.genexus.com/commwiki/wiki?49778): Adds a new customer to the database.
* [Update](https://wiki.genexus.com/commwiki/wiki?49780): Updates the information of an existing customer.
* [Delete](https://wiki.genexus.com/commwiki/wiki?49781): Deletes a customer from the database.
* [GetByKey](https://wiki.genexus.com/commwiki/wiki?50052): Gets the information of a specific customer by its ID.

In addition, the following is configured:

* The [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) has the value True configured at the [version level](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7860,,).
* The APICustomer has the [Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) set to Authentication.
* The following [permissions are defined](https://wiki.genexus.com/commwiki/wiki?29723):
  + Read\_Permission to authorize access to methods that only consult information, such as ListCustomers.
  + Write\_Permission to authorize access to methods that perform modifications, such as Insert, Update, and Delete.

Then the Service Source of the APICustomer looks like the one below:

```
APICustomer{
    
    [SecurityLevel(Authorization)]
    [SecurityPermission("Read_Permission")]
    ListCustomers(out:&SDTCustomers) 
    => CustomerList(&SDTCustomers);

    [RestMethod(POST)]
    [SecurityLevel(Authorization)]
    [SecurityPermission("Write_Permission")]
    Insert(in:&CustomerId, in:&CustomerName, in:&CustomerLastName, out:&Messages) 
    => CustomerInsert(&CustomerId, &CustomerName, &CustomerLastName, &Messages);

    [RestMethod(PUT)]
    [SecurityLevel(Authorization)]
    [SecurityPermission("Write_Permission")]
    Update(in:&CustomerId, in:&CustomerName, in:&CustomerLastName, out:&Messages)
    => CustomerUpdate(&CustomerId, &CustomerName, &CustomerLastName, &Messages);

    [RestMethod(DELETE)]
    [SecurityLevel(Authorization)]
    [SecurityPermission("Write_Permission")]
    Delete(in:&CustomerId, out:&Messages)
    => CustomerDelete(&CustomerId, &Messages);

    [SecurityLevel(None)]
    GetByKey(in:&CustomerId, out:&Customer, out:&Messages)
    => CustomerGetByKey(&CustomerId, &Customer);
}
```

In this case:

* ListCustomers method requires the Read\_Permission  to be executed. Only authenticated users with this permission will be able to list all customers.
* The Insert, Update, and Delete methods require Authorization and the Write\_Permission to be executed. Only authenticated users with this permission will be able to add, update or delete customers.
* The "GetByKey method does not require authentication and does not have a specific permission associated with it. This means that it can be accessed by any user, even without authentication.

### [Availability](#Availability)

Since [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240).

### [See Also](#See+Also)

[SecurityPermission annotation](https://wiki.genexus.com/commwiki/wiki?55422)  
[API object - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?55436)


|  |
| --- |
| **Backlinks** |
| [API object - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?55436) | [Table of contents:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) | [Permissions by Method in the API object](https://wiki.genexus.com/commwiki/wiki?55405) |

---
