---
title: "Documenting RESTFul services"
source_id: 30776
source_url: https://wiki.genexus.com/commwiki/wiki?30776
genexus_version: "18"
---

# Documenting RESTFul services

[RESTful applications](http://en.wikipedia.org/wiki/Representational_state_transfer) are widely used in different kinds of solutions because they are simple, lightweight, and fast. As a consequence, there's an obvious need that the service providers and consumers converge on how to describe the REST APIs. They are very similar to the already standardized WSDL for SOAP web services.

In this case, [Swagger](https://wiki.genexus.com/commwiki/wiki?50321,,) is a solution for solving the standardization problem of REST APIs. Therefore, consumers of RESTFul services use Swagger as a standardized way of interacting with REST APIs.

### [How to document RESTful services in GeneXus](#How+to+document+RESTful+services+in+GeneXus)

Configure the [Generate OpenAPI interface property](https://wiki.genexus.com/commwiki/wiki?31859) to TRUE. Afterward, all the [Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213) will have their documentation in a file called default.yaml, located under the application directory. The file can be accessed as follows: *http://<server>/<virtual\_dir>/default.yaml* when 
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)/
[.NET](https://wiki.genexus.com/commwiki/wiki?38604) generators are used and *http://<server>/<virtual\_dir>/static/default.yaml* when
[Java](https://wiki.genexus.com/commwiki/wiki?12258) generator is used.

The default.yaml file is updated when any of these objects is generated

* [Procedures as Rest Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?21467)
* [Data Providers as Rest Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28216)
* [Business Components as Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28214)

### [Requirements](#Requirements+)

HTTP Access Control ([CORS](https://wiki.genexus.com/commwiki/wiki?52092,,)) has to be enabled on the server so that the server can accept HTTP requests from the swagger.io server.

#### [.NET generator](https://wiki.genexus.com/commwiki/wiki?38604)

Add the following HTTP headers through the IIS manager:

```
Name:Access-Control-Allow-Headers  Value:Origin, X-Requested-With, Content-Type, Accept
Name:Access-Control-Allow-Origin     Value:http://editor.swagger.io
```

#### [Java generator](https://wiki.genexus.com/commwiki/wiki?12258)

Add the following filter in the web.xml file:

```
    <filter>
        <filter-name>CorsFilter</filter-name>
        <filter-class>org.apache.catalina.filters.CorsFilter</filter-class>
        <init-param>
            <param-name>cors.allowed.origins</param-name>
            <param-value>http://editor.swagger.io,https://editor.swagger.io</param-value>
        </init-param>
        <init-param>
            <param-name>cors.allowed.methods</param-name>
            <param-value>GET,POST,HEAD,OPTIONS,PUT</param-value>
        </init-param>
        <init-param>
            <param-name>cors.allowed.headers</param-name>
            <param-value>Origin,X-Requested-With,Content-Type, Accept</param-value>
        </init-param>
    </filter>
    <filter-mapping>
        <filter-name>CorsFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
```

**Note**: The swagger documentation can be interpreted using the [OpenAPI import tool](https://wiki.genexus.com/commwiki/wiki?31864).

### [See Also](#See+Also)

[Open API Initiative](http://swagger.io/introducing-the-open-api-initiative/)


|  |
| --- |
| **Backlinks** |
| [Business Components as Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28214) | [Data Providers as Rest Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28216) | [Generate OpenAPI interface property](https://wiki.genexus.com/commwiki/wiki?31859) |
| [Prototyping an API with Swagger](https://wiki.genexus.com/commwiki/wiki?50008) | [Toc:Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213) |

---
