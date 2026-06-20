---
title: "XSLTApply method"
source_id: 12748
source_url: https://wiki.genexus.com/commwiki/wiki?12748
genexus_version: "18"
---

# XSLTApply method

Applies XSLT to XML in order to obtain a formatted file.

### [Syntax](#Syntax)

*file-name***.XSLTApply(***string-filepath* | *variable***)**

**Where:**  
  
*file-name*  
   Is the file that will be transformed into another file.

*string-filepath* | *variable*  
   Contains the path to *file-name*.

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)   
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), 
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),  [Java](https://wiki.genexus.com/commwiki/wiki?12258),
Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

The XSLTApply method receives the XSLT file path, and applies it to a string variable or XML file variable.

**Note**: In Windows Java, it only works with Sun VM.

### [Samples](#Samples)

```
&StringVar.XSLTApply(&XsltFileName)   
&StringResult = &FileVar.XSLTApply(&XsltFileName) 
```

```
&lvc.SetEmpty()
&FileSource.Source = "C:\Temp\cdcatalog.xml"
&StringResult = &FileSource.XSLTApply("C:\Temp\cdcatalog.xsl")
&lvc = &StringResult
```

### [See Also](#See+Also)

[XSLTApply function](https://wiki.genexus.com/commwiki/wiki?12749)


|  |
| --- |
| **Backlinks** |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |

---
