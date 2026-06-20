---
title: "Gradle and the Java Generator"
source_id: 52359
source_url: https://wiki.genexus.com/commwiki/wiki?52359
genexus_version: "18"
---

# Gradle and the Java Generator

[Gradle](https://docs.gradle.org/current/userguide/userguide.html) is an advanced compilation tool that allows you to automate and manage the compilation process, as well as to define customized and flexible compilation configurations.

As from GeneXus 18, Gradle is the tool for managing the Java Generator’s dependencies and build process. Therefore, the compilation mechanism GXJMake and createwebapplication.bat are no longer used, and Gradle is used instead. In addition, the compile folder that contained a file for every GeneXus object to be compiled is no longer used either.

The use of Gradle brings about the following changes: at the folder structure level, the available command lines, and the properties to generate your KB.

### [Folder structure](#Folder+structure)

Below is a list of the folders structure:

* The \*.java sources are generated in the folder src\main\java.
* The JavaScript sources are generated in the js folder of the model.
* The compiled code is generated in the folder build\classes\java\main.

### [Command lines](#Command+lines+)

Gradle can be called from command line, indicating the task to be executed. The available tasks are listed below:

* #### [build](#build)

This task calls the tasks buildGenexus, copyTomcat, and compileJava.

* #### [buildGenexus](#buildGenexus)

This task calls the tasks copyRuntimeLibs and copyAdditionalFiles.

* #### [javaCompile](#javaCompile)

This task compiles all the existing sources in “src\main\java” and leaves the classes in “build\classes\java\main.”

* #### [copyRuntimeLibs](#copyRuntimeLibs)

This task downloads and copies all the necessary packages to the “build\libs” folder to execute any proc command line.

* #### [copyAdditionalFiles](#copyAdditionalFiles)

This task copies all the necessary files to the “build\classes\java\main” folder from the model folder to execute any proc command line.

* #### [copyTomcatLib](#copyTomcatLib)

This task downloads and copies all the necessary packages to the webapp lib folder in Tomcat to run the webapp.

* #### [copyTomcatClasses](#copyTomcatClasses)

This task copies all the necessary classes to the webapp classes folder in Tomcat in order to run the webapp.

* #### [copyTomcatStatic](#copyTomcatStatic)

This task copies all the static content to the 'static' folder of the webapp in Tomcat.

* #### [copyTomcatResources](#copyTomcatResources)

This task copies all necessary resources other than jars, static content, or classes to the Tomcat webapp.

* #### [copyTomcat](#copyTomcat)

This task calls the tasks that are necessary to run the webapp on Tomcat.

* #### [cleanDeps](#cleanDeps)

This task deletes the “dependencies” folder.

* #### [clean](#clean)

This task calls the cleanTomcat, cleanSources tasks and deletes the “build” folder.

* #### [cleanTomcat](#cleanTomcat)

This task deletes the webapp from Tomcat.

* #### [cleanSources](#cleanSources)

This task deletes all the sources from the “src\main\java” folder.

* #### [getDeps](#getDeps)

This task downloads all the packages needed to run to the “dependencies” folder.

### [Properties](#Properties+)

The Gradle project is located in the build.gradle file that is distributed by GeneXus with the generator. This file is overwritten when the generator is updated.

In addition, Gradle uses a set of properties to run the project. These properties are located in the gradle.properties file, which is generated every time you compile.

To run Gradle from the command line, you may want to overwrite some of the properties of the gradle.properties file, which are shown in the table below. To overwrite the values of these properties, you must indicate the value of the property in the command line.

|  |  |
| --- | --- |
| GENEXUS\_VERSION | Version of the standard classes to be used. |
| JAVA\_PACKAGE\_NAME\_FOLDER | Package name of the model. |
| TOMCAT\_WEBAPP\_PATH | Path to Tomcat. |
| TOMCAT\_STATIC\_PATH | Path to the static folder in Tomcat. |
| JAVA\_PLATFORM | It can have the values jakartaEE, javaEE or both. |
| SQLSERVER | If a SQL Server datastore exists. |
| ORACLE | If an Oracle datastore exists. |
| POSTGRESQL | If a PostgreSQL datastore exists. |
| MYSQL | If a MySQL datastore exists. |
| DBMS\_MYSQL\_VERSION | MySQL Datastore Version. |
| DB2ISERIES | If an iSeries datastore exists. |
| WEBAPP\_NAME | Name of the webapp in Tomcat. |
| LAYOUT\_METADATA\_FOLDER | If there are dynamic reports, their templates are saved in this folder. |
| DAMENG | If a Dameng datastore exists. |

### [Samples](#Samples)

The following examples are command line calls to Gradle.

#### [Sample #1](#Sample+%231)

You can make a Build using the Build task with the properties defined by default in the gradle.properties file that GeneXus generated. To do so, type the following in command line:

```
gradlew.bat build
```

It is the same command that is called from GeneXus when selecting any Build option.

#### [Sample #2](#Sample+%232)

It is also possible to make a Build by typing the value of the GENEXUS\_VERSION property, as shown in the following line:

```
gradlew.bat build -PGENEXUS_VERSION="2.8-SNAPSHOT"
```

### [Notes](#Notes)

* To start Gradle it uses the value defined in the JAVA\_HOME environment variable.
* To include additional dependencies in your GeneXus application, create a .gradle file in the web directory of your project. This file allows you to specify external libraries that your application needs. Add the required dependencies within the.gradle file, following the standard Gradle syntax. For example, to integrate Spring Boot Actuator, refer to the official Spring Boot documentation for the specific dependency you need to add: <https://docs.spring.io/spring-boot/reference/actuator/tracing.html>.

  When you build your GeneXus application, Gradle will automatically incorporate these dependencies, ensuring that your application has access to the necessary libraries. Once you've added the dependencies, follow the instructions in the relevant documentation to configure and use the libraries in your application.

### [Availability](#Availability)

This feature is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).


|  |
| --- |
| **Backlinks** |
| [Application Deployment MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?42073) | [Compilation process with the Java Generator](https://wiki.genexus.com/commwiki/wiki?52362) | [Compilation process with the Java Generator (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?53881) |
| [Gradle Options property for Java Generator](https://wiki.genexus.com/commwiki/wiki?54273) | [Table of contents:Java Applications Development](https://wiki.genexus.com/commwiki/wiki?52358) | [Java Generator Requirements](https://wiki.genexus.com/commwiki/wiki?54302) | [Java Generator Standard Classes](https://wiki.genexus.com/commwiki/wiki?52361) |
| [JDK Directory (JAVA HOME) property](https://wiki.genexus.com/commwiki/wiki?52135) | [Offline scenario of the Java Generator](https://wiki.genexus.com/commwiki/wiki?52360) | [Packaging Java sources](https://wiki.genexus.com/commwiki/wiki?54656) | [Packaging Java sources (GeneXus 18 Upgrade 9)](https://wiki.genexus.com/commwiki/wiki?57920) |

---
