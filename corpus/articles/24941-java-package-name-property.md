---
title: "Java package name property"
source_id: 24941
source_url: https://wiki.genexus.com/commwiki/wiki?24941
genexus_version: "18"
---

# Java package name property

Indicates in which Java package the programs must be generated.

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator, Back end

### [Description](#Description)

The Java package name property is located in the [Preferences window](https://wiki.genexus.com/commwiki/wiki?7109) at the Backend Generator level.

By default the value of the property is com.KnowledgeBaseName.

This property is used to set the base structure of the packages in which the source code of your Java application will be generated. By defining it, you are determining the common prefix that will be used for all the modules in your project.

When you define a module in GeneXus, the value you have set in the property is combined with the module name to form the complete package structure in which the code for that module will be generated. This means that every time you create a new module, GeneXus automatically generates a new part of the Java package structure using the module name as part of the package path.

For example, if you have set the Java package name as "com.knowledgebase" and then define a module called "mymodule", GeneXus will generate the source code for that module inside the package com\knowledgebase\mymodule.

In the case of a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) (KB) migrated from previous versions, if the Java Package name property is empty, it is kept as it is.

As the property needs to have a value other than null when using [Modules](https://wiki.genexus.com/commwiki/wiki?22441,,), you must enter a value for the property when creating the first Module in the KB.

**Note:** The package name must be specified in lowercase as recommended by Oracle [here](http://java.sun.com/docs/codeconv/html/CodeConventions.doc8.html). Even though you can use uppercase if you want, you need to be careful about the URL used. For example, if the package name is com.Artech.Test, the classes will be copied to web-inf\classes\com\Artech\Test and the link to execute this web app must be http://<appserver>:8080/<webappname>/servlet/com.Artech.Test.webpanel1. Pressing F5 in GeneXus will not consider this at runtime, so it must be changed by the developer.

### [See Also](#See+Also)

[External Package Name property](https://wiki.genexus.com/commwiki/wiki?57626)


|  |
| --- |
| **Backlinks** |
| [Android specific properties](https://wiki.genexus.com/commwiki/wiki?31449) | [HowTo: Deploy an application to Google App Engine](https://wiki.genexus.com/commwiki/wiki?32211) | [HowTo: Deploy an application to Google App Engine (GeneXus 18 Upgrade 8)](https://wiki.genexus.com/commwiki/wiki?57567) |
| [Java Class Import Wizard](https://wiki.genexus.com/commwiki/wiki?6176) | [Modules - URL Syntax](https://wiki.genexus.com/commwiki/wiki?25224) |
| [Packaging Java sources](https://wiki.genexus.com/commwiki/wiki?54656) | [Use native SOAP support in Java](https://wiki.genexus.com/commwiki/wiki?27172) |

---
