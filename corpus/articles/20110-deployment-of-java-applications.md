---
title: "Deployment of Java Applications"
source_id: 20110
source_url: https://wiki.genexus.com/commwiki/wiki?20110
genexus_version: "18"
---

# Deployment of Java Applications

To deploy applications generated with GeneXus 15 and the Java generator, use the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092).  
That generates a .war file containing the Web application and/or the Web services (SOAP or REST) or a .jar file containing your command line programs.

### [Servlet server specific considerations](#Servlet+server+specific+considerations)

Although [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) does the job creating the .war following standard servlet server specifications, there are some special considerations to take into account in some servlet servers depending on their configuration.  
JBoss

JBoss implements its own module for REST services called RESTeasy. Since Smart Device applications created with GeneXus use Rest services for their implementation using the Sun RESTful module, the JBoss RESTeasy module has to be disabled for the application in order to avoid incompatibility issues between them.

To do so, 2 options are available:  
    1- Disable the RESTeasy module just for one application by adding the following lines to the web.xml file:  
        <context-param>  
            <param-name>resteasy.scan</param-name>  
            <param-value>false</param-value>  
        </context-param>  
        <context-param>  
            <param-name>resteasy.scan.providers</param-name>  
            <param-value>false</param-value>  
        </context-param>  
        <context-param>  
            <param-name>resteasy.scan.resources</param-name>  
            <param-value>false</param-value>  
        </context-param>

  2-Disable the JBoss RESTeasy module:

    - For JBoss 6, deleting the RESTeasy module is enough.  
    - For JBoss 7, before performing the following procedure, backing up the modified files is recommended:

Remove the references to jaxrs from the configuration. Depending on the JBoss configuration used -which can be standalone or domain- the corresponding file must be edited:  
        <JBoss\_AS\_7\_Home>/standalone/configuration/standalone.xml

        <JBoss\_AS\_7\_Home>/domain/configuration/domain.xml

            By deleting the following lines (comments can be added to these lines, but JBoss removes them at startup):

        ...  
        <extension module="org.jboss.as.jaxrs"/>  
        ...  
        <subsystem xmlns="urn:jboss:domain:jaxrs:1.0"/>  
        ...

        When working with JBoss 7.1.0.Final, the references to WebServices must also be removed (org.jboss.as.webservices). The tags that belong to the extension and its corresponding subsystem must be deleted as well.

        To learn more about JBoss, click [here](https://wikis.forgerock.org/confluence/display/openam/Deploy+OpenAM+in+JBoss+AS+7).

### 

GeneXus 15 uses JAX 2.0 libraries. If your server is configured to use JAX 1.0, you have to turn the libraries off, as the following example shows.  
  
In Jboss, for instance, you have to add the following file jboss-deployment-structure.xml in the web-inf directory

```
<?xml version="1.0" encoding="UTF-8"?>
<jboss-deployment-structure xmlns="urn:jboss:deployment-structure:1.2">
  <deployment>
    <exclude-subsystems>
      <subsystem name="jaxrs" />
      <subsystem name="webservices" />
      <subsystem name="resteasy" />
    </exclude-subsystems>
    <exclusions>
      <module name="javaee.api" />
      <module name="javax.ws.rs.api" />
      <module name="org.jboss.as.jaxrs" />
      <module name="org.jboss.resteasy.resteasy-jaxrs" />
      <module name="org.jboss.resteasy.resteasy-cdi" />
      <module name="org.jboss.resteasy.jackson-provider" />
      <module name="org.jboss.resteasy.resteasy-atom-provider" />
      <module name="org.jboss.resteasy.resteasy-hibernatevalidator-provider" />
      <module name="org.jboss.resteasy.resteasy-jaxb-provider" />
      <module name="org.jboss.resteasy.resteasy-jettison-provider" />
      <module name="org.jboss.resteasy.resteasy-jsapi" />
      <module name="org.jboss.resteasy.resteasy-multipart-provider" />
      <module name="org.jboss.resteasy.resteasy-yaml-provider" />
      <module name="org.codehaus.jackson.jackson-core-asl" />
      <module name="org.codehaus.jackson.jackson-jaxrs" />
      <module name="org.codehaus.jackson.jackson-mapper-asl" />
      <module name="org.codehaus.jackson.jackson-xc" />
      <module name="org.codehaus.jettison" />
      <module name="org.jboss.as.webservices.*" />
      <module name="org.jboss.ws.*" />
    </exclusions>

    <dependencies>
      <module name="javax.activation.api" export="true" />
      <module name="javax.annotation.api" export="true" />
      <!-- <module name="javax.ejb.api" export="true" />
      <module name="javax.el.api" export="true" /> -->
      <module name="javax.enterprise.api" export="true" />
      <module name="javax.enterprise.deploy.api" export="true" />
      <module name="javax.inject.api" export="true" />
      <module name="javax.interceptor.api" export="true" />
      <!-- <module name="javax.jms.api" export="true" />
      <module name="javax.jws.api" export="true" />
      <module name="javax.mail.api" export="true" />
      <module name="javax.management.j2ee.api" export="true" /> -->
      <module name="javax.persistence.api" export="true" />
      <module name="javax.resource.api" export="true" />
      <!-- <module name="javax.rmi.api" export="true" />
      <module name="javax.security.auth.message.api" export="true" />
      <module name="javax.security.jacc.api" export="true" /> -->
      <module name="javax.servlet.api" export="true" />
      <module name="javax.servlet.jsp.api" export="true" />
      <module name="javax.transaction.api" export="true" />
      <module name="javax.validation.api" export="true" />
      
      <!-- <module name="javax.ws.rs.api" export="true" services="export" /> -->
      
      <module name="javax.xml.bind.api" export="true" />
      <module name="javax.xml.registry.api" export="true" />
      <module name="javax.xml.soap.api" export="true" />
      <module name="javax.xml.ws.api" export="true" />

      <!-- This one always goes last. -->
      <module name="javax.api" export="true" />
    </dependencies>
   </deployment>
</jboss-deployment-structure>
```

### [Glassfish](#Glassfish)

PDF Reports

During deployment, the \*.rpt files generated in the generation directory of the WebApp root must be included:

To learn more about dynamic reports, click [here](https://wiki.genexus.com/commwiki/wiki?14918,,)


|  |
| --- |
| **Backlinks** |
| [Deploying a Java application on a JBoss server](https://wiki.genexus.com/commwiki/wiki?46032) |

---
