---
title: "ExcelDocument data type"
source_id: 2476
source_url: https://wiki.genexus.com/commwiki/wiki?2476
genexus_version: "18"
---

# ExcelDocument data type

Unifies interaction with the generation of Microsoft Excel documents for the different languages generated. It allows you to generate and handle Microsoft Excel worksheets. In addition, the [ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?6958) is implemented internally and is used to handle the group of cells contained in the worksheet.

An important advantage of this implementation is that the spreadsheets are handled with an object-oriented model, and it is not necessary to control Handles.

### [Properties](#Properties)

|  |  |
| --- | --- |
| [AutoFit property](https://wiki.genexus.com/commwiki/wiki?6983) | [MacroReturnNumber Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6949,,) |
| [Delimiter Property](https://wiki.genexus.com/commwiki/wiki?7028) | [MacroReturnText Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6946,,) |
| [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) | [Extended Data Types Read-Only property](https://wiki.genexus.com/commwiki/wiki?2565) |
| [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) | [Template property](https://wiki.genexus.com/commwiki/wiki?6991) |
| [ErrDisplay Property](https://wiki.genexus.com/commwiki/wiki?6929) | [UseAutomation Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7682,,) |
| [MacroReturnDate Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6948,,) |  |

### [Methods](#Methods)

|  |  |
| --- | --- |
| [Cells method](https://wiki.genexus.com/commwiki/wiki?6957) | [RenameSheet method](https://wiki.genexus.com/commwiki/wiki?7100) |
| [Clear method](https://wiki.genexus.com/commwiki/wiki?7084) | [RunMacro method](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6947,,) |
| [Close method](https://wiki.genexus.com/commwiki/wiki?7093) | [Save Method for excel document and word document extended data types](https://wiki.genexus.com/commwiki/wiki?7057) |
| [Hide method](https://wiki.genexus.com/commwiki/wiki?7066) | [SelectSheet method](https://wiki.genexus.com/commwiki/wiki?7087) |
| [Open method](https://wiki.genexus.com/commwiki/wiki?6992) | [Show method](https://wiki.genexus.com/commwiki/wiki?7065) |
| [Print method](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?5476,,) | [Unbind method](https://wiki.genexus.com/commwiki/wiki?7053) |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Samples](#Samples)

```
Event "Excel"
   &ExcelDocument.Open(&FileName)  

   If &ExcelDocument.ErrCode <> 0 
       msg(&ExcelDocument.ErrDescription) 
   Else 
       &ExcelDocument.Clear()  
    
       &ExcelDocument.Cells(1,1).Text = 'Customers list'  
       &ExcelDocument.Cells(1,1).Bold = 1 
       &ExcelDocument.Cells(1,1).Color = RGB(0, 0, 255) 
       &ExcelDocument.Cells(1,1).Size = 10 
        
       &ExcelDocument.Cells(3,1).Text = 'Customer Id' 
       &ExcelDocument.Cells(3,1).Italic = 1 
       &ExcelDocument.Cells(3,1).Bold = 1 
    
       &row = 4 
       &col = 1 
       For Each Line in Grid 
    
               &ExcelDocument.Cells(&row,&col).Number = CustomerId 
               &ExcelDocument.Cells(&row,&col).Color = RGB(0, 0, 255) 
               &row += 1    
              
       Endfor  
       &ExcelDocument.Save()  
   Endif
EndEvent
```

### [.NET and .NET Framework](#.NET+and+.NET+Framework)

There are two possible implementations:

* **EPPLUS:** GeneXus uses this implementation when .xlsx file extension is configured (which is advisable). Click [here](https://www.genexus.com/en/developers/websac?data=27868;;) for more information.
* **ExcelLite DLL:** GeneXus uses this implementation when the necessary file –GemBox.Spreadsheet.dll– is available after installing [GemBox's spreadsheet software](https://www.gemboxsoftware.com/spreadsheet).

**Note**: The only way to generate the proprietary .xls files is using ExcelLite.

### [Java](#Java)

Click [here](https://www.genexus.com/developers/websac?,,,31755;;) to know the files that you must have in the webapp directory for the generation of Excel spreadsheets with .xlsx extension to work correctly.

Please note that the Java Generator also supports Excel spreadsheets with .xls extension.

[Managing Excel documents common issues](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?14712,,)

## [See Also](#See+Also)

[ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?6958)  
[GeneXus Office Module](https://wiki.genexus.com/commwiki/wiki?45973)


|  |
| --- |
| **Backlinks** |
| [AutoFit property](https://wiki.genexus.com/commwiki/wiki?6983) | [Bold Property](https://wiki.genexus.com/commwiki/wiki?6986) | [Cells method](https://wiki.genexus.com/commwiki/wiki?6957) |
| [Clear method](https://wiki.genexus.com/commwiki/wiki?7084) | [Close method](https://wiki.genexus.com/commwiki/wiki?7093) | [Color Property](https://wiki.genexus.com/commwiki/wiki?7029) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) |
| [Date Property](https://wiki.genexus.com/commwiki/wiki?7036) | [Delimiter Property](https://wiki.genexus.com/commwiki/wiki?7028) | [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) | [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) |
| [ErrDisplay Property](https://wiki.genexus.com/commwiki/wiki?6929) | [Error Codes and Messages for ExcelDocument](https://wiki.genexus.com/commwiki/wiki?6939) | [ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?6958) | [Extended Data Type Font Property](https://wiki.genexus.com/commwiki/wiki?7002) |
| [Extended Data Type Size Property](https://wiki.genexus.com/commwiki/wiki?7004) | [Extended Data Type Type Property](https://wiki.genexus.com/commwiki/wiki?6987) | [Extended Data Types Read-Only property](https://wiki.genexus.com/commwiki/wiki?2565) |
| [GeneXus Office Module](https://wiki.genexus.com/commwiki/wiki?45973) | [GeneXus Office Module (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55218) | [Hide method](https://wiki.genexus.com/commwiki/wiki?7066) | [Italic Property](https://wiki.genexus.com/commwiki/wiki?6973) |
| [Number Property](https://wiki.genexus.com/commwiki/wiki?7010) |
| [Open method](https://wiki.genexus.com/commwiki/wiki?6992) | [OpenRequest method](https://wiki.genexus.com/commwiki/wiki?7692) | [OpenResponse method](https://wiki.genexus.com/commwiki/wiki?7694) |
| [RenameSheet method](https://wiki.genexus.com/commwiki/wiki?7100) | [Save Method for excel document and word document extended data types](https://wiki.genexus.com/commwiki/wiki?7057) |
| [SelectSheet method](https://wiki.genexus.com/commwiki/wiki?7087) | [SetAll method](https://wiki.genexus.com/commwiki/wiki?46100) | [Show method](https://wiki.genexus.com/commwiki/wiki?7065) | [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) |
| [Storage Provider property (GeneXus 18 Upgrade 10 or prior)](https://wiki.genexus.com/commwiki/wiki?59174) | [Storage Provider property (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57448) | [Template property](https://wiki.genexus.com/commwiki/wiki?6991) | [Text Property for Extended Data Types](https://wiki.genexus.com/commwiki/wiki?10197) |
| [Unbind method](https://wiki.genexus.com/commwiki/wiki?7053) | [Underline Property](https://wiki.genexus.com/commwiki/wiki?6956) | [Value property for ExcelCells data type](https://wiki.genexus.com/commwiki/wiki?22868) |
|

---
