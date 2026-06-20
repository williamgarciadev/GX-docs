---
title: "Dynamic Transactions Samples"
source_id: 36273
source_url: https://wiki.genexus.com/commwiki/wiki?36273
genexus_version: "18"
---

# Dynamic Transactions Samples

Below are shown samples of use of [Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062).

**1)**Consider the following Product transaction:

```
Product
{
   ProductId*
   ProductDescription
   ProductStock
   ProductExpirationDate
}
```

Now suppose the company has defined promotions in the following way. They offer a 50% off for:

- products for which there are more than 1000 units in stock  
- products for which their expiration date is during this year

To always know the current promotions, we suggest to create a Dynamic Transaction (called Promotion) and with its associated Data Provider (Promotion\_DataProvider) retrieve the products that meet the requirements for promotion.

```
Promotion
{
  PromotionId*
  PromotionDescription
  PromotionStock
  PromotionExpirationDate
}
```

We set the properties of the Promotion Transaction:

* [Data Provider property](https://wiki.genexus.com/commwiki/wiki?29597) = True
* [Used To property](https://wiki.genexus.com/commwiki/wiki?29584) = Retrieve Data

GeneXus understands that it must not create any physical table associated with the Promotion Transaction, and creates the Data Provider by default (Promotion\_DataProvider) with its source initialized with the transaction’s structure:

`[imagen omitida: wiki id 36247]`

The next step we must follow is to complete the Promotion\_DataProvider with the data we wish to load in the attributes of the Promotion Transaction:

`[imagen omitida: wiki id 36307]`

The Data Provider, as you can see, is scanning the products that fulfill with the defined conditions to be in the promotion. Then, for each product that fulfills with that conditions, its attributes values are loaded to the Promotion attributes values.

Note that we have used the [ServerDate function](https://wiki.genexus.com/commwiki/wiki?8490) in order to obtain the current date because variables nor functions that can't be evaluated in the server are not allowed to be used in Data Providers associated with Dynamic Transactions.

Once we have thus modeled the Promotion transaction with its associated Data Provider, it is possible to work with the Promotion transaction and its attributes as usual. We could, for example, execute the form of the Promotion transaction to view the current promotions. We could apply also the Work With for Web and the Work With for Smart Devices Patterns to the Promotion transaction. Besides, the Promotion attributes can be used as regular attributes in a transparent way regardless of not having neither physical tables nor physical fields associated. In addition to this, it is possible to mention the Promotion transaction as [Base Transaction](https://wiki.genexus.com/commwiki/wiki?25418) in For each commands, Data Providers and grids in Web Panels and SD Panels.

**Why is it advantageous to define a dynamic transaction to obtain the current promotions?**  
Because it is a global definition in the Knowledge Base and this is powerful. The Promotion concept exists and in this way, it is defined without storing the involved data (in the database, a view will be created instead a table).  
Note that if the way to define promotions in the company changes, by only modifying the Data Provider associated with the Promotion Dynamic Transaction, all the rest objects that work with the promotions are still valid!

**2)**Let's suppose that in the same GeneXus KB we have the following transactions:

```
Customer
{
   CustomerId*
   CustomerName
   CustomerAddress
   .... 
}
```

```
Invoice
{
   InvoiceId*
   InvoiceDate
   CustomerId
   CustomerName
   CustomerAddress
   InvoiceAmount
   ....
}
```

Some queries that can be requested to you would be:

2.1.  For a given period, to know the amount billed per day.  
2.2. For a given date, to know the total amount billed.  
2.3.  Best day of the year.

Although it is possible to define individual and local solutions to solve each of the above queries, there is a more powerful way to solve the above petitions, and it consists of defining a Dynamic Transaction and executing it in several scenarios to solve the above queries. So, we propose to create a Dynamic Transaction (called Statistics):

```
Statistics
{
   StatisticsDate*
   StatisticsTotalAmount
}
```

We set the properties of the Statistics Transaction:

[Data Provider property](https://wiki.genexus.com/commwiki/wiki?29597) = Yes  
[Used To property](https://wiki.genexus.com/commwiki/wiki?29584) = Retrieve Data

GeneXus understands that it must not create any physical table associated with the Statistics Transaction, and creates the Data Provider by default (Statistics\_DataProvider) with its source initialized with the transaction’s structure. The next step we must follow is to complete the Statistics\_DataProvider, with the data we wish to load in the attributes of the Statistics transaction:

`[imagen omitida: wiki id 36342]`

The Data Provider, as you can see, is scanning the invoices. Each value of invoice date is being used one time only, and it is assigned to the StatisticsDate attribute. For the said date, all the invoice amounts are summarized and the result is assigned to the StatisticsTotalAmount attribute. Then, having the total amounts per date available in Statistics, we will now see that each need can be solved navigating Statistics as our base transaction, and using its attributes as usual.

**2.1.  For a given period, to know the amount billed per day.**

```
For each Statistics
      where StatisticsDate >= &InitialDate 
      where StatisticsDate >= &FinalDate 
      Print Printblock1 {StatisticsDate,StatisticsTotalAmount}
Endfor
```

**2.2. For a given date, to know the total amount billed.**

```
For each Statistics 
   where StatisticsDate = &Date
  Print Printblock1 {StatisticsDate,StatisticsTotalAmount}
Endfor
```

**2.3.  Best day of the year.**

```
For each Statistics order (StatisticsTotalAmount)
    where StatisticsDate.Year() = &Today.Year() 
        Print Printblock1 {StatisticsDate,StatisticsTotalAmount}
        exit
Endfor
```


|  |
| --- |
| **Backlinks** |
| [Toc:Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062) |

---
