---
title: "API object - GetByKey service definition and declaration"
source_id: 50052
source_url: https://wiki.genexus.com/commwiki/wiki?50052
genexus_version: "18"
---

# API object - GetByKey service definition and declaration

This article describes all the necessary steps to declare, inside an [API object](https://wiki.genexus.com/commwiki/wiki?46151) called APICustomers, a GetByKey service that returns all the information of a certain customer.

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

2) An [API object](https://wiki.genexus.com/commwiki/wiki?46151) called APICustomers. In its **Service Source**tab, it already contains a declared service that maps an external name exposed as a service (ListCustomers) with the internal implementation in the KB (the CustomerList Data Provider):

`[imagen omitida: wiki id 50856]`

Now, suppose you need to define another service (method) named GetByKey, as part of the APICustomers object, to bring the information of a particular Customer received as a parameter (the customer identifier).

To do so, first set the Customer Transaction as a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846).

After that, create a new [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) and name it CustomerGetByKey.

In the Procedure Rules section, define a [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) as follows:

```
Parm(in:&CustomerId, out:&Customer);
```

In the Procedure Source, define the following code:

```
&Customer.Load(&CustomerId)
If &Customer.Fail()
    &Customer.CustomerId=0
    &Customer.CustomerName= "Invalid data"
EndIf
```

* &CustomerId is a variable based on the CustomerId attribute.
* &Customer is a variable based on the Customer Business Component data type.

Next, go to the APICustomers API object, and inside its Service Source declare the new method (GetByKey) under the ListCustomers method:

```
Customer{
    ...
    GetByKey(in:&CustomerId, out:&Customer, out:&Messages)=> CustomerGetByKey(&CustomerId, &Customer);
}   
```

The GetByKey method uses input and output parameters represented by variables, so these variables must also be defined in the API object Variables section.

Note that in the service declaration, the &Messages variable is an out parameter and it is not mentioned in the implementation. This is supported. This kind of variable can be assigned in the [AFTER event](https://wiki.genexus.com/commwiki/wiki?46151) of the service.

The next step is to define the [Events](https://wiki.genexus.com/commwiki/wiki?46151) in the Events section of the APICustomers API object.

For each defined method, such as GetByKey, you can define their respective Events: Before and After.

```
Event GetByKey.Before
    If &CustomerId < 0
        &RestCode=412
        return
    endif
EndEvent

Event GetByKey.After
    If &Customer.CustomerId= 0
        &Message.Type= MessageTypes.Error
        &Message.Description= format("There was an error loading Customer Information &1.",&CustomerId)
        &Messages.Add(&Message)
        &RestCode= 404
    EndIf
EndEvent
```

Remember that &RestCode is a predefined variable that you need to set to customize the returned [HTTP Status Code](https://www.restapitutorial.com/httpstatuscodes.html).

The order of events executed when calling the GetByKey method is as follows:

1. Event 'Before'
2. Event 'GetByKey.Before'
3. GetByKey method (CustomerGetByKey Procedure internally)
4. Event 'GetByKey.After'
5. Event 'After'

Below you can see all the steps being executed:

`[imagen omitida: wiki id 50028]`

**Note**: This service supports the use of optional HTTP headers to provide additional parameters or metadata during the request. It is useful to pass context-specific information, such as user preferences, local settings, or feature toggles. Read more at [Handling parameters via headers in API Objects methods](https://wiki.genexus.com/commwiki/wiki?60084).


|  |
| --- |
| **Backlinks** |
| [API object - GetByKey service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60074) | [Calling rest API Using Postman app](https://wiki.genexus.com/commwiki/wiki?50054) | [Table of contents:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) |
| [Handling parameters via headers in API Objects methods](https://wiki.genexus.com/commwiki/wiki?60084) | [SecurityLevel annotation](https://wiki.genexus.com/commwiki/wiki?55437) |

---
