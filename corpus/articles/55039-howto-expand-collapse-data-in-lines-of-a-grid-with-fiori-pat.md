---
title: "HowTo: Expand/collapse data in lines of a Grid with Fiori Pattern"
source_id: 55039
source_url: https://wiki.genexus.com/commwiki/wiki?55039
genexus_version: "18"
---

# HowTo: Expand/collapse data in lines of a Grid with Fiori Pattern

When applying the [Fiori for Web Pattern](https://wiki.genexus.com/commwiki/wiki?34251) using the [Fiori Horizon Design System](https://wiki.genexus.com/commwiki/wiki?54721), Grids allow expanding or collapsing each line to show more or fewer data.

### [Sample](#Sample)

Consider a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) called Customer that is defined as follows:

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

After selecting Initialize Fiori Horizon, the checkbox "Apply this pattern on save" and the List Report floorplan, you will see the "List Report" tab (that corresponds to a Web Panel object):

`[imagen omitida: wiki id 55012]`

First, select the CustomerAddress, CustomerPhone, and CustomerEmail attributes and set their Visible property to False (because the idea isn't to show these attributes in the Grid lines but when expanding a line).

Next, right-click on the Grid node, and in the contextual menu select **Add > Standard Action**. From the new Standard Action, select the **ExpandGridLine** event for the **Name property**.

For the **GXObject property**, enter the name of a [Web Component object](https://wiki.genexus.com/commwiki/wiki?1864) (that you must have previously defined) which will display the data you want to show when pressing the selector to expand a line.

`[imagen omitida: wiki id 55079]`

Finally, add the parameter to be sent to the Web Component. To do so, right-click on the **Standard Action(ExpandGridLine)** node and select **Add > Parameters**. Then, right-click on the **Parameters** node and select **Add > Parameter**. Complete the **Name property**with the parameter to be sent (CustomerId).

`[imagen omitida: wiki id 55080]`

### [Web Component definition guides](#Web+Component+definition+guides)

After creating the [Web Component object](https://wiki.genexus.com/commwiki/wiki?1864), go to its **Patterns** tab and select the **Fiori for Web** tab.

Select the "Apply this pattern on save" checkbox and save.

Click on the "Select floorplan…" link.

Select the **List For Grid Expanded Line** option under the **List floorplans** node.

![](https://lh3.googleusercontent.com/KQV9oe895IuPjm-j9lb9cfbMl1EJ1Pgq8P_pqfQ2lIbRjSef9_zBpI-1fuaT4nlI3WxnoSlzsVdEUypRhG0QB6FuubhMu-xo0ZAQmvyvMLmFGhuqY8kMBjSmGuf9-w0fTOQRfxwuXdhCVGVpj6yjKeU)

The following options are displayed:

`[imagen omitida: wiki id 55081]`

Leave the option selected ("Based on a Transaction").

Select the Customer Transaction.

`[imagen omitida: wiki id 55082]`

Select the CustomerId, CustomerName, and CustomerLastName attributes and set their Visible property to False (because the idea is not to show them when expanding a line).

Note that a grid was automatically added when the floorplan based on a Transaction was applied. The objective is to display additional information **about only one customer**, so a filter is needed. Remember that this Web Component is called from a Grid Line with the CustomerId parameter. Therefore, in the Web Component Rules section you have to define the following:

```
Parm(CustomerId);
```

In this way, the filter is solved.

### [Runtime screenshot](#Runtime+screenshot)

### 

### [Availability](#Availability)

Since GeneXus 18 Upgrade 4 (GeneXus for SAP Systems - Fiori Horizon Pack).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) |

---
