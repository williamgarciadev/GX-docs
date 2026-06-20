---
title: "Location data type"
source_id: 6981
source_url: https://wiki.genexus.com/commwiki/wiki?6981
genexus_version: "18"
---

# Location data type

Configures the calls to GeneXus' main objects remotely, when using SOAP protocol.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258),
Ruby (up to GeneXus X Evolution 3),
Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

When you call a remote object via SOAP, you use the Location data type to configure the invocation.

First, you need to associate a Location variable to an existing location through [GetLocation function](https://wiki.genexus.com/commwiki/wiki?7696), and then configure the call using the Location data type properties. You can use [GetSOAPErr](https://wiki.genexus.com/commwiki/wiki?7021) and [GetSOAPErrMsg](https://wiki.genexus.com/commwiki/wiki?7022) functions to check for errors.

### [Properties](#Properties)

|  |  |
| --- | --- |
| [Host](https://wiki.genexus.com/commwiki/wiki?6999) | [Port](https://wiki.genexus.com/commwiki/wiki?5019) |
| [BaseURL](https://wiki.genexus.com/commwiki/wiki?7008) | [Secure](https://wiki.genexus.com/commwiki/wiki?7032) |
| [Timeout](https://wiki.genexus.com/commwiki/wiki?7042) | [Authentication](https://wiki.genexus.com/commwiki/wiki?6982) |
| [AuthenticationMethod](https://wiki.genexus.com/commwiki/wiki?6990) | [AuthenticationRealm](https://wiki.genexus.com/commwiki/wiki?6980) |
| [AuthenticationUser](https://wiki.genexus.com/commwiki/wiki?7018) | [AuthenticationPassword](https://wiki.genexus.com/commwiki/wiki?7019) |
| [CancelOnError](https://wiki.genexus.com/commwiki/wiki?7020) | [Resource Name](https://wiki.genexus.com/commwiki/wiki?11434) |

### [Sample](#Sample)

The Location Data Type can be used, for example, to change the WebService Host, or to give the user a more friendly error message for a WebService problem.

If you have a WebService External Object named "MyWebService", and a variable based on this WebService in an object, the location can be used as:

```
&location = getLocation("MyWebService")
&location.Host = 'www.genexus.com'  // don't include protocol (i.e. HTTP/HTTPS)
&location.BaseUrl = '/services/'
&location.port = 443
&location.secure = 1 // For WebService in Secure Server.
&location.CancelOnError = 2 // When you want to manage the errors (1)
&mywebservice.execute()
```

(1) - Error information can be obtained using the [GetSoapErr](https://wiki.genexus.com/commwiki/wiki?7021) and [GetSoapErrMsg](https://wiki.genexus.com/commwiki/wiki?7022) functions.

#### [**More Details**](#More+Details)

It also commonly uses [Location.xml](https://wiki.genexus.com/commwiki/wiki?6111,,), in order to specify location settings  
The properties specified in runtime by means of a location Datatype, will have preference over the ones specified in runtime by means of a location.xml file, and the latter, in turn, will have preference over the ones specified in generation time; this will allow  more dynamism in the locations setting.

Since [GeneXus X Evolution 3 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?29770,,) location is working properly, when the [Use Native Soap property](https://wiki.genexus.com/commwiki/wiki?13446) is active Previous Versions is not working.

In case of Authentication or Proxy Authentication, it's necessary to know the realm name in order to work properly. Otherwise, an error occur when the services is invoked.  
i.e.: if a proxy is used and the property ProxyAuthenticationRealm was not defined, the following error will be shown when executing the service:  
407: Proxy Authentication Required

In some particular cases of Service Soap, is necessary to configure more data in the location datatype. For that reason is provided a way to extend the location data type. Read more about it at this page: [GxSoapHandlers mechanism for extending Location Data type](https://wiki.genexus.com/commwiki/wiki?39413).  
It only applies when the [Use Native Soap property](https://wiki.genexus.com/commwiki/wiki?13446) is active.

### [See Also](#See+Also)

[Locations](https://wiki.genexus.com/commwiki/wiki?6981)  
[GetLocation Function](https://wiki.genexus.com/commwiki/wiki?7696)  
[GetSOAPErr Function](https://wiki.genexus.com/commwiki/wiki?7021)  
[GetSOAPErrMsg Function](https://wiki.genexus.com/commwiki/wiki?7022)


|  |
| --- |
| **Backlinks** |
| [A10:2021 - Server-side request forgery (SSRF)](https://wiki.genexus.com/commwiki/wiki?50190) | [Authentication Property](https://wiki.genexus.com/commwiki/wiki?6982) | [AuthenticationMethod Property](https://wiki.genexus.com/commwiki/wiki?6990) |
| [AuthenticationPassword Property](https://wiki.genexus.com/commwiki/wiki?7019) | [AuthenticationRealm Property](https://wiki.genexus.com/commwiki/wiki?6980) | [AuthenticationUser Property](https://wiki.genexus.com/commwiki/wiki?7018) | [BaseUrl property](https://wiki.genexus.com/commwiki/wiki?7008) |
| [CancelOnError Property](https://wiki.genexus.com/commwiki/wiki?7020) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [External Object: WSDL - Web Service](https://wiki.genexus.com/commwiki/wiki?6154) |
| [GetLocation function](https://wiki.genexus.com/commwiki/wiki?7696) | [GetSOAPErr function](https://wiki.genexus.com/commwiki/wiki?7021) | [GetSOAPErrMsg function](https://wiki.genexus.com/commwiki/wiki?7022) | [Host Property](https://wiki.genexus.com/commwiki/wiki?6999) |
| [Location data type](https://wiki.genexus.com/commwiki/wiki?6981) | [Port Property](https://wiki.genexus.com/commwiki/wiki?5019) | [Resource Name Property](https://wiki.genexus.com/commwiki/wiki?11434) | [Secure Property](https://wiki.genexus.com/commwiki/wiki?7032) |
| [Timeout property](https://wiki.genexus.com/commwiki/wiki?7042) | [WSAddressing Data Type](https://wiki.genexus.com/commwiki/wiki?44549) | [WSSecurity Data Type](https://wiki.genexus.com/commwiki/wiki?44552) |

---
