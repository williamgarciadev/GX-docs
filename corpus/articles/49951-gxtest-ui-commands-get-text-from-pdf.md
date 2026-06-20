---
title: "GXtest UI Commands - Get Text from PDF"
source_id: 49951
source_url: https://wiki.genexus.com/commwiki/wiki?49951
genexus_version: "18"
---

# GXtest UI Commands - Get Text from PDF

Extracting the text content of a PDF can be useful if your application generates these documents.

Typically is used combined with [assertions](https://wiki.genexus.com/commwiki/wiki?38336) to let GXtest check for expected content within the document. Take into account that this command retrieves all the text inside a PDF file, you must extract and process the particular piece of information you want to validate. Regular expressions are a good asset to do such tasks.

## [GetTextFromPDF](#GetTextFromPDF)

Gets the text from the PDF in the given path.

### [Syntax](#Syntax)

```
&myVar = &driver.GetTextFromPDF("C:\mypdf.pdf")
```

**Where:**

*&myVar*Is a variable based on the [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778).

*&driver*  
   Is a variable based on the Webdriver, GXtest external object.

### [**Parameters**](#Parameters)

* Path: the path of the PDF to extract text from.

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?49971,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
