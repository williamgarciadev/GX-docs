---
title: "HttpClient data type (GeneXus 18 Upgrade 6 or prior)"
source_id: 55613
source_url: https://wiki.genexus.com/commwiki/wiki?55613
genexus_version: "18"
---

# HttpClient data type (GeneXus 18 Upgrade 6 or prior)

Builds a request, send it to a URL, and read the results.

This object reflects an HTTP connection.

### [Properties](#Properties)

|  |  |
| --- | --- |
| [BaseURL](https://wiki.genexus.com/commwiki/wiki?7008) | [ProxyServerHost and ProxyServerPort](https://wiki.genexus.com/commwiki/wiki?6988) |
| [Basic and Digest](https://wiki.genexus.com/commwiki/wiki?7103) | [ReasonLine](https://wiki.genexus.com/commwiki/wiki?7027) |
| [ErrCode](https://wiki.genexus.com/commwiki/wiki?40308,,) | [Secure](https://wiki.genexus.com/commwiki/wiki?7032) |
| [ErrDescription](https://wiki.genexus.com/commwiki/wiki?6931) | [StatusCode](https://wiki.genexus.com/commwiki/wiki?7035) |
| [Host](https://wiki.genexus.com/commwiki/wiki?6999) | [Timeout](https://wiki.genexus.com/commwiki/wiki?7042) |
| [Port](https://wiki.genexus.com/commwiki/wiki?5019) | [IncludeCookies](https://wiki.genexus.com/commwiki/wiki?46728) |

The URL format is the following: http://Host:Port/BaseUrl/Resource

### [Methods](#Methods)

|  |  |
| --- | --- |
| [AddAuthentication](https://wiki.genexus.com/commwiki/wiki?7091) | [AddVariable](https://wiki.genexus.com/commwiki/wiki?7078) |
| [AddFile](https://wiki.genexus.com/commwiki/wiki?7046) | [Execute](https://wiki.genexus.com/commwiki/wiki?7047) |
| [AddHeader](https://wiki.genexus.com/commwiki/wiki?7064) | [GetHeader](https://wiki.genexus.com/commwiki/wiki?7061) |
| [AddProxyAuthentication](https://wiki.genexus.com/commwiki/wiki?7749) | [ToFile](https://wiki.genexus.com/commwiki/wiki?7089) |
| [AddString](https://wiki.genexus.com/commwiki/wiki?7063) | [ToString](https://wiki.genexus.com/commwiki/wiki?7090) |

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects:** | [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work With for Web](https://wiki.genexus.com/commwiki/wiki?25475), [Work With](https://wiki.genexus.com/commwiki/wiki?15974), [Panel](https://wiki.genexus.com/commwiki/wiki?24829) |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

### [Availability](#Availability)

This data type is available since [GeneXus X](https://wiki.genexus.com/commwiki/wiki?5924,,)

### [Samples](#Samples)

See [Consuming a Rest Service with GeneXus](https://wiki.genexus.com/commwiki/wiki?44405,,)

### [See Also](#See+Also)

[HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934)  
[HttpRequest data type](https://wiki.genexus.com/commwiki/wiki?6933)  
[Maximum pool size per route property](https://wiki.genexus.com/commwiki/wiki?48111)  
[Maximum pool size property](https://wiki.genexus.com/commwiki/wiki?48110)
