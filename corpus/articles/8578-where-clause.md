---
title: "Where clause"
source_id: 8578
source_url: https://wiki.genexus.com/commwiki/wiki?8578
genexus_version: "18"
---

# Where clause

Indicates a list of conditions that must be matched by the data in order to be processed within the level —[For each command](https://wiki.genexus.com/commwiki/wiki?24744) or [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082)—. The conditions are boolean expressions, simples or very complex nested ones.

It is possible to specify more than one Where clause. In this case, the conditions are evaluated as if they were separated by an **'and'** operator.  

### [Syntax](#Syntax)

|  |  |
| --- | --- |
| {**where** | {*<condition>* [**when** *<constraint>*]}  | |
|  | { [**not**]*<attribute>* **in** *<DataSelectorName>*( [*<parameterList>*]) }}... |

Where:

*<condition>*

specifies any valid logical expression to condition the data retrieval. It can be a compound condition, using 'and', 'or' and 'not' logical operators.

Those attributes appearing in the boolean condition may be either from the for each [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) or from its [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029). In some cases, attributes that do not belong to the extended table can be included. See [Filters As Hint](https://wiki.genexus.com/commwiki/wiki?2015) for more details.

The occurrence of n where clauses is equivalent to the occurrence of only one where clause, with the boolean conjunction of the conditions.

|  |  |
| --- | --- |
| *<condition>* ::= | [**not**] *<condition>* [ {**or** | **and**} *<condition>*] |
|  | [**(**] *<condition>* [**)**] |
|  | *<relationalExpr>* |
|  | *<stringExpr>***like***<stringExpr>* |
|  | *<booleanFunctionExpr>* |

|  |  |
| --- | --- |
| *<relationalExpr>* ::= | *<expr>*[ {**>** | **>=** | **=** | **<** | **<=**} *<expr>*] |
|  | *<expr>* is an expression. If used for comparison, its datatype has to allow comparison (i.e. numeric, character, etc.). It can also be an aggregate formula (inline) (i. e: count, sum, min, max, average). | |

|  |  |
| --- | --- |
| *<booleanFunctionExpr>* ::= | **True** | **False** | *<bool\_attribute>* | *<bool\_variable>* | *<bool\_function>***(** *<expr>* **)**| *<bool\_proc>*}**(** [*<parametersList>*] **)** |
|  | *<bool\_attribute>*, *<bool\_variable>* are attribute/variable of a Boolean datatype, respectively.  *<bool\_fuction>* is a function returning a boolean result (True or False). <expr> is an expresion of the datatype required by *<bool\_function>*.  *<bool\_proc>* is a user-defined Procedure that returns a boolean value. |

*<constraint>*

is a *<condition>* that specifies when the where clause will apply. In client/server platforms, the [When clause](https://wiki.genexus.com/commwiki/wiki?8629) of each where clause is first evaluated, and if its condition is met, the filter specified by the where clause will be applied. See more about [When clause](https://wiki.genexus.com/commwiki/wiki?8629).

[**not**]*<attribute>* **in** *<DataSelectorName>*( [*<parameterList>*])

The [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) determines a query itself. This means that a SELECT sentence will be generated for the Data selector definition, which will be a different and independent SELECT from the level one—[For each command](https://wiki.genexus.com/commwiki/wiki?24744) or [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082)—. Thus, it will return a collection of values corresponding to the same definition as the *<attribute>*. This <attribute> must belong to the extended table of the Data Selector base table. See more: [Data Selectors in For each command](https://wiki.genexus.com/commwiki/wiki?5312).

### [Conditions as properties](#Conditions+as+properties)

The same concept but with a slightly different syntax (for example, without the 'where' keyword) applies to [Data Selectors](https://wiki.genexus.com/commwiki/wiki?5271), as well as 'Conditions' section of [Web panels](https://wiki.genexus.com/commwiki/wiki?6916), [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) and [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974), as well as grid 'Conditions' property.

### [Optimization](#Optimization)

*<Condition>* in the where clause constraints the dataset that is obtained. However, more than that is meant here. There is a great difference between a full scan table access and an index-optimized random access. If applying some rules of logic, GeneXus determines that the order clause (or the primary key order) is compatible with the where condition(s), it optimizes the access to the table using indices and not doing a full table scan. This is obviously the desired behavior whenever possible.

The conditions that can be optimized are the ones that use the operators: '>', '>=', '=', '<' and '<='.

If the Where condition is optimized, it will appear as "Navigation Filter" in the Navigation report. Otherwise, it will appear as "Constraint".

Be sure that the conditions used in the where clause respect type definitions. If this is not the case, an error message indicating a type mismatch will be displayed.

See more about [Conditional Orders and Filters](https://wiki.genexus.com/commwiki/wiki?12566).

### [Examples](#Examples)

1. Suppose you need to print the customer names for those customers who were born in a certain country and after a certain date.

```
For each Customer
Where CountryId = &CountryId
Where CustomerBirthDate.year() >= &youngDate
    print youngCustomer //printblock with: CustomerName
EndFor
```

Note the code is valid only as of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?20247,,) because you have included the [Base Transaction clause](https://wiki.genexus.com/commwiki/wiki?25418) in order to specify the base table. Remember this is not mandatory, and you could not include it. In such a case, the code will be valid for previous GeneXus versions.

CountryId, CustomerBirthDate, and CustomerName belongs to CUSTOMER extended table. Note you have not specified an [order](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6075,,). This will affect the performance as you can see in [Conditional Orders and Filters](https://wiki.genexus.com/commwiki/wiki?12566).

2. Now suppose &CountryId is set by the end-user, by means of a web panel, for instance. As the user can let the variable empty, you need the filter will not be applied in that case:

```
for each Customer
where CountryId = &CountryId when not &CountryId.lsEmpty()
where CustomerBirthDate.year() >= &youngDate
    print youngCustomer // printblock with: CustomerName
endfor
```

3. If you need in several objects to filter the young customers of a certain country, probably you would have created a Data selector in order to define that query:

`[imagen omitida: wiki id 25525]`

Thus, the previous for each would be:

```
for each Customer
where CustomerId in YoungCustomer( &CountryId, &youngDate )
   print youngCustomer // printblock with: CustomerName
endfor
```

4. Finally, you need to print the countries for which you have more than one hundred customers:

```
for each Country
where Count( CustomerName ) > 100
   print countryInfo //printblock with: CountryName
endfor
```

Note the For each base table is now COUNTRY.

### [Scope](#Scope)

**Commands:** [For each command](https://wiki.genexus.com/commwiki/wiki?24744), [Xfor each command](https://wiki.genexus.com/commwiki/wiki?8596), [Xfor First command](https://wiki.genexus.com/commwiki/wiki?8601), [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082)

### [See Also](#See+Also)

[Conditional Orders and Filters](https://wiki.genexus.com/commwiki/wiki?12566)


|  |
| --- |
| **Backlinks** |
| [For each command](https://wiki.genexus.com/commwiki/wiki?24744) | [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
| [Inline Formulas within a contextual table](https://wiki.genexus.com/commwiki/wiki?6426) | [Order Clause Specification](https://wiki.genexus.com/commwiki/wiki?5100) | [When clause](https://wiki.genexus.com/commwiki/wiki?8629) |
| [Xfor each command](https://wiki.genexus.com/commwiki/wiki?8596) | [Xfor First command](https://wiki.genexus.com/commwiki/wiki?8601) |

---
