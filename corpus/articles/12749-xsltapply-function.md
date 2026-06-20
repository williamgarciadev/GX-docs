---
title: "XSLTApply function"
source_id: 12749
source_url: https://wiki.genexus.com/commwiki/wiki?12749
genexus_version: "18"
---

# XSLTApply function

Applies XSLT to XML in order to obtain a formatted file.

### [Syntax](#Syntax)

**XSLTApply(***XMLFi**lepath* |***&**varXMLFile**,* *XSLTFilepath*|***&**varXSLTFile***)**

**Where:**  
*XMLFilepath*|***&**varXMLFile*  
   Is the path of the XML file.  
  
*XSLTFilepath*|***&****varXSLTFile*  
    Is the path of the XSLT file.

**Type returned:**  
Character

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258),
Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

The XSLTApply function receives an [XSLT file path](https://en.wikipedia.org/wiki/XSL), and applies it to an XML file.

### [Samples](#Samples)

```
&XmlFile = "C:\Temp\cdcatalog.xml"
&FormattedContent = XSLTApply(&XmlFile,"C:\Temp\cdcatalog.xsl")
```

**Note**: In Windows Java, it only works with the Sun VM.

### [See Also](#See+Also)

[XSL (Extensible Stylesheet Language)](https://en.wikipedia.org/wiki/XSL)


|  |
| --- |
| **Backlinks** |
| [XSLTApply method](https://wiki.genexus.com/commwiki/wiki?12748) |

---
