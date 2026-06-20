---
title: "Group Navigations that receive attributes as parameters"
source_id: 18243
source_url: https://wiki.genexus.com/commwiki/wiki?18243
genexus_version: "18"
---

# Group Navigations that receive attributes as parameters

## [Introduction](#Introduction)

When an object receives input attributes as a parameter (or input-output), filter conditions can be applied to some groups (For Each, Grids, etc) (See [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) for more details).

The above rule is not being considered in some situations and therefore some changes have been introduced in GeneXus X Evolution 2 to fix it. This document explains the error and its solution.

## [Previous behavior (until GeneXus X Evolution 1 inclusive)](#Previous+behavior+%28until+GeneXus+X+Evolution+1+inclusive%29)

Suppose we have the following Transactions and objects described below:

TRN Category  
{  
   CategoryId\*  
}

```
TRN Customer
{
   CustomerId*
   CategoryId
}

TRN Invoice
{
   InvoiceId*
   CustomerId
}

parm( CategoryId)

...
for each
   defined by CategoryId, InvoiceId, CustomerId
   ...
endfor
```

For that For Each clause, the *Invoice* table is considered as its Base Table and that navigation **does not** access the *Customer* table.

### [Where is the problem?](#Where+is+the+problem%3F)

The code generated for the WWSD patterns allowed us to identify the error more clearly.

Suppose we have the data structure mentioned above. When the pattern is applied to Category a Section for each related table is created, in this case, to view all Customers from a given CategoryId. The code of the Section has CategoryId as parm and the grid shows CustomerId. The generated code displays all Customers instead of the given CategoryId.

### [What is the technical reason for this behavior?](#What+is+the+technical+reason+for+this+behavior%3F)

CategoryId attribute is a parameter (in this case an in-out parameter) and is considered as instantiated (with a value). This is correct since, according to the general rule, a filter condition could be generated with it.

In addition, it is considered constant and it would therefore be unnecessary to navigate it. As a consequence, it is taken off the list of attributes to navigate. As a result:

* Customer table is not navigated (where CategoryId belongs to).
* No filter is applied by the parameter.
* All invoices are processed.

## [Current behavior (from GeneXus X Evolution 2 inclusive)](#Current+behavior+%28from+GeneXus+X+Evolution+2+inclusive%29)

The above problem is fixed in the new version, adding the following criteria:

* The base table of a group is determined as [usual](https://wiki.genexus.com/commwiki/wiki?6347), by considering all the attributes belonging to the group, regardless of whether they are mentioned or not in the parm rule.

Besides, these criteria are still applied for each parm attribute:

* If the attribute belongs to one of the tables determined by the group (note that this doesn’t mean all the extended tables), then the filter is applied.
* If it doesn't belong to any of the above tables, but there exists an explicit condition by the attribute, the condition is applied (see Example 2 in Appendix).

## [Compatibility](#Compatibility)

For Knowledge Bases converted from previous versions, it is important to perform a [Navigation Comparison](https://wiki.genexus.com/commwiki/wiki?3217,,) in order to detect any changes related to this fix.

In general, some of these situations could happen:

* The navigation changes some tables or conditions, because the parm attributes are also mentioned in Events outside For Each groups.   
  For instance, in the Start Event you have a Call to invoke a Procedure that passes some of these attributes as parameters. Now, the object navigation could change because those attributes are considered to infer the base and extended table.

In addition, the followings SACs have been fixed:

* [SAC  #6453](https://www.genexus.com/en/developers/websac?data=6453)   The base table is not well determined when the primery key is received as an attribute in the parm
* [SAC #18904](http://www2.gxtechnical.com/portal/hgxppredirect.aspx?15,26,0,,,18904)  Incorrect warning spc0037 by an att received as parameter
* [SAC #20460](http://www2.gxtechnical.com/portal/hgxppredirect.aspx?15,26,0,,,20460)  Filter is not applied by the parm attribute also mentioned in the group
* [SAC #22824](http://www2.gxtechnical.com/portal/hgxppredirect.aspx?15,26,0,,,22824)  Obj navigation includes a condition by an attribute mentioned within a call command inside the Start Event

## [Appendix](#Appendix)

### [Example 1](#Example+1)

```
TRN Category
{
   CategoryId*
}
TRN Customer
{
   CustomerId*
   CustmerName
   CategoryId
}
```

Suppose we want a Web Panel to list all the Customers that belong to a specific Category. The expected code is:

```
parm(CategoryId);
...
// Insert a Grid with the attributes: CustomerId and CustomerName
// Insert CategoryId as a hidden control in the form, to force the join navigation.
```

However, this navigation did not include the condition and only the Customer Table is accessed.

While this can be easily solved by changing the parm(ATT) with parm(& VAR) and adding the condition ATT = &Var; this behavior could lead to a confusion due to the general rule of how Base Tables and Extended Tables are inferred in a For Each, Grid, DP, etc.

### [Example 2](#Example+2)

```
TRN A
{
    A1*
    A2
}

Trn B
{
    B1*
    B2
}

Proc:

Parm(A1)
For each
  Where B1 = A1
Endfor
```

In this case, the expected behavior is to navigate the B Table with this condition: B1 = @A1   (this case did not change)
