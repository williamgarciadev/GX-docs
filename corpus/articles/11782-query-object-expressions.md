---
title: "Query object expressions"
source_id: 11782
source_url: https://wiki.genexus.com/commwiki/wiki?11782
genexus_version: "18"
---

# Query object expressions

When adding query elements to a [query definition](https://wiki.genexus.com/commwiki/wiki?9026), several options are available to  be assigned.

### [Arithmetic expressions](#Arithmetic+expressions)

Any valid arithmetic expression such as:

```
# Formula Expression
CustomerAge + CustomerIdentifierId – 1245
InvoiceSubtotal * 2
# Conditional Expression
iif(CitizenStatus = 1, "Waiting", Iif(CitizenStatus = 2, "OK", Iif(CitizenStatus = 3, "Error", Iif(CitizenStatus = 4, "Pending", "Other"))))
```

**arithmetic expression:**  
`[imagen omitida: wiki id 46224]`

### [Aggregate expressions](#Aggregate+expressions)

Any valid aggregatte expression such as:

```
Sum(CustomerId + CustomerId)
Sum(InvoiceTaxes+InvoiceNonTaxes)
Sum(CustomerId) + Sum(CustomerId)
Sum(InvoiceTotal)/Count(InvoiceId)
```

`[imagen omitida: wiki id 46209]`  
**by:**  
`[imagen omitida: wiki id 46212]`

**defined by:**  
`[imagen omitida: wiki id 46213]`

**weighted by:**  
`[imagen omitida: wiki id 46214]`

### [Filtering expressions](#Filtering+expressions)

A valid filtering expression:

```
Sum(InvoiceTotal) where Year(InvoiceDate) = 2008
Sum(InvoiceTotal) where Year(InvoiceDate) < 2008 / Sum(InvTot) where Year(InvoiceDate) > 2007
Sum(InvoiceTotal) where Year(InvoiceDate) in (2010,2020)
```

Check the [Filters](https://wiki.genexus.com/commwiki/wiki?12250) section for more detail.

### [For Each Clause](#For+Each+Clause)

Check the usage of the [For each clause](https://wiki.genexus.com/commwiki/wiki?33957).

### [Functions](#Functions)

The following list of available functions can be used:

* [AddMth](https://wiki.genexus.com/commwiki/wiki?8314)
* [AddYr](https://wiki.genexus.com/commwiki/wiki?12673)
* [EoM](https://wiki.genexus.com/commwiki/wiki?8392)
* [YMDHMStoT](https://wiki.genexus.com/commwiki/wiki?7626)
* [YMDtoD](https://wiki.genexus.com/commwiki/wiki?7627)
* [Lower](https://wiki.genexus.com/commwiki/wiki?8464)
* [LTrim](https://wiki.genexus.com/commwiki/wiki?8423)
* [PadL](https://wiki.genexus.com/commwiki/wiki?8475)
* [PadR](https://wiki.genexus.com/commwiki/wiki?8476)
* [RTrim](https://wiki.genexus.com/commwiki/wiki?8425)
* [Str](https://wiki.genexus.com/commwiki/wiki?7474)
* [StrReplace](https://wiki.genexus.com/commwiki/wiki?8505)
* [Substr](https://wiki.genexus.com/commwiki/wiki?8527)
* [Trim](https://wiki.genexus.com/commwiki/wiki?8424)
* [Upper](https://wiki.genexus.com/commwiki/wiki?8466)
* [Age](https://wiki.genexus.com/commwiki/wiki?8330)
* [Dow](https://wiki.genexus.com/commwiki/wiki?8344)
* [Hour](https://wiki.genexus.com/commwiki/wiki?8415)
* [Int](https://wiki.genexus.com/commwiki/wiki?8418)
* [Len](https://wiki.genexus.com/commwiki/wiki?8436)
* [Minute](https://wiki.genexus.com/commwiki/wiki?8416)
* [Month](https://wiki.genexus.com/commwiki/wiki?8379)
* [Second](https://wiki.genexus.com/commwiki/wiki?8417)
* [StrSearch](https://wiki.genexus.com/commwiki/wiki?8529)
* [StrSearchRev](https://wiki.genexus.com/commwiki/wiki?8507)
* [Year](https://wiki.genexus.com/commwiki/wiki?8380)
* [Round](https://wiki.genexus.com/commwiki/wiki?8486)
* [Trunc](https://wiki.genexus.com/commwiki/wiki?8488)
* [Val](https://wiki.genexus.com/commwiki/wiki?8528)
* [TAdd](https://wiki.genexus.com/commwiki/wiki?8512)
* [TDiff](https://wiki.genexus.com/commwiki/wiki?8513)
* [ServerNow](https://wiki.genexus.com/commwiki/wiki?8491)
* [ServerDate](https://wiki.genexus.com/commwiki/wiki?8490)
* [Asc](https://wiki.genexus.com/commwiki/wiki?13973)
* [Iif](https://wiki.genexus.com/commwiki/wiki?14280)
* [IsNull](https://wiki.genexus.com/commwiki/wiki?2357)
* [IsEmpty](https://wiki.genexus.com/commwiki/wiki?9645)
* [ToWKT](https://wiki.genexus.com/commwiki/wiki?32408)
* [FromWKT](https://wiki.genexus.com/commwiki/wiki?32408)
* [Distance](https://wiki.genexus.com/commwiki/wiki?32408)

### [Examples](#Examples)

```
# Simple
Month(InvDate)
Upper(CustomerName)
# Composed
Trim(Str(Year(InvoiceDate)))
```

### [Availability](#Availability)

This behavior is available since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,).


|  |
| --- |
| **Backlinks** |
|
| [Category:Query object](https://wiki.genexus.com/commwiki/wiki?9026) | [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |

---
