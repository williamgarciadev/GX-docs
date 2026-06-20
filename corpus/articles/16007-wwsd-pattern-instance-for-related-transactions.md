---
title: "WWSD Pattern instance for Related Transactions"
source_id: 16007
source_url: https://wiki.genexus.com/commwiki/wiki?16007
genexus_version: "18"
---

# WWSD Pattern instance for Related Transactions

Supposing a Neighborhood Transaction with the following attributes:  
`[imagen omitida: wiki id 37462]`

And a Property Transaction that defines the following relation with the Real Estate Companies Transaction:  
`[imagen omitida: wiki id 37463]`

Upon applying for the Work With Devices pattern to the Property and Neighborhood Transactions, the following instances associated with the Transactions are generated:

`[imagen omitida: wiki id 37464]`

The instance generated for the Property Transaction is the same as the one generated for [Transactions with more than one level](https://wiki.genexus.com/commwiki/wiki?16004), and Negibhrood will have a [Section Node](https://wiki.genexus.com/commwiki/wiki?20624) referencing Property Transaction.

At runtime, upon selecting a Neighborhood, a Tab will be viewed with the detailed data on that Neighborhood (i.e. *Section (General)*), and another Tab with the list of Properties (i.e. *Section (Property)*) corresponding to that Neighborhood.

`[imagen omitida: wiki id 37465]`

For the case of more related transactions, a new Section will be generated for each one of them. In this case, because the pattern also applies to the Property transaction, upon clicking on one of the properties from the list, it is possible to edit the property data by calling the Edit generated in the Property transaction instance (since only the View, and not the property’s Edit, is generated from the Real Estate transaction instance).

If the pattern is not applied to the Property Transaction, it will only be possible to view the properties from the Property Tab, but upon clicking on any of them, no actions will be executed.

## [See also](#See+also)

[Work With Pattern instance for Multi-level Transactions](https://wiki.genexus.com/commwiki/wiki?16004)

## [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Container of sections in the Detail screen of the Work With](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/container-of-sections-in-the-detail-screen-of-the-work-with?p=3658)


|  |
| --- |
| **Backlinks** |
| [Category:Work With object](https://wiki.genexus.com/commwiki/wiki?15974) |
|

---
