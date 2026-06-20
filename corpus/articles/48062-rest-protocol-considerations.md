---
title: "REST Protocol considerations"
source_id: 48062
source_url: https://wiki.genexus.com/commwiki/wiki?48062
genexus_version: "18"
---

# REST Protocol considerations

### [What is REST?](#What+is+REST%3F)

[Representational State Transfer](http://en.wikipedia.org/wiki/Representational_State_Transfer) or REST is a style of software architecture for distributed environments. It is not a protocol.

REST is a resource-oriented model. It means that each URL is a representation of an object —or resource—. Each resource is represented by a URI. You can do a GET of that resource using the HTTP GET method, modify it with the HTTP PUT method, create a new representation with HTTP POST and HTTP DELETE to delete the method (i.e. that, there is a uniform interface to access the resource) .

In turn, each resource has n possible representations that can be XML, JSON, etc.

REST makes a series of rules or [restrictions](http://en.wikipedia.org/wiki/Representational_State_Transfer#Constraints). REST's followers say the web has enjoyed scalability as a result of some key basic designs. Based on these foundations is that they created the principles or constraints that must meet a REST architecture.

### [Design considerations](#Design+considerations)

You will need to consider the methods that you need to implement for a REST based API. For example, to let end users access the list of products - GET, to access each product (GET), to insert a purchase order (POST) or to update an order (PUT).

Besides, take into account the parameter types, it is recommended to use basic data types (scalar types such as numeric, string, date, GUID) when using the GET and DELETE verbs, because they will use the URL queryString to transfer it; the Output does not have this restriction.

### [See Also](#See+Also)

[API object](https://wiki.genexus.com/commwiki/wiki?46151)


|  |
| --- |
| **Backlinks** |
| [REST Protocol property](https://wiki.genexus.com/commwiki/wiki?37254) | [REST Protocol property in API Object](https://wiki.genexus.com/commwiki/wiki?46380) | [Category:REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) |
| [Toc:Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213) |

---
