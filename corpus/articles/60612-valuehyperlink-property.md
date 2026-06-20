---
title: "ValueHyperlink property"
source_id: 60612
source_url: https://wiki.genexus.com/commwiki/wiki?60612
genexus_version: "18"
---

# ValueHyperlink property

Sets or gets the hyperlink of a cell or cell range of the [ExcelCellRange data type](https://wiki.genexus.com/commwiki/wiki?46081) in an Excel spreadsheet.

### [Syntax](#Syntax)

#### [**Set**](#Set)

&CellRange**.ValueHyperlink** = <URL|File\_path>

#### [**Get**](#Get)

&Url = &CellRange.**ValueHyperlink**

### [Description](#Description)

Use this property when you want a cell to function as a clickable link to a URL. If you also need to control the visible text, set the [ValueText Property](https://wiki.genexus.com/commwiki/wiki?46302) first, then assign **ValueHyperlink**.

### [Scope](#Scope)

**Extended Data Types:** [ExcelCellRange data type](https://wiki.genexus.com/commwiki/wiki?46081)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Samples](#Samples)

Below is an example of how to get the hyperlink:

```
Event 'Excel'
    &ExcelDocument.Open(&FileName)

    If &ExcelDocument.ErrCode <> 0
        msg(&ExcelDocument.ErrDescription)
    Else
        &row = 2
        &col = 2

       &excelcellrange = &ExcelDocument.Cell(&row, &col)        // Get the single cell at row &row, column &col

       If not &excelcellrange.ValueHyperlink.IsEmpty()          // Check if the cell has a hyperlink
            &filename = &excelcellrange.ValueHyperlink          // Read the hyperlink target (could be http/https or a file:/// URL to a local file)
            &filename = URLDecode(&filename)                    // Decode percent-encoded characters (%20 for spaces, accents, etc.) for a readable path/URL
       Else
            &filename = ""                                      // no hyperlink in this cell
       EndIf
            
  EndIf
EndEvent
```

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59631,,).


|  |
| --- |
| **Backlinks** |
| [ExcelCellRange data type](https://wiki.genexus.com/commwiki/wiki?46081) |

---
