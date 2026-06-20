---
title: "PDF Reports"
source_id: 13531
source_url: https://wiki.genexus.com/commwiki/wiki?13531
genexus_version: "18"
---

# PDF Reports

You can create a PDF [report](https://wiki.genexus.com/commwiki/wiki?5489) by defining a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) with [Layout](https://wiki.genexus.com/commwiki/wiki?5468). After that, to be able to run it in PDF format, you must set the following properties and define the following rule in the Procedure:

**Properties**

* [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) = True
* [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) = HTTP
* [Report output property](https://wiki.genexus.com/commwiki/wiki?7943) = Only to file

**Rule**

* [Output\_File rule](https://wiki.genexus.com/commwiki/wiki?7965)

### [Requirements](#Requirements)

Acrobat Reader (or any other PDF viewer) must be installed on the client.

### [Sample](#Sample)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Customer
{
  CustomerId*
  CustomerName
  CustomerAddress
  CustomerPhone
}
```

Suppose you need to implement a PDF report that lists the name and phone of all the customers.

To do so, first of all, you have to [create](https://wiki.genexus.com/commwiki/wiki?9931) a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293).

Next, configure the Procedure properties as follows:

* [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) = True
* [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) = HTTP
* [Report output property](https://wiki.genexus.com/commwiki/wiki?7943) = Only to file

Go to the Rules tab and write:

```
Output_File("CustomersReport","PDF");
```

Go to the [Layout](https://wiki.genexus.com/commwiki/wiki?5468) tab. You will see one predefined Printblock (named "printBlock1"). Insert the Customer attributes you want to list inside that Printblock:

`[imagen omitida: wiki id 56068]`

Finally, in the [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) define the following code:

```
For each Customer
   Print printBlock1
endfor
```

### [Page sizes](#Page+sizes)

All the page sizes that can be used in GeneXus are supported:

|  |  |
| --- | --- |
| **Type** | **Dimensions** |
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

They are not automatically embedded in the generated PDF. Therefore, if you need to embed a specific font, please read: [How to embed a font in the pdf](https://www.genexus.com/developers/websac?es,,,53863).

For supported fonts, see [How to use Cyrillic characters in a PDF?](https://kb.itextpdf.com/home/it7kb/faq/how-to-use-cyrillic-characters-in-a-pdf)

### [Settings](#Settings)

PDF report settings should be configured in the [PDFReport.ini file](https://wiki.genexus.com/commwiki/wiki?27500).

Set the following PDFReport.ini properties to generate a PDF file with a fixed page size such as A3, A4, Letter.

* LeftMargin = 0
* TopMargin = 0

By default, PDF files are generated using version 1.4.

If your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) has the [Java Generator](https://wiki.genexus.com/commwiki/wiki?12258) or [.NET Generator](https://wiki.genexus.com/commwiki/wiki?38604) as [Environment](https://wiki.genexus.com/commwiki/wiki?7115), you can configure the library you want to use to generate the PDF reports. To do this, set the appropriate value in the [PDF Reports Library property](https://wiki.genexus.com/commwiki/wiki?54844).

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [PDF Reports and For each command to query the database](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/lists-and-for-each-command-to-query-the-database-6104762)

### [See Also](#See+Also)

[Web printing on client printer (without an applet)](https://wiki.genexus.com/commwiki/wiki?33912)  
[SAC # 34500](https://www.genexus.com/developers/websac?es,,,34500)


|  |
| --- |
| **Backlinks** |
| [After Trn event](https://wiki.genexus.com/commwiki/wiki?8045) | [End user customizable reports](https://wiki.genexus.com/commwiki/wiki?18909) | [External utilities used by GeneXus generated Android applications](https://wiki.genexus.com/commwiki/wiki?25098) |
| [External utilities used by GeneXus generated web applications](https://wiki.genexus.com/commwiki/wiki?15671) | [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54956) | [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55934) |
| [PDF Reports (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54937) | [PDF Reports (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55935) | [PDF Reports Library property](https://wiki.genexus.com/commwiki/wiki?54844) |
| [PDF Reports Library property (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55459) | [PDF Reports Library property (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55933) | [Procedure Layout](https://wiki.genexus.com/commwiki/wiki?5468) | [Category:Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) |
| [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) | [Category:Static reports](https://wiki.genexus.com/commwiki/wiki?5489) |

---
