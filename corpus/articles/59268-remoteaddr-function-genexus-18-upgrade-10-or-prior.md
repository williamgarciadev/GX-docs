---
title: "RemoteAddr function (GeneXus 18 Upgrade 10 or prior)"
source_id: 59268
source_url: https://wiki.genexus.com/commwiki/wiki?59268
genexus_version: "18"
---

# RemoteAddr function (GeneXus 18 Upgrade 10 or prior)

Returns the client IP address.

### [Syntax](#Syntax)

**RemoteAddr()**  
  
**Type Returned:**   
String

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),[Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

The RemoteAddr() function returns the IP address of the client PC that made the web request. The format of the string returned is: "nnn.nnn.nnn.nnn"

**Notes:**

* This function is available and can be used from any GeneXus object. The result only makes sense if the object was directly or indirectly called by a Web Panel, or if it’s being executed in a web environment.
* The RemoteAddr function is designed to return the IP of the client making the web request. However, when the [X-Forwarded Headers](https://wiki.genexus.com/commwiki/wiki?59271) is used, it can contain multiple IPs separated by commas, representing each proxy through which the request has passed. In order for the RemoteAddr function of a .NET application to behave correctly behind a proxy (such as nginx), it is necessary to configure the X-Forwarded Headers (for example, X-Forwarded-For and X-Forwarded-Proto) and enable their processing using the ASPNETCORE\_FORWARDEDHEADERS\_ENABLED=“true” environment variable.

### [See Also](#See+Also)

[RemoteAddress Property](https://wiki.genexus.com/commwiki/wiki?7026)
