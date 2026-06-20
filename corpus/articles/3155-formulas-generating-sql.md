---
title: "Formulas/Generating SQL"
source_id: 3155
source_url: https://wiki.genexus.com/commwiki/wiki?3155
genexus_version: "18"
---

# Formulas/Generating SQL

GeneXus will generate a single SQL statement to retrieve all the attributes in a For Each statement, including formulas. This happens for every aggregation formula (sum/count/find/min/max), even if they are defined over other formula attributes. This will boost your application's performance.

### [Examples](#Examples)

If you define the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

```
Customer
{
   CustomerId*
   CustomerName
   CustomerTotal = sum(InvoiceTotal)
}

Invoice
{
   InvoiceId*
   CustomerId
   {
      ItemId*
      ItemPrice
      InvoiceLineQty
      InvoiceLineTotal = ItemPrice * InvoiceLineQty
   }

   InvoiceTotal = sum(InvoiceLineTotal)
}

Item
{
   ItemId*
   ItemPrice
}
```

And then create a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) such as:

```
For Each
    &CustomerTotal = CustomerTotal
    &CustomerName = CustomerName
Endfor
```

GeneXus will create the following SQL statement for SQL Server:

```
SELECT T1.[CustomerId], COALESCE( T2.[CustomerTotal], 0) AS CustomerTotal, T1.[CustomerName] 
        FROM ([CUSTOMER] T1  
        LEFT JOIN (
            SELECT SUM(COALESCE( T4.[InvoiceTotal], 0)) AS CustomerTotal, T3.[CustomerId] 
                FROM ([INVOICE] T3  
                LEFT JOIN (
                    SELECT SUM(T6.[ItemPrice] * T5.[InvoiceLineQty]) AS InvoiceTotal, T5.[InvoiceId] 
                    FROM ([INVOICELEVEL1] T5 
                        INNER JOIN [ITEM] T6  ON T6.[ItemId] = T5.[ItemId])
                    GROUP BY T5.[InvoiceId] ) T4 
                ON T4.[InvoiceId] = T3.[InvoiceId])
                GROUP BY T3.[CustomerId] ) T2 ON T2.[CustomerId] = T1.[CustomerId]) 
        ORDER BY T1.[CustomerId]
```

Basically, the inner SELECT calculates the InvoiceTotal over the InvoiceLines, the next SELECT calculates the CustomerTotal over the InvoiceTotal, and the top SQL Sentence reads the Customer data and combines it with the second level to get the value of the formula.  
  
If, instead of having Customer as [Base Table](https://wiki.genexus.com/commwiki/wiki?6347), the For Each command has Invoice as Base Table :

```
 For Each
    &CustomerTotal = CustomerTotal
    &CustomerName = CustomerName
    &InvoiceDate= InvoiceDate
EndFor
```

Then the SQL statement for SQL Server is:

```
SELECT T1.[CustomerId], T1.[InvoiceId], COALESCE( T4.[InvoiceTotal], 0) AS InvoiceTotal, 
     COALESCE( T3.[CustomerTotal], 0) AS CustomerTotal, T1.[InvoiceDate], T2.[CustomerName] 
       FROM ((([INVOICE] T1  INNER JOIN [CUSTOMER] T2  ON T2.[CustomerId] = T1.[CustomerId]) 
       LEFT JOIN (
            SELECT SUM(COALESCE( T6.[InvoiceTotal], 0)) AS CustomerTotal, T5.[CustomerId] 
                   FROM ([INVOICE] T5  
                   LEFT JOIN (
					   SELECT SUM(T8.[ItemPrice] * T7.[InvoiceLineQty]) AS InvoiceTotal, T7.[InvoiceId], T7.[ItemId] 
					   FROM ([INVOICELEVEL1] T7  
					         INNER JOIN [ITEM] T8  ON T8.[ItemId] = T7.[ItemId]) 
					   GROUP BY T7.[InvoiceId], T7.[ItemId] ) T6 
				   ON T6.[InvoiceId] = T5.[InvoiceId]) 
				   GROUP BY T5.[CustomerId] ) T3 ON T3.[CustomerId] = T1.[CustomerId]) 
		LEFT JOIN (
		     SELECT SUM(T6.[ItemPrice] * T5.[InvoiceLineQty]) AS InvoiceTotal, T5.[InvoiceId] 
		            FROM ([INVOICELEVEL1] T5  
		            INNER JOIN [ITEM] T6  ON T6.[ItemId] = T5.[ItemId]) 
		            GROUP BY T5.[InvoiceId] ) T4 
		     ON T4.[InvoiceId] = T1.[InvoiceId]) 
	  ORDER BY T1.[InvoiceId]
```

Other examples:

```
For Each
     Order CustomerTotal                  // Formulas in the Order clause
     Where CustomerTotal > &CustomerTotal // Formulas in conditions
    &CustomerName = CustomerName
    &InvoiceDate= InvoiceDate
EndFor 
```

```
For Each
    &DescriptionForMostExpensiveItem = max(ItemPrice, 1=1, 0, ItemDescription)  // Max formula defined over the invoice lines 
    //that returns an attribute in Invoice Lines' extended table
    &InvoiceDate= InvoiceDate
EndFor
```

```
For Each
    &DescriptionForMostExpensiveItem = max(ItemPrice, ItemId > &ItemId, 0, ItemDescription)  // Variables in formulas' conditions
    &InvoiceDate= InvoiceDate
EndFor
```

```
For Each
    &InvoiceTotalAverage = sum(InvoiceTotal) / Count(InvoiceDate)  // Expressions with formulas that are defined over formulas
    &CustomerName = CustomerName
EndFor
```

```
For Each
    Where Sum(InvoiceTotal) >  100 // Filter by aggregation formulas
    &CustomerName = CustomerName
EndFor
```

```
For Each
    Where Sum(InvoiceTotal) / Count(InvoiceDate) >  100 // Filter by compound aggregation formulas
    &CustomerName = CustomerName
EndFor
```


|  |
| --- |
| **Backlinks** |
| [Examples of Using Formulas](https://wiki.genexus.com/commwiki/wiki?5882) | [Category:Formulas](https://wiki.genexus.com/commwiki/wiki?5861) |

---
