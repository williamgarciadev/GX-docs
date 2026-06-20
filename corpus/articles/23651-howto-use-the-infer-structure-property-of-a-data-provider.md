---
title: "HowTo: Use the Infer Structure property of a Data Provider"
source_id: 23651
source_url: https://wiki.genexus.com/commwiki/wiki?23651
genexus_version: "18"
---

# HowTo: Use the Infer Structure property of a Data Provider

You often need to show information from your database in data collections. The [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) is a [GeneXus object](https://wiki.genexus.com/commwiki/wiki?1866) aimed at providing data collections (for example, a list of customers) or a data structure (for example, customer data) in an easy, high-level, and declarative manner.

The output is a hierarchical structure: how does GeneXus represent that? As a [Structured Data Type (SDT)](https://wiki.genexus.com/commwiki/wiki?10021) or BC ([Business Component](https://wiki.genexus.com/commwiki/wiki?5846)) (or a collection of them). This output may be defined externally by an SDT (see [Example: 'CustomersProvider' Data Provider](https://wiki.genexus.com/commwiki/wiki?6310). See more information on how to create a Data Provider using an SDT), or implicitly through its own source/structure.

This article is meant to show an example of how to use the [Infer Structure property](https://wiki.genexus.com/commwiki/wiki?23628) to let GeneXus infer the structure of the SDT associated with your Data Provider, and to provide an example of how GeneXus can help us in defining the SDT structure when you have defined a Data Provider but not its associated SDT.

Suppose that you have defined the 'Customer' transaction as shown below:

`[imagen omitida: wiki id 23656]`

And you need to load all Customers into a collection and send it to another object, such as a Web Panel for instance, or to any other object.

#### [Step 1: Define the Data Provider structure](#Step+1%3A+Define+the+Data+Provider+structure)

You define the following 'CustomersProvider' Data Provider structure:

```
Clients
{
    Client
    {
        Code = CustomerId
        Name = CustomerName
    }
}
```

Now you need to define its output SDT.

#### [Step 2: Set the Infer Structure property as 'Yes, if SDT is dynamic'](#Step+2%3A+Set+the+Infer+Structure+property+as+%27Yes%2C+if+SDT+is+dynamic%27)

Now you have to set the Infer Structure property as "Yes, if SDT is dynamic" for 'CustomersProvider'.

#### [Step 3: Save](#Step+3%3A+Save)

Save the 'CustomersProvider' *Data Provider*.

When you save the *Data Provider*, GeneXus will automatically generate an SDT with the structure necessary, associating it to the Data Provider [Output property](https://wiki.genexus.com/commwiki/wiki?41037).

#### [Step 4: Done!](#Step+4%3A+Done%21)

The following output will result after you set the Infer Structure property as "Yes, if SDT is dynamic" and save:

```
========== Specification started ==========
Specifying CustomersProvider (1 of 1) ...
Specification Success
Reloading Data Provider 'CustomersProvider'...Done
```

The newly-created SDT will be available from the Folder View associated with the 'CustomersProvider':

`[imagen omitida: wiki id 23652]`

With its structure inferred from the 'CustomersProvider' *Data Provider*:

`[imagen omitida: wiki id 23655]`

Note that the SDT generated will have its [Dynamic structure property](https://wiki.genexus.com/commwiki/wiki?23632) set to true. This means that every time that the Data Provider is saved, the structure of the SDT set in the Data Provider's [Output property](https://wiki.genexus.com/commwiki/wiki?41037) will be updated (inferred by the specifier using the Data Provider structure). When the SDT is updated by the user, this property is automatically set to 'False', thus disabling the inference mechanism, and consequently, the SDT will not be updated when the Data Provider structure is changed.

### [Availability](#Availability)

The inference mechanism for SDTs is available as of [GeneXus Tilo Beta 3](https://wiki.genexus.com/commwiki/wiki?23693,,).

### [See Also](#See+Also)

[Example: 'CustomersProvider' Data Provider](https://wiki.genexus.com/commwiki/wiki?6310)  
[Dynamic structure property](https://wiki.genexus.com/commwiki/wiki?23632)


|  |
| --- |
| **Backlinks** |
| [Defining a Data Provider](https://wiki.genexus.com/commwiki/wiki?23658) | [Infer Structure property](https://wiki.genexus.com/commwiki/wiki?23628) |

---
