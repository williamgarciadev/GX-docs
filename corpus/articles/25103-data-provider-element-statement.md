---
title: "Data Provider Element statement"
source_id: 25103
source_url: https://wiki.genexus.com/commwiki/wiki?25103
genexus_version: "18"
---

# Data Provider Element statement

A [Data Provider Element](https://wiki.genexus.com/commwiki/wiki?25096) It is one of the three main components of the [Data Provider output-based declarative language](https://wiki.genexus.com/commwiki/wiki?5309).

An Element is an atomic value in the Output which may also be of a SDT data type.

Each Element must be **assigned** inside a [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082), and the syntax used is that of [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441).

## [Syntax](#Syntax)

```
<elementName>[=<formula>]'['<elementProperties>']'
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*elementName*  
         Is the name of the element in the output SDT or BC. If it matches the attribute name that is assigned to the right  (e.g. "CustomerName = CustomerName"), the assignment could be omitted, making it more compact. But beware: the elements on the left are not attributes (but "elements"), unlike those on the right. The data type of *<elementName>* must match with *<formula>* resulting data type. It can be an SDT as well.

*formula*  
         Is a conditional [formula](https://wiki.genexus.com/commwiki/wiki?5861) ([horizontal](https://wiki.genexus.com/commwiki/wiki?5864) as well as [aggregate](https://wiki.genexus.com/commwiki/wiki?5868) or [compound](https://wiki.genexus.com/commwiki/wiki?5879)). That is, it could be several conditional expressions. This includes either an isolate attribute, or an invocation to a procedure with output or a Data Provider, a constant, as well as the typical formulas. 

*elementProperties*  
         It can take one of the following values: *Default,* *XmlInfo.*  
         XmlInfo is defined as follows*:***'[' XmlType =**  attribute | cdata | element | value **']'**

### [Samples](#Samples)

```
Customers
{
    Customer
    {
         Code = CustomerId
         CustomerName
         Address = GetAddress(CustomerAddress, CityName)
         Age = &Today.Year() - CustomerBirthDate.Year()
         Discount = 100 if CustomerStatus = Status.Gold; 0 otherwise;
         Amount = Sum( InvoiceTotal )
    }
}
```

Here you have four element assignments inside the Customer group.

1. The element Code is assign with the value of CustomerId attribute.
2. The element CustomerName is assign with the value of the attribute with the same name.
3. Address, an element of a SDT data type is assign with the result of executing the GetAddress Data Provider (that returns such a SDT loaded)
4. The element Age is assign with the result of evaluating the horizontal formula
5. The element Discount is assign with the result of evaluating the conditional horizontal formula
6. The element Amount is assign with the result of calculating the aggregate formula

####


|  |
| --- |
| **Backlinks** |
| [Data Provider Element](https://wiki.genexus.com/commwiki/wiki?25096) | [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [Toc:Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309) |
| [Data Provider Subgroup statement](https://wiki.genexus.com/commwiki/wiki?25412) | [Inline Formulas outside a contextual table](https://wiki.genexus.com/commwiki/wiki?6442) |

---
