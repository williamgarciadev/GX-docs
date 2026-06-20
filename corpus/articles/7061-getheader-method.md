---
title: "GetHeader method"
source_id: 7061
source_url: https://wiki.genexus.com/commwiki/wiki?7061
genexus_version: "18"
---

# GetHeader method

Returns the value of a header converted to the variable type.

### [Syntax](#Syntax)

*Value =* **&***DataType***.GetHeader(***Character-expression***)**  
  
**Where:**  
*Character-expression*  
   Name of the header

*Value*  
   Value of the header; any type will be converted.

### [Scope](#Scope)

**Extended Data Types:** [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932), [HttpRequest](https://wiki.genexus.com/commwiki/wiki?6933)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Samples](#Samples)

**Example 1**

```
&value = &httpclient.GetHeader(“User-Agent”)
```

If the value of the “User-Agent” header is “GeneXus”, its value is stored in the &value variable.

**Example 2**

The following image shows the Response and Request headers of this article.

`[imagen omitida: wiki id 18164]`

### [See Also](#See+Also)

[HttpClient Data Type](https://wiki.genexus.com/commwiki/wiki?6932)  
[HttpRequest Data Type](https://wiki.genexus.com/commwiki/wiki?6933)

### [More Details](#More+Details)

[List of HTTP header fields](http://en.wikipedia.org/wiki/List_of_HTTP_header_fields)


|  |
| --- |
| **Backlinks** |
| [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) | [HttpRequest data type](https://wiki.genexus.com/commwiki/wiki?6933) |

---
