---
title: "EOF Property"
source_id: 6975
source_url: https://wiki.genexus.com/commwiki/wiki?6975
genexus_version: "18"
---

# EOF Property

Indicates whether the end of the document or data stream has been reached.

### [Syntax](#Syntax)

**&***DataType***.EOF**  
  
**Type Returned:**   
Boolean

### [Description](#Description)

It can be used after invoking the read or readtype methods.

The EOF property on an [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) allows you to control and verify whether the end of the server response has been reached when reading data in fragments, as is the case with the ["Chunked Response" technique](https://wiki.genexus.com/commwiki/wiki?55630).

When EOF is true, it means that the end of the response has been reached and there are no more data fragments to be read.

### [Sample](#Sample)

```
if (&DataType.EOF)

....

Endif
```

### [Scope](#Scope)

**Extended Data Types:** [XmlReader](https://wiki.genexus.com/commwiki/wiki?6928), [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258),  [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Availability](#Availability)

This property is available in the HttpClient data type since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241).


|  |
| --- |
| **Backlinks** |
| [EOF Property (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55641) | [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [ReadChunk method](https://wiki.genexus.com/commwiki/wiki?55645) |
| [Reading and writing chunked responses](https://wiki.genexus.com/commwiki/wiki?55630) | [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) |

---
