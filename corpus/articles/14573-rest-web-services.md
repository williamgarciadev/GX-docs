---
title: "REST Web Services"
source_id: 14573
source_url: https://wiki.genexus.com/commwiki/wiki?14573
genexus_version: "18"
---

# REST Web Services

Web services allow programs written in different languages and running on different platforms to communicate with each other, following standards. There are cases where you want to access resources provided by other applications with particular emphasis on the optimization of HTTP traffic (important when clients are mobile devices for example).

REST is a style of web services design, which guarantees Interoperability under a paradigm of simplicity and "saving of resources".

In GeneXus, [REST](http://en.wikipedia.org/wiki/Representational_State_Transfer) solutions can be incorporated into applications very easily.

Basically, the goal is to expose application data, that is also called "resources" or entities on the web, with an output with a standard format (XML, JSON), to be interpreted by a program that runs on any platform or framework, or even on any HTTP client.

`[imagen omitida: wiki id 14525]`

### [SOAP solution to the problem of interoperability: REST](#SOAP+solution+to+the+problem+of+interoperability%3A+REST)

There are some protocols and standards built on HTTP that are designed to create web services such as as WS \*. Soap is a lightweight protocol for the exchange of information in a decentralized, distributed environment; data representation is done through XML protocol. A SOAP message is an XML document that consists of a mandatory SOAP envelope, an optional header, and a required body. Another solution to the same problem: REST.

The following is an example of invoking a REST service, where you can see in the HTTP header the invocation (HTTP GET) and the body's response (JSON containing the answer.) Note that the answer is a list of products, where each product contains a URI to access the product detail. The response is characterized by being compact and lightweight.

`[imagen omitida: wiki id 14526]`  
`[imagen omitida: wiki id 14527]`

Check the [REST Protocol considerations](https://wiki.genexus.com/commwiki/wiki?48062) section to understand what is REST and the considerations to take into account when designing a REST based API.


|  |
| --- |
| **Pages** |
| [Consuming REST Data Providers in Genexus](https://wiki.genexus.com/commwiki/wiki?20977,Consuming+REST+Data+Providers+in+Genexus,) | [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146) | [Troubleshooting secure rest services](https://wiki.genexus.com/commwiki/wiki?29439,Troubleshooting+secure+rest+services,) |

---
