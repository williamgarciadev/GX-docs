---
title: "GeneXus Office Module"
source_id: 45973
source_url: https://wiki.genexus.com/commwiki/wiki?45973
genexus_version: "18"
---

# GeneXus Office Module

It implements a module for the creation and management of excel spreadsheets.

It includes the following objects:

|  |  |  |
| --- | --- | --- |
| [ExcelSpreadSheet data type](https://wiki.genexus.com/commwiki/wiki?46040) | module GeneXusOffice.Office.Excel | Manages the excel spreadsheet. |
| [ExcelWorksheet data type](https://wiki.genexus.com/commwiki/wiki?46080) | module GeneXusOffice.Office.Excel | Manages a specific worksheet in the spreadsheet. |
| [ExcelCellRange data type](https://wiki.genexus.com/commwiki/wiki?46081) | module GeneXusOffice.Office.Excel.Cell | Manages a cell or a group of cells in the spreadsheet. |
| [ExcelAlignment data type](https://wiki.genexus.com/commwiki/wiki?46082) | module GeneXusOffice.Office.Excel.Style | Sets the vertical and horizontal alignment of a cell. |
| [ExcelBorderStyle data type](https://wiki.genexus.com/commwiki/wiki?46308) | module GeneXusOffice.Office.Excel.Style | Sets the color and type of the border of a cell. |
| [ExcelCellBorder data type](https://wiki.genexus.com/commwiki/wiki?46084) | module GeneXusOffice.Office.Excel.Style | Sets the different borders of a cell (up, down, left, right and diagonal). |
| [ExcelCellStyle data type](https://wiki.genexus.com/commwiki/wiki?46315) | module GeneXusOffice.Office.Excel.Style | Sets the style of a cell. |
| [ExcelColor data type](https://wiki.genexus.com/commwiki/wiki?46086) | module GeneXusOffice.Office.Excel.Style | Sets the color of a cell. |
| [ExcelFill data type](https://wiki.genexus.com/commwiki/wiki?46316) | module GeneXusOffice.Office.Excel.Style | Sets the style of the background of a cell. |
| [ExcelFont Data Type](https://wiki.genexus.com/commwiki/wiki?46318) | module GeneXusOffice.Office.Excel.Style | Sets the font of a cell. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Sample](#Sample)

```
event "Excel"

    //opens an excel sheet
    &excelSpreadsheet.Open("C:\testExcel\test.xlsx")

    //select a cell
    &excelcellrange = &excelSpreadsheet.Cell(1,2)

    //sets a value in the cell
    &excelcellrange.ValueText = "hidden"
    

    //sets the style of a cell
    &excelCellStyle = new()
    &excelCellStyle.Hidden = true
    &excelCellStyle.Indent = 5
    &excelCellStyle.Alignment.Horizontal = CellHorizontalAlignment.Left
    //sets the border in the style (diagonal down and bottom borders)
    &ExcelCellStyle.Border.DiagonalDown.Type = CellBorderType.DOUBLE
    &ExcelCellStyle.Border.DiagonalDown.Color.SetColorRGB(200,20,50)
    &ExcelCellStyle.Border.Bottom.Type = CellBorderType.DOUBLE
    &ExcelCellStyle.Border.bottom.Color.SetColorRGB(200,20,50)
    

    //sets the new style in the cell 
    &excelcellrange.SetCellStyle(&excelCellStyle)

    //saves the changes in the sheet and close
    &boolean =&excelSpreadsheet.Save()
    if &boolean
        &excelSpreadsheet.Close()
    else
        msg("Error code:"+&excelSpreadsheet.ErrCode.ToString())    
        msg("Error description:"+&excelSpreadsheet.ErrDescription.ToString())    
    endif

endevent
```

## [This module compared to Excel document data type](#This+module+compared+to+Excel+document+data+type)

This module has more features to customize spreadsheets and workbooks than the [ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?2476). But, on the other side, it does not support (by the design of the implementation on which it lies, called [POI XSSF](https://poi.apache.org/components/spreadsheet/) in Java) creating spreadsheets with thousands of rows and hundreds of columns.  
You may use one or another depending on your needs.

## [Availability](#Availability)

This feature is available in the .NET Generator since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239)


|  |
| --- |
| **Backlinks** |
| [ExcelAlignment data type](https://wiki.genexus.com/commwiki/wiki?46082) | [ExcelCellBorder data type](https://wiki.genexus.com/commwiki/wiki?46084) | [ExcelCellRange data type](https://wiki.genexus.com/commwiki/wiki?46081) |
| [ExcelColor data type](https://wiki.genexus.com/commwiki/wiki?46086) | [ExcelDocument data type](https://wiki.genexus.com/commwiki/wiki?2476) | [ExcelSpreadSheet data type](https://wiki.genexus.com/commwiki/wiki?46040) | [ExcelWorksheet data type](https://wiki.genexus.com/commwiki/wiki?46080) |
| [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239) | [GeneXus Office Module (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55218) |

---
