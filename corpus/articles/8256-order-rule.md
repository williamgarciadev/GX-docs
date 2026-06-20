---
title: "Order rule"
source_id: 8256
source_url: https://wiki.genexus.com/commwiki/wiki?8256
genexus_version: "18"
---

# Order rule

In the case of Panels, it establishes the order for the implicit navigation associated with the fixed part.  
In the case of Web Panels, it establishes the order for the implicit navigation associated with the fixed part when the object has no Grids. If the Web Panel contains at most one Grid, the Order rule establishes the order for the implicit navigation associated with the Grid.   
If there is more than one Grid (either in a Panel or a Web Panel), use each Grid's Order property.

### [Syntax](#Syntax)

**Order(**<*Att1*>,<*Att2*>,....<*Attn*>**);**

### [Scope](#Scope)

**Objects:** [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work With](https://wiki.genexus.com/commwiki/wiki?15974), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)  
**Generators:** [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

The Order rule applies to implicit navigations; that is to say, in those cases where you do not write a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) and GeneXus determines a navigation. Since you do not write a For each command with its corresponding [Order clause](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6075,,), you can indicate the desired order to navigate and retrieve the scanned records using the **Order rule**.

#### [**Using the Order rule in a Panel**](#Using+the+Order+rule+in+a+Panel)

For [Panels](https://wiki.genexus.com/commwiki/wiki?24829), the Order rule only applies to the fixed part, not to the Grids within the Panel. This is because the fixed part has its own [Base Table](https://wiki.genexus.com/commwiki/wiki?6347), which is separate from the Base Tables of the Grids.

#### [**Using the Order rule in a Web Panel without Grids**](#Using+the+Order+rule+in+a+Web+Panel+without+Grids)

In this case, consider that only one record is displayed. The Order rule can be useful, for example, if you need to display the first or last record of a set based on a specific order.

#### [**Using the Order rule in a Web Panel with one Grid**](#Using+the+Order+rule+in+a+Web+Panel+with+one+Grid)

When the Order rule is defined in a Web Panel with one Grid it applies to the Grid navigation. You can also achieve the same result by setting the Grid's [Order property](https://wiki.genexus.com/commwiki/wiki?9842).

If there is more than one Grid, use each Grid's [Order property](https://wiki.genexus.com/commwiki/wiki?9842).

#### [**General behavior for all cases**](#General+behavior+for+all+cases)

If you don't specify an order using this rule nor the [Order property](https://wiki.genexus.com/commwiki/wiki?9842) for a Grid, GeneXus will use the base table's primary key to order the records. This is the same behavior as in a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744).

To indicate a descending order for an attribute, enclose its name in brackets ( ).

When defining compound orders, you can include some attributes in ascending order and other attributes in descending order within the same Order rule.

### [Samples](#Samples)

**Sample 1**

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) called “Customer”:

```
Customer
{
    CustomerId*
    CustomerName
    CustomerAddress
    CustomerPhone
}
```

Suppose you define a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) with a Grid containing the Customer attributes.

`[imagen omitida: wiki id 59370]`

The Grid's base table is Customer; by default, the Customer records will be retrieved and sorted by their CustomerId.

If you need to display the customers sorted by name in ascending order, you can define a rule in the Rules tab of the Web Panel as follows:

```
Order(CustomerName);
```

At runtime, the Web Panel will look as shown below:

`[imagen omitida: wiki id 59371]`

**Note**: The same behavior can be obtained by setting the Grid's [Order property](https://wiki.genexus.com/commwiki/wiki?9842) to CustomerName.

**Sample 2**

Given the following Transaction objects:

```
Supplier
{
    SupplierId*
    SupplierName
}
```

```
Invoice
{
    InvoiceId*
    InvoiceDate
    SupplierId
    SupplierName
    ......
}
```

Suppose you need to define a Web Panel that displays the invoice records in the Grid sorted by an order consisting of InvoiceDate in descending order and SupplierName in ascending order. In that case, you can define a rule in the Rules tab of the Web Panel as follows:

```
Order((InvoiceDate), SupplierName);
```

**Note**: The same behavior can be obtained by setting the Grid's [Order property](https://wiki.genexus.com/commwiki/wiki?9842) to (InvoiceDate), SupplierName.

### [See Also](#See+Also)

[Order clause](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6075,,)  
[Order property](https://wiki.genexus.com/commwiki/wiki?9842)


|  |
| --- |
| **Backlinks** |
| [Rules in Web Panels](https://wiki.genexus.com/commwiki/wiki?8288) |
| [Sortable property](https://wiki.genexus.com/commwiki/wiki?14173) | [SRC Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?38589) |

---
