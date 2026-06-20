---
title: "HowTo: Deploy an application in Weblogic Server"
source_id: 46355
source_url: https://wiki.genexus.com/commwiki/wiki?46355
genexus_version: "18"
---

# HowTo: Deploy an application in Weblogic Server

This document explains how to deploy an application using the [Application Deployment Tool](https://wiki.genexus.com/commwiki/wiki?32092) in Weblogic Server.

### [Step 1](#Step+1)

Select the main objects in the Application Deployment Tool; that is, set [Application Server](https://wiki.genexus.com/commwiki/wiki?32092) = Generic Servlet 3.1.

**Note**: If your application includes [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746), set the property [Include GAM Backend](https://wiki.genexus.com/commwiki/wiki?44996) = True.

`[imagen omitida: wiki id 46356]`

### [Step 2](#Step+2)

To avoid any conflicts between the application server and the application, you can set priorities for package names. So, you can include the *weblogic.xml* file with the packages.

```
<?xml version="1.0" encoding="UTF-8"?>

<weblogic-web-app>

    <container-descriptor>

        <prefer-application-packages>

            <package-name>com.genexuscore.*</package-name>

            <package-name>com.genexus.*</package-name>

            <package-name>HTTPClient.*</package-name>

            <package-name>org.apache.poi.*</package-name>

            <package-name>org.apache.xmlbeans.*</package-name>

            <package-name>org.apache.commons.*</package-name>

             <package-name>org.glassfish.jersey.jackson.*</package-name>

             <package-name>com.sun.jersey</package-name>

             <package-name>org.joda.*</package-name>
             
             <package-name>genexus.security.*</package-name>

        </prefer-application-packages>

    </container-descriptor>

</weblogic-web-app>
```

This is a sample file (*weblogic.xml*) with common package names. Other packages can be added.

* Open the WAR file with WinRAR:

`[imagen omitida: wiki id 46358]`

* Place weblogic.xml inside the WEB-INF folder: `[imagen omitida: wiki id 46359]`

### [Step 3](#Step+3)

Deploy the WAR file in Weblogic Server.

`[imagen omitida: wiki id 46360]`

#### **GAM considerations**

* If you get the Error *java.lang.ClassNotFoundException: genexus.security.api.aGAMSSORestRequestTokenAndUserInfo\_v20* in the deployment:  
    
  `[imagen omitida: wiki id 46363]`

           Check the [SAC#47978](https://www.genexus.com/en/developers/websac?data=47978)

* If you get the Error: *The connection to GAM was not found. Please contact the application administrator. (GAM 30)*:                                                                                      `[imagen omitida: wiki id 46362]`

The unpacked WAR file may be disabled. To enable it, you need to configure ["Archived Real Path Enabled"](https://wiki.genexus.com/commwiki/wiki?27947,,) in Weblogic Server

* If you are using Mobile Devices, check that the *connection.gam* file has one entrance –the Application repository connection–, and it doesn't include the GAM-Manager repository connection.

### [Environment](#Environment)

* [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,)
* Weblogic Server 12c
* Java 1.8
