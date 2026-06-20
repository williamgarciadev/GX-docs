---
title: "AddFile method"
source_id: 7046
source_url: https://wiki.genexus.com/commwiki/wiki?7046
genexus_version: "18"
---

# AddFile method

Adds file contents to a data buffer that is going to be sent.

### [Syntax](#Syntax)

&DataType**.AddFile(***Path,*[*Name*])

**Where:**  
*&DataType*  
     Variable name based on an [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932) or an [HttpResponse](https://wiki.genexus.com/commwiki/wiki?6934) data type.

*Path*  
     String containing the file's path.

*Name (Optional)*  
     String containing the name of the variable with which the server waits for the file.

### [Scope](#Scope)

**Extended data types:** [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932), [HttpResponse](https://wiki.genexus.com/commwiki/wiki?6934)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),  [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

If the content of the HttpClient message is multipart / form-data (given by Content-Type Header), then the AddFile method adds the file as multipart. In this case, the second parameter is needed to indicate the name of the variable that the file represents. Also, you have to necessarily precede your sentence with a header that specifies a specific Content-Type, like this:

```
&Httpclient.Addheader("Content-Type", !"multipart/form-data")
```

### [See Also](#See+Also)

[HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932)  
[HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934)


|  |
| --- |
| **Backlinks** |
| [AddString method](https://wiki.genexus.com/commwiki/wiki?7063) | [Angular application - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46352) | [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) |
| [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) | [HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934) |

---
