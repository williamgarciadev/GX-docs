---
title: "Tips for deploying an application that references External Objects (GeneXus 18 Upgrade 2 or prior)"
source_id: 57576
source_url: https://wiki.genexus.com/commwiki/wiki?57576
genexus_version: "18"
---

# Tips for deploying an application that references External Objects (GeneXus 18 Upgrade 2 or prior)

When an application uses some features of an [External Object](https://wiki.genexus.com/commwiki/wiki?5669) (distributed in a [Module](https://wiki.genexus.com/commwiki/wiki?22414)), the implementation (and all dependencies of that external object) to make the application run is generally needed.

This document explains some details on how to take those dependencies to runtime, including at the deploy time using the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092).

### [.NET](#.NET)

When working with the [.NET Generator](https://wiki.genexus.com/commwiki/wiki?38604), External Objects (EO) provide the [Assembly Name property](https://wiki.genexus.com/commwiki/wiki?40609) where the implementation of the EO is declared. Sometimes, it may happen that this assembly has other dependencies which are not specified in the EO.

To avoid prototyping errors, take into account the following:

1. The assembly that implements the External Object (and all the dependencies) must be created as a [File object](https://wiki.genexus.com/commwiki/wiki?5852) in the KB.
2. Extract the file to the current directory; that is, you should not set anything in the [.NET Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39510) (or set the bin directory). That way, the file stays in the bin directory and it will works at runtime, as it is looked for in that place.

When making the deployment using the Application deployment tool, it will include all the depencies in the package, as it checks at the EO Assembly implementation and the module dependencies.

### [JAVA](#JAVA)

In the [Java Generator](https://wiki.genexus.com/commwiki/wiki?12258), at development time consider the following:

1. The JAR file containing the External Object implementation must be in the KB as a File object.
2. The JAR file must be extracted in the lib directory; that is, you have to set the [Java Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39500) to the lib directory.
