---
title: "HttpResponse data type"
source_id: 6934
source_url: https://wiki.genexus.com/commwiki/wiki?6934
genexus_version: "18"
---

# HttpResponse data type

This data type enables the definition of variables that represent the server's response to an HTTP request.

### [Properties](#Properties)

* [ErrCode](https://wiki.genexus.com/commwiki/wiki?6930)
* [ErrDescription](https://wiki.genexus.com/commwiki/wiki?6931)

### [Methods](#Methods)

* [AddFile](https://wiki.genexus.com/commwiki/wiki?7046)
* [AddHeader](https://wiki.genexus.com/commwiki/wiki?7064)
* [AddString](https://wiki.genexus.com/commwiki/wiki?7063)

### [Considerations](#Considerations)

HttpResponse data is sent in chunks from the application server. It is important that your Procedure code first sets the needed HttpHeaders ([AddHeader](https://wiki.genexus.com/commwiki/wiki?7064)) and then the content (using the [AddFile](https://wiki.genexus.com/commwiki/wiki?7046) or [AddString](https://wiki.genexus.com/commwiki/wiki?7063) methods).

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:**[Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)

### [See Also](#See+Also)

[HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932)  
[HttpRequest data type](https://wiki.genexus.com/commwiki/wiki?6933)  
[SAC #42759 Liberty WARNING: Cannot set header. Response already committed.](https://www.genexus.com/developers/websac?en,,,42759)  
[Reading and writing chunked responses](https://wiki.genexus.com/commwiki/wiki?55630)


|  |
| --- |
| **Backlinks** |
| [A01:2021 - Broken access control](https://wiki.genexus.com/commwiki/wiki?50181) | [A02:2021 - Cryptographic failures](https://wiki.genexus.com/commwiki/wiki?50182) |
| [AddFile method](https://wiki.genexus.com/commwiki/wiki?7046) | [AddHeader method](https://wiki.genexus.com/commwiki/wiki?7064) | [AddString method](https://wiki.genexus.com/commwiki/wiki?7063) |
| [Buffer Response property](https://wiki.genexus.com/commwiki/wiki?55195) | [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) | [Cookie data type](https://wiki.genexus.com/commwiki/wiki?21582) | [Data Types for Http Handling](https://wiki.genexus.com/commwiki/wiki?10150) |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) | [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) | [ErrDisplay Property](https://wiki.genexus.com/commwiki/wiki?6929) |
| [Good practices for secure development using GAM](https://wiki.genexus.com/commwiki/wiki?47241) | [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) |
| [HttpRequest data type](https://wiki.genexus.com/commwiki/wiki?6933) | [Reading and writing chunked responses](https://wiki.genexus.com/commwiki/wiki?55630) | [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) |
| [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |

---
