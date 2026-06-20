---
title: "Dynamic Transactions that receive parameters"
source_id: 36732
source_url: https://wiki.genexus.com/commwiki/wiki?36732
genexus_version: "18"
---

# Dynamic Transactions that receive parameters

Sometimes you may need to define [Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062) that require receiving parameters in order to use them in the Data Provider associated with the Transaction.

Let's see a scenario that proposes the use of a Dynamic Transaction that needs to receive parameters in order to use them in the Data Provider that retrieves and assigns the data to the Dynamic Transaction attributes.

Consider the following transactions:

```
Customer
{
   CustomerId*
   CustomerName
   CustomerAddress
   ....
}

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

To find out which customers have made the more substantial purchases within a certain period, we're required to define a web panel to allow the end-user entering a date range. After that, the end-user must be able to press a button in order to obtain a PDF list that prints a ranking of all customers, showing the total amount invoiced to each customer in this period. **The output must show the invoiced amounts in descending order.**

So, we propose to create a Dynamic Transaction (called Ranking) and initially, we define it as shown:

```
Ranking
{
   RankingCustomerId*
   RankingCustomerName
   RankingTotalAmount
}
```

We set the properties of the Ranking Transaction:

[Data Provider property](https://wiki.genexus.com/commwiki/wiki?29597) = Yes  
[Used To property](https://wiki.genexus.com/commwiki/wiki?29584) = Retrieve Data

GeneXus understands that it must not create any physical table associated with the Ranking Transaction, and creates the Data Provider by default (Ranking\_DataProvider) with its source initialized with the transaction’s structure. The next step we must follow is to complete the Ranking\_DataProvider, with the data we wish to load in the attributes of the Ranking transaction:

```
RankingCollection
{
   Ranking from Invoice unique CustomerId
   {
       RankingCustomerId = CustomerId
       RankingCustomerName = CustomerName
       RankingTotalAmount = Sum(InvoiceTotal, ....
   }
}
```

The Data Provider, as you can see, is scanning the invoices. Each value of CustomerId is being used one time only, and it is assigned to the RankingCustomerId attribute. For the said customer, all the invoice amounts are summarized and the result is assigned to the RankingTotalAmount attribute. But, it is missingto completethe [Sum Formula](https://wiki.genexus.com/commwiki/wiki?6500) with a filter condition to consider just the invoices that belong to the date range entered by the end-user in the web panel!

When we need to receive parameters in the Data Provider associated with a Dynamic Transaction to use them in its source, we have to:

**1)** Define as many attributes as parameters we need to know, as part of the Dynamic Transaction key (and of course the data type must match). So, in this example, the Ranking transaction must be modified as shown:

```
Ranking
{
  RankingInitialDateReceived*
  RankingFinalDateReceived*
  RankingCustomerId*
  RankingCustomerName
  RankingTotalAmount
}
```

**2)** Include a Parm rule with the new attributes - in our example: Parm(RankingInitialDateReceived, RankingFinalDateReceived); - for the Data Provider associated with the Dynamic Transaction and also for the Dynamic Transaction.

```
Ranking_DataProvider

Rule:
Parm(RankingInitialDateReceived, RankingFinalDateReceived);

Source:
RankingCollection
{
  Ranking from Invoice unique CustomerId
  {
   RankingInitialDateReceived  
   RankingFinalDateReceived
   RankingCustomerId = CustomerId
   RankingCustomerName = CustomerName
   RankingTotalAmount = Sum(InvoiceTotal, InvoiceDate >= RankingInitialDateReceived and InvoiceDate <= RankingFinalDateReceived)
  }
}
```

Look at the Ranking\_DataProvider source that all the attributes that compose the primary key have been declared and the Sum formula definition has been completed.

**3)**The Dynamic Transaction definition with parameters is complete! So now, from the web panel it is possible to call the procedure that lists the ranking, of course sending to it the variables entered by the end-user:

```
Event 'CallRanking'
  Ranking(&InitalDate, &FinalDate)
End event

Ranking Procedure

Rule:
Parm(RankingInitialDateReceived,RankingFinalDateReceived);

Source:
For each Ranking order (RankingTotalAmount)
    print OneLineRanking     ---> {RankingCustomerId, RankingCustomerName, RankingTotalAmount}
Endfor
```

### [Notes:](#Notes%3A)

* GeneXus creates a FUNCTION in the database instead of a VIEW as from Dynamic Transactions that receive parameters.
* The parameters must be instantiated to be able to use the FUNCTION.
* The objects that use the Dynamic Transaction attributes (in our example the Procedure that lists), must have instantiated the attributes that make up the Dynamic Transaction primary key (in our example they are received in the Parm rule, but they can be instantiated inside a For each, etc.). This is because the FUNCTION needs to know the parameters.
* MySQL and SAP Hana DBMS do not support this kind of definition.

### Scope

**Data Store:** SQLServer, Postgre, Oracle, DB2 y DB2 for iSeries


|  |
| --- |
| **Backlinks** |
| [Toc:Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062) | [Reorganization Error Codes and Messages](https://wiki.genexus.com/commwiki/wiki?5952) | [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) |

---
