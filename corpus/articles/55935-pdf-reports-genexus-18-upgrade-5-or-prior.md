---
title: "PDF Reports (GeneXus 18 Upgrade 5 or prior)"
source_id: 55935
source_url: https://wiki.genexus.com/commwiki/wiki?55935
genexus_version: "18"
---

# PDF Reports (GeneXus 18 Upgrade 5 or prior)

You can create a PDF [report](https://wiki.genexus.com/commwiki/wiki?5489) by defining a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) with [Layout](https://wiki.genexus.com/commwiki/wiki?5468).

You have to set the following properties and rule in the procedure, in order to run it in PDF format:

**Properties**

* [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) = True
* [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) = HTTP
* [Report output property](https://wiki.genexus.com/commwiki/wiki?7943) = Only to file

**Rule**

* [Output\_File rule](https://wiki.genexus.com/commwiki/wiki?7965) must be set

### [Requirements](#Requirements)

Acrobat Reader (or any other PDF viewer) must be installed on the client.

### [Page sizes](#Page+sizes)

All the page sizes that can be used in GeneXus are supported:

|  |  |
| --- | --- |
| **Type** | **Measures** |
| Letter | 8 1/2 x 11 inches |
| Office | 8 1/2 x 14 inches |
| Executive | 7 1/4 x 10 1/2 inches |
| A4 | 210 x 297 mm |
| A5 | 148 x 210 mm |
| B5 | 182 x 257 mm |
| Envelope #9 | 3 7/8 x 8 7/8 inches |
| Envelope #10 | 10 4 1/8 x 9 ½ inches |
| Envelope DL | 110 x 220mm |
| Envelope C5 | 162 x 229 mm |
| Envelope B5 | 176 x 250 mm |
| Envelope Monarch | 3.875 x 7.5 inches |
| User Size |  |

### [Fonts](#Fonts)

They are not automatically embedded in the generated PDF, so if you need to embed a specific font please read: [How to embed a font in the pdf](https://www.genexus.com/en/developers/websac?data=16412).

For supported fonts, see [How to use Cyrillic characters in a PDF?](https://kb.itextpdf.com/home/it7kb/faq/how-to-use-cyrillic-characters-in-a-pdf)

### [Settings](#Settings)

PDF report settings should be configured in the [PDFReport.ini file](https://wiki.genexus.com/commwiki/wiki?27500).

Set the following PDFReport.ini properties to generate a PDF file with a fixed page size such as A3, A4, Letter.

* LeftMargin = 0
* TopMargin = 0

By default, PDF files are generated using version 1.4.

If your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) has the [Java Generator](https://wiki.genexus.com/commwiki/wiki?12258) as [Environment](https://wiki.genexus.com/commwiki/wiki?7115), you can configure the library you want to use to generate the PDF reports. To do this, you must set the appropriate value in the  [PDF Reports Library property](https://wiki.genexus.com/commwiki/wiki?54844).

### [See Also](#See+Also)

[Web printing on client printer (without an applet)](https://wiki.genexus.com/commwiki/wiki?33912)  
[SAC # 34500](https://www.genexus.com/developers/websac?es,,,34500)
