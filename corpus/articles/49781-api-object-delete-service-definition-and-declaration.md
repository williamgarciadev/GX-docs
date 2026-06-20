---
title: "API object - Delete service definition and declaration"
source_id: 49781
source_url: https://wiki.genexus.com/commwiki/wiki?49781
genexus_version: "18"
---

# API object - Delete service definition and declaration

This article describes all the necessary steps to declare, inside an [API object](https://wiki.genexus.com/commwiki/wiki?46151) called APICustomers, a Delete service that deletes a certain customer record (received by parameter) from the Database.

Consider a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) containing:

1) A Customer [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

```
Customer
{
  CustomerId*
  CustomerName
  CustomerLastName
}
```

Note: The Customer Transaction has [Automatic data population](https://wiki.genexus.com/commwiki/wiki?32706).

2) An [API object](https://wiki.genexus.com/commwiki/wiki?46151) called APICustomers. In its **Service Source**tab, it already contains four services declared that map external names exposed as services with the internal implementations in the KB:

`[imagen omitida: wiki id 50948]`

Now, suppose you need to define another service (method) named Delete, as part of the APICustomers object, to allow deleting a certain Customer from the database (the customer identifier is sent as a parameter).

To achieve this, the Customer Transaction must be set as a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846).

Next, you have to create a new [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) named CustomerDelete.

In the Procedure Rules section, define a [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) as follows:

```
Parm(in:&CustomerId, out:&Messages);
```

In the Procedure Source, define the following code:

```
&Customer.Load(&CustomerId)
&Customer.Delete()
If &Customer.Success()
    commit
else
    rollback
endif
&Messages=&Customer.GetMessages()
```

* &Customer is a variable based on the Customer Business Component data type.
* &Messages is a variable based on the Messages data type.

Now, go to the APICustomers API object, and inside its **Service Source** declare the new method (Delete) under the last method:

```
Customer{
    ...
    [RestMethod(DELETE)]
    Delete(in:&CustomerId, out:&Messages)
    => CustomerDelete(&CustomerId, &Messages);
}
```

Note that in this case, the [RestMethod annotation](https://wiki.genexus.com/commwiki/wiki?50508) precedes the service declaration indicating that the HTTP method to be used is DELETE.

It is important to add the same variables you already defined in the Procedure object in the API object.

The next step is to define–if necessary–the [Events](https://wiki.genexus.com/commwiki/wiki?46151) in the Events section of the API object (APICustomers).

```
Event Delete.Before
    //Some Code if is needed
EndEvent
Event Delete.After
    //Some Code if is needed
EndEvent
```

The order of events executed in this example is as follows:

1. Event 'Before'
2. Event 'Delete.Before'
3. Delete method (CustomerDelete procedure internally)
4. Event 'Delete.After'
5. Event 'After'

Below you can see all the steps being executed:

`[imagen omitida: wiki id 50030]`

**Note**: This service supports the use of optional HTTP headers to provide additional parameters or metadata during the request. It is useful to pass context-specific information, such as user preferences, local settings, or feature toggles. Read more at [Handling parameters via headers in API Objects methods](https://wiki.genexus.com/commwiki/wiki?60084).


|  |
| --- |
| **Backlinks** |
| [API object - Delete service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60083) | [Calling rest API Using Postman app](https://wiki.genexus.com/commwiki/wiki?50054) | [Table of contents:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) |
| [Handling parameters via headers in API Objects methods](https://wiki.genexus.com/commwiki/wiki?60084) | [SecurityLevel annotation](https://wiki.genexus.com/commwiki/wiki?55437) |

---
