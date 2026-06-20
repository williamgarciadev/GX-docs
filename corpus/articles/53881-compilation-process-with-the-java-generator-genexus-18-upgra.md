---
title: "Compilation process with the Java Generator (GeneXus 18 Upgrade 2)"
source_id: 53881
source_url: https://wiki.genexus.com/commwiki/wiki?53881
genexus_version: "18"
---

# Compilation process with the Java Generator (GeneXus 18 Upgrade 2)

Whenever you [Build](https://wiki.genexus.com/commwiki/wiki?5692) a KB created with the [Java Generator](https://wiki.genexus.com/commwiki/wiki?12258) for the first time, the necessary libraries are downloaded from [Gradle](https://wiki.genexus.com/commwiki/wiki?52359) to a cache memory that is located by default at C:\Users\<user>\.gradle\caches\modules-2\files-2.1.

Then, the required set of Standard Classes is copied from this cache to the model's \web\build\libsdirectory.

**Notes:**

* Because Gradle has this cache memory, where the packages are downloaded, it is not necessary to access the internet every time a Build is executed. Read [Offline scenario of the Java Generator](https://wiki.genexus.com/commwiki/wiki?52360).
* From now on, each folder and file will be placed in the **model directory**.

Java Standard Classes are published in two repositories: Maven Central and Azure Artifacts. Both repositories are configured in the file build.gradle.

The generated code (\*.java files) is located in the folder src\main\java.

To compile this generated code, in addition to using the necessary libraries that were downloaded in the Gradle Cache, the \*.jar files in the lib folder are taken into account. In this way, additional packages can be added to the classpath.

**Note**: At the moment, the \*.jar files found in the drivers folder are also considered as additional packages to the classpath. This will be discontinued in the future, so you should place the \*.jar files in the lib folder.

The compiled files remain in the folder \build\classes\java\main and from there the command line processes that are triggered from GeneXus are executed.

The libraries that are taken into account to run these processes are found in the folder \web\build\libs.

**Note**: If you want to add a \*.jar file to be used at runtime, it is important that you add it in the lib folder and not in the \web\build\libs folder because, eventually, that folder is deleted when a Gradle clean is run.

In addition, Gradle creates the webapp in the Tomcat that you have configured in GeneXus and copies all the necessary files for its execution (\*.jar, classes, static resources, etc.).

The \*.jar files that it copies are those that are downloaded on demand when the compilation is done and the \*.jar files that are in the lib and drivers folders.

The JavaScript files are generated in the js folder of the model. At compilation time, they are copied to Tomcat.

### [Rebuild All](#Rebuild+All+)

When you perform a Rebuild All on your KB, GeneXus calls Gradle with the clean option. This option deletes:

* The Tomcat webapp.
* The build folder, which has the compiled sources.
* The folder “src\main\java.”

### [Considerations](#Considerations)

If you have an External Object, you need to make sure it is correctly added to the ClassPath. To do this, follow these steps:

1. Go to the JAR file object that contains the External Object.
2. Set Extract Java = .\lib.

With these steps, GeneXus will automatically copy the JAR file to the "lib" folder in the web folder, add it to the ClassPath, and bring it to Tomcat. This ensures that the external object is available and accessible for use in the KB.

### [Troubleshooting](#Troubleshooting)

GeneXus may not be able to compile if:

* An Object has been renamed.
* An Object has been deleted.
* An Object has been moved from one module to another.

This is because Gradle tries to compile all sources found in the src\main\java folder of the model.

To fix the problem, you must delete that source by hand so that Gradle does not try to compile it.

### [Availability](#Availability)

This feature is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).
