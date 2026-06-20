---
title: "Use native SOAP support in Java"
source_id: 27172
source_url: https://wiki.genexus.com/commwiki/wiki?27172
genexus_version: "18"
---

# Use native SOAP support in Java

Web services can be generated when using native JAVA support based on [JAX-WS](https://jax-ws.java.net/). This allows you to implement ws\* (web service security, web service addressing, etc).

## [How to implement native SOAP support in GeneXus using Java](#How+to+implement+native+SOAP+support+in+GeneXus+using+Java)

Set [Use Native Soap](https://wiki.genexus.com/commwiki/wiki?13446), Generator or Object property to Yes.

### [Requirements](#Requirements)

1. It is recommended that you use JDK 1.6 or higher.  
   JDK / JRE 1.9 is supported as of [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).  
   JVM 1.9 needs to be started with parameter "--add-modules java.xml.ws"  
   For OpenJdk, it is recommended to use Version 11 or higher. In this case, GeneXus Version V16 U8 or higher is required.
2. Set a value for [Java package name property](https://wiki.genexus.com/commwiki/wiki?24941).

### [Details of the implementation](#Details+of+the+implementation)

As usual, for each procedure with [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) = SOAP (e.g: "mywebservice"), a source file named "amywebservice\_impl.java" is generated containing the web service implementation.  
In addition, when [Use Native Soap property](https://wiki.genexus.com/commwiki/wiki?13446) = Yes, a source file named amywebservice\_services.java is generated. It declares the web service definition using annotations, as well as the parameters of the web service and its methods (at present, the only method is "Execute").

Under the Java model (under the jaxws directory) some classes are compiled and transferred to the jaxws directory under the webapp.

### [Generated Descriptors](#Generated+Descriptors)

When the Use Native SOAP property is set to Yes, some additional descriptors are copied to the WEB-INF directory.

* sun-jaxws.xml.   
  It contains the definition of web services.

In the following example, the package name is com.webservices.test, and the sun-jaxws.xml is as follows:

```
<endpoint name="get Clientes" implementation="com.webservices.test.agetclientes_services" url-pattern="/servlet/ws/com.webservices.test.agetclientes_services"/>
```

* web.xml.   
  It is automatically generated from the web\*\_native\_ws.xml template under the web directory of the model and transferred to the WEB-INF directory.

### [Web service WSDL URI](#Web+service+WSDL+URI)

The web services WSDL URL will be as follows:

```
http://server:port/<URL BASE>/servlet/ws/<package>.<servicename>_services?wsdl
```

Example:

```
http://172.16.3.3:8080/JavaEnvironment/servlet/ws/com.webservices.test.agetclientes_services?wsdl
```


|  |
| --- |
| **Backlinks** |
| [Use Native Soap property](https://wiki.genexus.com/commwiki/wiki?13446) |

---
