---
title: "Example: 'CustomersProvider' Data Provider"
source_id: 6310
source_url: https://wiki.genexus.com/commwiki/wiki?6310
genexus_version: "18"
---

# Example: 'CustomersProvider' Data Provider

A Data Provider is a GeneXus object aimed at providing data collections (for example, a list of customers) or a data structure (for example, customer data) in an easy and high-level, declarative way.  
  
The output is a hierarchical structure: how GeneXus represents that? As an [SDT](https://wiki.genexus.com/commwiki/wiki?10021) or [BC](https://wiki.genexus.com/commwiki/wiki?5846), or a collection of them.  
  
The strength of Data Providers lies in that the focus is on the output. As a result, the GeneXus analyst only has to declare how several data items of the hierarchical output structure should be filled.  
  
Suppose that you have defined the 'Customer' transaction shown below:

`[imagen omitida: wiki id 6297]`

You need to load the customers' database into a collection to send it to another object, such as a Web Panel, for example, or any other object:

`[imagen omitida: wiki id 6311]`

First, you have to define the SDT to load the customers. The first consideration is that you cannot name the SDT with the same name as the transaction (it's not allowed), so you will call it 'Clients'. A second consideration is about the fact that you have [two ways to work with collections](https://wiki.genexus.com/commwiki/wiki?6296). As you will see, you can choose any of them.

### [First option](#First+option)

Defining the 'Clients' collection SDT:

`[imagen omitida: wiki id 6312]`

Next, you have to create the Data Provider. Call it 'CustomersProvider'. In order to work less, after creating the Data Provider we can drag the 'Clients' SDT and the Source will look as follows:

`[imagen omitida: wiki id 6314]`

You only have to fill the values on the right with CustomerId and CustomerName, respectively.  
The 'Output' Property is a special property that should be given special attention, even if it goes unnoticed because the drag and drop operation automatically set it. The image below shows how to indicate which SDT will be the Data Provider output:

|  |  |
| --- | --- |
|  | Note the 'Collection' property. If you had chosen the other possibility, you would have changed to True. |

The rest is easy and familiar. From the object that requires the customer list, i.e. the Web Panel of the image above, we only have to define a  variable of 'Clients' SDT data type to receive the output of the Data Provider and, for example, later convert it to XML format:

```
&clients = CustomersProvider()
&xml = &clients.toXML()
```

See more [Using Data Providers in Other GX Objects](https://wiki.genexus.com/commwiki/wiki?5310)

### [Second option](#Second+option)

Defining the 'Client' SDT:

`[imagen omitida: wiki id 6313]`

As in the previous option, suppose now you have to create the 'CustomersProvider' Data Provider. Doing the same as before, after dragging the 'Client' SDT to the Source area, you will have the following:

|  |  |
| --- | --- |
|  | with the Output Property:    However, this is not what you want... You need to load a collection of customers, so you need to change the 'Collection' property as follows: |

Note that changing 'Collection' to True introduces a new 'Collection Name' Property. You have to enter a name and then change the Source, adding a group with that name as a root:

`[imagen omitida: wiki id 6318]`

The rest is similar to the first option (defining the &clients variable as a collection of the 'Client' SDT data type).


|  |
| --- |
| **Backlinks** |
| [Category:Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) | [Defining a Data Provider](https://wiki.genexus.com/commwiki/wiki?23658) | [HowTo: Use the Infer Structure property of a Data Provider](https://wiki.genexus.com/commwiki/wiki?23651) |

---
