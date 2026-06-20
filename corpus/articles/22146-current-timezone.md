---
title: "Current TimeZone"
source_id: 22146
source_url: https://wiki.genexus.com/commwiki/wiki?22146
genexus_version: "18"
---

# Current TimeZone

The Current TimeZone ([CTZ](https://wiki.genexus.com/commwiki/wiki?22005)) is the [TimeZone](https://wiki.genexus.com/commwiki/wiki?21997,,) of the "client" running an application. This concept is valid only when [TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) is enabled.

* In Web applications, the browser is the client.
* In [Smart Device](https://wiki.genexus.com/commwiki/wiki?20427,,) applications, the device is the client
* In objects exposed as Command Line, REST Service, SOAP Service, HTTP Service or Enterprise Java Bean, the computer where they are hosted (usually an application server) is the client.

Exceptions:

* Procedures exposed as HTTP Services that are called from other objects in the same Web application, the browser is the client.
* In Objects exposed as REST Services that are called from a Smart Device application, the device is the client.

The Current TimeZone can be changed with the [SetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21893)


|  |
| --- |
| **Backlinks** |
| [CTZ](https://wiki.genexus.com/commwiki/wiki?22005) | [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218) | [GetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21915) |
| [SetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21893) | [The TimeZone problem](https://wiki.genexus.com/commwiki/wiki?22135) | [Toc:TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) | [TimeZone Support - DateTime handling](https://wiki.genexus.com/commwiki/wiki?21990) |
| [View DateTime values in a selected time zone - TimeZone Scenario](https://wiki.genexus.com/commwiki/wiki?22140) |

---
