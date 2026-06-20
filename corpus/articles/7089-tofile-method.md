---
title: "ToFile method"
source_id: 7089
source_url: https://wiki.genexus.com/commwiki/wiki?7089
genexus_version: "18"
---

# ToFile method

Returns the entire HTML body in a File.

### [Syntax](#Syntax)

**&***VarBasedOnExtendedDataType***.ToFile(***FileName***)**  
  
**Where:**  
  
**&***VarBasedOnExtendedDataType*  
     Is a [variable](https://wiki.genexus.com/commwiki/wiki?7375) based on the [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932) or [HttpRequest](https://wiki.genexus.com/commwiki/wiki?6933) Extended data type.

*FileName*  
     Is the path to the file.

### [Scope](#Scope)

**Extended Data Types:** [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932), [HttpRequest](https://wiki.genexus.com/commwiki/wiki?6933)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Samples](#Samples)

**HttpClient:**

```
&httpclient.execute("GET","/servlet/clients")
&httpclient.ToFile(“c:\htmls\clients.html”)
```

It returns the HTML code of the clients [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) in the clients.html file.

**HttpRequest:**

```
&httprequest.ToFile(“c:\files\clients.json”)
```

When the object is a [Main](https://wiki.genexus.com/commwiki/wiki?5770) Procedure with the [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) set to HTTP, it saves a file received by a web service call.

### [Security tips](#Security+tips)

Do not use the user's input concatenations or sanitize the user's entries to avoid path traversal or path manipulation vulnerability risks.

### [See Also](#See+Also)

[HttpClient Data Type](https://wiki.genexus.com/commwiki/wiki?6932)  
[HttpRequest Data Type](https://wiki.genexus.com/commwiki/wiki?6933)  
[Execute method](https://wiki.genexus.com/commwiki/wiki?7047)


|  |
| --- |
| **Backlinks** |
| [Execute method](https://wiki.genexus.com/commwiki/wiki?7047) | [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) |
| [HttpRequest data type](https://wiki.genexus.com/commwiki/wiki?6933) | [ToFile method (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59676) |

---
