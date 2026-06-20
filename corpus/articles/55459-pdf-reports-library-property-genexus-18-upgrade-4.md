---
title: "PDF Reports Library property (GeneXus 18 Upgrade 4)"
source_id: 55459
source_url: https://wiki.genexus.com/commwiki/wiki?55459
genexus_version: "18"
---

# PDF Reports Library property (GeneXus 18 Upgrade 4)

Sets the library to use for generating web reports in PDF format.

### [Values](#Values)

|  |  |
| --- | --- |
| **iText (Legacy)** | Default value. Uses iText 2 to generate PDF and provides HTML print management in PDF reports. |
| **iText 8** | Uses iText 8 Core for general handling of PDF generation and pdfHTML for handling HTML printing in PDF reports. |
| **PDFBox** | Uses the free and open source PDFBox library to generate PDF reports. |

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

This property allows you to choose between different library options to suit the specific needs of your application.

By selecting the iText (Legacy) value, you choose the library that has also been referenced by programs generated with versions prior to GeneXus 18 Upgrade 4.

It is important to note the different licensing schemes of iText 8. For more information, see [iText License Model](https://itextpdf.com/how-buy).

When choosing a particular library, do not expect the reports generated to be identical in all visual details. Each library has its own ways of handling certain features, such as bold or italicized text. For example, iText provides methods to bold or italicize any text, while PDFBox does not provide those features and suggests the use of a specific font file (ttf) to accomplish this.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute [Build any object](https://wiki.genexus.com/commwiki/wiki?17719) with the purpose of generating the \*.config files.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).

### [See Also](#See+Also)

[PDF Reports](https://wiki.genexus.com/commwiki/wiki?13531)  
[External utilities used by GeneXus generated web applications](https://wiki.genexus.com/commwiki/wiki?15671)
