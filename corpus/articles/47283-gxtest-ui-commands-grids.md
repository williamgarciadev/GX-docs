---
title: "GXtest UI Commands - Grids"
source_id: 47283
source_url: https://wiki.genexus.com/commwiki/wiki?47283
genexus_version: "18"
---

# GXtest UI Commands - Grids

Here you can find specific GXtest commands for grids

## [GetRowsCount](#GetRowsCount)

`[imagen omitida: wiki id 47284]`

Gets the number of rows of a table or grid

**Parameters**

* TableName: table or grid control name as defined in the KB

**Returns**: the number of rows of the table

Examples

```
&driver.Verify(&driver.GetRowsCount("GridControlName")  = 3)
```

Note: for tables of type *Canvas* this command returns the number of cells instead of rows.

### [Availability](#Availability)

This command  is available since GeneXus 17 upgrade 1.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
