---
title: "Cookie data type"
source_id: 21582
source_url: https://wiki.genexus.com/commwiki/wiki?21582
genexus_version: "18"
---

# Cookie data type

The Cookie data type enables to create [Cookies](https://wiki.genexus.com/commwiki/wiki?6322) and set different properties of them in [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) web objects.

### [Properties](#Properties)

|  |  |
| --- | --- |
| **Name** | Is the cookie's name and it is a character type. |
| **Value** | Is the value to be stored and it is a character type. |
| **Path** | Is the Path that indicates the [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916) for which the cookie is valid, and it is also a character type. If it isn’t specified, the cookie is valid for the Web Panels that are in the same directory as the one it is stored in, or in subordinated directories. If “/” is indicated, the cookie will be valid for the entire domain. |
| **ExpirationDate** | Indicates the expiration date of the cookie. It is a Date/DateTime type. If it isn’t specified, it will expire when the session is closed in the browser. |
| **Domain** | Is the domain where the cookie is valid. It is a character type. The default domain is the domain where it has been created. |
| **Secure** | Is a numeric type. If it is 1, the cookie is transmitted only if the connection is secure (HTTPS). If it is 0, it is always transmitted. |
| [HttpOnly](https://wiki.genexus.com/commwiki/wiki?21583) | Is a boolean type. It allows avoiding saving or set a cookie from JavaScript code. |

### 

### [Example](#Example)

In a Web Panel, &cookie is a variable of Cookie data type, &ok is [Numeric data type](https://wiki.genexus.com/commwiki/wiki?6793), and &httpresponse is [HttpResponse Data Type](https://wiki.genexus.com/commwiki/wiki?6934). [SetCookie function](https://wiki.genexus.com/commwiki/wiki?6878) is Used to save cookies.

```
Event 'SetCookie example'
    &cookie.Name = 'USR_CTRY'
    &cookie.Value = 'UY'
    &cookie.ExpirationDate = ADDYR(&Today, 1)
    &cookie.Domain = 'otherdom.artech.com.uy'
    &cookie.Secure = 1
    &cookie.HttpOnly = true
    &OK = &httpresponse.SetCookie(&cookie) 
EndEvent
```

### [About SameSite attribute](#About+SameSite+attribute)

It will use the configuration given by the [SameSite cookie attribute property](https://wiki.genexus.com/commwiki/wiki?47685) since [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/wiki?47659,,).

In previous versions, it can be configured using configuration options of the webserver or other infrastructure resources as a WAF or proxy server.

### [Security tips](#Security+tips)

* Set the Secure attribute in 1. This way the cookie will only be transmitted using HTTPS.
* Set the HttpOnly attribute in True. This way the cookie can not be readen or edited by JavaScript.
* Configure the SameSite attribute accordingly to the application needs. The most restrictive way possible. This is a way to restrict sharing the cookie and a mitigation option for CSRF attacks.

### [Availability](#Availability)

From version GeneXus X Evolution 2 Upgrade 3.

### 

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators** | Java, .NET, .NET Core |
| **Interfaces** | Web |
|  |  |

### [See also](#See+also)

[SetCookie function](https://wiki.genexus.com/commwiki/wiki?6878)  
[GetCookie function](https://wiki.genexus.com/commwiki/wiki?6879)  
[SameSite cookie attribute property](https://wiki.genexus.com/commwiki/wiki?47685)


|  |
| --- |
| **Backlinks** |
| [A07:2021 - Identification and authentication failures](https://wiki.genexus.com/commwiki/wiki?50187) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) |
| [HttpOnly property](https://wiki.genexus.com/commwiki/wiki?21583) |
| [SameSite cookie attribute property](https://wiki.genexus.com/commwiki/wiki?47685) | [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |

---
