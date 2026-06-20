---
title: "PDF Reports Library property (GeneXus 18 Upgrade 8 or prior)"
source_id: 57550
source_url: https://wiki.genexus.com/commwiki/wiki?57550
genexus_version: "18"
---

# PDF Reports Library property (GeneXus 18 Upgrade 8 or prior)

Sets the library to use for generating web reports in PDF format.

### [Values](#Values)

|  |  |
| --- | --- |
| **iText (Legacy)** | Default value. Uses iText 2 or 4 (depending on the Generator) to generate PDF and provides HTML print management in PDF reports. |
| **iText 8** | Uses iText 8 Core for general handling of PDF generation and pdfHTML for handling HTML printing in PDF reports. |
| **PDFBox** | Uses the free and open source PDFBox library to generate PDF and manage HTML printing in PDF reports. |

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604)  
**Level:** Generator

### [Description](#Description)

This property allows you to choose between different library options to suit the specific needs of your application.

By selecting the iText (Legacy) value, you choose the library that has also been referenced by programs generated with versions prior to GeneXus 18 Upgrade 4. This means that:

* For the [Java Generator](https://wiki.genexus.com/commwiki/wiki?12258), iText version 2 of the library is used.
* For the [.NET Generator](https://wiki.genexus.com/commwiki/wiki?38604), iText version 4 of the library is used.

It is important to note the different licensing schemes of iText 8. For more information, see [iText License Model](https://itextpdf.com/how-buy).

When choosing a particular library, do not expect the reports generated to be identical in all visual details. Each library has its own ways of handling certain features, such as bold or italicized text. For example, iText provides methods to bold or italicize any text, while PDFBox does not provide those features and suggests the use of a specific font file (ttf) to accomplish this.

In addition, it is important to note that PDFBox (available only in the Java Generator) is a low-level library that is not designed to create [complex layouts](https://pdfbox.apache.org/2.0/faq.html), such as multi-level lists, tables, inline or internal styles. If a more sophisticated rendering of HTML content in PDF reports is required, it is recommended to consider using iText 8, which offers enhanced rendering capabilities for more advanced presentation in the generated PDF documents.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute [Build any object](https://wiki.genexus.com/commwiki/wiki?17719) with the purpose of generating the \*.config files.

### [See Also](#See+Also)

[PDF Reports](https://wiki.genexus.com/commwiki/wiki?13531)  
[External utilities used by GeneXus-generated web applications](https://wiki.genexus.com/commwiki/wiki?15671)
