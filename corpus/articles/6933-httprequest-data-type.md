---
title: "HttpRequest data type"
source_id: 6933
source_url: https://wiki.genexus.com/commwiki/wiki?6933
genexus_version: "18"
---

# HttpRequest data type

This data type enables the definition of variables used to define HTTP requests from the client to a server.

### [Properties](#Properties)

* [BaseURL](https://wiki.genexus.com/commwiki/wiki?7008)
* [ErrCode](https://wiki.genexus.com/commwiki/wiki?6930)
* [ErrDescription](https://wiki.genexus.com/commwiki/wiki?6931)
* [Method](https://wiki.genexus.com/commwiki/wiki?7040)
* [QueryString](https://wiki.genexus.com/commwiki/wiki?7017)
* [Referrer](https://wiki.genexus.com/commwiki/wiki?7014)
* [RemoteAddress](https://wiki.genexus.com/commwiki/wiki?7026)
* [ScriptName](https://wiki.genexus.com/commwiki/wiki?6974)
* [ScriptPath](https://wiki.genexus.com/commwiki/wiki?6972)
* [Secure](https://wiki.genexus.com/commwiki/wiki?7032)
* [ServerHost](https://wiki.genexus.com/commwiki/wiki?7016)
* [ServerPort](https://wiki.genexus.com/commwiki/wiki?7005)

### [**Methods**](#Methods)

* [GetHeader](https://wiki.genexus.com/commwiki/wiki?7061)
* [GetVariable](https://wiki.genexus.com/commwiki/wiki?7056)
* [ToFile](https://wiki.genexus.com/commwiki/wiki?7089)
* [ToString](https://wiki.genexus.com/commwiki/wiki?7090)

### [Description](#Description)

The URL format is as follows:

http://ServerHost:ServerPort/ScriptPath/ScriptName

Therefore, the [BaseUrl property](https://wiki.genexus.com/commwiki/wiki?7008) must be:

http://ServerHost:ServerPort/ScriptPath/

### [Sample](#Sample)

Consider the following URL: http://wiki.genexus.com/commwiki/servlet/heditpage?6933

The property values of the HttpRequest variable should be:

| Property | Result |
| --- | --- |
| &Httprequest.RemoteAddress | fe80::4081:515a:9289:2dc6%11 \* |
| &Httprequest.BaseUrl | http://wiki.genexus.com/commwiki/servlet/ |
| &Httprequest.ErrDescription | - |
| &Httprequest.Method | GET |
| &Httprequest.QueryString | 6933 |
| &Httprequest.Referrer | Caller's URL |
| &Httprequest.ScriptName | heditpage |
| &Httprequest.ScriptPath | /commwiki/servlet/ |
| &Httprequest.Secure | 0 |
| &Httprequest.ServerHost | wiki.genexus.com |
| &Httprequest.ServerPort | 80 |

#### (\*) If localhost is used, the RemoteAddress will return::1

### [Scope](#Scope)

**Objects:** [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Transactions](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916)  
**Languages:** .NET, Java, Ruby (up to and including GeneXus X Evolution 3)

### [See Also](#See+Also)

[HttpClient](https://wiki.genexus.com/commwiki/wiki?6932)  
[HttpResponse](https://wiki.genexus.com/commwiki/wiki?6934)


|  |
| --- |
| **Backlinks** |
| [ContextPath Rewrite: X-Forwarded Headers Support (App behind Reverse Proxy)](https://wiki.genexus.com/commwiki/wiki?45983) | [ContextPath Rewrite: X-Forwarded Headers Support (App behind Reverse Proxy) (GeneXus 18 Upgrade 10)](https://wiki.genexus.com/commwiki/wiki?59271) | [Data Types for Http Handling](https://wiki.genexus.com/commwiki/wiki?10150) |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) | [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) | [ErrDisplay Property](https://wiki.genexus.com/commwiki/wiki?6929) |
| [GetHeader method](https://wiki.genexus.com/commwiki/wiki?7061) | [GetVariable method](https://wiki.genexus.com/commwiki/wiki?7056) | [HowTo: Integrate a new WhatsApp partner into a GeneXus Chatbot](https://wiki.genexus.com/commwiki/wiki?46271) | [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) |
| [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) | [HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934) | [Method Property](https://wiki.genexus.com/commwiki/wiki?7040) | [QueryString Property](https://wiki.genexus.com/commwiki/wiki?7017) |
| [Referrer Property](https://wiki.genexus.com/commwiki/wiki?7014) | [RemoteAddress Property](https://wiki.genexus.com/commwiki/wiki?7026) | [ScriptName Property](https://wiki.genexus.com/commwiki/wiki?6974) | [ScriptPath Property](https://wiki.genexus.com/commwiki/wiki?6972) |
| [Secure Property](https://wiki.genexus.com/commwiki/wiki?7032) | [ServerHost Property](https://wiki.genexus.com/commwiki/wiki?7016) | [ServerPort Property](https://wiki.genexus.com/commwiki/wiki?7005) | [ToFile method](https://wiki.genexus.com/commwiki/wiki?7089) |
| [ToFile method (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59676) | [ToString method](https://wiki.genexus.com/commwiki/wiki?7090) |

---
