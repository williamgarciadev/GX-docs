---
title: "One clause in Data Provider Group statement"
source_id: 25411
source_url: https://wiki.genexus.com/commwiki/wiki?25411
genexus_version: "18"
---

# One clause in Data Provider Group statement

Enables returning only the first record from a navigation of many.

## [Syntax](#Syntax)

```
'['One']'
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

### [Samples](#Samples)

Suppose the SDT used as Output of the Data Provider is not a collection because you need only the first Customer of all possibles. If the Data Provider is written as follows, the result was the last Customer (because the Data Provider will read all the table and would modify the SDT to return with each Customer).

```
OneCustomer
{
   CustomerId
   CustomerName
}
```

**Data**

|  |  |
| --- | --- |
| **CustomerId** | **CustomerName** |
| 1 | Customer one |
| 2 | Customer two |
| 3 | Customer three |

The result would be:

```
<OneCustomer>
   <CustomerId>3</CustomerId>
   <CustomerName>Customer three</CustomerName>
</OneCustomer>
```

The generated select is as follows, which does not have good performance, because to obtain only one record it reads all the Table.

```
SELECT [CustomerName], [CustomerId] FROM [Customer] WITH (NOLOCK) ORDER BY [CustomerId]
```

In order to improve this case the clause [one] was implemented, if you now write:

```
OneCustomer [one]
{
   CustomerId
   CustomerName
}
```

The result would be:

```
<OneCustomer>
   <CustomerId>1</CustomerId>
   <CustomerName>Customer one</CustomerName>
</OneCustomer>
```

The performance is improved because the generated select in that case is:

```
SELECT TOP 1 [CustomerName], [CustomerId] FROM [Customer] WITH (NOLOCK) ORDER BY [CustomerId]
```

Note that in the Data Provider navigation:

`[imagen omitida: wiki id 15173]`

####


|  |
| --- |
| **Backlinks** |
| [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [Toc:Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309) |

---
