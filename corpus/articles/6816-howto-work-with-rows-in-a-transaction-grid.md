---
title: "HowTo: Work with rows in a Transaction Grid"
source_id: 6816
source_url: https://wiki.genexus.com/commwiki/wiki?6816
genexus_version: "18"
---

# HowTo: Work with rows in a Transaction Grid

This article describes properties, methods, and ways to work with the rows of a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) in a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908).

### [Properties](#Properties)

The [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) is used to specify the number of empty lines that the Grid will contain by default in the Transaction.

`[imagen omitida: wiki id 54069]`

### [Methods](#Methods)

When a Transaction contains a Grid, it also contains the "+ NEW ROW" option.

`[imagen omitida: wiki id 54074]`

By pressing "+ NEW ROW," a new empty line will be added to the grid:

`[imagen omitida: wiki id 54073]`

In addition, the [AddLines method](https://wiki.genexus.com/commwiki/wiki?10123) is available to be applied to Grid controls. When it is used, the "+ NEW ROW" option will not appear.

For instance, suppose you have the following code for the Grid of a Customer Transaction:

```
Event 'Add Phone'  //Event associated with a button control added in the Layout 
    GridPhones.AddLines(1)
Endevent
```

In this case, the "+ NEW ROW" option won't be available for the grid, and each time the end user presses the "Add Phone" button a new line will be added to the Grid.

### [Deletion of lines](#Deletion+of+lines)

To delete a Grid line at runtime, the end user has to click on the row's minus symbol, and the row will be automatically deleted:

`[imagen omitida: wiki id 54071]`

### Automatic mode inference

For each line, the mode (Insert, Update, Delete, Display) is automatically inferred.

### No Orders and conditions properties in Transaction Grids

Transaction Grids allow interaction with all the records of a [Base Table](https://wiki.genexus.com/commwiki/wiki?6347). If conditions were enabled in Transaction Grids, it would not be possible to know if a record was hidden by a condition.

### Considerations

When using Grids in a Transaction, at least one editable Grid control is necessary.

### [See Also](#See+Also)

[Web Form Refresh](https://wiki.genexus.com/commwiki/wiki?6566)


|  |
| --- |
| **Backlinks** |
| [AddLines method](https://wiki.genexus.com/commwiki/wiki?10123) | [HowTo: Configure the New Row style in grids](https://wiki.genexus.com/commwiki/wiki?30610) | [Sortable property](https://wiki.genexus.com/commwiki/wiki?14173) |

---
