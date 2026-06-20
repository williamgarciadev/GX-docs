---
title: "AddString method"
source_id: 7063
source_url: https://wiki.genexus.com/commwiki/wiki?7063
genexus_version: "18"
---

# AddString method

Adds a string to the Http Request or Response.

### [Syntax](#Syntax)

**&***DataType***.AddString(***Value***)**  
  
**Where:**  
*&DataType*  
     Variable name based on an [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932) or an [HttpResponse](https://wiki.genexus.com/commwiki/wiki?6934) data type.

*Value*  
   Any character data (including Character, Varchar and Longvarchar data type attributes | variables).

### [Scope](#Scope)

**Extended data types:** [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932), [HttpResponse](https://wiki.genexus.com/commwiki/wiki?6934)  
**Generators:**[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This method is used to create a custom request or response.

### [Samples](#Samples)

This is a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) with the [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) set as True and the [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) set as HTTP with the following source:

```
&httpresponse.AddString(!"<html>")
&httpresponse.AddString(!"Hello world")
&httpresponse.AddString(!"</html>")
// &httpresponse is HttpResponse data type
```

It creates a sample html page, sending the html code in the Http response; the browser will render the html code:

`[imagen omitida: wiki id 55664]`

**Note**: Do not use this method if you need to send a file content as a string because the string is encoded, for this case use the [AddFile method](https://wiki.genexus.com/commwiki/wiki?7046).

### [See Also](#See+Also)

[HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932)  
[HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934)


|  |
| --- |
| **Backlinks** |
| [Buffer Response property](https://wiki.genexus.com/commwiki/wiki?55195) | [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) |
| [HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934) | [Reading and writing chunked responses](https://wiki.genexus.com/commwiki/wiki?55630) |

---
