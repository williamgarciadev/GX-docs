---
title: "HowTo: Group grid columns with a title with Fiori Pattern"
source_id: 55010
source_url: https://wiki.genexus.com/commwiki/wiki?55010
genexus_version: "18"
---

# HowTo: Group grid columns with a title with Fiori Pattern

When applying the [Fiori for Web Pattern](https://wiki.genexus.com/commwiki/wiki?34251) using the [Fiori Horizon Design System](https://wiki.genexus.com/commwiki/wiki?54721), it is possible to select a set of attributes and/or variables (adjacent in a Grid) to group them and show a title that describes or categorizes those columns. The same can be done with several groups.

To achieve this, set the Title Header property with the desired title. This will show the title of the header above the titles of the fields belonging to the group.

### [Sample](#Sample)

Consider a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) called Customer defined as follows:

```
{
    CustomerId*
    CustomerName
    CustomerLastName
    CustomerAddress
    CustomerPhone
    CustomerEmail
}
```

Follow all the steps in [Apply the Fiori for Web pattern for the first time](https://wiki.genexus.com/commwiki/wiki?38862).

After selecting Initialize Fiori Horizon, the checkbox "Apply this pattern on save", and the List Report floorplan, you will see the "List Report" tab (that corresponds to a Web Panel object):

`[imagen omitida: wiki id 55012]`

Under the Grid node, select CustomerId, CustomerName, and CustomerLastName. Go to the Properties window and find the Title Header property. Complete this property with the title you want to show above the grouped attributes. In this case, the title entered is "Customer Information"”:

`[imagen omitida: wiki id 55013]`

Save the changes (Ctrl + S).

Next, select the CustomerAddress, CustomerPhone, and CustomerEmail attributes and complete the Title Header property with "Customer Additional information":

`[imagen omitida: wiki id 55014]`

Save the changes and run (F5).

The result will look as follows:

`[imagen omitida: wiki id 55015]`

### [Availability](#Availability)

Since GeneXus 18 Upgrade 4 (GeneXus for SAP Systems - Fiori Horizon Pack).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) |

---
