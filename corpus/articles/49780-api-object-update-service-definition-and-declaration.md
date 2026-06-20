---
title: "API object - Update service definition and declaration"
source_id: 49780
source_url: https://wiki.genexus.com/commwiki/wiki?49780
genexus_version: "18"
---

# API object - Update service definition and declaration

This article describes all the necessary steps to declare, inside an [API object](https://wiki.genexus.com/commwiki/wiki?46151) called APICustomers, an Update service that updates the data of a certain customer (received by parameter) into the Database.

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

2) An [API object](https://wiki.genexus.com/commwiki/wiki?46151) called APICustomers. In its **Service Source**tab, it already contains three services declared that map external names exposed as services with the internal implementations in the KB:

`[imagen omitida: wiki id 50947]`

Now, suppose you need to define another service (method) named Update, as part of the APICustomers object, to allow updating a certain Customer in the database (the customer data is sent as parameters).

To achieve this, the Customer Transaction must be set as a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846).

Next, you have to create a new [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) named CustomerUpdate.

In the Procedure Rules section, define a [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) as follows:

```
Parm(in:&CustomerId, in:&CustomerName, in:&CustomerLastName, out:&Messages);
```

In the Procedure Source, define the following code:

```
&Customer.Load(&CustomerId)
&Customer.CustomerName=&CustomerName
&Customer.CustomerLastName=&CustomerLastName

If &Customer.Update()
    commit
else
    rollback
Endif

&Messages= &Customer.GetMessages()
```

* &Customer is a variable based on the Customer Business Component data type.
* &Messages is a variable based on the Messages data type.

Now, go to the APICustomers API object, and inside its Service Source declare the new method (Update) under the last method:

```
Customer{
    ...

    [RestMethod(PUT)]
    Update(in:&CustomerId, in:&CustomerName, in:&CustomerLastName, out:&Messages)
    =>CustomerUpdate(&CustomerId, &CustomerName, &CustomerLastName, &Messages);
}
```

Note that in this case, the [RestMethod annotation](https://wiki.genexus.com/commwiki/wiki?50508) precedes the service declaration indicating that the HTTP method to be used is PUT.

The &CustomerId, &CustomerName, and &CustomerLastName variables are defined as input parameters (they are sent to be assigned).

The &Messages variable is an output parameter that returns the messages obtained after performing the [Business Component Update method](https://wiki.genexus.com/commwiki/wiki?31696) to inform the user if the operation was successful.

It is important to add the same variables you already defined in the Procedure object in the API object.

The next step is to define–if necessary–the [Events](https://wiki.genexus.com/commwiki/wiki?46151) in the Events section of the API object (APICustomers).

```
Event Update.Before
    //Some Code if is needed
EndEvent

Event Update.After
    //Some Code if is needed
EndEvent
```

The 'Update.Before' and 'Update.After' events will be executed on each invocation of the Update service.

The order of events executed in this example is as follows:

1. Event 'Before'
2. Event 'Update.Before'
3. Update method (CustomerUpdate Procedure internally)
4. Event 'Update.After'
5. Event 'After'

Below you can see all the steps being executed:

`[imagen omitida: wiki id 49793]`

**Note**: This service supports the use of optional HTTP headers to provide additional parameters or metadata during the request. It is useful to pass context-specific information, such as user preferences, local settings, or feature toggles. Read more at [Handling parameters via headers in API Objects methods](https://wiki.genexus.com/commwiki/wiki?60084).


|  |
| --- |
| **Backlinks** |
| [API object - Update service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60082) | [Calling rest API Using Postman app](https://wiki.genexus.com/commwiki/wiki?50054) | [Table of contents:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) |
| [Handling parameters via headers in API Objects methods](https://wiki.genexus.com/commwiki/wiki?60084) | [SecurityLevel annotation](https://wiki.genexus.com/commwiki/wiki?55437) |

---
