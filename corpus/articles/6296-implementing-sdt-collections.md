---
title: "Implementing SDT collections"
source_id: 6296
source_url: https://wiki.genexus.com/commwiki/wiki?6296
genexus_version: "18"
---

# Implementing SDT collections

There are at least two ways to work with collections of [Structured Data Types (SDTs)](https://wiki.genexus.com/commwiki/wiki?10021):

1. Defining an SDT object as a collection and then defining a variable (in a certain object) based on that SDT.
2. Defining an SDT object that is not a collection, and then defining a variable (in a certain object) based on that SDT and configuring the variable as a collection.

## [Samples](#Samples)

### [1. Defining an SDT as a collection](#1.+Defining+an+SDT+as+a+collection)

`[imagen omitida: wiki id 32667]`

Note that although 'ClientsItem' is structured data representing each item of the collection, it does not exist as an independent SDT. The defined SDT is the collection one, 'Clients'.

After defining the [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021), you have to define a variable (in a certain object) based on the SDT collection (i.e. named &myClients) and another variable based on a single item of the SDT collection (i.e. named &eachClient):

`[imagen omitida: wiki id 32669]` `[imagen omitida: wiki id 32670]`

Thus, you can, for example, iterate the collection as follows:

```
For &eachClient in &myClients 
     ...  //do something with &eachClient  
EndFor
```

Note that the [Collection property](https://wiki.genexus.com/commwiki/wiki?9761) is set to 'False' for both variables in the above example.

### [2. Define an SDT that is not a collection](#2.+Define+an+SDT+that+is+not+a+collection)

`[imagen omitida: wiki id 32671]`

In this case, the SDT structure has been defined exactly the same as the previous sample but the IsCollection checkbox has not been selected. This means that the SDT definition consists of one item, not a collection. So, how do you define a collection of this data type?

By defining the &myClients variable based on the SDT data type and indicating that it is a collection:

`[imagen omitida: wiki id 32673]`

And defining the &eachClient variable based on the SDT:

`[imagen omitida: wiki id 32672]`

The same code can be defined to iterate the collection:

```
For &eachClient in &myClients     
    ...  // do something with &eachClient
EndFor
```

The way to work with a collection will depend on the need to have defined the item itself. For example, if you need to return it from a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) because in the [Output property](https://wiki.genexus.com/commwiki/wiki?41037) of the Data Provider you cannot specify **Clients.Client**,a non-defined SDT. In that case, you will need to choose the second option.

### [What if you define both SDTs?](#What+if+you+define+both+SDTs%3F)

That is, in the same Knowledge Base, 'Clients' SDT and 'Client' SDT, as they appeared before. Be careful, because GeneXus will not understand that 'Clients.Client' and 'Client' are the same.

### [See also](#See+also)

[Recursive SDTs](https://wiki.genexus.com/commwiki/wiki?4680)  
[Structured Data Type editor](https://wiki.genexus.com/commwiki/wiki?6365)  
[New operator (SDT)](https://wiki.genexus.com/commwiki/wiki?8615)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Loading Compound Data Types (SDT) using Data Providers](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/loading-compound-data-types-sdt-using-data-providers?p=5265)  
`[imagen omitida: wiki id 20668]` [Two ways of returning a collection using a Data Provider](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/two-ways-of-returning-a-collection-using-a-data-provider?p=5271)


|  |
| --- |
| **Backlinks** |
| [Best Practices for Manual Synchronization](https://wiki.genexus.com/commwiki/wiki?22276) | [Collection variables](https://wiki.genexus.com/commwiki/wiki?6352) |
| [Example: 'CustomersProvider' Data Provider](https://wiki.genexus.com/commwiki/wiki?6310) | [For in command](https://wiki.genexus.com/commwiki/wiki?6359) | [IN Operator](https://wiki.genexus.com/commwiki/wiki?11688) | [Recursive SDTs](https://wiki.genexus.com/commwiki/wiki?4680) |
| [Structured Data Type editor](https://wiki.genexus.com/commwiki/wiki?6365) |

---
