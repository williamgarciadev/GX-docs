---
title: "Nested For each commands to implement a Control Break"
source_id: 30878
source_url: https://wiki.genexus.com/commwiki/wiki?30878
genexus_version: "18"
---

# Nested For each commands to implement a Control Break

Many times you may need to process for every record in a table, their related records in another one, **but only for the records of the first table that have related records in the second table**. To achieve this, it is necessary to scan and process data stored in the second table, grouped by certain criteria. This is known as a control break.

Look at the following [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) structures:

```
Country
{
   CountryId*
   CountryName
}
Customer
{
   CustomerId*
   CustomerName
   CustomerEmail
   CountryId
   CountryName
}
```

Suppose you are asked to list all customers grouped by country, but only the countries that have customers associated with them should be included in the list.

It is clear that to solve this, you cannot obtain the countries from the COUNTRY table, because many countries are entered there, regardless of whether they have customers or not. On the other hand, you will have to go over the CUSTOMER table, and for each customer to extract the corresponding country. By doing this, you will only obtain countries that belong to a customer. But apart from preventing the appearance of countries with no customers, you need **to group** the customers that belong to the same country and proceed to print each country name followed by its related customer's data.

Defining a control break is quite simple and may be performed following “the recipe" below:

1. [Nested For each commands](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?30865,,) are needed.

2. They must have the same [base table](https://wiki.genexus.com/commwiki/wiki?6347).  
2.1. How many For each commands? A number exceeding the number of breaks by one.

3. You must establish, in the [order clause](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6075,,) of each external [For each command](https://wiki.genexus.com/commwiki/wiki?24744), the attribute or the set of attributes by which you want to “break”.

The following Procedure source shows the code that defines the control break asked in the above requirement:

```
For each Customer order CountryName
    print country {CountryName}
    For each Customer
        print customer {CustomerName, CustomerEmail}
    Endfor
Endfor
```

From the previous code, GeneXus will assume that the base table it must navigate is CUSTOMER and that it must take the first record in the CUSTOMER table and retain the country name in memory (because it is CountryName, the attribute mentioned next to the order clause). Then, it will have to print the country name (first sentence written within the main For each), and “as long as the country name remains unchanged, it will have to execute the nested For each and sequentially process all records with that country name". In the case of a record with a different country name, it will have to execute the external For each again and proceed as explained.

It is important to understand that, even when there are two nested For each commands, there is no double access to the table. You can imagine that a pointer is running along with the table in a sequential manner. Since the table is accessed as ordered by the grouping criterion desired, you can think its records are processed sequentially showing each country name once, followed by the customer data for that country.

So, upon a code that fulfills with the control break "recipe", GeneXus will determine:

1. To scan a base table (CUSTOMER in this case), ordered by the attribute(s) specified in the order clause of the external For each (CountryName in this case, which belongs to the CUSTOMER [extended table](https://wiki.genexus.com/commwiki/wiki?6029)).

2. For the record pointed at, to execute sentences defined before the nested For each (in this case, the value of the CountryName attribute is retrieved and printed).

3. While the attribute value(s) mentioned in the order clause (CountryName in this case) remains unchanged:  
3.1. To execute the sentences defined inside the nested For each (in this case CustomerName and CustomerEmail values of the record pointed at are printed on the same line).  
3.2. To read the following record.

4. To return to Step 2 (this point is reached either because we arrived at the table´s end, or because the CountryName value has been changed).

The following image shows customers data linked with its countries, in order to show which records are processed by the main For each and which are processed by the nested For each:

`[imagen omitida: wiki id 30957]`

At runtime, the list looks as follows:

`[imagen omitida: wiki id 30972]`

There are more countries stored in the COUNTRY table that not appear on the list because they have no related customers.

If you want besides to group by CountryName, then, to print all the customers of each country sorted by CustomerName, you only have to add the desired order clause to the nested For each (in this case: order CustomerName) as shown:

```
For each Customer order CountryName
    print country {CountryName}
    For each Customer order CustomerName
        print customer {CustomerName, CustomerEmail}
    Endfor
 Endfor
```

GeneXus will choose to scan the CUSTOMER table ordered by an index made up by the concatenation of the orders of each For each command with order clause (in the above example: CountryName, CustomerName). Thus, the records will be scanned ordered by the compound index, the break will be performed by CountryName (the attribute specified in the order clause of the external For each) and for each country, its related customers will be shown ordered by CustomerName (because the records are accessed sequentially sorted by CountryName, CustomerName).

### [Another example: Double control break](#Another+example%3A+Double+control+break)

Now consider the following transaction structures (they are almost the same as above, except that the Continent transaction is new, and each country belongs to one continent):

```
Continent
{
    ContinentId*
    ContinentName
}
Country
{
    CountryId*
    CountryName
    ContinentId
    ContinentName
}
Customer
{
    CustomerId*
    CustomerName
    CustomerEmail
    CountryId
    CountryName
}
```

Suppose a listing is required to show the set of customers grouped by continent, and by country, as shown. The list must only include the continents and countries for which customers have been registered.

`[imagen omitida: wiki id 30979]`

Since now you have to group by continent, and within this group by country, you need three nested For each commands on the same base table (CUSTOMER table must be the base table because the list must only include the continents and countries that have customers associated with them). Keep in mind that the order clauses are fundamental to establish the break criteria. Since in this case, you need to group by ContinentName and then –for all the customers with this continent- to group by CountryName, the first For each must be ordered by ContinentName and the immediately nested For each by CountryName:

```
For each Customer order ContinentName
    print continent  {ContinentName}
    For each Customer order CountryName
        print country  {CountryName}
        For each Customer
            print customer {CustomerName, CustomerEmail}
        Endfor
    Endfor
Endfor
```

From the previous code, GeneXus will choose to scan the CUSTOMER table ordered by an index made up by the concatenation of the orders of each For each command with order clause (ContinentName, CountryName). Then, it will take the first record in the CUSTOMER table and retain the continent name in memory (because it is ContinentName the first break criterion). Then, it will print the continent name (first sentence written within the main For each). After that, “as long as the continent name remains unchanged, it will execute the nested For each and sequentially process all records with that continent name". So, it will retain the country name in memory (because it is CountryName the second break criterion). Next, it will print the country name (first sentence written within the second For each). After that, **“as long as the continent name remains unchanged and the country name remains unchanged too**", it will execute the last nested For each and it will sequentially process all records **with that continent name and that country name**". In the case of a record with a different country name, it will execute the immediately above external For each and all the sentences within it, including the last nested For each. In the case of a record with a different continent name, it will execute the main For each and proceed as explained until the table´s end is reached.

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [How to process grouped information](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/how-to-process-grouped-information-6104758)
