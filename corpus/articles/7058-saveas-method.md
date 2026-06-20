---
title: "SaveAs method"
source_id: 7058
source_url: https://wiki.genexus.com/commwiki/wiki?7058
genexus_version: "18"
---

# SaveAs method

Saves the document on a disk with a new name and, optionally, a new file type may be chosen.

### [Syntax](#Syntax)

**&***WordDocument***.SaveAs(***FileName* [ **,** *FileType* [ **,** *DOSText* [ **,** *LineBreaks* ] ] ] **)**  
  
**Where:**  
*FileName*  
     New name of the Word document.  
  
*FileType*  
     New file type to be generated from the Word document.  
  
Valid file types are:

|  |  |
| --- | --- |
| **DOC** | Word format |
| **RTF** | Rich Text Format |
| **HTM** | HyperText Markup/ HyperText Markup Language |
| **DOT** | DOC Template |

*TXT (Text)*  
     This parameter is optional. The default file type is DOC.  
  
*DOSText*  
     If TXT type is specified, it is possible to specify whether the format of the text to be used will be DOS (1) or not (0). This parameter is optional. The default value is 0.  
  
*LineBreaks*  
     If TXT type is specified, it indicates whether a line break will be added at the end of each line (1) or not (0). This parameter is optional. The default value is 0.

**Type Returned:**   
Numeric

### [Scope](#Scope)

**Extended data types:**[WordDocument Data Type](https://wiki.genexus.com/commwiki/wiki?2478,,)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258),
Ruby (up to GeneXus X Evolution 3),
Visual FoxPro (up to GeneXus X Evolution 3)

**Note**: This method returns an error code, so it is possible to call it as a function (**&**Err **= &**WordDocument**.SaveAs(…..)**).

### [See Also](#See+Also)

[Save Method for excel document and word document extended data types](https://wiki.genexus.com/commwiki/wiki?7057)  
[WordDocument Data Type](https://wiki.genexus.com/commwiki/wiki?2478,,)


|  |
| --- |
| **Backlinks** |
| [ExcelSpreadSheet data type](https://wiki.genexus.com/commwiki/wiki?46040) | [Save Method for excel document and word document extended data types](https://wiki.genexus.com/commwiki/wiki?7057) |

---
