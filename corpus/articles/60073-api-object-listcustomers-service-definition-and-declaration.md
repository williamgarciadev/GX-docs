---
title: "API object - ListCustomers service definition and declaration (GeneXus 18 Upgrade 12 or prior)"
source_id: 60073
source_url: https://wiki.genexus.com/commwiki/wiki?60073
genexus_version: "18"
---

# API object - ListCustomers service definition and declaration (GeneXus 18 Upgrade 12 or prior)

This article describes all the necessary steps to define an [API object](https://wiki.genexus.com/commwiki/wiki?46151) (called APICustomers) and declare inside it a ListCustomers service that returns all the Customer data.  
  
Consider a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) containing:

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

2) An [SDT](https://wiki.genexus.com/commwiki/wiki?2427) that is a collection with the same structure as the Customer Transaction:

`[imagen omitida: wiki id 50250]`

3) A [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) with the logic needed to return all the customer's data:

`[imagen omitida: wiki id 50252]`

Note that the Data Provider has the previously defined SDT as the output parameter.

Create an [API object](https://wiki.genexus.com/commwiki/wiki?46151) (by selecting in the main GeneXus Menu **File > New > Object**) and name it "APICustomers". Inside its **Service Source** tab, you have to declare, for each service, a mapping between its external name (exposed as a service) and the internal implementation in the KB (in this example, the CustomerList Data Provider). Look at the following mapping:

```
Customer{
    ListCustomers(out:&SDTCustomers) => CustomerList(&SDTCustomers);
}
```

The external service name is ListCustomers; internally, it is solved with the CustomerList Data Provider.

The service source is not allowed to access data. Therefore, you have to use a [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270) or a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) object instead of a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) or [Business Component](https://wiki.genexus.com/commwiki/wiki?2277).

You could define the following events in the Events tabs, if necessary:

```
Event Before
    //Some Code if is needed
Endevent

Event After
    //Some Code if is needed
Endevent

Event ListCustomers.Before
    //Some code if is needed
Endevent

Event ListCustomers.After
    //Some Code if is needed
EndEvent
```

The events execution order would be as follows:

1. Event 'Before'
2. Event 'ListCustomers.Before'
3. ListCustomers method (CustomerList Data Provider)
4. Event 'ListCustomers.After'
5. Event 'After'

You can see all the steps being executed:

`[imagen omitida: wiki id 49758]`

### [See Also](#See+Also)

[Json Collection Serialization property](https://wiki.genexus.com/commwiki/wiki?48147)
