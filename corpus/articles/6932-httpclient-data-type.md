---
title: "HttpClient data type"
source_id: 6932
source_url: https://wiki.genexus.com/commwiki/wiki?6932
genexus_version: "18"
---

# HttpClient data type

This data type enables the definition of variables that, through property configuration and method invocation, allow you to build an HTTP request, send it to a URL, and read the results.  
  
The defined variable represents an HTTP connection.

### [Properties](#Properties)

* [BaseURL](https://wiki.genexus.com/commwiki/wiki?7008)
* [Basic and Digest](https://wiki.genexus.com/commwiki/wiki?7103)
* [ErrCode](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?40308,,)
* [ErrDescription](https://wiki.genexus.com/commwiki/wiki?6931)
* [EOF](https://wiki.genexus.com/commwiki/wiki?6975) (\*)
* [Host](https://wiki.genexus.com/commwiki/wiki?6999)
* [IncludeCookies](https://wiki.genexus.com/commwiki/wiki?46728)
* [Port](https://wiki.genexus.com/commwiki/wiki?5019)
* [ProxyServerHost and ProxyServerPort](https://wiki.genexus.com/commwiki/wiki?6988)
* [ReasonLine](https://wiki.genexus.com/commwiki/wiki?7027)
* [Secure](https://wiki.genexus.com/commwiki/wiki?7032)
* [StatusCode](https://wiki.genexus.com/commwiki/wiki?7035)
* [Timeout](https://wiki.genexus.com/commwiki/wiki?7042)

The URL format is as follows: http://Host:Port/BaseUrl/Resource

### [Methods](#Methods)

* [AddAuthentication](https://wiki.genexus.com/commwiki/wiki?7091)
* [AddFile](https://wiki.genexus.com/commwiki/wiki?7046)
* [AddHeader](https://wiki.genexus.com/commwiki/wiki?7064)
* [AddProxyAuthentication](https://wiki.genexus.com/commwiki/wiki?7749)
* [AddString](https://wiki.genexus.com/commwiki/wiki?7063)
* [AddVariable](https://wiki.genexus.com/commwiki/wiki?7078)
* [Execute](https://wiki.genexus.com/commwiki/wiki?7047)
* [GetHeader](https://wiki.genexus.com/commwiki/wiki?7061)
* [ReadChunk method](https://wiki.genexus.com/commwiki/wiki?55645) (\*)
* [ToFile](https://wiki.genexus.com/commwiki/wiki?7089)
* [ToString](https://wiki.genexus.com/commwiki/wiki?7090)

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work With for Web](https://wiki.genexus.com/commwiki/wiki?25475), [Work With](https://wiki.genexus.com/commwiki/wiki?15974), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)

### [Availability](#Availability)

(\*) The EOF property and ReadChunk method are available in the Java, .NET, .NET Framework and Angular generators since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241).

### [Samples](#Samples)

See [Consuming a Rest Service with GeneXus](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44405,,)

### [See Also](#See+Also)

[HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934)  
[HttpRequest data type](https://wiki.genexus.com/commwiki/wiki?6933)  
[Maximum pool size per route property](https://wiki.genexus.com/commwiki/wiki?48111)  
[Maximum pool size property](https://wiki.genexus.com/commwiki/wiki?48110)


|  |
| --- |
| **Backlinks** |
| [A10:2021 - Server-side request forgery (SSRF)](https://wiki.genexus.com/commwiki/wiki?50190) | [AddAuthentication method](https://wiki.genexus.com/commwiki/wiki?7091) | [AddFile method](https://wiki.genexus.com/commwiki/wiki?7046) |
| [AddHeader method](https://wiki.genexus.com/commwiki/wiki?7064) | [AddProxyAuthentication method](https://wiki.genexus.com/commwiki/wiki?7749) | [AddString method](https://wiki.genexus.com/commwiki/wiki?7063) | [AddVariable method](https://wiki.genexus.com/commwiki/wiki?7078) |
| [Angular application - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46352) | [BaseUrl property](https://wiki.genexus.com/commwiki/wiki?7008) | [Basic and Digest Properties](https://wiki.genexus.com/commwiki/wiki?7103) | [Best Practices for Manual Synchronization](https://wiki.genexus.com/commwiki/wiki?22276) |
| [Business Components as Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28214) | [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) | [ContextPath Rewrite: X-Forwarded Headers Support (App behind Reverse Proxy)](https://wiki.genexus.com/commwiki/wiki?45983) |
| [ContextPath Rewrite: X-Forwarded Headers Support (App behind Reverse Proxy) (GeneXus 18 Upgrade 10)](https://wiki.genexus.com/commwiki/wiki?59271) | [Data Types for Http Handling](https://wiki.genexus.com/commwiki/wiki?10150) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [EOF Property](https://wiki.genexus.com/commwiki/wiki?6975) |
| [ErrCode Property](https://wiki.genexus.com/commwiki/wiki?6930) | [ErrDescription Property](https://wiki.genexus.com/commwiki/wiki?6931) | [ErrDisplay Property](https://wiki.genexus.com/commwiki/wiki?6929) | [Execute method](https://wiki.genexus.com/commwiki/wiki?7047) |
| [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54956) | [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55934) | [External utilities used by GeneXus-generated web applications](https://wiki.genexus.com/commwiki/wiki?15671) | [Facebook external object](https://wiki.genexus.com/commwiki/wiki?38432) |
| [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239) | [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [GetHeader method](https://wiki.genexus.com/commwiki/wiki?7061) | [Host Property](https://wiki.genexus.com/commwiki/wiki?6999) |
| [HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864) | [HowTo: Consume a Procedure exposed as a Rest service](https://wiki.genexus.com/commwiki/wiki?15314) | [HowTo: Consume a Rest Data Provider](https://wiki.genexus.com/commwiki/wiki?30737) | [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) |
| [HowTo: Delete data from a BC exposed as a Rest service](https://wiki.genexus.com/commwiki/wiki?30702) | [HowTo: Request data from Facebook using Graph API and Access Token](https://wiki.genexus.com/commwiki/wiki?38437) | [HowTo: Retrieve data from a BC exposed as a Rest service](https://wiki.genexus.com/commwiki/wiki?30699) | [HowTo: Update data using a BC exposed as a Rest service](https://wiki.genexus.com/commwiki/wiki?30701) |
| [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) | [HowTo: Use the Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?23558) |
| [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) | [HttpRequest data type](https://wiki.genexus.com/commwiki/wiki?6933) | [HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934) | [IncludeCookies Property](https://wiki.genexus.com/commwiki/wiki?46728) |
| [Json 2 SDT](https://wiki.genexus.com/commwiki/wiki?22574) | [Manual Synchronization Code Sample](https://wiki.genexus.com/commwiki/wiki?22543) | [Maximum pool size per route property](https://wiki.genexus.com/commwiki/wiki?48111) | [Maximum pool size per route property (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58081) |
| [Maximum pool size property](https://wiki.genexus.com/commwiki/wiki?48110) | [KB:OnlineShop (Shopping cart sample)](https://wiki.genexus.com/commwiki/wiki?27158) | [OpenAPI import tool](https://wiki.genexus.com/commwiki/wiki?31864) | [OpenAPI import tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54370) |
| [Port Property](https://wiki.genexus.com/commwiki/wiki?5019) | [ProxyServerHost, ProxyServerPort Properties](https://wiki.genexus.com/commwiki/wiki?6988) | [ReadChunk method](https://wiki.genexus.com/commwiki/wiki?55645) | [Reading and writing chunked responses](https://wiki.genexus.com/commwiki/wiki?55630) |
| [ReasonLine Property](https://wiki.genexus.com/commwiki/wiki?7027) | [Secure Property](https://wiki.genexus.com/commwiki/wiki?7032) | [StatusCode Property](https://wiki.genexus.com/commwiki/wiki?7035) | [Timeout property](https://wiki.genexus.com/commwiki/wiki?7042) |
| [TLS Services](https://wiki.genexus.com/commwiki/wiki?39253) | [ToFile method](https://wiki.genexus.com/commwiki/wiki?7089) | [ToFile method (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59676) | [ToString method](https://wiki.genexus.com/commwiki/wiki?7090) |
| [Updating entities using REST Protocol](https://wiki.genexus.com/commwiki/wiki?28205) |

---
