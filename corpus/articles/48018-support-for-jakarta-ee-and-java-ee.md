---
title: "Support for Jakarta EE and Java EE"
source_id: 48018
source_url: https://wiki.genexus.com/commwiki/wiki?48018
genexus_version: "18"
---

# Support for Jakarta EE and Java EE

This article describes how GeneXus Java generator adds support for Jakarta EE and what you need to take into account to build and deploy your applications to servlet servers supporting Java EE, Jakarta EE or creating packages that support later to be deployed on any of them.

## [Introduction](#Introduction)

Jakarta EE is the evolution of Java EE. Oracle decided to transfer Java EE to an open source foundation (Eclipse Foundation). That transfer involved a name change to Jakarta EE and, most importantly, all the packages of the classes were renamed from javax.\* to jakarta.\*.

New versions of container servlets already began to implement Jakarta EE, for example Tomcat 10, GlassFish 6.0 and Jetty 11 among others.  
This implies that existing programs have to be recompiled by changing the packages of the used framework classes from javax.\* to jakarta.\* if they want to be run on the newer versions of the servers.

## [Changes in the GeneXus Java Generator](#Changes+in+the+GeneXus+Java+Generator)

From [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48247,,) both versions are supported, so you can choose whether you want to continue executing the code in the new versions of the container servlets or in the ones you have already been running. For this, a refactoring has been carried out in the standard classes and changes in the generated code.

### [Standard classes](#Standard+classes)

A refactoring in the [GeneXus Standard Classes](https://wiki.genexus.com/commwiki/wiki?18859) has been made.

All references to javax packages from the gxclassR.jar JAR have been removed and a new JAR called gxwrappercommon.jar that contains only interfaces that are implemented with

* javax support are now in a new JAR called gxwrapperjavax .jar, and
* jakarta support are now in a new JAR called gxwrapperjakarta.jar.

### [Generated code](#Generated+code)

Regarding the generated code, there is a new property [Java platform support property](https://wiki.genexus.com/commwiki/wiki?48353) in which you will be able to choose if you want to generate for Java EE or Jakarta EE or both.

### [Deployment](#Deployment)

GeneXus from now on, in addition to carrying the JAR gxclassR.jar always carries the JAR gxwrappercommon.jar and, depending on the version of the servlet container you choose, the JAR gxwrapperjavax.jar or gxwrapperjakarta.jar.

New properties [Tomcat version property](https://wiki.genexus.com/commwiki/wiki?48352) [Tomcat path property](https://wiki.genexus.com/commwiki/wiki?48354) have been created for managing the deployment to the local tomcat environment.

### [Compatibility](#Compatibility)

A) GeneXus assumes that you use a Tomcat to prototype. If not, you may need to copy files to your Application Server. For that, you can use [Build Events](https://wiki.genexus.com/commwiki/wiki?39474) or [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092).

B) It may happen that, if you had handwritten code that uses some of the standard classes that are now implemented as interfaces in the gxwrappercommon.jar JAR, that you need to fix that code.

#### [Samples](#Samples)

Here is a pair of samples of code with problems and the code that fixes them:

Old code1:

```
java javax.servlet.http.HttpServletResponse response = httpContext.getResponse();
java response.setStatus([!&CodeService!]);
```

Fixed code1:

```
java com.genexus.servlet.http.IHttpServletResponse response = httpContext.getResponse();
java response.setStatus([!&CodeService!]);
```

Old code2:

```
java bos = new java.io.BufferedOutputStream( respuesta.getOutputStream() );
```

Fixed code2:

```
java bos = new java.io.BufferedOutputStream( respuesta.getOutputStream().getOutputStream() );
```

**Note**: The fixed code works on both, Jakarta EE and Java EE, the old only worked on Java EE.

## 

## [See Also](#See+Also)

* More about the Java Standard Classes project at <https://github.com/genexuslabs/JavaClasses#genexus-standard-classes-for-java>
* [Java platform support property](https://wiki.genexus.com/commwiki/wiki?48353)
* [Tomcat version property](https://wiki.genexus.com/commwiki/wiki?48352)
* [Tomcat path property](https://wiki.genexus.com/commwiki/wiki?48354)
* [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Compatibility Section](https://wiki.genexus.com/commwiki/wiki?51080) |

---
