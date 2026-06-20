---
title: "ProxyServerHost, ProxyServerPort Properties"
source_id: 6988
source_url: https://wiki.genexus.com/commwiki/wiki?6988
genexus_version: "18"
---

# ProxyServerHost, ProxyServerPort Properties

These properties allow you to specify a proxy http.

### [Syntax](#Syntax)

**&***DataType***.ProxyServerHost**  
  
**Type Returned:**   
Character  
  
**&***DataType***.ProxyServerPort**  
  
**Type Returned:**   
Numeric

### [Description](#Description)

They allow you to specify a proxy http. In windows environment, the one configured in the PC is automatically used.  
  
**Note:**  
In the case of Java generators, it should be noted that if the servlet engine is executed in Windows, the application will automatically obtain the proxy http configuration and the list of hosts for which it is not possible to use the proxy.   
  
If it is executed in another platform, the proxy must be specified as a ‘System Property’ from the command line of the interpreter, e.g.:   
java -Dhttp.proxyHost=your.proxy.com -Dhttp.proxyPort=XX <mainclass>

In the case of .NET Framework generator, getting the value of the proxy with these properties may depend on the user configured in the IIS and the permissions assigned to it.

In case the properties return empty, change the user configured in the application pool that the application uses directly in the IIS Manager for another one with more permissions, for example, the user administrator of the machine.

If you receive an ErrCode=1 and a timeout error while using the configured proxy under Network & Internet -> Proxy Server on Windows, please ensure that the 'Proxy IP Address' property does not begin with 'http' or 'https'. For example, instead of '[http://myproxy.com](http://myproxy.com/)' or '[https://193.15.14.198](https://193.15.14.198/)', use 'myproxy.com' or '193.15.14.198' respectively.

### [Scope](#Scope)

**Extended Data Types:** [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932)  
**Languages:** .NET, Java, Visual FoxPro (up to GeneXus X Evolution 3), Ruby(up to GeneXus X Evolution 3),

### [See Also](#See+Also)

[HttpClient Data Type](https://wiki.genexus.com/commwiki/wiki?6932)


|  |
| --- |
| **Backlinks** |
| [A10:2021 - Server-side request forgery (SSRF)](https://wiki.genexus.com/commwiki/wiki?50190) | [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) |

---
