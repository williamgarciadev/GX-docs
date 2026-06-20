---
title: "SameSite cookie attribute property"
source_id: 47685
source_url: https://wiki.genexus.com/commwiki/wiki?47685
genexus_version: "18"
---

# SameSite cookie attribute property

Declares the scope of the cookies, and controls if they should be restricted to a first-party or same-site context.

### [Values](#Values)

|  |  |
| --- | --- |
| **Lax** | Cookies are sent with same-site requests, and with cross-site top-level navigations. |
| **None** | Cookies are sent with same-site and cross-site requests. It requires a secure context/HTTPS. |
| **Strict** | Cookies are sent along with same-site requests. |
| **Do not specify** | Cookies are sent with same-site and cross-site requests. |

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)  
**Level:** [Environment](https://wiki.genexus.com/commwiki/wiki?7115)

### [Description](#Description)

For new [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)s the default value for the property is "Lax," while for existing KBs created with a version prior to [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/wiki?47659,,) it is "Do not specify."

This property is used as a countermeasure to mitigate CSRF attacks. For more information regarding security on this attribute, please read the [OWASP recommendations](https://owasp.org/www-community/SameSite).

The browser's behavior on this matter was defined by the [IETF](https://www.ietf.org/) in the document [Incrementally Better Cookies](https://tools.ietf.org/html/draft-west-cookie-incrementalism-00), and it has been implemented on Chromium Browser since [version 85](https://www.chromestatus.com/feature/5088147346030592); other browsers will follow.

In summary, there are 3 possible values for this cookie attribute:

* Lax: The cookie will be attached to the browser's responses for requests from same-site or cross-site requests on the top-level navigation. This is also the default value browsers will apply if the Secure attribute is set to True and the SameSite value is not specified, which means that applications containing or using iFrames will not work unless the SameSite attribute is set to None.
* Strict: The cookie will not be sent on any cross-site request; it will be sent only for same-site requests. This is the safer and more restrictive configuration.
* None: The cookie will always be sent when the Secure attribute is set to True. If the Secure attribute is set to False (in developing environments using HTTP, for example) the cookie will never be sent.

The Do not specify value was implemented because of backward compatibility reasons. It can be changed on deployment using infrastructure or web server configuration options. The same applies to the Secure attribute.

This configuration will apply to all cookies, including those generated using the [Cookie data type](https://wiki.genexus.com/commwiki/wiki?21582).

### [.NET Specific](#.NET+Specific)

Values different than 'Do not specify' are only supported in .NET Framework 4.7.2 or higher

#### [.Net Framework 4.7.2 and 4.8 specific information for 'Do not specify' configuration setting](#.Net+Framework+4.7.2+and+4.8+specific+information+for+%27Do+not+specify%27+configuration+setting)

Because the 2016 and 2019 draft specifications are not compatible, the November 2019 .Net Framework update introduces some changes that may be breaking. Session State and Forms Authentication cookies are now written to the network as Lax instead of unspecified. As a consequence, 'Unspecified' is only available to httpCookies at the moment. That means all cookies except the ASPNet Cookie (ASP.Net\_SessionId).

For more information, please visit [this link](https://docs.microsoft.com/en-us/aspnet/samesite/system-web-samesite).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

For example, requests for https://example.com/sekrit-image will attach same-site cookies if and only if initiated from a context whose 'site for cookies' is example.com.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, execute [Build any object](https://wiki.genexus.com/commwiki/wiki?17719) with the purpose of generating the \*.config files. |

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/wiki?47659,,).


|  |
| --- |
| **Backlinks** |
| [Cookie data type](https://wiki.genexus.com/commwiki/wiki?21582) | [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55768) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) | [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) |
| [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |

---
