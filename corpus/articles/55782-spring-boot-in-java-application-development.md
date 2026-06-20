---
title: "Spring Boot in Java Application Development"
source_id: 55782
source_url: https://wiki.genexus.com/commwiki/wiki?55782
genexus_version: "18"
---

# Spring Boot in Java Application Development

[Spring Boot](https://spring.io/projects/spring-boot) is an extension of the [Spring Framework](https://spring.io/projects/spring-framework) project, which simplifies the configuration and development of Java applications. It provides a set of predefined standards and default settings to speed up development.

The main difference when using Spring Boot on a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) with the Java [environment](https://wiki.genexus.com/commwiki/wiki?7115) is that you don't need to have Tomcat installed to [Build](https://wiki.genexus.com/commwiki/wiki?5692) your KB. This is because Spring Boot comes with an embedded Tomcat server.

In addition to this advantage, Spring Boot offers other benefits in GeneXus, such as:

* Accelerated prototyping, which allows creating Java applications quickly and easily.
* Automatic download and configuration of Spring Boot by setting Spring Boot in the [Java Framework property](https://wiki.genexus.com/commwiki/wiki?55711) and selecting "Rebuild All".
* Unlike Tomcat, which generates a folder structure in the "webapps" directory, Spring Boot generates a single JAR file called "web.jar" in "build\libs", which contains your application ready to run.

### [Steps to Build your KB with Spring Boot](#Steps+to+Build+your+KB+with+Spring+Boot)

Follow the steps below to Build your KB using Spring Boot:

1. Make sure you have JDK 17 or higher installed.
2. Go to Preferences and check that the current environment is Java.
3. Configure the [JDK Directory (JAVA HOME) property](https://wiki.genexus.com/commwiki/wiki?52135) with the path where the JDK is installed.
4. Set the value Spring Boot in the [Java Framework property](https://wiki.genexus.com/commwiki/wiki?55711) and select "Rebuild All". GeneXus detects that you have selected Spring Boot as the framework and automatically downloads and configures Spring Boot.  
   If the server is not previously active, GeneXus will start it automatically after compilation or before running the application.
5. Press F5 or select Build > Run Developer Menu. Also, it is possible to run from the command line, using:  
   java.exe -jar web.jar  
   Note that Spring Boot uses the same default port as Tomcat (port 8080). Therefore, if you decide to use Spring Boot, make sure to disable all Tomcat servers on the machine. This will avoid port conflicts so that the application runs smoothly with Spring Boot.

### [Considerations](#Considerations)

* **Java Platform**  
    
  Applications using Spring Boot framework are always JakartaEE applications.

* **Changing the server port at runtime**  
    
  When packaging and running the Spring Boot application, you can set the server.port argument with the java command:

  ```
  java -jar web.jar --server.port=8083
  ```

  Also, you can do so by using the equivalent syntax:

  ```
  java -jar -Dserver.port=8083 web.jar
  ```

   See [Externalized Configuration](https://docs.spring.io/spring-boot/docs/2.1.9.RELEASE/reference/html/boot-features-external-config.html) for more information.

* **Changing the context path at runtime**  
    
  By default, the context path is taken from the application.properties file, for example:

  server.servlet.context-path=/TestAzureJavaSQLServer

  To change that value, you can use the SERVER\_SERVLET\_CONTEXT\_PATH environment variable or other options available, like setting the property at runtime:

  ```
  java -jar app.jar --server.servlet.context-path=/mypath
  ```

  See [Spring Boot Change Context Path](https://www.baeldung.com/spring-boot-context-path) for more information.
* **Using Http Error Handlers property**  
    
  In Spring Boot, when you enable [Http Error Handlers property](https://wiki.genexus.com/commwiki/wiki?45949), it is critical that the error redirect pages are named according to the error code you want to handle. For example, to handle a 404 error, the error page should be named 404.html, and for a 500 error, it should be 500.html.  
    
  For more details, you can refer to the official Spring Boot documentation on [Custom error pages](https://docs.spring.io/spring-boot/docs/1.4.3.RELEASE/reference/html/boot-features-developing-web-applications.html#boot-features-error-handling-custom-error-pages).

### [Deployment](#Deployment)

See [Deploying Java applications with Spring Boot](https://wiki.genexus.com/commwiki/wiki?58269)

### [Temporary Limitations](#Temporary+Limitations)

[URL Rewrite object](https://wiki.genexus.com/commwiki/wiki?46523) is not supported or considered.

### [Availability](#Availability)

This functionality is available since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).


|  |
| --- |
| **Backlinks** |
| [Deploying Java applications with Spring Boot](https://wiki.genexus.com/commwiki/wiki?58269) | [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) | [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240) |
| [HowTo: My first GeneXus Java Application](https://wiki.genexus.com/commwiki/wiki?45875) | [Http Error Handlers property](https://wiki.genexus.com/commwiki/wiki?45949) | [Table of contents:Java Applications Development](https://wiki.genexus.com/commwiki/wiki?52358) | [Java Framework property](https://wiki.genexus.com/commwiki/wiki?55711) |
| [Packaging Java sources](https://wiki.genexus.com/commwiki/wiki?54656) | [Tomcat version property](https://wiki.genexus.com/commwiki/wiki?48352) |

---
