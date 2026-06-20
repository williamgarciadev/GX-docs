---
title: "AddHeader method"
source_id: 7064
source_url: https://wiki.genexus.com/commwiki/wiki?7064
genexus_version: "18"
---

# AddHeader method

Adds a header to the HTTP header.

### [Syntax](#Syntax)

*&*DataType.**AddHeader(***Name*, *Value***)**

**Where:**  
*&DataType*  
     Variable name based on an [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932) or an [HttpResponse](https://wiki.genexus.com/commwiki/wiki?6934) data type.  
  
*Name*  
   Name of the header, must be string.

*Value*  
   Value of the header, must be string.

### [Scope](#Scope)

**Extended Data Types:** [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932), [HttpResponse](https://wiki.genexus.com/commwiki/wiki?6934)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Samples](#Samples)

```
&httpresponse.AddHeader(!"User-Agent",!"GeneXus")
// &httpresponse is HttpResponse data type
```

The former line sets the “User-Agent” header with the “GeneXus” value

```
&HttpResponse.AddHeader(!'Content-Disposition',!'attachment; filename="WhatsApp Image 2020-01-10 at 12.45.59.jpeg"')
```

The former line is part of the code of probably a procedure with [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) set to 'HTTP' that returns a file. The line sets the Content-Disposition header so that the file downloaded to the browser with the name "WhatsApp Image 2020-01-10 at 12.45.59.jpeg"

### [See Also](#See+Also)

[HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932)  
[HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934)


|  |
| --- |
| **Backlinks** |
| [Add method - SDT Collection](https://wiki.genexus.com/commwiki/wiki?8657) | [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) | [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) |
| [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) | [HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934) |

---
