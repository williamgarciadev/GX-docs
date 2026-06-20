---
title: "Automatic data population associated with Transactions"
source_id: 32706
source_url: https://wiki.genexus.com/commwiki/wiki?32706
genexus_version: "18"
---

# Automatic data population associated with Transactions

Since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?27605,,), it is possible to easily define how to populate data automatically to physical tables associated with Transactions.

This saves you the task of manually having to load initial data to the tables.

By setting the following properties in a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

* [Data Provider](https://wiki.genexus.com/commwiki/wiki?29597) = True
* [Used To](https://wiki.genexus.com/commwiki/wiki?29584) = Populate Data

you can take advantage of this feature.

For example, let's consider the Country Transaction:  
  
`[imagen omitida: wiki id 32705]`

If you set its **Data Provider property =True**, GeneXus creates a Data Provider named **Country\_DataProvider** and initializes its source with the Transaction’s structure:

`[imagen omitida: wiki id 29598]`

You may for example complete the Data Provider as shown below:

`[imagen omitida: wiki id 29629]`

And if the property **Used To = Populate Data**, GeneXus understands that the objective of the Data Provider is to populate the Country physical table.

### [See also](#See+also)

[Used to property](https://wiki.genexus.com/commwiki/wiki?29584)  
[Automatic data population associated with Transactions - FAQ](https://wiki.genexus.com/commwiki/wiki?31018)

### [Availability](#Availability)

This feature is available as of [GeneXus 15 Upgrade 1](https://wiki.genexus.com/commwiki/wiki?32288,,).


* [Populate Data property](https://wiki.genexus.com/commwiki/wiki?46340)
* [Automatic data population associated with Transactions - FAQ](https://wiki.genexus.com/commwiki/wiki?31018)

---
