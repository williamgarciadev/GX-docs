---
title: "Execute method"
source_id: 7047
source_url: https://wiki.genexus.com/commwiki/wiki?7047
genexus_version: "18"
---

# Execute method

Executes an HTTP method in a defined URL path.

### [Syntax](#Syntax)

**&***VarBasedOnHttpClient***.Execute(***Method***,** *URL***)**

**Where:**  
  
**&***VarBasedOnHttpClient* Is a variable based on the [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932).

*Method*  
    Is the type of HTTP method used to retrieve data. Only accepts [HttpMethod domain](https://wiki.genexus.com/commwiki/wiki?31498) values.

*URL*  
    Relative URL path for the object whose information wants to be obtained.

**Type Returned:**  
HttpClient

### [Scope](#Scope)

**Data Types:**[HttpClient](https://wiki.genexus.com/commwiki/wiki?6932)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

The retrieved data is stored in [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) based variable, and it can be obtained using [ToString](https://wiki.genexus.com/commwiki/wiki?7090) or [To File](https://wiki.genexus.com/commwiki/wiki?7089) methods.

### [Samples](#Samples)

```
&HttpClient.execute(HttpMethod.Get, "/servlet/hclientes")
&Result = &HttpClient.ToString()
```

###


|  |
| --- |
| **Backlinks** |
| [A10:2021 - Server-side request forgery (SSRF)](https://wiki.genexus.com/commwiki/wiki?50190) | [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) | [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) |
| [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) | [HttpMethod domain](https://wiki.genexus.com/commwiki/wiki?31498) | [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626) | [ToFile method](https://wiki.genexus.com/commwiki/wiki?7089) |

---
