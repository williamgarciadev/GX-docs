---
title: "Dynamic Transactions"
source_id: 28062
source_url: https://wiki.genexus.com/commwiki/wiki?28062
genexus_version: "18"
---

# Dynamic Transactions

Dynamic Transactions are those [Transactions](https://wiki.genexus.com/commwiki/wiki?1908) that are defined with the aim of having data queried at runtime (views in the database are created by GeneXus) instead of having associated physical tables.

This kind of definition is very powerful because it offers total flexibility to freely define queries that can be executed not only by executing the Transactions forms but also by making reference to them as [Base Transaction](https://wiki.genexus.com/commwiki/wiki?25418) in [For Each command](https://wiki.genexus.com/commwiki/wiki?24744)s, [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270) and Grids in [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916) and [Panels](https://wiki.genexus.com/commwiki/wiki?24829). In addition to this, it is possible to apply the Work With [Patterns](https://wiki.genexus.com/commwiki/wiki?2814) to Dynamic Transactions. Furthermore, the Dynamic Transactions attributes can be used as regular attributes in Printblocks, Conditions, etc., in a transparent way regardless of not having neither physical tables nor physical fields associated with these Transactions.

A Transaction is set as Dynamic by setting its object properties:

1. [Data Provider](https://wiki.genexus.com/commwiki/wiki?29597) = True
2. [Used To](https://wiki.genexus.com/commwiki/wiki?29584) = Retrieve Data

In consequence of setting the [Data Provider property](https://wiki.genexus.com/commwiki/wiki?29597) = True, GeneXus automatically creates a Data Provider named TransactionName\_DataProvider with its source initialized with the Transaction’s structure, and you only have to complete that initialized source in order to define the desired data to be loaded into the Dynamic Transaction attributes.

As a consequence of setting the [Used To](https://wiki.genexus.com/commwiki/wiki?29584) = Retrieve Data, GeneXus understands that the Transaction is Dynamic. Therefore, it will not create physical table(s) associated with said Transaction. Instead, **GeneXus will create a view in the database.**

### [Examples of use to understand the concept](#Examples+of+use+to+understand+the+concept)

Suppose that a company sells products and offers services. It could be an automotive company or any other kind of company.

As you can see below, two Transactions have been defined: Product and Service, to record products and services respectively.

```
Product
{
   ProductId*
   ProductDescription
   ProductStock
   ProductExpirationDate
}

Service
{
   ServiceId*
   ServiceDescription
   ServiceHoursDuration
}
```

There are many ways to model this reality, where a company sells products and services. In this case, it was chosen to define two independent Transactions, to design that they are two different concepts.

The objective is to have together all the data of all the products and services for whatever is needed; for example, to list in alphabetical order all the things (both products and services) the company offers.

To solve the union in a very easy way, our approach is to define a Dynamic Transaction, for example, named SaleItem as shown:

```
SaleItem
{   
    SaleItemId*
    SaleItemType*
    SaleItemDescription
}
```

Note that the key of the SaleItem Transaction is a compound key. It has been defined this way because our objective is to load, in its attributes, the data of all the products and the data of all the services. So, to be able to coexist products and services with the same identifier value, each sales item has a compound key: SaleItemId\*, SaleItemType\*, so that we can assign in SaleItemType a “P” for products and an “S” for services as part of the key.

Then, by setting the SaleItem transaction properties:

* Data Provider=True
* Used To=Retrieve Data

GeneXus understands that it must not create any physical table associated with that transaction, and creates a Data Provider named SaleItem\_DataProvider with its source initialized with the transaction’s structure:

`[imagen omitida: wiki id 36189]`

The next step is to complete this Data Provider with the data required to load in the attributes of the SaleItem Transaction:

`[imagen omitida: wiki id 36193]`

In the above Data Provider, the code block offered by default was copied and pasted below. In the first code structure, all the Products were retrieved and assigned as Sale items, and in the second one, all the Services were retrieved and assigned as Sale items. Once the SaleItem Transaction is modeled with its associated Data Provider, it’s possible to work on the Transaction, as usual, executing its form and viewing all the sale items and/or referencing it as <base Transaction> and/or naturally using its attributes in other objects.

Look at the following Procedure that prints all the sale items offered by the automotive company ordered alphabetically. You can see that all the concepts are used as usual, despite the fact that the SaleItem Transaction is Dynamic.

`[imagen omitida: wiki id 36194]`

As mentioned before, you could choose to define a Web Panel using the Dynamic Transaction attributes as well as apply all the GeneXus features naturally.

Now, suppose that the automotive company has the following requirement: They want only one grid in the invoice’s form when an invoice is entered (they do not want two independent grids with Products in one and Services in the other in the invoice). This can be modeled without any problem since the primary key of a Dynamic Transaction (in this case SaleItemId\*, SaleItemType\*) can be a foreign key in another Transaction (in the example, in the invoice’s lines):

```
Invoice
{
 InvoiceId*
 InvoiceDate
 CustomerId
 CustomerName
 Line
 { 
   SaleItemId*
   SaleItemType*
   SaleItemDescription
   InvoiceLineQuantity
 }
}
```

The following image shows the form of the Invoice Transaction at runtime. Note that the grid contains four sale items (three are services and one is a product). You can also see the selection list of sale items.

`[imagen omitida: wiki id 36229]`

Note: This is a small example that does not solve the issue of the prices of products and services. Suppose that prices for products and services are recorded by date respectively and they are obtained in the invoice.

### [Why is it advantageous to define Dynamic Transactions?](#Why+is+it+advantageous+to+define+Dynamic+Transactions%3F)

* Because they offer the benefit of working with the Transaction/Attribute paradigm, instead of defining local solutions (for example with [SDTs](https://wiki.genexus.com/commwiki/wiki?2427) and Data Providers, or Procedures, or defining the same filters in several objects or a Data Selector). In other words, a Transaction is a global and powerful definition in a Knowledge Base. So, if a concept exists, it can be represented by defining a Dynamic Transaction (thus, a view will be created instead of a physical table in the database) and it will be used as usual.
* They allow describing realities and intentions with flexibility.
* Simplify programming.
* When a Dynamic Transaction ceases to be dynamic, then a [Reorganization](https://wiki.genexus.com/commwiki/wiki?5288) happens in the upcoming database impact: The physical table is created but not empty. On the other hand, the view is executed and the new physical table is initialized with the view execution result. (Note: This does not happen with [Dynamic Transactions that receive parameters](https://wiki.genexus.com/commwiki/wiki?36732)).

### [Restrictions](#Restrictions)

* Dynamic Transactions can not have parallel Transactions in the KB. In other words, a necessary requirement for defining a Transaction as Dynamic is that its primary key must be different from other Transactions' primary keys.
* Not all Transactions can be defined as Dynamic Transactions. Some restrictions apply: the Data Provider query can be represented as a View. If that's not the case, the Specification will report an error.
* Variables are not allowed to be used in Data Providers associated with Dynamic Transactions. Functions that can not be evaluated by the server, either.
* Dynamic Transactions are calculated and resolved at reorganization time. At that moment a CREATE VIEW is performed in the database and that is fixed. At generation time or runtime, the Data Store values are not taken into account, nor changes made in the web.config file.

### [Performance](#Performance)

GeneXus creates an SQL View for these Transactions, and usually, the DBMS is capable of deploying a wide array of optimization strategies to ensure good performance.


* [Dynamic Transactions Samples](https://wiki.genexus.com/commwiki/wiki?36273)
* [Dynamic Transactions that update data](https://wiki.genexus.com/commwiki/wiki?28656)
* [Dynamic Transactions that receive parameters](https://wiki.genexus.com/commwiki/wiki?36732)
  + [Temporal Data using Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?45622)

---
